# v0.02 Development State

## M001 — Strategy Tutorial

### Rejected candidate

The first v0.02 M001 Vita candidate is **REJECTED** for the two full-screen strategy tutorial pages.

Reason: the Chinese layout was designed in raw 1024×512 texture space without first validating the actual Vita display transform, line spacing, baseline alignment, and strict overlay against original hardware screenshots.

Do not reuse the rejected full-screen tutorial raster/layout as a baseline.

### Accepted clean plate

The project uses a single clean plate based on `info2_set`:

- `info2` V12 clean plate: user visually approved / FINAL clean-plate baseline.
- `info1` must reuse the exact same clean plate; only the translated body copy differs between page 1 and page 2.

### Source-to-Vita transform — measured from original hardware screenshots

Original texture size: `1024×512`

Original Vita screenshots: `960×544`

Independent SIFT/RANSAC affine registration of original `info1_set` and `info2_set` against the supplied Vita screenshots produced nearly identical transforms. Average transform:

```text
x_screen ≈ 0.937448988 * x_source - 0.000068203 * y_source + 0.045778
y_screen ≈ 0.000064234 * x_source + 1.127019970 * y_source - 12.528998
```

Operational interpretation:

- X scale: approximately `0.93745×`
- Y scale: approximately `1.12702×`
- Y offset/crop: approximately `-12.53 px`
- non-uniform stretch is real and must be included in layout QC

### Mandatory layout rule

**Japanese line width is not a matching target.** Chinese text must retain natural proportions. Required typography targets are:

- visible font/glyph height;
- baseline or vertical center;
- line-center spacing / line spacing;
- anchor/alignment logic;
- safe-area fit and collision avoidance;
- independent main-title/subtitle sizing when the original uses multiple typographic levels.

Required visual QC before packaging a Vita candidate:

1. Original Vita screenshot.
2. Chinese candidate simulated/decoded in Vita geometry.
3. 50% original/candidate overlay where meaningful.
4. Font-height and vertical-center/baseline guides.
5. Line-spacing comparison.
6. Separate title hierarchy comparison (`戦略画面` vs `解説`; `战略界面` vs `说明`).
7. BC3 roundtrip decode in game orientation.

### REDO3 layout approval

The user approved the REDO3 screen-space layout after the width-matching constraint was removed. Persistent accepted layout rules include:

- Chinese width is natural and unconstrained except for safe-area/collision limits.
- `战略界面` and `说明` use separate title sizes matching the original hierarchy.
- Page 1 `出击` uses cyan emphasis.
- Page 2 control notation uses `按【 R 】键即可移动。`; there are no spaces outside the full-width brackets and spaces are inside only.

### REDO4 hardware result — REJECTED as a cumulative development baseline

REDO4 was tested on PSV Vita on 2026-08-24.

Hardware findings:

1. The two full-screen tutorial pages had correct transparency and broadly correct geometry, but all newly rendered Chinese text showed severe blocky/mosaic blur resembling low-bitrate video. The full-screen REDO4 raster is therefore **FAIL / REJECTED** and must not become the next cumulative Mother.
2. Right-side fleet annotation was too close to the safe boundary. Replacement wording is locked for the next candidate:
   - line 1: `当前舰队旗舰`
   - line 2: `（秘书舰）`
3. `TutorialGuide1` displayed the previous body string with the `键` glyph missing on hardware. The desired replacement body is:
   - line 1: `按下` + native R-button sprite + `键`
   - line 2: `即可前往旗舰提督室！`
   The R sprite should be positioned as a real UI element rather than approximated with spaces if needed.
4. `TutorialGuide1` title may remain `前往旗舰提督室界面` with `旗舰提督室` highlighted green unless later reopened.

Because REDO4 failed hardware visual quality, the next M001 candidate must again start from **v0.01 FINAL** `resources.assets` SHA-256:

`f19fbcf5f2be01bd386ff4f126688ab7685f3df3426881924797863348f7fce8`

Do not patch on top of REDO4.

### Corrected strict RCA — full-screen tutorial mosaic blur

The earlier explanation that the extra inverse-affine transform was the main cause was incomplete. Controlled A/B testing on 2026-08-24 identifies two primary causes and two secondary contributors.

#### PRIMARY #1 — Pillow DXT5 encoder quality

Using the **exact same REDO4 uncompressed raster** in the body-text region:

- Pillow DXT5: RGB MAE `14.46`, Alpha MAE `3.54`, PSNR `22.04 dB`
- ImageMagick DXT5: RGB MAE `11.45`, Alpha MAE `0.75`, PSNR `24.78 dB`

This is an encoder-only comparison; layout and source pixels are identical.

A stronger control test used the untouched original Japanese `info1_set` decoded texture and compressed it one extra generation without editing any pixels:

- Pillow DXT5: RGBA MAE `2.16`, Alpha MAE `3.20`, PSNR `31.41 dB`
- ImageMagick DXT5: RGBA MAE `0.47`, Alpha MAE `0.42`, PSNR `48.41 dB`

Therefore Pillow's DXT5 encoder is formally rejected for these dense text textures. It adds materially more generation loss even to the original Japanese artwork.

#### PRIMARY #2 — too many antialias/interpolation colors per BC3 block

REDO4's supersampled/resampled text produces a very high number of intermediate RGB edge colors before compression.

For 4×4 blocks touched by body text:

- REDO4 supersampled raster: median `13` distinct RGB colors/block; P90 `16`
- Native 1× hinted test raster: median `7`; P90 `12`

BC3's color payload is BC1-like and can represent only **4 RGB colors per 4×4 block**. The REDO4 raster therefore forces aggressive color collapse of white fill, gray outline, cyan emphasis, blue background, and multiple antialias shades. This is the direct mechanism behind the visible low-bitrate/mosaic appearance.

With native-pixel/hinted text plus ImageMagick DXT5, the same test body region improves further to:

- RGB MAE `8.06`
- Alpha MAE `0.44`
- PSNR `26.63 dB`

This proves that reducing pre-BC3 edge-color complexity matters independently from changing the encoder.

#### CONTRIBUTOR — dense/fine CJK geometry

Supporting measurement from the source-space body mask:

- original Japanese mean effective mask thickness: approximately `3.53 px`, P90 `7.00 px`
- REDO4 Chinese: approximately `3.01 px`, P90 `5.79 px`

Chinese strings also contain more dense high-frequency stroke transitions. That makes block quantization more visible. This does **not** justify changing font height or compressing text width; any weight/hinting adjustment must preserve the already approved game-space typography geometry.

#### SECONDARY — game non-uniform scaling

The measured `X≈0.93745 / Y≈1.12702` game transform magnifies codec damage that already exists after BC3 decode. It is not the primary source of the mosaic artifact.

#### Ruled out as root causes

- Clean-plate transparency: hardware transparency is visually correct.
- Overall 1024×512 texture resolution: the original Japanese text is sharp at the same texture resolution.
- Vita screenshot/capture quality: original Japanese text in the same hardware capture remains substantially cleaner.
- Layout/line spacing: REDO3 geometry was user-approved before the sharpness failure was isolated.

### Mandatory replacement rendering/encoding pipeline

The previous `high-resolution source-direct + Pillow DXT5` concept is superseded. High-resolution supersampling alone does not solve this issue and can increase intermediate edge colors.

For the next candidate:

1. start from the accepted V12 clean plate and **v0.01 FINAL** Mother;
2. retain the approved REDO3 font heights, baselines, line spacing, anchors, title hierarchy, and natural Chinese width;
3. rasterize dense baked CJK text with source-pixel-aware/hinted geometry that minimizes unnecessary intermediate edge colors;
4. avoid whole-page or 1× screen inverse-affine rasterization;
5. avoid gratuitous high-order supersampling/downsampling if it increases per-block color complexity;
6. use a higher-quality BC3 encoder; **Pillow DXT5 is prohibited for this component**;
7. after encoding, decode the actual BC3 payload and inspect at normal game orientation;
8. run measured Vita-transform simulation;
9. produce 3× or greater nearest-neighbor comparison against the previous hardware failure and original Japanese reference;
10. only then package a Vita candidate.

Current corrected status: **RCA COMPLETE / replacement raster+encoder candidate not yet hardware validated**.

### Current next-candidate text decisions

Full-screen pages:

- right-side annotation: `当前舰队旗舰` / `（秘书舰）`;
- all other REDO3-approved wording, color emphasis, font heights, baselines, line spacing, and title hierarchy remain frozen unless explicitly reopened.

TutorialGuide1 body:

- line 1: `按下` + native R-button sprite + `键`
- line 2: `即可前往旗舰提督室！`

The previous missing `键` is now a dedicated hardware glyph gate: a future Vita candidate cannot PASS merely because the serialized string contains `键`; the glyph itself must visibly render on hardware.
