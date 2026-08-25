# v0.02 M002 — PortTop Shortcut Menu RGBA32

## Current status

**Visual revision: `V4.25R2`**

Status as of 2026-08-25:

**USER VISUAL APPROVED / TYPOGRAPHY FINAL / WRITEBACK PACKAGE READY / EXACT MOTHER REPLAY PENDING / PSV VITA VALIDATION PENDING**

This is not a hardware PASS yet. The exact cumulative `sharedassets5.assets` output SHA-256 must first be produced from the required Mother, and that exact output must then pass PSV Vita testing.

## Scope

M002 is deliberately limited to the normal PortTop shortcut/command menu.

Scene mapping:

- `level15` = `Port/PortTop.unity`

Primary asset:

- file: `sharedassets5.assets`
- Texture2D: `Atlas_ShortCutMenu`
- PathID: `367`
- Material PathID: `80`
- UIAtlas metadata PathID: `25750`
- dimensions: `1024×1024`

The menu translation set currently covered by this component is:

- `入渠`
- `工厂`
- `改装`
- `编成`
- `母港`
- `改修`
- `任务`
- `战略`
- `补给`
- `物资`
- `记录`

Both normal and highlighted states are redrawn through the same calibrated visual system.

## Required development Mother

M002 must start from the current cumulative Vita-accepted `sharedassets5.assets`:

- size: `54,898,340` bytes
- SHA-256: `c43eed5af97a0f8b2feb826759fa5cbbca1641e47d65928f2fde91e554f1fa23`

The clean 1.02 file is useful for asset discovery and structural testing, but it is **not** the M002 development Mother.

## V4.25R2 visual replication SOP

The user approved V4.25R2 as the target visual feel for this component. This is also the preferred precedent for future baked UI text when the same method is applicable.

### 1. Redraw the entire line

Never preserve/cut out an original glyph merely because the same character remains after translation.

The entire original text raster is cleaned, and every character in the translated label is redrawn through one consistent pipeline.

### 2. Reference-glyph redraw calibration

Use unchanged/comparable original glyphs as calibration anchors only.

M002 reference set:

- `工` from `工廠`
- `成` from `編成`
- `任` from `任務`
- `略` from `戦略`
- `物` from `物資`

For each reference:

`original glyph -> freshly redrawn same glyph -> 50% overlay`

Adjust the shared rendering parameters until the redrawn reference nearly reproduces the original visible size and stroke weight. Do not reuse the original raster.

### 3. Whole-line coherence

Per-glyph boxes are measurement aids, not independent vertical placement instructions.

Locked V4.25R2 geometry:

- font size: `32 px`
- horizontal normalization: `0.96×`
- shared baseline: `Y = 36`
- nominal character centers: `X = 95 / 141`
- calibrated weight: `V4.25`
- each glyph expands `2 px` toward the word interior relative to V4.25 while the outer line edges remain fixed

This preserves a coherent two-character line while correcting the narrower perceived proportion of the Simplified Chinese outlines.

### 4. Reproduce the original material effect, not just the glyph silhouette

The PortTop original is visually **recessed/engraved**, not raised.

V4.25R2 therefore uses:

- narrow dark inner groove;
- narrow bright inner bevel edge;
- no soft drop shadow;
- no full-mask multi-layer ghost;
- deliberately sharpened edge transition to reproduce the original etched appearance.

Relief direction and sharpness must be inferred from the original pixels rather than applied from a generic text-effect preset.

### 5. Calibrate color from final visible original pixels

Do not choose the internal text fill by eyeballing a nominal RGB swatch alone.

For M002, original visible reference-glyph midtones were measured in the rendered button:

- OFF original visible median approximately `RGB (195,195,198)`
- ON original visible median approximately `RGB (66,149,198)`

The final V4.25R2 target was nudged slightly darker:

- OFF target approximately `RGB (191,191,194)`
- ON target approximately `RGB (63,145,194)`

Because the body color is composited with the button background/effect alpha, the internal fill was solved from the final visible target:

- OFF internal body approximately `RGB (171,171,175)`
- ON internal body approximately `RGB (31,129,187)`

Persistent lesson: **measure the final visible original result, account for compositing/background, then solve the candidate internal color needed to reproduce that visible result.**

### 6. Final visual evidence

The accepted pre-writeback QC set includes:

- multiple same-glyph reference overlays;
- all-button original vs Chinese OFF/ON side-by-side;
- full-label 50% overlays;
- shared baseline/character-center guides.

V4.25R2 was explicitly user-approved for visual appearance before binary writeback.

## RGBA32 writeback

The original target is:

- TextureFormat: `12` = DXT5/BC3
- DXT payload size: `1,048,576`
- serialized Texture2D object size: `1,048,660`

M002 candidate rebuild:

- TextureFormat: `4` = RGBA32
- RGBA payload size: `4,194,304`
- serialized Texture2D object size: `4,194,388`
- object growth: `3,145,728` bytes = `0x300000`
- expected full `sharedassets5.assets` output size: `58,044,068` bytes

Source BC3 payload SHA-256:

`cb7168657ab5b609ae5bcb1f91de84847748f681481377585c568cc960a8ac46`

Approved reconstructed RGBA32 payload SHA-256:

`cb65fd1d1e1738ccb54517ee8289f31385faef0a186a41109686b35816124212`

The local BC3 decoder used by the writeback tool was verified pixel-identical against the previously decoded atlas before delta application.

## Changed-pixel reconstruction payload

To avoid distributing a complete proprietary atlas, the test package stores only the approved changed-pixel delta.

- changed pixels: `47,035`
- compressed delta size: `163,758` bytes
- delta SHA-256: `9249d9f2901d0a2f3710de834a06b00191f9d5d288586bcf47a5ac019ca793fd`

The patcher:

1. verifies the exact `c43eed5a...` Mother;
2. validates PathID 367 and the source BC3 payload;
3. decodes the Mother BC3 locally;
4. applies only the approved changed-pixel delta;
5. verifies the reconstructed RGBA32 payload hash;
6. performs a SerializedFile v15 rebuild;
7. verifies target growth, downstream `byteStart` shifts, target header fields, object count/PathIDs, and non-target byte preservation;
8. emits the rebuilt file plus an exact SHA-256 report.

## Test package

Local hardware test package:

`Kancolle_Kai_v0.02_M002_PortTop_RGBA32_V425R2_TESTPACK.zip`

- size: `681,056` bytes
- SHA-256: `c8fc59f37b0fa5166b700f0225a2fe935a3337c8010b66b9a9c1a6589b4e8d09`

The package does not contain a complete `sharedassets5.assets` file.

## Structural testing vs exact candidate testing

A structurally equivalent clean-1.02 test was used only to validate the rebuild algorithm:

- output size: `58,044,068`
- unexpected metadata diff: `0`
- non-target data preservation: PASS
- reconstructed RGBA payload hash: exact

The clean-source structural-test output SHA-256 was:

`b2417a8cc091924e5b819d9ac2afb5f4bebde61d4df28b116e13b72e31123944`

**This is not the M002 candidate full-file hash and must never be recorded as such.**

The correct cumulative output full-file SHA-256 remains unknown until the writeback tool is run against the exact required Mother:

`c43eed5af97a0f8b2feb826759fa5cbbca1641e47d65928f2fde91e554f1fa23`

After that replay, record the exact output SHA-256 and test that exact binary on PSV Vita.

## Final disposition before hardware test

V4.25R2 visual design is frozen unless explicitly reopened.

Binary/hardware state remains fail-closed:

**WRITEBACK PACKAGE READY / EXACT MOTHER REPLAY PENDING / PSV VITA PENDING**

Do not advance the cumulative M002 Mother or mark this component `VITA PASS` until the exact output hash has been produced and hardware accepted.
