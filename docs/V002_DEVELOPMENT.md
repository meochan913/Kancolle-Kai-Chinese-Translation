# v0.02 Development State

## Current status

- Formal public release remains **v0.01 — Pre-Game Translation Milestone**.
- v0.02 is a development line and is **not** a formal GitHub Release yet.
- **M001 — Strategy Tutorial RGBA32 is PSV Vita HARDWARE PASS / ACCEPTED / LOCKED** as of 2026-08-24.
- The exact Vita-tested package was `Kancolle_Kai_v0.02_M001_RGBA32_VITA_CANDIDATE.zip`.
- ZIP SHA-256: `2e0f1a312dbf4f0618ac2860aa4ee72943045c79253ae69912e0bd8cdcf22eb8`.

M001 is frozen by default. Do not reopen or rebuild it unless explicitly requested.

## M001 development Mother

M001 was developed cumulatively from the v0.01 FINAL Vita-validated state, not directly from clean 1.02.

Development Mothers used for M001:

- `resources.assets`: `f19fbcf5f2be01bd386ff4f126688ab7685f3df3426881924797863348f7fce8`
- `sharedassets2.assets`: `7cde6cf01ae29fa4a31d72c1d2865016e30ddf4809d7d699cb3b7d415568ee61`

For future formal v0.02 publication, development history must be normalized again to deterministic single-step patches from the clean 1.02 public Mother.

## M001 FINAL Vita-PASS outputs

### resources.assets

- SHA-256: `fe3c836c9f3a4ad98a2a34e4bd7c2319ca7e1a9d6e3eb9c8d99f1245d3903c7e`
- Size: `1,281,469,816` bytes
- Status: `VITA_PASS_FINAL_LOCKED`

### sharedassets2.assets

- SHA-256: `80121aad85c0790472c474f2988f5ea5b41a2868eade45fabdfa5a9c6014b34d`
- Size: `3,382,312` bytes
- Status: `VITA_PASS_FINAL_LOCKED`

## Current cumulative v0.02 development Mother after M001

M002 and later v0.02 development work must start from this cumulative Vita-PASS state unless M001 itself is intentionally rebuilt and revalidated:

| File | SHA-256 |
| --- | --- |
| `level2` | `e4620fba82e4b50124c412d5a885ca9255be9e8590b3db0ec080122762bb2e73` |
| `level5` | `9d83c6183e0cb4d064d2bc69199059396c0f5d06e970c335777a37749ee9fff5` |
| `Managed/Assembly-CSharp.dll` | `ae2b1f2a6c008f05f19ad10dd4a7c963ef8b5294d2e8d3b538b387370149d90e` |
| `resources.assets` | `fe3c836c9f3a4ad98a2a34e4bd7c2319ca7e1a9d6e3eb9c8d99f1245d3903c7e` |
| `sharedassets2.assets` | `80121aad85c0790472c474f2988f5ea5b41a2868eade45fabdfa5a9c6014b34d` |
| `sharedassets3.assets` | `05474b778394a89e3f11f3081418a6256fda1a7a16ff23d702279713fa83638b` |
| `sharedassets5.assets` | `c43eed5af97a0f8b2feb826759fa5cbbca1641e47d65928f2fde91e554f1fa23` |
| `sharedassets6.assets` | `f67cbd9f3cc8752a32e7383c2d04578c466ae9f5913ca7bcc34570f5ac78a487` |

Do **not** start M002 from the older v0.01 `resources.assets=f19f...` or `sharedassets2=7cde...` cumulative files.

## Full-screen Strategy Tutorial textures

Both targets are in `resources.assets`.

### Page 1

- Name: `info1_set`
- PathID: `4363`

### Page 2

- Name: `info2_set`
- PathID: `2180`

Original assets:

- dimensions: `1024×512`
- TextureFormat: `12 = DXT5/BC3`
- payload: `524,288` bytes
- serialized object size: `524,364` bytes

M001 FINAL:

- dimensions: `1024×512`
- TextureFormat: `4 = RGBA32`
- payload: `2,097,152` bytes
- serialized object size: `2,097,228` bytes

### Accepted clean plate

The single maintained clean plate is `info2 V12`.

- V12: user approved / FINAL
- `info1` reuses the exact same clean base and differs only in translated body content.
- Older V3/V4/V5/V7/V8 clean-plate experiments are superseded.
- Known failures: V4 original-glyph residue; V8 black-spot contamination.

## Source-to-Vita transform

Source texture: `1024×512`

Vita screenshot: `960×544`

Measured average SIFT/RANSAC affine transform:

```text
x_screen ≈ 0.937448988 * x_source
           - 0.000068203 * y_source
           + 0.045778

y_screen ≈ 0.000064234 * x_source
           + 1.127019970 * y_source
           - 12.528998
```

Operational approximation:

- X scale: `0.93745×`
- Y scale: `1.12702×`
- Y offset: `-12.53 px`
- non-uniform stretch is real

All source-texture UI work must be evaluated in game/screen space before acceptance.

## Permanent typography rules confirmed by M001

### Translation width

Japanese line width is **not** an overlay target. Do not horizontally squeeze or expand Chinese text merely to match Japanese line length.

Match instead:

- visible glyph/font height;
- baseline / vertical center;
- line spacing;
- hierarchy;
- anchor/alignment logic;
- safe area;
- final game-space glyph aspect.

### Title hierarchy

Original:

- `戦略画面` = large
- `解説` = smaller

Chinese:

- `战略界面` = large
- `说明` = smaller

These levels must be measured independently.

### Special-symbol spacing

Locked form:

`按【 R 】键`

Do not use:

- `按 【R】 键`
- `按 【 R 】 键`

There are no outside spaces. Breathing room is placed only inside the full-width brackets.

## FINAL translated text

### Shared labels

Title:

- `战略界面`
- `说明`

Left:

- `回合信息`
- `战略指令`
- `资源/资材信息`

Right:

- `海域区域名`
- `当前舰队旗舰`
- `（秘书舰）`
- `舰队图标`

The central example screenshot's native Japanese UI is not redundantly translated.

### Page 1 body

```text
战略界面是《舰队Collection 改》的核心界面。
在这里可让舰队出击至作战海域、向相邻海域移动，
并可配置运输船等，以获取资源、确保兵站补给。
```

Blue emphasis must include:

- `战略界面`
- `出击`
- `移动`
- `配置`

`出击` is an explicit QC gate because it was accidentally left white in an earlier failed candidate.

### Page 2 body

```text
从战略界面可前往舰队旗舰所在的旗舰提督室，
按【 R 】键即可移动。
```

Blue emphasis:

- `战略界面`
- `旗舰提督室`
- `【 R 】`

## REDO4 failure and corrected RCA — historical record

REDO4 reached hardware with acceptable transparency and broad geometry, but newly rendered Chinese text showed severe low-bitrate/mosaic-like blockiness. It is rejected and must never be used as a cumulative Mother.

Controlled testing isolated two primary causes:

1. Pillow DXT5 encoder quality was materially worse than ImageMagick DXT5 on the same raster.
2. Supersampled antialiasing generated too many intermediate colors for BC3 4×4 blocks, whose RGB payload can represent only four colors per block.

Representative measurements:

- REDO4 same-raster Pillow: RGB MAE ~`14.46`, Alpha MAE ~`3.54`, PSNR ~`22.04 dB`
- REDO4 same-raster ImageMagick: RGB MAE ~`11.45`, Alpha MAE ~`0.75`, PSNR ~`24.78 dB`
- untouched Japanese one-generation Pillow recompress: PSNR ~`31.41 dB`
- untouched Japanese one-generation ImageMagick recompress: PSNR ~`48.41 dB`
- REDO4 text blocks: median ~`13` distinct RGB colors/block; P90 ~`16`

The project therefore stopped trying to rescue these two pages inside BC3.

## FINAL RGBA32 rendering strategy

The accepted M001 solution is:

- V12 background retained;
- text layer rendered with `8×` supersampling;
- a single Lanczos downsample to `1024×512`;
- final Texture2D stored as `RGBA32` (`TextureFormat = 4`);
- no BC3/DXT5 re-encoding for these two pages.

The user judged this candidate visually superior to the original, and the exact package subsequently passed PSV Vita hardware testing.

## RGBA32 SerializedFile rebuild

Unity version: `5.2.2p3`

`resources.assets` is SerializedFile v15. Its object table stores explicit `byteStart` and `byteSize` values.

Per converted Texture2D:

- old DXT5: 76-byte header + `524,288` payload
- new RGBA32: 76-byte header + `2,097,152` payload
- new object size: `2,097,228`
- net growth: `0x180000`

Compatibility evidence already existed in the same original game file: `header_bg2`, PathID `434`, uses TextureFormat `4` RGBA32.

The final structured rebuild preserves:

- object count;
- PathIDs;
- dataOffset;
- target object identity;
- non-target object bytes;
- gaps;
- expected downstream byteStart shifts only;
- zero unexpected metadata differences.

PSV Vita successfully loaded the rebuilt file, so this RGBA32 SerializedFile reconstruction method is now Vita-proven.

## TutorialGuide1

File: `resources.assets`

- Prefab root `TutorialGuide1`: PathID `29580`
- `Atlas_TutorialGuide`: PathID `1886` — unchanged
- Title UILabel: PathID `59638`
- Body UILabel: PathID `58051`
- R ButtonGuide uses the native `btn_R_l` Sprite

Final title:

`前往旗舰提督室界面`

`旗舰提督室` is highlighted green.

Final body visual structure:

- line 1: `按下` + native R Sprite + `键`
- line 2: `即可前往旗舰提督室！`

Do not replace the native R Sprite with textual `【 R 】` here; it is a real UI element positioned between `按下` and `键`.

## Dynamic-font `键` glyph fix

An earlier candidate serialized the character `键` correctly but rendered it blank on Vita. Therefore serialized string correctness is not sufficient hardware evidence.

Final fix in `sharedassets2.assets`:

- donor: true Simplified Chinese `键` outline from the UD Shin Go Pro font resource in `sharedassets3`
- target unused glyph: `cid15443`
- new mapping: `U+952E 键 → cid15443`
- existing ~9811 Unicode mappings preserved
- only U+952E mapping added
- all other glyph outlines preserved
- glyph metrics preserved
- Traditional `鍵` remains unchanged

Do not regress to an alias-based `键 → 鍵` workaround.

The exact final package passed Vita hardware testing, so the true-Simplified `键` glyph transplant is `VITA PASS / ACCEPTED`.

## Installer notes retained from M001

Two wrapper failures are permanently recorded:

1. CMD must be ASCII/no BOM; UTF-8 BOM caused `´╗┐@echo off`.
2. PowerShell must use descriptive hash helpers such as `Get-Sha256Hex` / `Get-BytesSha256Hex`; do not use a one-letter `H` function that can collide with shell aliases/history.

The final RGBA32 candidate followed these rules and was successfully used on Vita.

## M001 final disposition

**M001 = PSV Vita HARDWARE PASS / ACCEPTED / LOCKED.**

Historical REDO/BC3 failures remain useful RCA evidence but are superseded as active development state.

Next development work should begin as M002 from the cumulative M001 Vita-PASS file set above.
