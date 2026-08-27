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

**Outer changed-pixel bbox equality is not sufficient.** The rejected V4.1 title matched the Japanese outer subtitle rectangle but its Chinese bright-core glyph height was still about 15.4% too small. See `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`.

## Shared subtitle anchor

All four pages use source subtitle `解説`; Chinese is `说明`.

Do not stretch `说明` to Japanese width.

The exact M001 Vita-PASS `info1_set` was re-extracted and re-measured with one consistent bright-core criterion. Current canonical bright-core measurements are:

- original info1 `戦略画面`: about `196×38`;
- original info1 `解説`: about `68×27`;
- accepted M001 `战略界面`: about `169×33`;
- accepted M001 `说明`: about `57×23`.

These values supersede earlier rough notes that mixed outline/core thresholds (`175×39`, `61×27`, etc.). Future sessions must preserve the measurement criterion when quoting sizes.

Reverse-fit current implementation parameters for the M001 Chinese title style:

- main title: SS8 size `~40.75`, stroke `~1.0`;
- `说明`: SS8 size `~28.0`, stroke `~1.0`;
- Noto Sans CJK SC, TTC index 2;
- one Lanczos source mapping using the established Vita/source transform.

For V5 info3–6 placement:

- main title bright-core right edge + vertical center = original main title;
- `说明` bright-core left edge + vertical center = original `解説`;
- preserve natural Chinese width;
- preserve exact original main→subtitle gap.

Current gaps reproduced exactly:

- info3 `11 px`;
- info4 `12 px`;
- info5 `13 px`;
- info6 `13 px`.

V5 remains user-review pending.

## Paragraph font-size consistency

The user approved the current body layout. During title/button convergence the body is frozen.

- info3: paragraph 1 and paragraph 2 use the **same body font size**; all six lines share that size and a common left alignment.
- info4: paragraph 1 uses one larger font size; paragraph 2 uses one smaller font size. Every line inside each paragraph uses its paragraph's single frozen size.
- info5: the entire body uses one font size and one common left alignment.
- info6: both lower body blocks use one common body font size. Warning lines are not a separate size.

Do not resize individual lines to compensate for translation length.

## info6 command-panel hierarchy

Exactly three semantic typography tiers:

1. primary cyan command term — one common large size:
   `接近 / 脱离 / 航空 / 炮击 / 对潜攻击 / 突击 / 雷击 / 回避 / 统射`
2. secondary cyan suffix — one common smaller size:
   `攻击 / （接近＋炮击） / （统制射击）`
3. white command explanation — one common explanation size.

No per-button shrink-to-fit is allowed.

Original bright-core targets used for convergence:

- primary terms: typically `47–49×17–18` for two-character terms;
- `航空`: about `49×18`;
- `攻击`: `37×14`;
- `突击`: about `49×18`;
- `（接近＋炮击）`: about `108×15`;
- `统射`: about `48×18`;
- `（统制射击）`: about `91×14`;
- white explanations: typically about `13 px` bright-core height.

V5 role sizes solved before rendering:

- primary cyan `22.5`;
- suffix cyan `17.75`;
- white explanation `15.0`.

Representative V5 bright cores:

- `接近` `46×18`;
- `航空` `45×18`;
- `攻击` `36×14`;
- `突击` `45×18`;
- `（接近＋炮击）` `107×14`;
- `统射` `45×18`;
- `（统制射击）` `88×14`;
- sampled white explanations reproduce about `13 px` height.

Translated widths remain natural and are not forced to Japanese explanation lengths.

The explanation for `统射（统制射击）` is locked as:

`实施电探统制射击。`

## Simplified-Chinese font-face lock

Baked Chinese tutorial text must explicitly use a Simplified-Chinese localized font face.

- TTC index `2` = Simplified Chinese (`Noto Sans CJK SC`) — required
- TTC default/index `0` = Japanese (`Noto Sans CJK JP`) — prohibited

The rejected JP-face candidate visibly produced a Japanese-localized `将` in info4/info5.

## Current rendering path

- accepted clean background / refined donor reconstruction;
- overlay + line spacing as the only layout solver;
- explicit SC font face;
- SS8 text layer;
- one Lanczos source mapping;
- natural Chinese width;
- M001 white/cyan/outline style;
- RGBA32 visual path;
- measured source-to-Vita transform for QC.

Do not package until user explicitly approves the visual candidate.

## Rejected / current versions

- V3/V3.1: rejected; overlay still functioned too much as a post-render report.
- V4: body substantially improved; body later approved, title and info6 command typography still wrong.
- V4.1: title method rejected. It forcibly resized `说明` to Japanese rectangle and hid a ~15.4% core-height error.
- **V5:** body frozen; only title and info6 command typography regenerated from measured bright-core targets. Status: `VISUAL CANDIDATE / USER REVIEW PENDING`.
