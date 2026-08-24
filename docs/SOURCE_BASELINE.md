# Clean 1.02 Source Baseline

This manifest was calculated from the project source set supplied as the **clean 1.00 game + official 1.02 update overlaid** baseline.

These hashes are the authoritative **public-release Mother/input hashes**. Historical project Mother hashes may represent intermediate cumulative localization states and must not be used as clean-install validation.

## Key files

| File | Size | SHA-256 |
| --- | ---: | --- |
| `resources.assets` | 1,278,324,088 | `7845a58df2c72ff15fe72ebf134050bb4cc660e5de10274b317da4e9f62c72f4` |
| `resources.resource` | 406,278,496 | `56d779c13728ec5d0e3c630228c36713b35ff1d335fde91d5f2198e76ac2401a` |
| `mainData` | 4,790,252 | `0ad5357016e8b3e9368c35acdf54ed44562f014140ff1c7b0457223cc33ba2f8` |
| `Managed/Assembly-CSharp.dll` | 4,857,856 | `cb74f8991c7d80f7519b028581753acd006b488f8d160613dc6b215015362327` |
| `level2` | 31,308 | `1baf870b0bfded8c6298c133ccd63aba434009d88deeabba7333fd1f7b07ed07` |
| `level5` | 36,444 | `c2739e6fd7440b200d44b46a492c3e9bb337302a1cc9ba92a01963f971be093b` |
| `sharedassets2.assets` | 3,380,708 | `7a799248d4e73c87d56fc047026921161ed1f2eb3b9bd57afe33afa0a4e643fc` |
| `sharedassets3.assets` | 7,131,440 | `dc1ee9c49058fb7f582c6c36ba076e2dfc4c50107f2d6350f026d0e4c25d9ec1` |
| `sharedassets5.assets` | 54,898,340 | `1c483cf3f68ddf7bf4693094a21468c95ca3287815204f8fdf1ced8a23b5aae0` |
| `sharedassets6.assets` | 3,014,252 | `914b586adcb0f28cbb7cc127d4032d8b0728c5d64e15ac85b20781533ed8a2a0` |

## Patcher validation rule

The release patcher should validate the clean-baseline SHA-256 **for every file it will modify** before writing any bytes. It does not need to reject an installation merely because an unrelated, untouched game file differs, unless a future strict full-install verification mode is explicitly enabled.

The complete 57-file baseline fingerprint is stored in [`../manifests/clean-1.02.sha256.json`](../manifests/clean-1.02.sha256.json).

## Current clean release-input candidates

- `resources.assets`
- `sharedassets2.assets`
- `sharedassets3.assets`
- `sharedassets5.assets`
- `sharedassets6.assets`
- `level2`
- `level5`
- `Managed/Assembly-CSharp.dll`

The final touched-file list will be determined by an actual clean-vs-FINAL binary diff before v0.01 is published.
