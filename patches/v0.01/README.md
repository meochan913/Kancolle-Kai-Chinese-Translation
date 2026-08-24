# v0.01 Patch Set

These files are binary differences only. They do not contain complete game files.

## Input

Clean KanColle Kai 1.02 Media tree (`1.00 base + official 1.02 update overlay`).

The installer performs SHA-256 preflight validation on all eight required Mother files **before creating any output**.

## Output

`rePatch/PCSG00684/Media/`

The generated eight files are byte-identical to the cumulative Vita-validated `rePatch` set used to close the pre-game milestone.

## Patch format

`.kckpatch` is a ZIP container with:

- `manifest.json`
- `payload.bin`

Two modes are supported:

- `overwrite`: same-size files; exact Mother hash + per-span old SHA-256 validation.
- `rebuild`: size-changing files; reconstructs the output from source COPY commands and literal delta DATA.

Every output is checked against its expected final SHA-256.
