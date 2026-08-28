# v0.02 info3–6 Translation / Highlight Specification

> Historical note: this document was created under the working label `M002 info3–6`. Project-level M002/M003 numbering is also used by another parallel chat. Treat this as the canonical translation spec for `strategy-tutorial-info3-6-rgba32`, not as the global component-order source.

Status: **TRANSLATION LOCKED / V6 PSV VITA HARDWARE PASS / FINAL / LOCKED** as of 2026-08-28.

Exact Vita-tested package:

`Kancolle_Kai_v0.02_M002_Info3_6_RGBA32_VITA_CANDIDATE.zip`

SHA-256:

`87b3d0838ec6b1050e51b5914014edb824ef694c325b12107abeb89542cca2c8`

## Persistent translation rules

- Write natural Chinese syntax. Do not preserve Japanese word order when it produces Japanese-style Chinese.
- When the original distinguishes a game function/keyword through blue highlighting, preserve that distinction through blue highlighting in Chinese.
- Do **not** invent quotation marks, book-title marks, parentheses, or other emphasis punctuation absent from the source merely to emphasize a game function.
- Missing, extra, or semantically incorrect blue highlighting is QC FAIL.
- Chinese line width is not required to match Japanese line width. Match font height, line center/baseline, line spacing, hierarchy, alignment, safe area and final game-space aspect ratio.
- Special key notation uses no literal spaces outside the brackets; breathing room goes inside: `按【 L 】键`, `按【 R 】键`.
- Baked Simplified-Chinese text must explicitly use the Simplified-Chinese localized font face. For Noto CJK TTC files, index `2` is SC; default/index `0` is JP and is prohibited.
- Overlay + line spacing is the **only accepted layout solver** for these baked tutorial pages. See `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`.

## info3 — 旗舰提督室 说明

### Paragraph 1

1. `这里就是旗舰提督室，相当于《舰队Collection 改》的母港界面。`
2. `在这里可进行舰队的编成，在工厂可进行舰娘的建造和装备的开发`
3. `也可通过补给、入渠和改装来强化舰娘。`

Blue semantic keywords:

- `旗舰提督室`
- `编成`
- `工厂`
- `建造`
- `开发`
- `补给`
- `入渠`
- `改装`

### Paragraph 2

1. `按【 L 】键可切换至图鉴、家具店等提督室子菜单。`
2. `此外，还可使用战略点数获取各种有助于战局的道具。`
3. `请通过记录进行战况的保存。`

Blue semantic keywords:

- `【 L 】`
- `图鉴`
- `家具店`
- `记录`

Do not add quotation marks around `记录`.

## info4 — 编成界面 说明

The first and second paragraphs use different source typography sizes and must remain two distinct tiers.

### Paragraph 1 — larger body tier

1. `在编成界面中，可将舰娘编入舰队或进行替换。`
2. `在每支舰队中，可编入最多六支舰娘。`

Blue semantic keywords:

- `编成`
- `最多六支`

`最多六支` intentionally mirrors the semantic emphasis of original `最大六隻`.

### Paragraph 2 — smaller body tier

1. `根据舰队编成，出击时的航线有时会发生较大变化。`
2. `若无法顺利攻略作战海域，除了提升舰队练度、`
3. `完善装备外，调整舰队编成也是一种有效的方法。`
4. `尤其是驱逐舰为主力的水雷战队，由1艘轻巡洋舰担任旗舰会更有效。`

Blue semantic keywords:

- `航线`
- `水雷战队`

### Ship-category list

The right-side Japanese ship-category list is intentionally preserved exactly as original. Do not clean, translate, redraw or otherwise modify it in this component.

## info5 — 战斗指挥输入 说明

1. `遭遇敌舰队后，可向舰娘舰队下达大致的战斗方针，`
2. `从而指挥战斗。`
3. `将战斗指挥指令编入战斗指挥框后，即可进行指挥输入。`

Blue semantic keyword:

- `战斗指挥指令`

The glyph `将` must render with a Simplified-Chinese localized form. A Japanese-localized glyph shape is QC FAIL.

## info6 — 战斗指挥输入 说明

### Nine command panels — final copy

| Visual command | Explanation |
| --- | --- |
| large `接近` | `逼近敌方舰队。` |
| large `脱离` | `尝试脱离战斗海域。` |
| large `航空` + small `攻击` | `实施舰载机航空攻击。` |
| large `炮击` | `展开炮击战。` |
| large `对潜` + small `攻击` | `实施爆雷攻击。` |
| large `突击` + small `（接近＋炮击）` | `一边炮击，一边逼近敌舰。` |
| large `雷击` | `展开鱼雷战。` |
| large `回避` | `实施回避机动。` |
| large `统射` + small `（统制射击）` | `实施电探统制射击。` |

The hierarchy itself is part of the translation spec. `攻击` after both `航空` and `对潜` is the secondary smaller cyan tier.

Do not change the final `统射` explanation to `电探控制射击`; the locked wording is:

`实施电探统制射击。`

### Body paragraph 1

1. `可输入的战斗指挥框数量，会随着旗舰练度的提升而增加。`
2. `可使用的战斗指挥指令，也会根据舰队编成和装备等发生变化。`

Blue semantic keywords:

- `旗舰练度`
- `战斗指挥指令`

### Body paragraph 2 + warning — one continuous block

1. `驱逐舰等舰船的基本雷击（鱼雷攻击），在最终阶段十分有效。`
2. `对潜水舰则推荐使用对潜（爆雷）攻击。舰队中编有航空母舰时，`
3. `也可选择航空攻击。如果只输入接近、回避、脱离等非攻击类指令，`
4. `舰队将完全不会发动攻击，请务必注意。`
5. `根据舰队编成、配置顺序和指挥输入，战斗内容也会发生变化。`

Blue semantic keywords:

- `雷击`
- `对潜`
- `航空攻击`
- `接近、回避、脱离`

The parenthetical explanations `（鱼雷攻击）` and `（爆雷）` remain white, matching the source semantic highlighting.

## Final rendering direction

The accepted V6 implementation uses the M001 info1/info2 visual principles, with original-page pixel measurements driving every placement decision:

- measured source-to-Vita non-uniform transform
- original bright-core bboxes and line-center spacing as layout constraints
- explicit Noto Sans CJK SC face, TTC index 2
- natural Chinese width
- SS8 text-layer rasterization
- one Lanczos source-space mapping/downsample
- RGBA32 Texture2D storage rather than BC3
- same white/cyan/outline family as the accepted tutorial style
- strict original-vs-Chinese overlay + line-spacing convergence
- explicit blue-highlight segment map

Do not recreate these pages from V2/V3/V4/V4.1. V6 is the accepted final visual state.

## Hardware result

The exact V6 asset writeback passed PSV Vita hardware testing on 2026-08-28.

Final cumulative `resources.assets` for this tested branch:

- Mother SHA-256: `cb8cdd0e872aa22ab603e5b2be2bba78219cd8d54450f96bc9107bbdc5b1d50a`
- Mother size: `1,283,402,344`
- Output SHA-256: `20e0a0232c96eeba213fe09f65e3f1742302e50eec6fcb777e4952ad07c79311`
- Output size: `1,290,218,052`

The Mother already contained parallel work from another chat. All non-target serialized objects were preserved byte-for-byte, so this hardware result does **not** supersede or renumber that parallel M003 work.
