# v0.02 info3–6 Overlay-Driven Layout Locks

> Historical note: this work was developed in one chat under the working label `M002 info3–6`, while another parallel chat already used the project-level M002/M003 numbering for other components. Do **not** use this filename as the global component-order source. The canonical cross-track ID is `strategy-tutorial-info3-6-rgba32`.

Status: **V6 FINAL / PSV VITA HARDWARE PASS / ACCEPTED / LOCKED** as of 2026-08-28.

Exact Vita-tested package:

`Kancolle_Kai_v0.02_M002_Info3_6_RGBA32_VITA_CANDIDATE.zip`

ZIP SHA-256:

`87b3d0838ec6b1050e51b5914014edb824ef694c325b12107abeb89542cca2c8`

Exact cumulative `resources.assets` Mother used for that package:

`cb8cdd0e872aa22ab603e5b2be2bba78219cd8d54450f96bc9107bbdc5b1d50a`

Mother size: `1,283,402,344` bytes.

Exact Vita-tested output:

`20e0a0232c96eeba213fe09f65e3f1742302e50eec6fcb777e4952ad07c79311`

Output size: `1,290,218,052` bytes.

This Mother already contained work from another chat. The structured rebuild preserved every non-target serialized object byte-for-byte; therefore the info3–6 writeback must never be reconstructed from an older M001-only Mother when continuing from that parallel cumulative state.

**Critical dependency:** read `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md` and `docs/TUTORIAL_TEXTURE_RENDERING_SOP.md` before any future baked tutorial render.

## Overlay + line spacing is the layout solver

For these pages, overlay is not a post-render illustration. The only accepted workflow is:

1. Measure the original Japanese raster first.
2. Extract actual visible line bands and **bright-core glyph bboxes** from original-vs-clean-plate evidence.
3. Measure line centers, adjacent line-center spacing, typography tiers and anchors.
4. Freeze one font size per semantic/source typography tier.
5. Render Chinese using those measured constraints.
6. Overlay original and Chinese and use the difference to adjust parameters.
7. Iterate until the measured geometry converges.
8. Only then generate a user-facing QC image.

If the typography was guessed first and overlay was generated afterward, the candidate is `INCOMPLETE`.

**Outer changed-pixel bbox equality is not a font-size measurement.** The rejected V4.1 title matched an outer rectangle while the Chinese bright core was ~15.4% too short. Bright-core geometry, line center and line spacing are the relevant controls.

## Font-face lock

Baked Simplified-Chinese tutorial text must explicitly use:

- `Noto Sans CJK SC`
- TTC face index `2`

TTC default/index `0` is `Noto Sans CJK JP` and is prohibited. It previously produced visibly Japanese-localized glyph forms such as `将`.

## Final title solver — V6

The V6 title is not stretched to Japanese width.

Shared render parameters:

- main title: SS8 nominal size `45.5`, stroke `2.0`
- subtitle `说明`: SS8 nominal size `32.5`, stroke `2.0`
- font: Noto Sans CJK SC, TTC index 2
- one SS8 -> source-space Lanczos mapping
- natural Chinese width

Original bright-core target bboxes in source texture coordinates:

| Page | Main title target | `解説` target |
| --- | --- | --- |
| info3 | `(335,31)-(583,69)` | `(594,41)-(662,67)` |
| info4 | `(359,31)-(556,69)` | `(568,41)-(636,67)` |
| info5 | `(308,31)-(605,69)` | `(618,41)-(686,67)` |
| info6 | `(308,31)-(605,69)` | `(618,41)-(686,67)` |

Final constraints:

- main-title bright-core top/bottom = original top/bottom (`38 px` high)
- main-title bright-core right edge = original main-title right edge
- `说明` bright-core top/bottom = original `解説` top/bottom (`26 px` high)
- `说明` bright-core left edge = original `解説` left edge
- main-title center Y = `50.0`
- subtitle center Y = `54.0`
- subtitle-minus-main center offset = `+4.0 px`
- widths remain natural Chinese widths

Original and V6 horizontal gaps are identical:

- info3: `11 px`
- info4: `12 px`
- info5: `13 px`
- info6: `13 px`

This V6 title geometry is Vita-accepted. Do not regress to V4.1's anisotropic exact-width-box method or V5's incomplete height model.

## Final body typography — frozen

The body was user-approved before the V6 title/button correction and was kept byte-for-byte frozen while V6 was generated.

Approximate nominal render sizes from the accepted body solver:

- info3 body, both paragraphs: `24.3125`, stroke `1.1`
- info4 paragraph 1: `22.0625`, stroke `1.1`
- info4 paragraph 2: `20.6875`, stroke `1.0`
- info5 body: `24.5625`, stroke `1.1`
- info6 lower body, both blocks: `22.9375`, stroke `1.0`

These values are implementation records, not permission to skip measurement. If the raster is rebuilt, the original line bands/centers remain the authoritative geometry.

Paragraph rules:

- info3: paragraph 1 and paragraph 2 use the same size; all six lines share one left edge.
- info4: paragraph 1 has one larger size; paragraph 2 has one smaller size; every line inside each paragraph shares its paragraph size.
- info5: all body lines use one size and one left edge.
- info6: both lower body blocks, including the warning, use one common body size.
- never shrink individual lines to fit translated width.

## info6 final three-tier command typography

There are exactly three typography tiers.

### Primary cyan — shared large size

`22.5`, stroke `1.0`

Primary terms:

- `接近`
- `脱离`
- `航空`
- `炮击`
- `对潜`
- `突击`
- `雷击`
- `回避`
- `统射`

### Secondary cyan suffix — shared smaller size

`17.75`, stroke `1.0`

Suffixes:

- `攻击` after `航空`
- `攻击` after `对潜`
- `（接近＋炮击）`
- `（统制射击）`

The final V6 correction specifically changed `对潜攻击` from an all-large V5 label to **large `对潜` + small `攻击`**. The other eight command panels were frozen byte-identical to the already-approved V5 state during that correction.

### White explanation — shared size

`15.0`, stroke approximately `0.75`

All nine white explanations use this tier.

Locked final explanation for `统射（统制射击）`:

`实施电探统制射击。`

Do not regress to `电探控制射击`.

## Final render/writeback path

- accepted/refined clean background
- overlay + line spacing used as the only layout solver
- explicit SC font face
- SS8 text layer
- one Lanczos mapping into source texture space
- natural Chinese width
- semantic white/cyan mapping
- final Texture2D stored as RGBA32 rather than BC3
- measured source-to-Vita transform for QC

## Asset targets

All four are in `resources.assets`:

| Page | PathID | Original | Final |
| --- | ---: | --- | --- |
| `info3_set` | 1420 | DXT5, 1 mip | RGBA32, 1 mip |
| `info4_set` | 5059 | DXT5, 1 mip | RGBA32, 1 mip |
| `info5_set` | 3028 | DXT5, 11 mips | RGBA32, 11 mips |
| `info6_set` | 4413 | DXT5, 1 mip | RGBA32, 1 mip |

`info4` right-side Japanese ship-category list is intentionally preserved exactly and is not translated or cleaned.

For `info5`, all 11 mip levels are retained. Each mip is generated directly from the final mip0 using Lanczos and is vertically flipped independently for Unity raw RGBA storage. This was validated against existing game RGBA32 mipmapped textures; tested stored mips matched direct-Lanczos reconstruction at roughly `0.05–0.18` MAE/channel.

## Final structural QC

Unity: `5.2.2p3`

SerializedFile version: `15`

Object count: `65,462`

Current Mother dataOffset: `1,854,080`

Final offline reconstruction before hardware test had:

- non-target serialized object mismatch count: `0`
- inter-object gap mismatch count: `0`
- unexpected metadata diff count: `0`
- all four reconstructed mip0 rasters exact to the approved V6 RGBA source PNGs
- M001 Vita-PASS resources objects byte-identical to their accepted payloads

The exact resulting file subsequently passed PSV Vita hardware testing, so V6 is now `VITA PASS / FINAL / LOCKED`.

## Version history

- V2: rejected; manually approximated bands and default JP TTC face.
- V3/V3.1: rejected; overlay still operated too much as a report rather than the sole solver.
- V4: body substantially improved and later accepted; title/info6 hierarchy still wrong.
- V4.1: title method permanently rejected; outer-box matching hid ~15.4% bright-core height error.
- V5: info6 eight command panels largely accepted; title still incomplete; `对潜攻击` hierarchy still wrong.
- **V6: FINAL. Title overlay+line-spacing geometry converged, `对潜` + small `攻击` corrected, PSV Vita PASS.**
