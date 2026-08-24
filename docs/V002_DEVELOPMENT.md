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

### Sharpness root cause and replacement rendering pipeline

The REDO4 text pipeline rasterized Chinese at approximately Vita screen resolution, inverse-affine warped that 1× raster back into the 1024×512 source texture, encoded it to BC3/DXT5, and then let the game rescale it again. Dense Chinese strokes therefore suffered:

- an avoidable inverse-warp interpolation pass;
- BC3 4×4 color quantization on already-soft antialiased edges;
- a second non-uniform game rescale.

The replacement offline candidate uses a **source-direct high-resolution typography pipeline**:

1. render typography at 8× in final Vita geometry;
2. map each text item directly from that high-resolution artwork into its final source-space patch in one resampling step;
3. never create a 1× 960×544 text raster and inverse-warp the whole page;
4. optionally quantize edge coverage to a small number of BC3-friendly levels so blocks contain fewer blended colors;
5. BC3 roundtrip;
6. measured source→Vita transform simulation;
7. 3× nearest-neighbor OLD/NEW pixel QC before packaging.

The source-direct + BC3-friendly-edge result is currently **OFFLINE VISUAL CANDIDATE / Vita pending**, not PASS.

### Current next-candidate text decisions

Full-screen pages:

- right-side annotation: `当前舰队旗舰` / `（秘书舰）`;
- all other REDO3-approved wording, color emphasis, font heights, baselines, line spacing, and title hierarchy remain frozen unless explicitly reopened.

TutorialGuide1 body:

- line 1: `按下` + native R-button sprite + `键`
- line 2: `即可前往旗舰提督室！`

The previous missing `键` is now a dedicated hardware glyph gate: a future Vita candidate cannot PASS merely because the serialized string contains `键`; the glyph itself must visibly render on hardware.
