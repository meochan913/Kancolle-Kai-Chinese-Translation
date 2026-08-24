# QC Policy

This project uses fail-closed QC. A component is PASS only when the required evidence is produced from the current files.

## Core release rule

Any failed, missing, unknown, or unreproduced critical gate means `FAIL` or `INCOMPLETE`, never PASS.

Offline QC and PSV Vita hardware validation are separate states.

## Mandatory source-to-game geometry gate

For **every visual modification based on an original game texture, atlas, screenshot-like tutorial page, or other pre-rendered UI material**, the source-space edit must not be approved from the raw texture alone.

Before editing or approving the layout, the project must determine and record the actual source-to-game display transform from original game evidence whenever practical, including:

- source texture dimensions;
- game/screenshot dimensions;
- horizontal scale / stretch ratio;
- vertical scale / stretch ratio;
- translation / crop offset;
- orientation.

If the game applies non-uniform scaling, the Chinese layout must be designed and QC'd in **game/screen space**, then mapped back to source texture space. Raw source-space appearance is not sufficient.

## Mandatory overlay and typography gate

For source-based UI/text replacements, final visual QC must include, as applicable:

- original game-space reference;
- Chinese simulated or decoded game-space result;
- strict overlay (normally 50% original + 50% candidate and/or edge overlay);
- vertical text extent / font-height comparison;
- horizontal/vertical anchors where they are semantically meaningful;
- baseline or vertical-center comparison;
- line-spacing comparison;
- stretch/aspect comparison;
- target-region absolute diff.

### Translation-width rule

**Translated line width is not an overlay target by itself.** Japanese and Chinese strings naturally have different lengths. The Chinese layout must keep normal glyph proportions and must not be horizontally squeezed or expanded merely to reproduce the original Japanese line width.

For translated text, the primary typography constraints are:

- natural glyph aspect ratio in final game/screen space;
- font height / visible glyph height consistent with the original design;
- baseline or vertical center consistent with the original design;
- line-center spacing / line spacing consistent with the original design;
- correct alignment or anchor logic (for example, right-aligning a left-side label toward its arrow, or left-aligning a right-side label away from its arrow);
- remaining within the intended safe area without collisions or clipping.

Horizontal width may differ naturally. It becomes a QC constraint only if the translated text collides with another element, clips, crosses an intended safe boundary, or violates a specific alignment rule.

When a title contains multiple typographic levels, each level must be measured separately. For example, the Strategy Tutorial title uses a larger `戦略画面` main title and a smaller `解説` subtitle; the Chinese `战略界面` and `说明` must preserve that hierarchy rather than being rendered at one common size.

Line breaks, baseline positions, line spacing, vertical size, and text hierarchy must be deliberately matched to the original design. A layout must not be accepted merely because the Chinese text fits inside the texture.

If these measurements/evidence are missing, the visual build is `INCOMPLETE` and must not be packaged as a Vita candidate.

## Clean-plate gate

A clean plate must remove the original glyphs, outlines, shadows, and alpha contamination without introducing visible smears, dark blobs, seams, or flattened background texture.

Scope metrics such as `outside-mask changed = 0` are supporting evidence only. They do not override visible defects.

## BC3 / DXT5 gate

Codec integrity does not equal visual correctness. Texture work must be decoded after the actual BC3/DXT5 write and inspected in game orientation. Non-target blocks should remain byte-identical whenever the patch design permits.

## Hardware gate

`VITA PASS` may only be assigned after the exact candidate binary is tested successfully on PSV Vita.

## v0.02 M001 rejection note

The first `Strategy Tutorial` M001 candidate derived from v0.01 `resources.assets` (`f19fbcf5...fce8`) is **REJECTED** for the two full-screen tutorial pages because source-to-game non-uniform stretch and original line-spacing/layout were not validated before packaging.

The right-bottom `TutorialGuide1` UILabel translation is not rejected by this finding and remains pending hardware inspection; the two full-screen pages must be rebuilt from the accepted `info2` V12 clean plate with strict game-space geometry/overlay QC before a replacement Vita candidate is produced.
