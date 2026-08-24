# Installation — v0.01

## Requirements

- Your own clean KanColle Kai installation updated to game version **1.02**
- The decrypted `Media` folder from that supported installation
- Python 3 on Windows for the current repository installer

The expected source state is:

**1.00 base game + official 1.02 update overlay**

See [`SOURCE_BASELINE.md`](SOURCE_BASELINE.md) for the exact Mother hashes.

## Install

1. Download or clone this repository.
2. Locate the clean 1.02 `Media` folder.
3. Drag that `Media` folder onto `APPLY_V001.cmd`.
4. The patcher performs SHA-256 preflight checks on all eight required input files.
5. If every check passes, the patcher creates:

```text
output/
  rePatch/
    PCSG00684/
      Media/
```

6. Copy the generated `rePatch` folder to `ux0:/rePatch/` on the Vita.

## Fail-closed behavior

No output is created until **all eight required Mother files** pass SHA-256 validation.

After patching, every generated file is hashed again and must exactly match the v0.01 FINAL hash.

If any input or output hash differs, the patcher stops with an error.

## Files modified by v0.01

- `level2`
- `level5`
- `Managed/Assembly-CSharp.dll`
- `resources.assets`
- `sharedassets2.assets`
- `sharedassets3.assets`
- `sharedassets5.assets`
- `sharedassets6.assets`

The patch set does not distribute complete original or modified game binaries.
