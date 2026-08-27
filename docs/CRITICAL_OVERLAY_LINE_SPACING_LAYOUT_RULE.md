# CRITICAL — Overlay + Line Spacing Is the Only Accepted Typography Layout Method

Status: NON-NEGOTIABLE PROJECT RULE.

This file exists because multiple tutorial-text candidates repeatedly treated overlay as a post-render illustration instead of the actual source of typography geometry. That workflow is rejected permanently.

## 1. Exclusive layout rule

For baked tutorial/UI text based on an original raster, **overlay + line-spacing measurement is the only accepted typography layout method**.

No other method may be used to determine font size, vertical position, paragraph spacing, title scale, subtitle scale, command-label scale, or alignment.

Forbidden as layout inputs:

- eyeballing / visual approximation;
- guessed Y ranges;
- nominal font point size copied from another page without measurement;
- fitting text to a convenient rectangle;
- forcing translated text to match Japanese line width;
- scaling a whole translated title group to look centered;
- independent per-line or per-button shrinking merely to make text fit;
- generating an overlay only after the Chinese layout has already been chosen.

The mandatory order is:

1. load the exact original raster;
2. load the accepted clean plate;
3. extract the original typography from pixels;
4. measure the original glyph/core bbox, line center, baseline/vertical center, line-center spacing, paragraph-tier size, and anchor;
5. use those measurements to choose the Chinese font size and placement;
6. render the Chinese candidate;
7. overlay original and candidate;
8. if the overlay reveals mismatch, change the typography parameters and repeat;
9. only after overlay + line-spacing converge may a candidate be shown as a layout candidate.

Overlay is therefore a **design input / calibration loop**, not a presentation image.

## 2. Core-glyph bbox, not only outer changed-pixel bbox

A critical 2026-08-27 regression showed why matching only the outer changed-pixel bbox is invalid.

For info3–6 the original Japanese subtitle `解説` has an outer/source bbox of approximately `68×26` pixels. A rejected V4.1 Chinese `说明` candidate was forcibly resized so its outer changed-pixel bbox also became exactly `68×26`.

That looked numerically perfect but was visually wrong.

Measured bright/core glyph pixels:

- original `解説`: each glyph core is approximately `31–32 px wide × 26 px high`;
- rejected V4.1 `说明`: `说` core approximately `31×22`, `明` approximately `29×22`;
- candidate core height was therefore about `4 source pixels / 15.4%` too small despite the identical outer bbox.

After the known Vita Y scale (`~1.12702×`), that 4-source-pixel error becomes about `4.51 screen pixels`.

Therefore typography calibration MUST separately measure:

- outer outline/changed-pixel bbox;
- bright/core glyph bbox;
- per-glyph core height where useful;
- inter-glyph spacing/tracking;
- stroke/outline thickness.

An exact outer bbox is not PASS if the core glyph proportions do not overlay.

## 3. Never anisotropically force a Chinese glyph raster into the Japanese bbox

The rejected V4.1 title method rendered `说明` naturally and then resized the raster to the Japanese `68×26` rectangle. This changed the glyph aspect ratio and is permanently forbidden.

Chinese glyph width must remain natural. Match height/core scale and anchor first. If the translated text is naturally narrower or wider, allow that unless it causes collision/safe-area issues.

Do not solve width differences by horizontally or vertically distorting glyphs.

## 4. M001 Vita-PASS title typography is the canonical style reference

The exact final M001 `info1_set` was re-extracted from the Vita-tested package and measured.

Original info1 Japanese:

- `戦略画面` bright bbox approximately `196×38` source pixels;
- `解説` bright bbox approximately `68×27` source pixels;
- main/subtitle gap approximately `12 px` source-space.

M001 Vita-PASS Chinese:

- `战略界面` approximately `175×39` source pixels;
- `说明` approximately `61×27` source pixels;
- main/subtitle gap approximately `14 px` source-space.

Important conclusion: the accepted Chinese subtitle kept essentially the same HEIGHT as the Japanese subtitle while remaining naturally about `10.3%` narrower. It was NOT stretched to the Japanese width.

For future strategy tutorial titles, the M001 title typography/raster proportions are the canonical Chinese style baseline. The page-specific original `解説` position is the anchor; preserve the M001 Chinese glyph proportions and place them against the original anchor rather than forcing width.

## 5. Line spacing is inseparable from overlay

For every paragraph tier:

- one source typography tier = one frozen Chinese font size;
- derive every line center from the original raster;
- derive center-to-center spacing from the original raster;
- all lines inside a paragraph tier use that same font size;
- if two original paragraphs use the same type size, Chinese uses the same size;
- if the source clearly uses two sizes, preserve exactly those two tiers.

Never use per-line font-size adjustment to compensate for Chinese line length.

## 6. info3–6 current paragraph locks

- info3: both body paragraphs use one common body size and one common left alignment.
- info4: paragraph 1 uses one larger size; paragraph 2 uses one smaller size. Every line inside each paragraph is identical in size.
- info5: all body lines use one common size and one common left alignment.
- info6: both lower body blocks use one common body size.

## 7. info6 command-panel typography lock

Use exactly three semantic typography tiers, calibrated from the original overlay:

1. primary cyan command term — one common large size:
   `接近 / 脱离 / 航空 / 炮击 / 对潜攻击 / 突击 / 雷击 / 回避 / 统射`
2. secondary cyan suffix — one common smaller size:
   `攻击 / （接近＋炮击） / （统制射击）`
3. white explanation — one common explanation size.

Do not shrink individual command names independently.

Measured original-vs-rejected-V4 core examples show the previous candidate was still too small/narrow:

- simple primary labels: original bright-core width roughly `46–49 px`, height `17–18 px`; rejected V4 roughly `42–43 px`, height about `17 px`;
- `航空`: original primary core about `48×18`, rejected V4 about `43×17`;
- `攻击` suffix: original about `37×14`, rejected V4 about `31×13`;
- `突击`: original about `48×18`, rejected V4 about `42×17`;
- `（接近＋炮击）`: original about `108×13`, rejected V4 about `94×13`;
- `统射`: original about `48×18`, rejected V4 about `44×17`;
- `（统制射击）`: original about `91×14`, rejected V4 about `77×13`.

The next render must calibrate the three role sizes against these original core bboxes, not against nominal point sizes.

## 8. Memory / handoff requirement

Every future handoff MUST include this rule or point to this file explicitly.

Future sessions must read this file before any baked tutorial typography work.

If a candidate is later rejected, record WHY and mark the rejected method as prohibited. If a method is Vita-approved, record the exact accepted measurements/pipeline as the next canonical baseline.

Do not merely say “remember to overlay.” Preserve the actual measurement method and accepted/rejected numeric evidence.