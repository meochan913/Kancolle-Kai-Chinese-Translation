# v0.02 M002 — info3–6 Translation / Highlight Specification

Status: **translation copy locked; previous SS8 RGBA32 V2 visual layout rejected/incomplete pending strict original-pixel typography measurement.**

This document records the approved Chinese wording and semantic blue-highlight mapping so later sessions must not independently retranslate or restyle it.

## Persistent translation rules

- Write natural Chinese syntax. Do not preserve Japanese word order when it produces Japanese-style Chinese.
- When the original distinguishes a game function/keyword only through blue highlighting, preserve that distinction through blue highlighting in Chinese. Do **not** invent quotation marks, book-title marks, parentheses, or other emphasis punctuation that is absent from the source.
- Missing, extra, or semantically incorrect blue highlighting is QC FAIL.
- Chinese line width is not required to match Japanese line width. Match font height, baseline/vertical center, line spacing, hierarchy, alignment, safe area, and final game-space aspect ratio.
- Special key notation keeps no literal spaces outside the brackets; breathing room goes inside: `按【 L 】键`, `按【 R 】键`.
- Baked Simplified-Chinese tutorial text must explicitly select the Simplified-Chinese localized font face. For the current Noto CJK TTC files, index `2` is SC; default/index `0` is JP and is prohibited for Chinese baked text.

## Mandatory layout-measurement rule for this component

Before rendering a candidate, measure the original Japanese raster itself. Do not begin from visually guessed Y coordinates.

For every title, body paragraph, and info6 command panel:

1. derive the original visible glyph band from original-vs-clean-plate pixel evidence;
2. record top/bottom, visible height, line center, and adjacent line-center spacing;
3. measure each typography tier independently;
4. render Chinese with a shared baseline/line model;
5. compare original vs Chinese in measured Vita screen geometry using strict overlay and line guides;
6. reject any candidate rendered before this evidence exists.

A broad 50% page overlay by itself is not sufficient. The source-line measurements must drive the layout.

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

The first paragraph and second paragraph use different original font sizes. Preserve this hierarchy; do not redraw both paragraphs at one common size.

### Paragraph 1 — larger body size

1. `在编成界面中，可将舰娘编入舰队或进行替换。`
2. `在每支舰队中，可编入最多六支舰娘。`

Blue semantic keywords:
- `编成`
- `最多六支`

`最多六支` intentionally mirrors the semantic emphasis of original `最大六隻`.

### Paragraph 2 — smaller body size

1. `根据舰队编成，出击时的航线有时会发生较大变化。`
2. `若无法顺利攻略作战海域，除了提升舰队练度、`
3. `完善装备外，调整舰队编成也是一种有效的方法。`
4. `尤其是驱逐舰为主力的水雷战队，由1艘轻巡洋舰担任旗舰会更有效。`

Blue semantic keywords:
- `航线`
- `水雷战队`

### Ship-category list

The right-side Japanese ship-category list is intentionally preserved exactly as original. Do not clean, translate, redraw, or otherwise modify it in this component.

## info5 — 战斗指挥输入 说明

1. `遭遇敌舰队后，可向舰娘舰队下达大致的战斗方针，`
2. `从而指挥战斗。`
3. `将战斗指挥指令编入战斗指挥框后，即可进行指挥输入。`

Blue semantic keyword:
- `战斗指挥指令`

The glyph `将` must render with a Simplified-Chinese localized form; a Japanese localized glyph shape is QC FAIL.

## info6 — 战斗指挥输入 说明

### Nine command panels

Command name and explanation use different original font sizes. Preserve the hierarchy: command name is larger/cyan, explanation is smaller/white.

| Command name (cyan) | Explanation (white) |
| --- | --- |
| `接近` | `逼近敌方舰队。` |
| `脱离` | `尝试脱离战斗海域。` |
| `航空攻击` | `实施舰载机航空攻击。` |
| `炮击` | `展开炮击战。` |
| `对潜攻击` | `实施爆雷攻击。` |
| `突击（接近＋炮击）` | `一边炮击，一边逼近敌舰。` |
| `雷击` | `展开鱼雷战。` |
| `回避` | `实施回避机动。` |
| `统射（统制射击）` | `实施电探统制射击。` |

Do not change the final explanation to `电探控制射击`; the locked wording is `实施电探统制射击。`.

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

## Rendering direction

Render info3–6 using the accepted M001 info1/info2 visual path wherever compatible, but only after exact original typography measurements are recorded:

- measured source-to-Vita non-uniform transform;
- explicit Simplified-Chinese localized font face;
- natural Chinese width;
- SS8 text-layer rasterization;
- one Lanczos mapping/downsample into 1024×512 source-space;
- RGBA32 visual path instead of BC3 where the final Texture2D conversion is adopted;
- same white/cyan palette and outline logic as M001;
- strict original-vs-Chinese typography QC driven by actual source-pixel line bands, including title hierarchy, font height, vertical centers/baselines, line-center spacing, safe area, and explicit blue-highlight map.

The previous V2 render is not an accepted layout baseline because it used manually approximated line bands and the default Japanese TTC face. It must not be packaged or reused as-is.

Current render work remains visual-candidate only until exact asset writeback and PSV Vita hardware validation are completed.
