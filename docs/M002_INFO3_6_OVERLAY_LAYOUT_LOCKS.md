# v0.02 M002 — info3–6 Overlay-Driven Layout Locks

Status: persistent project rule for the current `info3_set`–`info6_set` tutorial component.

**Critical dependency:** read `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md` before any new render. That file is non-negotiable and supersedes any weaker interpretation of “overlay QC”.

This file exists because earlier candidates incorrectly treated overlay/line-spacing comparison as a post-render illustration instead of using the original raster measurements to drive the Chinese layout. That workflow is rejected.

## Overlay must be an input, not a post-hoc screenshot

For these pages, do **not** render a Chinese layout from guessed coordinates and then merely show a 50% overlay afterward.

Required order:

1. Measure the original Japanese raster first.
2. Extract actual visible text bboxes / **bright-core glyph bboxes** / line bands / line centers from original-vs-clean-plate pixel evidence.
3. Identify paragraph-level typography tiers and anchors from those measurements.
4. Freeze one font size per source typography tier.
5. Render the Chinese text using those measured centers/anchors.
6. Overlay original and candidate and inspect core-glyph scale, line spacing, anchor and stroke weight.
7. Iterate the layout parameters from the overlay until they converge.

If steps 1–4 were skipped, or if overlay is generated only after the typography parameters are already fixed, the candidate is `INCOMPLETE`.

**Outer changed-pixel bbox equality is not sufficient.** The rejected V4.1 title matched the Japanese outer subtitle bbox but its Chinese bright-core glyph height was still about 15.4% too small. See `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`.

## Shared subtitle anchor

All four pages use the source subtitle `解説`. The Chinese subtitle is `说明`.

`说明` is a hard calibration anchor. The correct workflow is:

- use the original `解説` position / center as the page-specific anchor;
- use the **M001 Vita-PASS Chinese `说明` typography proportions** as the canonical Chinese style;
- match core height and vertical center through overlay;
- preserve natural Chinese width;
- do **not** stretch `说明` to the Japanese width.

Measured original source-space `解説` bboxes:

- info3: `x=594..662, y=41..67`
- info4: `x=568..636, y=41..67`
- info5: `x=618..686, y=41..67`
- info6: `x=618..686, y=41..67`

All four are `68×26` outer bright regions in the current measurement pass.

Exact M001 Vita-PASS reference, re-extracted from the final package:

- original info1 `解説`: about `68×27` source px;
- accepted M001 Chinese `说明`: about `61×27` source px;
- accepted Chinese height matched while width stayed naturally about `10.3%` narrower.

The rejected V4.1 method that forcibly resized `说明` into `68×26` is permanently prohibited.

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

Measured original vs rejected V4 bright-core examples:

- simple primary terms: original approximately `46–49×17–18`; rejected V4 approximately `42–43×17`;
- `航空`: original `48×18`; rejected V4 about `43×17`;
- `攻击`: original `37×14`; rejected V4 about `31×13`;
- `突击`: original `48×18`; rejected V4 about `42×17`;
- `（接近＋炮击）`: original `108×13`; rejected V4 about `94×13`;
- `统射`: original `48×18`; rejected V4 about `44×17`;
- `（统制射击）`: original `91×14`; rejected V4 about `77×13`.

The next render must solve the three common role sizes against the original overlay/core-bbox data before the Chinese panel is considered a layout candidate.

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

## Rejected versions

- V3/V3.1: overlay was still being used too much as a post-render report; title and command typography did not sufficiently follow the source.
- V4: body layout substantially improved and the user approved the body, but title and info6 command typography remained wrong.
- V4.1: **rejected title method**. It forcibly resized Chinese `说明` to the Japanese outer bbox. Outer bbox equality hid a `~15.4%` bright-core height deficit and incorrect proportions. Never reuse this exact-bbox anisotropic title method.