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

If the game applies non-uniform scaling, the Chinese layout must be designed and QC'd in **game/screen space** and mapped back to source-space without unnecessary raster resampling. Raw source-space appearance is not sufficient.

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
- correct alignment or anchor logic;
- remaining within the intended safe area without collisions or clipping.

Horizontal width may differ naturally. It becomes a QC constraint only if the translated text collides with another element, clips, crosses an intended safe boundary, or violates a specific alignment rule.

When a title contains multiple typographic levels, each level must be measured separately. For example, the Strategy Tutorial title uses a larger `戦略画面` main title and a smaller `解説` subtitle; the Chinese `战略界面` and `说明` must preserve that hierarchy rather than being rendered at one common size.

Line breaks, baseline positions, line spacing, vertical size, and text hierarchy must be deliberately matched to the original design. A layout must not be accepted merely because the Chinese text fits inside the texture.

If these measurements/evidence are missing, the visual build is `INCOMPLETE` and must not be packaged as a Vita candidate.

### Special-symbol spacing rule

For control labels, button legends, bracketed keys, controller symbols, and similar special UI notation, **do not add literal spaces immediately outside the symbol/brackets** unless the original design specifically requires them.

Preferred pattern when extra visual breathing room is needed around a single key label:

- correct: `按【 R 】键`
- avoid: `按 【R】 键`
- avoid: `按 【 R 】 键`

Operational rule:

- keep surrounding Chinese text directly adjacent to the outer brackets/symbol;
- when the full-width brackets themselves look visually cramped, add spacing **inside** the brackets, e.g. `【 R 】`;
- do not silently normalize these spaces during later edits;
- every time a translated UI string contains this kind of special symbol, the assistant must explicitly tell the user which spacing form is being used so it can be visually confirmed.

This is a persistent project typography rule.

## Clean-plate gate

A clean plate must remove the original glyphs, outlines, shadows, and alpha contamination without introducing visible smears, dark blobs, seams, or flattened background texture.

Scope metrics such as `outside-mask changed = 0` are supporting evidence only. They do not override visible defects.

## BC3 / DXT5 gate

Codec integrity does not equal visual correctness. Texture work must be decoded after the actual BC3/DXT5 write and inspected in game orientation. Non-target blocks should remain byte-identical whenever the patch design permits.

For dense CJK text baked into BC3 textures, the rendering pipeline itself is a critical QC target. Avoid unnecessary low-resolution raster transforms before BC3. If the game applies non-uniform scaling, prefer high-resolution source-direct text generation or an equivalent single-resample method rather than `1× screen raster → inverse warp → BC3 → game rescale`.

When sharpness is a concern, required evidence should include:

- BC3 roundtrip decode;
- simulated/measured game transform;
- 3× or greater nearest-neighbor OLD/NEW pixel comparison;
- inspection for 4×4 block color bleeding, mosaic artifacts, low-bitrate-like smearing, and softened CJK strokes.

A texture that is structurally valid but visibly blocky or blurry is `FAIL`.

## Dynamic-font / glyph gate

For runtime UILabel or other dynamic-font text, a serialized string containing the intended character is **not sufficient evidence** that the glyph will render.

If a character has previously disappeared, rendered blank, or been substituted on Vita, that character becomes an explicit hardware glyph gate. The exact character must be visibly present in a hardware screenshot before the component can be marked `VITA PASS`.

Example: in v0.02 M001 `TutorialGuide1`, the character `键` disappeared on hardware in a previous candidate. Future candidates containing `键` must visibly render the glyph; otherwise the build is `FAIL` even when the serialized text itself is correct.

## Hardware gate

`VITA PASS` may only be assigned after the exact candidate binary is tested successfully on PSV Vita.

## v0.02 M001 rejection notes

The first `Strategy Tutorial` M001 candidate derived from v0.01 `resources.assets` (`f19fbcf5...fce8`) was rejected because source-to-game non-uniform stretch and original line-spacing/layout were not validated before packaging.

REDO4 was later tested on hardware. Its transparency and overall layout were broadly acceptable, but the two full-screen Chinese tutorial pages showed severe blocky/mosaic blur. REDO4 is therefore also rejected as a cumulative development baseline. The next candidate must again start from v0.01 FINAL and use a sharper source-direct text-rendering pipeline.
