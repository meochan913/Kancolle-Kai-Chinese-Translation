# Tutorial Texture Rendering SOP

This document is the durable implementation handoff for baked tutorial-text texture work. Future sessions must read this file before modifying `info*_set` tutorial pages.

It exists because previous handoffs preserved final screenshots and high-level QC rules but omitted enough implementation detail that later sessions could reproduce the visual direction only approximately.

## 1. Mandatory workflow order

Do not start by drawing Chinese text onto a cleaned image.

For every baked tutorial page, the required order is:

1. identify the exact original Texture2D / PathID / dimensions / orientation;
2. obtain the original decoded game-space/source-space raster;
3. build or load the accepted clean plate;
4. determine the actual source-to-game transform from original hardware evidence;
5. measure the original typography from pixels;
6. select the correct localized Chinese font face explicitly;
7. lock translation text and blue-highlight semantic segments;
8. render Chinese in the accepted supersampled text pipeline;
9. map/downsample once to source-space;
10. perform strict overlay / line-spacing / font-height / safe-area QC;
11. only after visual approval, write the Texture2D / rebuild the SerializedFile;
12. re-decode/reconstruct the exact written candidate and repeat visual QC;
13. PSV Vita hardware validation is a separate final gate.

If step 5 is missing, the render is `INCOMPLETE`. A page-level visual impression or broad 50% overlay is not a substitute for measured line geometry.

## 2. Source-to-Vita geometry for the strategy tutorial pages

For the 1024×512 strategy tutorial pages (`info1_set` onward), the measured source-to-Vita affine established from original Vita screenshots is:

```text
x_screen ≈ 0.937448988 * x_source
           - 0.000068203 * y_source
           + 0.045778

y_screen ≈ 0.000064234 * x_source
           + 1.127019970 * y_source
           - 12.528998
```

Operational approximation:

- X scale ≈ `0.93745×`
- Y scale ≈ `1.12702×`
- Y translation ≈ `-12.53 px`

This is non-uniform scaling. Raw 1024×512 source appearance is not sufficient for typography approval.

## 3. Accepted M001 info1/info2 clean-plate history

### 3.1 Final accepted base

`info2 V12 Clean Plate` is the accepted common clean background for M001 info1/info2.

`info1` and `info2` share the same underlying page background; after cleaning, the same clean master is reused and page differences are introduced only by translated text.

### 3.2 Final V12 corrective algorithm: A8 / D0

The final accepted corrective stage was not broad inpaint, rectangular color fitting, clone-stamp reconstruction, or a patch-based generic fill.

The recovered implementation is:

**glyph-local same-row RGBA interpolation using an A8 / D0 mask.**

For the info2 body region, the working ROI was approximately:

```text
x = 140..845
y = 380..462
```

For each scanline, estimate clean background alpha from safe side margins, conceptually:

```text
base_alpha(y) = median(
    original[y, left_clean_margin, alpha]
    + original[y, right_clean_margin, alpha]
)
```

The practical side-margin ranges used during the accepted work were around the far-left and far-right clean panel margins (approximately x 20..130 and x 875..980, adjusted when necessary to avoid art).

Build a text/residue mask from:

- white/light text pixels;
- cyan/blue-highlight text pixels;
- alpha pixels significantly above the row background baseline.

The final threshold branch was:

```text
alpha_hi = Alpha > base_alpha + 8
```

Hence `A8`.

Candidate branches with mask dilation were tested. The accepted final branch uses:

```text
D0 = no additional morphological dilation
```

For each contiguous masked glyph/residue run `[s,e]` on one row:

1. find the nearest clean non-mask pixel to the left (`L`);
2. find the nearest clean non-mask pixel to the right (`R`);
3. linearly interpolate **R, G, B, and Alpha** from `L` to `R`;
4. write only the masked run `[s,e]`;
5. do not alter surrounding clean pixels.

This local same-row method was chosen because it removes glyph/outline/alpha residue without creating the large flat rectangles, dark blobs, or smear bands seen in rejected experiments.

Important provenance note: V12 was a corrective stage applied over an earlier V1 clean plate. The exact original code that generated every V1 pixel was not preserved. Do not invent a missing V1 algorithm name. What is preserved here is the final V12 A8/D0 corrective logic and the accepted resulting clean master.

## 4. info3–6 clean-slate reconstruction notes

Current accepted working clean candidate family: `info3_6 Clean Slate Refined V4` (visual review stage; not yet Vita-validated as final translated pages).

Key rules:

- preserve page-specific artwork and overlays;
- `info4` right-side Japanese ship-category list is explicitly protected and remains untranslated;
- seaplane/waterplane logo areas are protected;
- `info6` command icons and panel shapes/colors are protected, while command text/explanations are cleared for translation.

Useful background fact discovered during reconstruction:

The blue semi-transparent panel background used across these tutorial pages shares exact or near-periodic pixel structure with the accepted V12 background. Multiple clean regions are RGBA-identical at the same coordinates, and the panel texture shows an approximately 49–50 px vertical repetition.

Therefore, for difficult clean regions prefer real V12 donor pixels / periodic V12 donor rows plus page-specific row correction, rather than inventing a flat color rectangle.

The refinement used for info3/info5 bottom-right residue takes same-coordinate V12 RGBA donor pixels where the background/logo alignment is proven. The seaplane logo itself must remain byte/pixel unchanged.

For info6 command panels, command text is removed while preserving the panel and icon geometry. The command panel background may be reconstructed from its own local panel colors/gradients; do not flatten the full page background or damage button icons.

Every new clean-plate revision still requires 1× and magnified visual inspection. Protected-region changed-pixel counts are supporting evidence, not visual PASS by themselves.

## 5. Original typography measurement — mandatory, pixel-driven

This is the most important layout rule for M002.

**Do not type approximate Y ranges by eye and start rendering.**

Before rendering, derive original text geometry from original raster pixels. Recommended method for pages with an accepted clean plate:

1. compute original-vs-clean difference;
2. restrict to the intended text ROI;
3. intersect with source white/cyan text-color evidence and appropriate alpha evidence;
4. use a conservative difference threshold to suppress background reconstruction noise;
5. derive contiguous row bands for each original text line;
6. record, per line:
   - source top row;
   - source bottom row;
   - visible source height;
   - source line center;
   - transformed Vita screen center;
   - adjacent line-center spacing;
7. measure title main/subtitle and all body typography tiers separately.

The render must be driven by these measurements.

A strict overlay image must additionally show original/candidate line guides. A broad 50% page overlay without the underlying measurements does not satisfy the gate.

## 6. M002 info3–6 measured original line bands

These ranges are extracted from original-vs-clean pixel evidence and are the current measurement baseline. Re-measure if the clean plate changes materially.

### info3 body

Approximate original source visible bands:

```text
L1 297..317
L2 325..345
L3 353..373
L4 389..411
L5 416..438
L6 443..465
```

Source line centers approximately:

```text
307, 335, 363, 400, 427, 454
```

Line-center spacing approximately:

```text
28, 28, 37, 27, 27 px
```

### info4 body

```text
L1 307..326
L2 335..354
L3 372..389
L4 398..415
L5 424..441
L6 449..467
```

The first two lines are the larger first paragraph. The last four lines are the smaller second paragraph.

Centers approximately:

```text
316.5, 344.5, 380.5, 406.5, 432.5, 458.0
```

### info5 body

```text
L1 369..389
L2 398..419
L3 427..449
```

Centers approximately:

```text
379, 408.5, 438
```

### info6 lower body

```text
L1 274..293
L2 302..319
L3 338..357
L4 366..385
L5 394..411
L6 420..441
L7 448..468
```

Centers approximately:

```text
283.5, 310.5, 347.5, 375.5, 402.5, 430.5, 458
```

### info6 command panels

Each command panel has two distinct typography tiers.

Typical original source bands:

```text
row 1 command name:       ~88/89..110/112
row 1 explanation:        ~115/116..130/132
row 2 command name:       ~148..171
row 2 explanation:        ~176..191
row 3 command name:       ~208..231
row 3 explanation:        ~234..251
```

Do not render name and explanation with one common font size.

## 7. Simplified-Chinese font selection

For baked tutorial textures, the current offline renderer uses Noto Sans CJK as the visual source, but the localized face must be selected explicitly.

Current TTC face map:

```text
NotoSansCJK-Regular.ttc
  index 0 = JP
  index 1 = KR
  index 2 = SC
  index 3 = TC
  index 4 = HK

NotoSansCJK-Bold.ttc
  index 0 = JP
  index 1 = KR
  index 2 = SC
  index 3 = TC
  index 4 = HK
```

For Simplified Chinese baked text use:

```text
index = 2
```

Never rely on Pillow's default TTC face. The default face is JP and caused visibly Japanese localized glyph forms such as `将` in an M002 candidate.

This font rule concerns offline baked tutorial textures. Runtime/dynamic UIFont glyph work follows the separate game-font/glyph SOP and may use transplanted game glyph outlines instead.

## 8. Accepted baked-text rendering path

The accepted M001 visual approach is:

1. render **text layer only** at `8×` supersampling (`SS8`);
2. use one shared baseline/line model per line; do not independently center individual glyphs;
3. preserve natural Chinese glyph width;
4. use explicitly segmented white/cyan spans for semantic blue highlights;
5. use the M001 white/cyan/outline palette and effect logic;
6. map/downsample the supersampled text layer **once** into 1024×512 source geometry using Lanczos;
7. composite onto the accepted clean background;
8. store accepted full-screen tutorial textures as RGBA32 when the SerializedFile conversion is adopted.

Do not enlarge and resample the entire background just to supersample text. The background should retain its accepted pixels; only the text layer needs supersampling.

Do not perform an intermediate 1× Vita raster followed by inverse-affine rasterization. That rejected path adds avoidable resampling.

## 9. RGBA32 rationale and binary path

M001 proved on PSV Vita that these 1024×512 pages can be stored as uncompressed RGBA32 Texture2D objects, avoiding BC3 block artifacts on dense Chinese strokes.

Accepted M001 conversion facts:

- TextureFormat `12` = DXT5/BC3
- TextureFormat `4` = RGBA32
- 1024×512 BC3 image payload = `524,288` bytes
- 1024×512 RGBA32 image payload = `2,097,152` bytes
- Texture2D header = `76` bytes for these objects
- RGBA32 object size = `2,097,228` bytes
- growth vs BC3 = `0x180000` bytes/object

`resources.assets` is SerializedFile v15 / Unity 5.2.2p3 and uses explicit object `byteStart` / `byteSize` entries. M001's structured rebuild preserving non-target object bytes and shifting downstream offsets passed Vita hardware validation.

Future format conversions must follow `docs/QC_POLICY.md` RGBA32 structured-rebuild gate.

## 10. Blue-highlight rendering

Blue source keywords are semantic UI information.

Before rendering, build a machine-readable or explicit segment map per line:

```text
white segment
cyan segment
white segment
...
```

Do not render the whole line white and manually recolor later.

Final QC must compare the original source blue-keyword inventory against the Chinese blue-segment inventory. Missing, extra, or wrong blue spans are FAIL.

## 11. Required visual evidence before approval

For every info page candidate provide:

- original page / candidate page in measured game geometry;
- strict 50% overlay;
- line-band and line-center guides derived from original pixels;
- table of original vs candidate visible text heights for every typography tier;
- original vs candidate line-center spacing;
- 3× or greater nearest-neighbor detail crops;
- safe-area/collision inspection;
- blue-highlight semantic map check;
- localized-glyph inspection for characters with JP/SC shape differences;
- protected-region changed-pixel checks where applicable.

If these are absent, do not package the candidate.

## 12. Handoff requirement

Every future cross-session handoff for tutorial texture work must include or point to this SOP and explicitly record:

- clean-plate version and algorithm;
- protected regions;
- source-to-game transform;
- font file and TTC face/index;
- supersampling factor;
- resampling filter;
- white/cyan/outline rendering logic;
- line-band measurement method;
- exact TextureFormat/writeback strategy;
- final candidate hashes and hardware status.

Do not hand off only a PNG name and the phrase “same as previous version.”
