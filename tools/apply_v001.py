#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import shutil
import sys
import zipfile
from pathlib import Path

CHUNK = 4 * 1024 * 1024

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()

def load_patch(path: Path):
    with zipfile.ZipFile(path, "r") as z:
        manifest = json.loads(z.read("manifest.json"))
        payload = z.read("payload.bin")
    if manifest.get("format") != "kckpatch-v2":
        raise RuntimeError(f"Unsupported patch format: {path}")
    return manifest, payload

def apply_one(mother: Path, patch_path: Path, output: Path) -> str:
    p, payload = load_patch(patch_path)
    if mother.stat().st_size != p["mother_size"]:
        raise RuntimeError(f"{mother}: Mother size mismatch")
    got = sha256_file(mother)
    if got != p["mother_sha256"]:
        raise RuntimeError(f"{mother}: Mother SHA-256 mismatch\n expected {p['mother_sha256']}\n got      {got}")
    output.parent.mkdir(parents=True, exist_ok=True)
    if p["mode"] == "overwrite":
        shutil.copyfile(mother, output)
        with output.open("r+b") as f:
            for idx, rec in enumerate(p["records"]):
                off = int(rec["offset"]); length = int(rec["length"])
                f.seek(off); old = f.read(length)
                if hashlib.sha256(old).hexdigest() != rec["old_sha256"]:
                    raise RuntimeError(f"{mother}: old-span verification failed at record {idx}, offset 0x{off:X}")
                po = int(rec["payload_offset"])
                new = payload[po:po + length]
                if len(new) != length:
                    raise RuntimeError(f"{patch_path}: truncated payload at record {idx}")
                f.seek(off); f.write(new)
    elif p["mode"] == "rebuild":
        with mother.open("rb") as src, output.open("wb") as dst:
            for idx, cmd in enumerate(p["commands"]):
                if cmd["op"] == "copy":
                    src.seek(int(cmd["source_offset"])); data = src.read(int(cmd["length"]))
                    if len(data) != int(cmd["length"]):
                        raise RuntimeError(f"{patch_path}: source read failed at command {idx}")
                    dst.write(data)
                elif cmd["op"] == "data":
                    po = int(cmd["payload_offset"]); length = int(cmd["length"])
                    data = payload[po:po + length]
                    if len(data) != length:
                        raise RuntimeError(f"{patch_path}: truncated payload at command {idx}")
                    dst.write(data)
                else:
                    raise RuntimeError(f"{patch_path}: unknown command at {idx}")
    else:
        raise RuntimeError(f"{patch_path}: unknown mode {p['mode']}")
    if output.stat().st_size != p["output_size"]:
        raise RuntimeError(f"{output}: output size mismatch")
    out_hash = sha256_file(output)
    if out_hash != p["output_sha256"]:
        raise RuntimeError(f"{output}: Output SHA-256 mismatch\n expected {p['output_sha256']}\n got      {out_hash}")
    return out_hash

def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    release_manifest = json.loads((repo / "manifests" / "v0.01.json").read_text(encoding="utf-8"))
    if len(sys.argv) < 2:
        print("Usage: python tools/apply_v001.py <clean_1.02_Media_folder> [output_folder]")
        return 2
    media = Path(sys.argv[1]).resolve()
    if not media.is_dir():
        print(f"ERROR: Media folder not found: {media}")
        return 2
    output_media = Path(sys.argv[2]).resolve() if len(sys.argv) >= 3 else repo / "output" / "rePatch" / release_manifest["title_id"] / "Media"
    print("Preflight SHA-256 validation...")
    for item in release_manifest["files"]:
        mother = media / item["source_path"]
        if not mother.is_file():
            print(f"ERROR: Missing required file: {mother}"); return 1
        if mother.stat().st_size != item["mother_size"]:
            print(f"ERROR: Size mismatch: {mother}"); return 1
        got = sha256_file(mother)
        if got != item["mother_sha256"]:
            print(f"ERROR: SHA-256 mismatch: {mother}")
            print(f" expected {item['mother_sha256']}")
            print(f" got      {got}")
            return 1
        print(f"  PASS  {item['source_path']}")
    if output_media.exists():
        shutil.rmtree(output_media)
    output_media.mkdir(parents=True, exist_ok=True)
    print("\nApplying v0.01 patches...")
    for item in release_manifest["files"]:
        mother = media / item["source_path"]
        patch = repo / item["patch"]
        output = output_media / item["output_path"]
        out_hash = apply_one(mother, patch, output)
        print(f"  PASS  {item['output_path']}  {out_hash}")
    print("\nSUCCESS")
    print(f"Output: {output_media}")
    print("Copy the generated rePatch tree to ux0:/rePatch/ on your Vita.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
