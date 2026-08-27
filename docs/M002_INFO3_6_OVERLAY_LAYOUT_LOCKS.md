# v0.02 M002 — info3–6 Overlay-Driven Layout Locks

Status: persistent project rule for the current `info3_set`–`info6_set` tutorial component.

This file exists because earlier candidates incorrectly treated overlay/line-spacing comparison as a post-render illustration instead of using the original raster measurements to drive the Chinese layout. That workflow is rejected.

## Overlay must be an input, not a post-hoc screenshot

For these pages, do **not** render a Chinese layout from guessed coordinates and then merely show a 50% overlay afterward.

Required order:

1. Measure the original Japanese raster first.
2. Extract actual visible text bboxes / line bands / line centers from original-vs-clean-plate pixel evidence.
3. Identify paragraph-level typography tiers and anchors from those measurements.
4. Freeze one font size per source typography tier.
5. Render the Chinese text using those measured centers/anchors.
6. Use 50% overlay and line guides to verify the already measurement-driven layout.

If steps 1–4 were skipped, the candidate is `INCOMPLETE` even if an overlay image was later generated.

## Shared subtitle anchor

All four pages use the source subtitle `解説`. The Chinese subtitle is `说明`.

`说明` is a hard calibration anchor and must match the original `解説` visible bbox/center/height on each page before the main title is accepted.

Measured original source-space `解説` bboxes:

- info3: `x=594..662, y=41..67`
- info4: `x=568..636, y=41..67`
- info5: `x=618..686, y=41..67`
- info6: `x=618..686, y=41..67`

All four are `68×26` visible pixels. The main translated title may have a naturally different width, but it must be positioned relative to this hard subtitle anchor rather than by re-centering the whole translated title group by eye.

## Paragraph font-size consistency

A paragraph/source typography tier uses one shared font size. Never independently resize individual lines just because one translated line is longer or shorter.

Current locks:

- info3: paragraph 1 and paragraph 2 use the **same body font size**; all six lines share that size and a common left alignment.
- info4: paragraph 1 uses one larger font size; paragraph 2 uses one smaller font size. Every line inside each paragraph must use its paragraph's single frozen size.
- info5: the entire body uses one font size and one common left alignment.
- info6: both body blocks use one common body font size. Do not make the warning block a separate font size.

If the source's two paragraphs are visually the same size, the Chinese version should also use the same size. Do not create artificial size differences from per-line bbox noise.

## info6 command-panel hierarchy

Do not size all nine command labels independently.

The source uses semantic typography tiers:

1. **Primary cyan command term — one common large size**
   - `接近`
   - `脱离`
   - `航空`
   - `炮击`
   - `对潜攻击`
   - `突击`
   - `雷击`
   - `回避`
   - `统射`

2. **Secondary cyan suffix — one common smaller size**
   - `攻击` in `航空攻击`
   - `（接近＋炮击）` in `突击（接近＋炮击）`
   - `（统制射击）` in `统射（统制射击）`

3. **White command explanation — one common explanation size**

The primary term and suffix share a coherent baseline within each label. Long labels must not be solved by shrinking the entire command name independently.

The explanation for `统射（统制射击）` is locked as:

`实施电探统制射击。`

## Simplified-Chinese font-face lock

Baked Chinese tutorial text must explicitly use a Simplified-Chinese localized font face.

For current Noto CJK TTC resources:

- TTC index `2` = Simplified Chinese (`Noto Sans CJK SC`) — required
- TTC default/index `0` = Japanese (`Noto Sans CJK JP`) — prohibited

The rejected JP-face candidate visibly produced a Japanese-localized form of `将` in info4/info5. Any such localized-glyph regression is QC FAIL.

## Current rendering path

The accepted M001 visual approach remains the baseline:

- clean background built from the approved reconstruction path;
- layout driven by source raster measurements;
- explicit SC font face;
- SS8 text-layer rasterization;
- one Lanczos mapping/downsample into `1024×512` source space;
- natural Chinese width;
- M001 white/cyan palette and outline logic;
- RGBA32 visual path where final Texture2D conversion is adopted;
- measured Vita source-to-screen transform for final QC.

Do not package an info3–6 Vita candidate until the user explicitly approves the overlay-driven visual candidate.