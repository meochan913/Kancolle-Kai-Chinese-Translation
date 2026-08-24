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

All translated text for these pages must be laid out with the original source-space text boxes and line spacing as targets, then validated after applying the measured source→Vita transform.

Required QC before packaging a replacement Vita candidate:

1. Original Vita screenshot.
2. Chinese candidate simulated/decoded in Vita geometry.
3. 50% original/candidate overlay.
4. Original vs Chinese text bbox overlay.
5. Baseline and line-spacing comparison.
6. Font-height comparison.
7. BC3 roundtrip decode in game orientation.

No replacement M001 Vita candidate may be packaged until these visual gates pass.
