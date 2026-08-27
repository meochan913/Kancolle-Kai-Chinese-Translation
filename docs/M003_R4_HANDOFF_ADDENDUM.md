# M003 R4 Handoff Addendum

Date: 2026-08-27

This addendum records two Windows PowerShell 5.1 compatibility fixes and the cumulative Media input SOP confirmed during v0.02 / M003 testing.

## Current M003 script revision

Current package revision: **R4**.

R1 is superseded because `Copy-StreamRange` used a parameter named `$Input`. PowerShell variables are case-insensitive, so this collided with the automatic `$input` variable and caused `ArrayListEnumeratorSimple` to be passed where a `System.IO.Stream` was required. Stream parameters must use explicit names such as `$InputStream`, `$OutputStream`, `$SourceStream`, and `$DestinationStream`.

R2 is superseded because it unnecessarily changed the established single-Media drag-and-drop workflow by adding multi-input/file-picker behavior.

R3 fixed the stream-variable collision and successfully completed M003 rebuild steps 1 through 6 on the user's machine, but failed at step 7 while serializing the final report. Root cause: `output_files=@($Reports)` where `$Reports` was a `System.Collections.Generic.List[object]`; Windows PowerShell 5.1 can throw `System.ArgumentException: Argument types do not match` for this conversion.

R4 keeps the R3 resource payloads/rebuild recipes unchanged and fixes report generation by explicitly copying report records into a normal PowerShell array before `ConvertTo-Json`. Hash-line generation also uses a normal PowerShell array.

R4 full candidate archive SHA-256:

`ba0c2b42ed12831cd95803d14beb8adf525d108d416751bb9e23b9315259c15e`

The R3-to-R4 core comparison found **65 core payload/recipe files identical, 0 differences, 0 missing**. Only scripts/documentation and the recovery helper changed.

## R3 step-7 recovery

If R3 already completed steps 1 through 6 and failed only at `[7/7] Write final report + hashes`, do not rebuild the assets. Use the R4 finish-only helper to hash the five existing outputs and generate `M003_WRITEBACK_REPORT.json` and `M003_OUTPUT_SHA256.txt`.

Known exact M003 outputs already gated by the rebuild recipe:

- `sharedassets5.assets` SHA-256 `e0637b783cf6d58b62bf0d60b2852571993739299ea0d37e501a1c53f764cfc5`
- `level4` SHA-256 `4a756494dcbd92106993d494d4b34b49e21c297bcadc630466e9b966532e7106`

M003 remains **Vita validation pending** until hardware testing succeeds.

## Permanent cumulative Media input SOP

Development patch packages continue to use one cumulative sparse rePatch `Media` directory as their single drag-and-drop input.

If a new M00X stage modifies a clean 1.02 file that has never previously entered the cumulative patched Media, the assistant must tell the user **before running/building the patch** exactly which clean file is newly required. The user will manually copy that clean 1.02 file into the current cumulative patched Media, and the patcher will continue to accept that one Media directory.

Do not replace this workflow with multi-input arguments, file-selection dialogs, or bundled full clean game files unless the user explicitly requests it.

M003 example: `level4` was untouched by M001/M002, so before M003 the user copied clean 1.02 `level4` into the M002 cumulative Media.

## Permanent PowerShell compatibility rules

- Never use `$Input` as a custom variable/parameter name.
- Prefer explicit stream names such as `$InputStream` / `$OutputStream`.
- Do not directly wrap `Generic.List` with `@($GenericList)` when constructing final reports for Windows PowerShell 5.1; explicitly copy to a normal array first.
- Final report/hash writing should be independently recoverable so a report-only failure does not require rebuilding very large Unity assets again.
