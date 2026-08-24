# v0.02 Development State

## M001 — Strategy Tutorial

### Rejected candidate

The first v0.02 M001 Vita candidate is **REJECTED** for the two full-screen strategy tutorial pages.

Reason: the Chinese layout was designed in raw 1024×512 texture space without first validating the actual Vita display transform, line spacing, baseline alignment, and strict overlay against original hardware screenshots.

Do not reuse the rejected full-screen tutorial raster/layout as a baseline.

The right-bottom `TutorialGuide1` UILabel translation is **not rejected by this finding** and remains pending hardware inspection.

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

### Mandatory redo rule

The Chinese tutorial typography is designed in Vita screen-space and then inverse-mapped back into the 1024×512 source texture.

**Japanese line width is not a matching target.** Chinese text must retain natural proportions. Required vertical/design targets are:

- visible font/glyph height;
- baseline or vertical center;
- line-center spacing / line spacing;
- anchor/alignment logic;
- safe-area fit and collision avoidance;
- independent main-title/subtitle sizing when the original uses multiple typographic levels.

Required QC before packaging a replacement Vita candidate:

1. Original Vita screenshot.
2. Chinese candidate simulated/decoded in Vita geometry.
3. 50% original/candidate overlay where meaningful.
4. Font-height and vertical-center/baseline guides.
5. Line-spacing comparison.
6. Separate title hierarchy comparison (`戦略画面` vs `解説`; `战略界面` vs `说明`).
7. BC3 roundtrip decode in game orientation.

### REDO3 approval and REDO4 surgical fixes

The user approved the REDO3 screen-space typography/layout, with two requested corrections only:

1. Page 1 second line: `出击` must use the original cyan/blue emphasis. Other Page 1 geometry is frozen.
2. Page 2 second line uses `按【 R 】键即可移动。`
   - no literal space before `【`;
   - no literal space after `】`;
   - spacing is inside the brackets only: `【 R 】`.

This special-symbol spacing convention is a persistent project typography rule and must be called out explicitly whenever similar controller/button notation appears in future translation work.

The right-bottom `TutorialGuide1` UILabel candidate remains unchanged and pending Vita inspection.

No REDO4 component may be marked `VITA PASS` until the exact REDO4 binary is tested on hardware.
