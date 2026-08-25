# QC Policy

This project uses fail-closed QC. A component is PASS only when the required evidence is produced from the current files.

## Core release rule

Any failed, missing, unknown, or unreproduced critical gate means `FAIL` or `INCOMPLETE`, never PASS.

Offline QC and PSV Vita hardware validation are separate states.

## Mandatory source-to-game geometry gate

For **every visual modification based on an original game texture, atlas, screenshot-like tutorial page, or other pre-rendered UI material**, the source-space edit must not be approved from the raw texture alone.

Before editing or approving the layout, the project must determine and record the actual source-to-game display transform from original game evidence whenever practical, including:

- source texture dimensions;
- game/screenshot dimensions;
- horizontal scale / stretch ratio;
- vertical scale / stretch ratio;
- translation / crop offset;
- orientation.

If the game applies non-uniform scaling, the Chinese layout must be designed and QC'd in **game/screen space** and mapped back to source-space without unnecessary raster resampling. Raw source-space appearance is not sufficient.

## Mandatory overlay and typography gate

For source-based UI/text replacements, final visual QC must include, as applicable:

- original game-space reference;
- Chinese simulated or decoded game-space result;
- strict overlay (normally 50% original + 50% candidate and/or edge overlay);
- vertical text extent / font-height comparison;
- horizontal/vertical anchors where they are semantically meaningful;
- baseline or vertical-center comparison;
- line-spacing comparison;
- stretch/aspect comparison;
- target-region absolute diff.

### Reference-glyph redraw calibration rule

When an original UI label and its Chinese replacement contain one or more identical characters, or when another nearby original glyph can act as a trustworthy typography reference, those glyphs should be used as **calibration anchors**, not preserved raster fragments.

If the target label is being rebuilt, do **not** keep/copy the original pixels of an unchanged character merely because that code point remains the same. The full original text region should be cleaned and the **entire translated line should be redrawn through one consistent rendering pipeline**.

Required calibration method when practical:

1. Choose several representative original glyphs that also exist in the target rendering pipeline. Prefer references with different stroke structures rather than relying on only one glyph.
2. Redraw those same reference glyphs from font/vector outlines using the exact candidate rasterization, weight, bevel/outline/shadow, and antialiasing pipeline intended for the translated UI.
3. Compare `original reference glyph → redrawn same glyph → 50% overlay` in the correct source/game geometry.
4. Adjust shared/global typography parameters until the **redrawn** reference glyphs nearly match the original visible size and stroke weight. Relevant parameters include font size, font weight or controlled synthetic weight, horizontal/vertical scale only when justified, baseline/midline, character advance/tracking, and effect geometry.
5. Once calibrated, freeze the shared parameters and apply them to **all glyphs in that line/component**, including characters whose translation did not change.
6. If missing Simplified Chinese glyphs require a donor font/outline source, normalize the donor glyph metrics/weight to the calibrated line rather than independently positioning each donor character.

Per-glyph bounding boxes are a **measurement tool**, not an instruction to vertically center every glyph independently. A multi-character label must remain a coherent line: use one shared baseline or visual midline and a deliberate character advance/tracking model for the whole label.

For v0.02 M002 PortTop shortcut-menu calibration, the explicit reference set is:

- `工` from `工廠`
- `成` from `編成`
- `任` from `任務`
- `略` from `戦略`
- `物` from `物資`

These characters are to be redrawn and overlaid against the original to establish size/weight; they are **not** to be cut out of the original atlas and reused in the Chinese raster.

Recommended evidence for this method includes:

- multiple reference-glyph original/redraw/50% overlay comparisons;
- visible-width/height or stroke-weight measurements;
- full-line baseline/midline and character-spacing guides;
- full-label 50% overlay;
- final game-space inspection after codec/format writeback.

This rule is persistent and should be reused for any future UI/texture work where unchanged or comparable original glyphs can serve as reliable typography calibration anchors.

### Translation-width rule

**Translated line width is not an overlay target by itself.** Japanese and Chinese strings naturally have different lengths. The Chinese layout must keep normal glyph proportions and must not be horizontally squeezed or expanded merely to reproduce the original Japanese line width.

For translated text, the primary typography constraints are:

- natural glyph aspect ratio in final game/screen space;
- font height / visible glyph height consistent with the original design;
- baseline or vertical center consistent with the original design;
- line-center spacing / line spacing consistent with the original design;
- correct alignment or anchor logic;
- remaining within the intended safe area without collisions or clipping.

Horizontal width may differ naturally. It becomes a QC constraint only if the translated text collides with another element, clips, crosses an intended safe boundary, or violates a specific alignment rule.

When a title contains multiple typographic levels, each level must be measured separately. For example, the Strategy Tutorial title uses a larger `戦略画面` main title and a smaller `解説` subtitle; the Chinese `战略界面` and `说明` must preserve that hierarchy rather than being rendered at one common size.

Line breaks, baseline positions, line spacing, vertical size, and text hierarchy must be deliberately matched to the original design. A layout must not be accepted merely because the Chinese text fits inside the texture.

If these measurements/evidence are missing, the visual build is `INCOMPLETE` and must not be packaged as a Vita candidate.

### Special-symbol spacing rule

For control labels, button legends, bracketed keys, controller symbols, and similar special UI notation, **do not add literal spaces immediately outside the symbol/brackets** unless the original design specifically requires them.

Preferred pattern when extra visual breathing room is needed around a single key label:

- correct: `按【 R 】键`
- avoid: `按 【R】 键`
- avoid: `按 【 R 】 键`

Operational rule:

- keep surrounding Chinese text directly adjacent to the outer brackets/symbol;
- when the full-width brackets themselves look visually cramped, add spacing **inside** the brackets, e.g. `【 R 】`;
- do not silently normalize these spaces during later edits;
- every time a translated UI string contains this kind of special symbol, the assistant must explicitly tell the user which spacing form is being used so it can be visually confirmed.

This is a persistent project typography rule.

## Clean-plate gate

A clean plate must remove the original glyphs, outlines, shadows, and alpha contamination without introducing visible smears, dark blobs, seams, or flattened background texture.

Scope metrics such as `outside-mask changed = 0` are supporting evidence only. They do not override visible defects.

## BC3 / DXT5 gate

Codec integrity does not equal visual correctness. Texture work must be decoded after the actual BC3/DXT5 write and inspected in game orientation. Non-target blocks should remain byte-identical whenever the patch design permits.

### Encoder-quality gate

The BC3 encoder itself is part of the release surface and must be validated. Do not assume all DXT5 encoders are visually equivalent.

For v0.02 M001 dense tutorial text, controlled testing proved Pillow DXT5 materially worse than ImageMagick DXT5 on the exact same raster. Pillow also introduced much larger generation loss when recompressing untouched original Japanese artwork. Therefore:

- **Pillow DXT5 is prohibited for the v0.02 M001 full-screen tutorial pages**;
- if an encoder is changed, the same uncompressed raster must be A/B roundtripped through both encoders and compared with objective metrics and pixel QC;
- encoder selection must be based on the actual target texture/content, not convenience.

Recommended evidence includes RGB MAE, Alpha MAE, PSNR, and 3× or greater nearest-neighbor visual comparisons.

### Pre-BC3 color-complexity gate

BC3 color encoding can represent only 4 RGB colors per 4×4 block. Dense antialiased CJK can easily exceed this capacity before compression.

Before encoding dense baked text, inspect 4×4 blocks touched by text and measure/inspect color complexity. A pipeline that creates many unnecessary antialias/interpolation colors is a release risk even when the uncompressed PNG looks excellent.

Avoid:

- high-order supersampling/downsampling that creates large numbers of intermediate shades with no demonstrated post-BC3 benefit;
- unnecessary inverse-affine raster transforms;
- repeated lossy BC3 generations;
- assuming a sharper pre-BC3 PNG will remain sharper after BC3.

Prefer source-pixel-aware/hinted rasterization and the smallest number of necessary resampling steps, while preserving approved screen-space font height, baseline, line spacing, title hierarchy, and natural Chinese proportions.

### Sharpness evidence gate

When sharpness is a concern for a lossy texture path, required evidence should include:

- uncompressed source candidate;
- actual codec roundtrip decode from the selected encoder;
- simulated/measured game transform;
- 3× or greater nearest-neighbor OLD/NEW pixel comparison;
- inspection for block color bleeding, mosaic artifacts, low-bitrate-like smearing, and softened CJK strokes;
- encoder A/B comparison when the codec may be implicated.

A texture that is structurally valid but visibly blocky or blurry is `FAIL`.

## RGBA32 structured-rebuild gate

Lossy BC3 is not mandatory when the target game and file format demonstrably support an uncompressed format and the structured rebuild can be proven correct.

v0.02 M001 established a Vita-proven RGBA32 path for `resources.assets` SerializedFile v15 under Unity `5.2.2p3`.

For any future Texture2D format conversion or object growth using this method, required binary evidence includes:

- target object identity and PathID preserved;
- object count preserved;
- expected TextureFormat and image byte size recorded;
- SerializedFile `dataOffset` preserved unless there is a documented reason to change it;
- target `byteSize` updated correctly;
- all downstream `byteStart` values shifted by exactly the required cumulative growth;
- non-target object bytes preserved byte-for-byte where expected;
- inter-object gaps/padding preserved where expected;
- unexpected metadata differences = 0;
- reconstructed file hash and size recorded;
- exact candidate tested on PSV Vita before `VITA PASS`.

For the accepted M001 conversion:

- `info1_set`, PathID `4363`: DXT5/BC3 → RGBA32
- `info2_set`, PathID `2180`: DXT5/BC3 → RGBA32
- dimensions remain `1024×512`
- payload changes from `524,288` to `2,097,152` bytes per texture
- object size changes from `524,364` to `2,097,228`
- net growth is `0x180000` per converted object
- original `resources.assets` already contained RGBA32 `header_bg2`, PathID `434`, providing in-game format compatibility evidence

The exact final rebuilt `resources.assets` SHA-256 is:

`fe3c836c9f3a4ad98a2a34e4bd7c2319ca7e1a9d6e3eb9c8d99f1245d3903c7e`

This file passed PSV Vita hardware validation on 2026-08-24. The method is therefore **Vita-proven for this file/version**, not merely structurally plausible.

The BC3 encoder/color-complexity RCA remains a permanent QC lesson, but the accepted M001 full-screen pages themselves no longer use BC3.

## Dynamic-font / glyph gate

For runtime UILabel or other dynamic-font text, a serialized string containing the intended character is **not sufficient evidence** that the glyph will render.

If a character has previously disappeared, rendered blank, or been substituted on Vita, that character becomes an explicit hardware glyph gate. The exact character must be visibly present in a hardware screenshot before the component can be marked `VITA PASS`.

Example: in v0.02 M001 `TutorialGuide1`, the character `键` disappeared on hardware in a previous candidate.

The accepted fix uses a true Simplified Chinese glyph outline rather than a Traditional alias:

- `U+952E 键 → cid15443`
- donor outline from the UD Shin Go Pro Simplified Chinese font resource
- Traditional `鍵` is not modified
- exact final `sharedassets2.assets` SHA-256: `80121aad85c0790472c474f2988f5ea5b41a2868eade45fabdfa5a9c6014b34d`

The exact final candidate visibly rendered `键` on Vita and passed hardware validation. This mapping is therefore `VITA PASS / ACCEPTED` and must not regress to `键 → 鍵` aliasing.

## Hardware gate

`VITA PASS` may only be assigned after the exact candidate binary is tested successfully on PSV Vita.

A hardware PASS applies to the exact validated output hashes. Any later binary modification reopens the affected gate unless independent evidence proves the change cannot affect it.

## v0.02 M001 historical failures and final disposition

The first `Strategy Tutorial` M001 candidate derived from v0.01 `resources.assets` (`f19fbcf5...fce8`) was rejected because source-to-game non-uniform stretch and original line-spacing/layout were not validated before packaging.

REDO4 was later tested on hardware. Its transparency and overall layout were broadly acceptable, but the two full-screen Chinese tutorial pages showed severe blocky/mosaic blur. REDO4 is rejected as a cumulative development baseline.

Strict RCA showed the main causes were poor Pillow DXT5 roundtrip quality and excessive pre-BC3 edge-color complexity from the rasterization pipeline; non-uniform game scaling was secondary.

The final accepted M001 superseded the failed BC3 path by using the V12 clean background plus SS8 text-layer rendering, one Lanczos downsample to `1024×512`, and RGBA32 Texture2D storage for `info1_set` and `info2_set`. `TutorialGuide1` also received the true Simplified `键` glyph transplant described above.

Exact Vita-tested package:

`Kancolle_Kai_v0.02_M001_RGBA32_VITA_CANDIDATE.zip`

SHA-256:

`2e0f1a312dbf4f0618ac2860aa4ee72943045c79253ae69912e0bd8cdcf22eb8`

Final status as of 2026-08-24:

**v0.02 M001 = PSV Vita HARDWARE PASS / ACCEPTED / LOCKED.**

Future M002 development must use the M001 cumulative Vita-PASS files as its development Mother. A future formal v0.02 release must still be normalized to deterministic clean-1.02 → v0.02 FINAL patches and independently replayed byte-for-byte.
