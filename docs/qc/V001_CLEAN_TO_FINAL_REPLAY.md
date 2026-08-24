# v0.01 Clean-to-Final Replay QC

Status: **PASS**

All eight patches were applied to the clean 1.02 Mother files and compared with the uploaded cumulative FINAL rePatch set.

| File | Patch bytes | Output SHA-256 | Byte-identical |
| --- | ---: | --- | --- |
| `level2` | 643 | `e4620fba82e4b50124c412d5a885ca9255be9e8590b3db0ec080122762bb2e73` | PASS |
| `level5` | 6,442 | `9d83c6183e0cb4d064d2bc69199059396c0f5d06e970c335777a37749ee9fff5` | PASS |
| `Managed/Assembly-CSharp.dll` | 1,253 | `ae2b1f2a6c008f05f19ad10dd4a7c963ef8b5294d2e8d3b538b387370149d90e` | PASS |
| `resources.assets` | 709,644 | `f19fbcf5f2be01bd386ff4f126688ab7685f3df3426881924797863348f7fce8` | PASS |
| `sharedassets2.assets` | 440,601 | `7cde6cf01ae29fa4a31d72c1d2865016e30ddf4809d7d699cb3b7d415568ee61` | PASS |
| `sharedassets3.assets` | 2,488,023 | `05474b778394a89e3f11f3081418a6256fda1a7a16ff23d702279713fa83638b` | PASS |
| `sharedassets5.assets` | 653,441 | `c43eed5af97a0f8b2feb826759fa5cbbca1641e47d65928f2fde91e554f1fa23` | PASS |
| `sharedassets6.assets` | 214,065 | `f67cbd9f3cc8752a32e7383c2d04578c466ae9f5913ca7bcc34570f5ac78a487` | PASS |

Overall gate: **PASS**

The installer also completed a full preflight + apply + final-hash verification run from the clean source tree.
