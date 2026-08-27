# Translation Style Rules

These rules are persistent project-level guidance for Chinese localization text and visual typography.

## Natural Chinese syntax

Do not preserve Japanese sentence order merely because the source sentence is structured that way. Translate meaning first, then rewrite into natural Chinese syntax.

A literal Japanese-order sentence that reads awkwardly in Chinese is not acceptable just because every source phrase has been preserved in sequence.

## Do not add editorial punctuation or emphasis

Do not add quotation marks, book-title marks, parentheses, or other editorial punctuation that is not present in the source unless the Chinese grammar itself genuinely requires it.

If the original distinguishes a game-function keyword only by color/highlight, preserve that semantic distinction through the corresponding Chinese highlight. Do not invent quotation marks around the function name.

Example confirmed for Strategy Tutorial info3:

- preferred: `请通过记录进行战况的保存。`
- avoid adding quotes around `记录` merely to mark it as a game function; its functional distinction is carried by the original blue-highlight convention.

## Blue-highlight semantic mapping

Original blue-highlighted words are part of the functional/semantic design, not decoration.

For every translated tutorial/UI texture:

1. inventory every blue-highlighted source keyword/phrase;
2. map it to the exact corresponding Chinese translation segment;
3. render that Chinese segment blue;
4. verify the map after final rasterization/writeback.

Missing a required blue highlight, highlighting the wrong Chinese segment, or losing a highlight during later edits is a QC failure.

This rule is especially important for the Strategy Tutorial pages, where blue text distinguishes operations, commands, locations, or game-function keywords from normal explanatory text.

## Preserve source typography hierarchy

Do not flatten distinct source font sizes into a single Chinese size.

For each page, separately identify and match the source hierarchy in game/screen space, including font height, baseline/vertical center, and line spacing.

Confirmed current examples:

- `info4`: the first body paragraph and second body paragraph use different source font sizes; the Chinese layout must preserve that difference.
- `info6`: each command button has a larger command name and a smaller explanatory line; the Chinese version must preserve these two sizes rather than rendering both at one size.
- Strategy Tutorial title: the main title and subtitle use different sizes and must be calibrated separately.

## Translation width is not a target

Do not squeeze or stretch Chinese merely to match the Japanese line width. Match height, baseline, line spacing, hierarchy, alignment, and safe area; allow Chinese line length to differ naturally.

## Special-symbol spacing

For textual full-width button brackets, keep Chinese text adjacent to the outer brackets and place optional visual spacing inside them.

Preferred: `按【 R 】键`

Avoid: `按 【R】 键` and `按 【 R 】 键`.

When a native UI sprite represents the button, use the sprite as a real UI element rather than replacing it with textual brackets.

## Current info3–6 translation/layout notes

- `info4` right-side ship-category list remains untranslated and must be preserved exactly unless the user explicitly reopens it.
- `info3` final second-paragraph last line: `请通过记录进行战况的保存。`
- `info4` first section second line: `在每支舰队中，最多可编入6名舰娘`
- `info4` second paragraph must fit the source paragraph count/typographic block and currently uses:
  - `根据舰队编成，出击时的航线有时会发生较大变化。`
  - `若无法顺利攻略作战海域，除了提升舰队练度、`
  - `完善装备外，调整舰队编成也是一种有效的方法。`
  - `尤其是驱逐舰为主力的水雷战队，由1艘轻巡洋舰担任旗舰会更有效。`
- `info5` reviewed translation is accepted as currently drafted.
- `info6` command-name and explanation text use different font sizes.
- `info6` `電探統制射撃` / command explanation is translated using `统制射击` terminology, not `电探控制射击`.
- `info6` lower explanatory/warning block should remain one continuous typographic block, matching the source grouping:
  - `驱逐舰等舰船的基本雷击（鱼雷攻击），在最终阶段十分有效。`
  - `对潜水舰则推荐使用对潜（爆雷）攻击。舰队中编有航空母舰时，`
  - `也可选择航空攻击。如果只输入接近、回避、脱离等非攻击类指令，`
  - `舰队将完全不会发动攻击，请务必注意。`
  - `根据舰队编成、配置顺序和指挥输入，战斗内容也会发生变化。`

These notes are a living localization reference and should be consulted before rendering or packaging later info3–6 candidates.
