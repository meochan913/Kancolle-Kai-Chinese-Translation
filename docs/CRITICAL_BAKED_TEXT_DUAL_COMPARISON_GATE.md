# CRITICAL — Baked Text Dual-Comparison Gate

Status: **NON-NEGOTIABLE PROJECT RULE / FAIL-CLOSED**

This rule supplements `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md` and applies to **all baked raster typography**, not only tutorials. Scope includes tutorial pages, atlases, StrategyFrame, shortcut/menu textures, header icons, button labels, and any other text rendered into a texture.

The purpose of this file is to turn the existing Overlay + Line Spacing rule into a hard release/review gate so that it cannot be satisfied by producing a QC image after layout decisions were already made.

## 1. Two independent comparisons are mandatory

Before a baked-text candidate may be shown to the user, both of the following must exist and PASS:

### A. Overlay comparison

Compare original Japanese typography and the Chinese candidate in the same source/game-space coordinate system.

The overlay must include, where applicable:

- original outer/effect bbox;
- original bright/core glyph bbox;
- candidate outer/effect bbox;
- candidate bright/core glyph bbox;
- vertical center / baseline relationship;
- anchor relationship;
- stroke / outline thickness;
- tracking / inter-glyph spacing when useful.

A color-coded mask overlay is preferred (for example Japanese=magenta, Chinese=cyan, overlap=white), but the important requirement is that the comparison exposes geometry rather than hiding it in a side-by-side screenshot.

Translated Chinese width is **not** required to equal Japanese width. Never anisotropically stretch or squeeze Chinese merely to force width equality.

### B. Edge-based line-spacing comparison

Line spacing MUST be checked using the **actual top and bottom edges of the typography envelopes**, not only center lines.

For every line/row, record at minimum:

- `top_y`;
- `bottom_y`;
- `height`;
- vertical center;
- center-to-center spacing to adjacent rows;
- bottom-to-next-top edge gap;
- top/bottom margin inside the containing panel/button when relevant.

A QC sheet that draws only horizontal center lines is **INCOMPLETE / FAIL** and cannot satisfy the line-spacing gate.

For stacked single-line buttons, top/bottom edge gaps are mandatory even when every row shares the same nominal font size.

## 2. Measurement must determine layout — never the reverse

Mandatory order:

1. Load the exact original raster.
2. Load the accepted clean plate.
3. Extract/measure original typography.
4. Measure original bright/core bbox, outer/effect bbox, top, bottom, center, baseline/vertical center, spacing, anchor, and stroke/weight.
5. Choose Chinese font face, weight, size, and placement **from those measurements**.
6. Render a candidate.
7. Generate BOTH the overlay comparison and edge-based line-spacing comparison.
8. Use the mismatch from those comparisons to change font/weight/size/X/Y/effect parameters.
9. Repeat render -> compare -> retune until the measurements converge.
10. Only then may the candidate be presented for user visual review.

The following workflow is permanently prohibited:

`guess font/size/Y -> render -> create overlay afterward -> show candidate`

If the overlay/spacing output did not feed back into the layout parameters before presentation, the candidate is **FAIL**, even if the final QC image itself looks informative.

## 3. Font weight / stroke thickness is a measured parameter

Do not default to `Bold`, `Regular`, or any other weight merely because another project component used it.

For each source typography family, measure and compare:

- bright/core stroke thickness;
- dark/light bevel or outline thickness;
- anti-aliased edge occupancy;
- apparent weight after the game's final compositing/scale.

If the candidate is visibly or measurably heavier/lighter than the source, change the base face/weight or render parameters before changing unrelated geometry.

The same logical button family must use one frozen base face/weight/size unless the original source proves that different rows use different typography tiers.

## 4. Normal / Selected state geometry lock

Unless source evidence proves otherwise, Normal and Selected states of one logical label must share identical base glyph geometry:

- same font face;
- same weight;
- same nominal size;
- same natural glyph proportions;
- same anchor logic.

State styling (gray/blue/pink, highlight/shadow, recessed/embossed effect, macro glow) is a separate rendering layer and must not silently alter glyph scale.

## 5. StrategyFrame specific lock — PathID 461

Target:

- `sharedassets5.assets`
- Texture2D PathID `461` — `StrategyFrame`
- UIAtlas PathID `17327`

For the three StrategyFrame button labels:

- `アイテム屋さん` -> `道具商店`
- `明石改修工廠` -> `明石改修工厂`
- `保有アイテム` -> `持有道具`

Use `明石改修工廠 -> 明石改修工厂` as the primary font-size/weight calibration anchor because it provides the strongest direct source-vs-translation comparison. Once calibrated, freeze the same Chinese face/weight/size for all three labels.

Do **not** force Chinese width to Japanese width. Match vertical geometry, weight, stroke/effect thickness, row spacing, and the original row/button anchor.

Exact original StrategyFrame row outer/effect envelopes measured from the current original raster are:

- row 1: `y=299..322`, height `24 px`;
- row 2: `y=337..360`, height `24 px`;
- row 3: `y=375..398`, height `24 px`.

Therefore:

- line centers: `310.5 / 348.5 / 386.5`;
- center-to-center spacing: `38 px / 38 px`;
- bottom-to-next-top empty edge gap: `14 px / 14 px`.

These values are source-specific evidence for the current PathID461 raster. Re-measure if the source raster changes.

## 6. Required QC artifacts before user review

Every baked-text candidate must include all of the following before it may be called a candidate:

1. `QC_OVERLAY` — original vs candidate geometry overlay;
2. `QC_EDGE_LINE_SPACING` — top/bottom edges plus centers and numeric gaps;
3. machine-readable measurements (`JSON` or `CSV`);
4. white-background transparency QC when Alpha is involved;
5. black-background transparency QC when Alpha is involved.

Missing any required artifact => `INCOMPLETE / FAIL-CLOSED`.

Do not write the candidate back to an `.assets` file until the user has visually approved the baked raster.

## 7. Exact approved source artifact rule

If the user asks to reuse a previously approved/locked raster or sprite, and the exact approved artifact or an exact reproducible recipe is unavailable, **do not reconstruct it from memory and present it as the old version**.

The correct state is `MISSING SOURCE EVIDENCE / INCOMPLETE` until one of the following is recovered:

- the exact approved PNG/payload;
- an exact archived package containing it;
- a deterministic reproduction recipe with sufficient parameters and reference evidence.

## 8. 2026-08-29 StrategyFrame regression RCA

Rejected preview lineage:

- `StrategyFrame_CHS_LAYOUT_PREVIEW_V1_R4_game_space_RGBA.png`

Failures:

1. The exact archived Strategy `V5.1 FINAL` Normal / `V6.1 CLEAN FINAL` Glow sprites were not available in the active runtime, but a new approximation was rendered anyway. This violated the exact-approved-source rule and produced a visibly different `战略`.
2. Button line-spacing QC used center lines as the primary visual guide and omitted the mandatory top/bottom edge comparison.
3. The button font was selected as `Noto Sans CJK SC Bold` at a guessed nominal size before a complete source stroke-weight calibration.
4. QC was generated after the layout had already been selected; the QC mismatch was not used as a mandatory feedback loop before the candidate was shown.
5. The presentation gate did not fail closed when the dual-comparison evidence was incomplete.

Permanent consequence:

- This R4 preview is **REJECTED / SUPERSEDED**.
- Center-line-only spacing QC is prohibited.
- Exact prior visual assets must be recovered instead of approximated when the user asks for reuse.
- Button weight, top/bottom envelope, and overlay must be solved first, and only then may a replacement preview be shown.

## 9. Handoff requirement

Every future handoff involving baked raster typography must explicitly reference BOTH:

- `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`
- `docs/CRITICAL_BAKED_TEXT_DUAL_COMPARISON_GATE.md`

Do not summarize them only as “remember to overlay.” Preserve the measurement-first order and the fail-closed artifact gates.
