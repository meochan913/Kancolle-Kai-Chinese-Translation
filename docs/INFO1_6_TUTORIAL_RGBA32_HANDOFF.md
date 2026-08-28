# Canonical Handoff — info1_set through info6_set Tutorial RGBA32 Pipeline

Date: 2026-08-28

Status: **info1–6 tutorial family PSV Vita hardware validated.**

This document is intentionally implementation-heavy. It exists so a future chat can answer not only “what is final?” but also “how was it produced, why was that method chosen, what failed before, and how must it be extended without regression?”

## 0. Component numbering warning

Two chats developed v0.02 work in parallel and reused M002/M003-style working labels.

Therefore:

- do **not** infer global component order from filenames containing `M002_INFO3_6`;
- do **not** rename or overwrite `docs/M003_R4_HANDOFF_ADDENDUM.md`;
- use the canonical non-numeric ID `strategy-tutorial-info1-6-rgba32` for this tutorial family;
- the current manifest is `manifests/v0.02-strategy-info1-6-vita-pass.json`.

The info3–6 exact Vita-tested Mother already contained other-chat cumulative changes. Our writeback preserved all non-target serialized objects byte-for-byte.

---

# 1. Final hardware status and exact hashes

## info1 / info2 + TutorialGuide1 — M001

Exact Vita-tested package:

`Kancolle_Kai_v0.02_M001_RGBA32_VITA_CANDIDATE.zip`

ZIP SHA-256:

`2e0f1a312dbf4f0618ac2860aa4ee72943045c79253ae69912e0bd8cdcf22eb8`

M001 development Mothers:

- `resources.assets`: `f19fbcf5f2be01bd386ff4f126688ab7685f3df3426881924797863348f7fce8`
- `sharedassets2.assets`: `7cde6cf01ae29fa4a31d72c1d2865016e30ddf4809d7d699cb3b7d415568ee61`

M001 outputs:

- `resources.assets`: `fe3c836c9f3a4ad98a2a34e4bd7c2319ca7e1a9d6e3eb9c8d99f1245d3903c7e`
- `sharedassets2.assets`: `80121aad85c0790472c474f2988f5ea5b41a2868eade45fabdfa5a9c6014b34d`

Status: `VITA PASS / FINAL / LOCKED`.

## info3 / info4 / info5 / info6 — final V6

Historical package name:

`Kancolle_Kai_v0.02_M002_Info3_6_RGBA32_VITA_CANDIDATE.zip`

ZIP SHA-256:

`87b3d0838ec6b1050e51b5914014edb824ef694c325b12107abeb89542cca2c8`

Exact cumulative `resources.assets` Mother supplied after parallel-chat work:

- SHA-256: `cb8cdd0e872aa22ab603e5b2be2bba78219cd8d54450f96bc9107bbdc5b1d50a`
- size: `1,283,402,344` bytes

Exact output used for successful Vita test:

- SHA-256: `20e0a0232c96eeba213fe09f65e3f1742302e50eec6fcb777e4952ad07c79311`
- size: `1,290,218,052` bytes

Status: `VITA PASS / FINAL / LOCKED`.

**Important:** `cb8c...` was not the old M001-only file. It already contained unrelated work from another chat. Future patching must start from the latest exact cumulative Mother actually in use, not from `fe3c...` unless intentionally rebuilding the older branch.

---

# 2. Asset locations

All six full-screen tutorial textures live in `resources.assets`.

| Page | Name | PathID | Original format | Final format | Mips |
| --- | --- | ---: | --- | --- | ---: |
| 1 | `info1_set` | 4363 | DXT5/BC3 | RGBA32 | 1 |
| 2 | `info2_set` | 2180 | DXT5/BC3 | RGBA32 | 1 |
| 3 | `info3_set` | 1420 | DXT5/BC3 | RGBA32 | 1 |
| 4 | `info4_set` | 5059 | DXT5/BC3 | RGBA32 | 1 |
| 5 | `info5_set` | 3028 | DXT5/BC3 | RGBA32 | 11 |
| 6 | `info6_set` | 4413 | DXT5/BC3 | RGBA32 | 1 |

M001 TutorialGuide1 also touches `resources.assets`:

- Prefab root: PathID `29580`
- title UILabel: PathID `59638`
- body UILabel: PathID `58051`
- `Atlas_TutorialGuide`: PathID `1886`, intentionally unchanged

The simplified `键` glyph fix is in `sharedassets2.assets`.

---

# 3. Why RGBA32 is final

Early REDO candidates kept the pages as BC3/DXT5. On Vita, new Chinese text looked like very low-bitrate video: blocky gray/blue contamination and blurred strokes.

Strict RCA found two primary causes.

## 3.1 Pillow DXT5 encoder quality was poor

Representative same-raster measurements:

- Pillow DXT5: RGB MAE ~`14.46`, Alpha MAE ~`3.54`, PSNR ~`22.04 dB`
- ImageMagick DXT5: RGB MAE ~`11.45`, Alpha MAE ~`0.75`, PSNR ~`24.78 dB`

Even a Japanese original texture recompressed without editing showed a large quality gap between Pillow and ImageMagick.

## 3.2 Chinese antialiasing is hostile to BC3's 4×4 color budget

Text-touching BC3 blocks often contained roughly:

- median `13` distinct RGB colors
- P90 `16`

while BC3 color endpoints/indexing can effectively represent only four RGB colors per 4×4 color block.

The result was inevitable block quantization.

## 3.3 Accepted solution

Stop trying to make the Chinese glyph raster “BC3-friendly”. Use:

- 1024×512 final source texture
- RGBA32 TextureFormat `4`
- text layer rendered at SS8
- one Lanczos mapping/downsample to source space
- no BC3 compression afterward

This removed texture-codec loss while preserving natural antialiasing and normal Chinese glyph proportions.

The exact RGBA32 files loaded correctly on Vita and were hardware accepted.

---

# 4. Source-to-Vita geometry

The game does not display the 1024×512 tutorial texture 1:1.

Measured source -> Vita affine:

```text
x_screen ≈ 0.937448988 * x_source
           - 0.000068203 * y_source
           + 0.045778

y_screen ≈ 0.000064234 * x_source
           + 1.127019970 * y_source
           - 12.528998
```

Operational approximation:

- X scale ≈ `0.93745×`
- Y scale ≈ `1.12702×`
- Y offset ≈ `-12.53 px`

The stretch is non-uniform and real.

All typography must be designed and QC'd in game/screen geometry. A raw 1024×512 source preview is not sufficient.

---

# 5. Non-negotiable layout method: Overlay + Line Spacing

This is the highest-priority rule for future tutorial pages.

**Overlay + line spacing is not a reporting format. It is the layout solver.**

Required workflow:

1. Start from the Japanese original raster.
2. Build/obtain a clean plate.
3. Measure actual source text pixels before Chinese rendering:
   - bright-core glyph bbox
   - top/bottom
   - visible height
   - line center
   - adjacent line-center spacing
   - paragraph typography tier
   - left/right anchor logic
4. Select one font size for each source typography tier.
5. Render Chinese from those constraints.
6. Transform both original and candidate into measured Vita geometry.
7. Overlay and compare.
8. Feed the mismatch back into the render parameters.
9. Repeat until the geometry converges.
10. Only then make a QC image for the user.

Prohibited workflow:

- guess a font size
- guess Y coordinates
- render a full page
- make an overlay afterward
- call it QC

If overlay does not influence the parameters, it is not the accepted method.

## 5.1 Measure bright core, not outer changed-pixel bbox

A rejected title candidate matched the Japanese outer subtitle rectangle exactly, yet the Chinese bright core was ~15.4% too short.

Therefore outer outline/shadow/antialias bbox equality does not prove equal font size.

Measure the visible bright core and use line center/spacing separately.

## 5.2 Translation width is not a constraint

Do not force Chinese line length to equal Japanese line length.

Do not horizontally squeeze/expand Chinese to match the source phrase width.

Match:

- font/glyph height
- vertical center/baseline
- line spacing
- hierarchy
- source anchor logic
- safe area
- final game-space aspect

Chinese width remains natural unless it collides or clips.

---

# 6. Font selection

For baked Simplified-Chinese tutorial text:

- family file used in this workflow: `NotoSansCJK-Bold.ttc`
- required localized face: **Noto Sans CJK SC**
- TTC index: **2**

Do not rely on TTC default face.

TTC index `0` is Japanese (`Noto Sans CJK JP`) and produced visibly Japanese-localized glyph forms such as `将`.

Future scripts must specify the SC face explicitly.

Do not rebuild already Vita-accepted info1/info2 from remembered font parameters just to “standardize” them. Preserve the exact accepted raster unless those pages are explicitly reopened.

---

# 7. Clean Plate — info1 / info2

The maintained accepted clean plate is `info2 V12`.

info1 and info2 use the same visual background; info1 reuses the exact clean base and differs in translated text.

Known rejected clean-plate iterations:

- V4: Japanese glyph residue remained
- V8: black-spot contamination

## 7.1 Recovered final V12 refinement algorithm

The final refinement branch was `A8 / D0`.

It was **not** a large flat-color rectangle and was not the final use of generic inpainting.

Core idea: **glyph-local same-row RGBA interpolation**.

For each target row, estimate clean background alpha from side regions, historically around:

```text
left side  x ≈ 20..130
right side x ≈ 875..980
```

Text-like mask includes:

- white text pixels
- cyan text pixels
- alpha significantly above row background

The final alpha excess threshold was `+8` (`A8`).

The final mask expansion was `D0`: **no dilation**.

For each contiguous masked glyph run on a row:

1. find nearest unmasked clean pixel to the left (`L`)
2. find nearest unmasked clean pixel to the right (`R`)
3. linearly interpolate **R/G/B/A** from L to R
4. replace only the run

This preserves panel transparency and the original background texture much better than flat paint.

### Important uncertainty

V12 was refined on top of an earlier V1 clean result. The exact original from-scratch V1 generation code was not fully preserved. Do not invent a missing algorithm name or claim V12 can be exactly recreated from only the A8/D0 note.

The accepted V12 raster itself is canonical.

---

# 8. Clean Plate — info3 through info6

The accepted clean-slate lineage is based on the refined info3–6 clean work, later combined with V12 donor reconstruction for the common blue panel background.

Key observations:

- large clean margins of info3–6 and V12 are RGBA byte-identical
- the blue tutorial background has an approximately 49–50 px vertical repeat structure
- the correct method is to reuse real game background texture, not synthesize a blue rectangle

## 8.1 Body-background donor logic

For body rows requiring reconstruction:

- use V12 clean lower-panel rows as donor
- for a target row below the clean donor range, shift by ~50px periods until a clean donor row is reached
- keep donor within the known clean lower-panel range
- derive a per-row RGBA correction from a genuinely clean page margin (historically x≈20..100) so page-specific row brightness/alpha remains consistent

This donor strategy avoids reintroducing the info1/info2 central demonstration screenshot.

## 8.2 info3 / info5 bottom-right residual cleanup

Residual Japanese text near the waterplane/seaplane logo was refined using **exact V12 same-coordinate real RGBA donor data**.

The plane-logo region itself was protected and verified unchanged.

## 8.3 info4 protection

The right-side Japanese ship-category list is intentionally **not translated** in this component.

It must not be cleaned, erased, redrawn or recolored.

The final workflow used a hard protected region and verified zero changes there.

## 8.4 info6 command panels

All nine Japanese command-name/explanation texts were removed for translation, while preserving:

- colored panel backgrounds
- button icons
- borders

Panel cleanup uses the panel's own local background structure rather than painting the main blue tutorial background into the colored button panels.

The final V6 only changed typography after the clean panel base was accepted.

---

# 9. Final title geometry — info3 through info6 V6

Final shared render parameters:

- main title SS8 nominal size: `45.5`
- main title stroke: `2.0`
- `说明` SS8 nominal size: `32.5`
- `说明` stroke: `2.0`
- font: Noto Sans CJK SC index 2
- one Lanczos source mapping
- no anisotropic text stretch

Original bright-core targets:

| Page | Main target bbox | `解説` target bbox |
| --- | --- | --- |
| info3 | `(335,31)-(583,69)` | `(594,41)-(662,67)` |
| info4 | `(359,31)-(556,69)` | `(568,41)-(636,67)` |
| info5 | `(308,31)-(605,69)` | `(618,41)-(686,67)` |
| info6 | `(308,31)-(605,69)` | `(618,41)-(686,67)` |

Constraints:

- main bright-core height exactly `38 px`
- subtitle bright-core height exactly `26 px`
- main right edge anchored to source main-title right edge
- main top/bottom anchored to source main top/bottom
- subtitle left edge anchored to source `解説` left edge
- subtitle top/bottom anchored to source subtitle top/bottom
- main center Y = `50.0`
- subtitle center Y = `54.0`
- relative center offset = `+4.0 px`
- Chinese widths natural

Exact main-to-subtitle gaps reproduced:

- info3: `11 px`
- info4: `12 px`
- info5: `13 px`
- info6: `13 px`

This is the accepted V6 title method.

Rejected alternatives:

- forcing `说明` into the Japanese subtitle width
- matching only an outer outline rectangle
- per-page arbitrary size selection without overlay convergence

---

# 10. Final body typography — info3 through info6

Body was approved before the V6 title correction and kept frozen while titles/buttons were finalized.

Recorded nominal sizes:

| Page/tier | Nominal size | Stroke |
| --- | ---: | ---: |
| info3 all body | ~24.3125 | 1.1 |
| info4 paragraph 1 | ~22.0625 | 1.1 |
| info4 paragraph 2 | ~20.6875 | 1.0 |
| info5 all body | ~24.5625 | 1.1 |
| info6 all lower body | ~22.9375 | 1.0 |

These numbers document the accepted implementation. They do not replace measuring the original raster if rebuilding.

Body hierarchy locks:

- info3: both paragraphs same size, all lines common left alignment
- info4: paragraph 1 one larger size; paragraph 2 one smaller size; no per-line size variation
- info5: entire body one size and common left alignment
- info6: both lower body blocks, including warning, one common size

Never resize one line just because the Chinese line is longer/shorter.

---

# 11. Final translation and blue-highlight map

Blue emphasis is semantic. Missing blue, extra blue or blue on the wrong word is QC FAIL.

Do not add quotation marks or other emphasis punctuation when the original uses only color to mark a game function.

## info3

Title:

`旗舰提督室　说明`

Paragraph 1:

```text
这里就是旗舰提督室，相当于《舰队Collection 改》的母港界面。
在这里可进行舰队的编成，在工厂可进行舰娘的建造和装备的开发
也可通过补给、入渠和改装来强化舰娘。
```

Blue:

- `旗舰提督室`
- `编成`
- `工厂`
- `建造`
- `开发`
- `补给`
- `入渠`
- `改装`

Paragraph 2:

```text
按【 L 】键可切换至图鉴、家具店等提督室子菜单。
此外，还可使用战略点数获取各种有助于战局的道具。
请通过记录进行战况的保存。
```

Blue:

- `【 L 】`
- `图鉴`
- `家具店`
- `记录`

`记录` has no quotation marks.

Special-symbol spacing reminder:

- correct: `按【 L 】键`
- no exterior spaces
- spaces are only inside `【 L 】`

## info4

Title:

`编成界面　说明`

Paragraph 1:

```text
在编成界面中，可将舰娘编入舰队或进行替换。
在每支舰队中，可编入最多六支舰娘。
```

Blue:

- `编成`
- `最多六支`

Paragraph 2:

```text
根据舰队编成，出击时的航线有时会发生较大变化。
若无法顺利攻略作战海域，除了提升舰队练度、
完善装备外，调整舰队编成也是一种有效的方法。
尤其是驱逐舰为主力的水雷战队，由1艘轻巡洋舰担任旗舰会更有效。
```

Blue:

- `航线`
- `水雷战队`

Right-side ship-category list remains original Japanese.

## info5

Title:

`战斗指挥输入　说明`

Body:

```text
遭遇敌舰队后，可向舰娘舰队下达大致的战斗方针，
从而指挥战斗。
将战斗指挥指令编入战斗指挥框后，即可进行指挥输入。
```

Blue:

- `战斗指挥指令`

The glyph `将` must use the SC form, not JP localized form.

## info6

Title:

`战斗指挥输入　说明`

Body block 1:

```text
可输入的战斗指挥框数量，会随着旗舰练度的提升而增加。
可使用的战斗指挥指令，也会根据舰队编成和装备等发生变化。
```

Blue:

- `旗舰练度`
- `战斗指挥指令`

Body block 2 + warning, one continuous block:

```text
驱逐舰等舰船的基本雷击（鱼雷攻击），在最终阶段十分有效。
对潜水舰则推荐使用对潜（爆雷）攻击。舰队中编有航空母舰时，
也可选择航空攻击。如果只输入接近、回避、脱离等非攻击类指令，
舰队将完全不会发动攻击，请务必注意。
根据舰队编成、配置顺序和指挥输入，战斗内容也会发生变化。
```

Blue:

- `雷击`
- `对潜`
- `航空攻击`
- `接近、回避、脱离`

`（鱼雷攻击）` and `（爆雷）` remain white.

---

# 12. info6 nine-command typography

Exactly three tiers.

## Primary cyan large tier

Nominal size `22.5`, stroke `1.0`.

- `接近`
- `脱离`
- `航空`
- `炮击`
- `对潜`
- `突击`
- `雷击`
- `回避`
- `统射`

## Secondary cyan smaller tier

Nominal size `17.75`, stroke `1.0`.

- `攻击` after `航空`
- `攻击` after `对潜`
- `（接近＋炮击）`
- `（统制射击）`

## White explanation tier

Nominal size `15.0`, stroke about `0.75`.

Final commands:

| Visual name | Explanation |
| --- | --- |
| `接近` | `逼近敌方舰队。` |
| `脱离` | `尝试脱离战斗海域。` |
| `航空` + small `攻击` | `实施舰载机航空攻击。` |
| `炮击` | `展开炮击战。` |
| `对潜` + small `攻击` | `实施爆雷攻击。` |
| `突击` + small `（接近＋炮击）` | `一边炮击，一边逼近敌舰。` |
| `雷击` | `展开鱼雷战。` |
| `回避` | `实施回避机动。` |
| `统射` + small `（统制射击）` | `实施电探统制射击。` |

V5 already had the other eight command panels accepted. V6 changed only the fifth name from all-large `对潜攻击` to large `对潜` + small `攻击`; the other eight panels remained byte-identical during that final correction.

---

# 13. info1 / info2 final text reminders

These pages are already locked. Do not redraw them merely to make them match later implementation code.

## info1

Title:

`战略界面　说明`

Body:

```text
战略界面是《舰队Collection 改》的核心界面。
在这里可让舰队出击至作战海域、向相邻海域移动，
并可配置运输船等，以获取资源、确保兵站补给。
```

Blue:

- `战略界面`
- `出击`
- `移动`
- `配置`

`出击` is a specific regression gate because an earlier candidate accidentally left it white.

## info2

Body:

```text
从战略界面可前往舰队旗舰所在的旗舰提督室，
按【 R 】键即可移动。
```

Blue:

- `战略界面`
- `旗舰提督室`
- `【 R 】`

Correct spacing: `按【 R 】键`.

---

# 14. TutorialGuide1 / dynamic 键 glyph

TutorialGuide1 is not a baked full-screen page.

Final visual structure:

- title: `前往旗舰提督室界面`
- `旗舰提督室` highlighted green
- body line 1: `按下` + native R button Sprite + `键`
- body line 2: `即可前往旗舰提督室！`

Do not replace the native R Sprite with textual `【 R 】` in this prefab.

An earlier candidate serialized `键` correctly but rendered it blank on Vita. The actual font chain lacked the simplified glyph.

Final fix in `sharedassets2.assets`:

- donor: real Simplified-Chinese `键` outline from the UD Shin Go Pro resource in `sharedassets3`
- destination unused glyph: `cid15443`
- new cmap mapping: `U+952E 键 -> cid15443`
- old mappings retained
- unrelated outlines retained
- Traditional `鍵` unchanged
- do not regress to a fake `键 -> 鍵` alias

This exact glyph transplant is Vita-proven.

---

# 15. SerializedFile RGBA32 reconstruction

Game Unity version: `5.2.2p3`.

`resources.assets` uses SerializedFile version `15`.

The object table stores explicit:

- `byteStart`
- `byteSize`

This makes safe object expansion/repacking possible when metadata is updated correctly.

## 15.1 1-mip 1024×512 pages

Old DXT5 object:

- Texture2D header: `76` bytes
- image payload: `524,288` bytes
- object size: `524,364`
- TextureFormat: `12`

New RGBA32 object:

- header: `76` bytes
- image payload: `2,097,152` bytes
- object size: `2,097,228`
- TextureFormat: `4`

## 15.2 info5 with 11 mips

Original:

- object size: `699,164`
- image bytes: `699,088`

Final RGBA32:

- object size: `2,796,280`
- image bytes: `2,796,204`
- mip count: `11`, preserved

RGBA mip dimensions/bytes:

1. 1024×512 = 2,097,152
2. 512×256 = 524,288
3. 256×128 = 131,072
4. 128×64 = 32,768
5. 64×32 = 8,192
6. 32×16 = 2,048
7. 16×8 = 512
8. 8×4 = 128
9. 4×2 = 32
10. 2×1 = 8
11. 1×1 = 4

Total = `2,796,204` image bytes.

Each mip is generated **directly from the final mip0 using Lanczos**, not recursively from the previous mip.

Each mip is vertically flipped independently before raw Unity RGBA storage.

This approach was checked against existing game RGBA32 mipmapped Texture2D data (e.g. PathID 2947), where stored lower mips matched direct-Lanczos-from-mip0 extremely closely (~0.05–0.18 MAE/channel in tested levels).

---

# 16. Final info3–6 writeback object data

Exact reconstruction recipe from the Vita-tested package:

Mother:

- hash `cb8cdd0e872aa22ab603e5b2be2bba78219cd8d54450f96bc9107bbdc5b1d50a`
- size `1,283,402,344`
- dataOffset `1,854,080`
- object count `65,462`

Output:

- hash `20e0a0232c96eeba213fe09f65e3f1742302e50eec6fcb777e4952ad07c79311`
- size `1,290,218,052`

Targets:

### PathID 1420 / info3_set

- old start `247,963,008`
- old size `524,364`
- new size `2,097,228`
- final source PNG SHA-256 `12e2ad80d6c0f0a10cccff1644ac75d4fd572d96167f29f750d2c61a34297c34`
- object payload SHA-256 `7326e8ffd1529beb3c3abb82ffa1205c427af3ddbf9e853bab2a1e9be16952fc`

### PathID 3028 / info5_set

- old start `591,818,956`
- old size `699,164`
- new size `2,796,280`
- final source PNG SHA-256 `59c10cc5a5bca2307f946ef1925e88ade3cc658a9fa2b02cba250cea899d3ad7`
- object payload SHA-256 `895fa0aee66405f7e9b034a063d857de59b77b72f471532ceab34f394ae793ac`

### PathID 4413 / info6_set

- old start `888,835,528`
- old size `524,364`
- new size `2,097,228`
- final source PNG SHA-256 `3b6e69019d897dd3ba7765803ac8143f7e431e2eb2374795082ee73917397274`
- object payload SHA-256 `0f7238c9424adb1dd1984fcb14580d2d9ee396416509a9dda84262986404a6e1`

### PathID 5059 / info4_set

- old start `1,017,916,696`
- old size `524,364`
- new size `2,097,228`
- final source PNG SHA-256 `4a693c7b8c90d8152415e08e0e5c08721fd80f2cf1a30663da98ef8438d2042e`
- object payload SHA-256 `d81ee68a7515204cf7d8f2b54ec7a8605badbd2755d7bda2c63f2c3fe9187ae1`

---

# 17. Structural QC gates

The final info3–6 reconstruction passed these offline gates before hardware testing:

- non-target serialized object mismatch count = `0`
- inter-object gap mismatch count = `0`
- unexpected metadata diff count = `0`
- all target mip0 rasters decoded from rebuilt assets = exact approved source RGBA
- M001 Vita-PASS resources objects remained byte-identical to their accepted payloads
- independent compact-recipe replay produced the exact same final full-file hash

M001 retained resource-object payload checks included PathIDs:

- 2180
- 4363
- 35599
- 58051
- 59638

Do not call a reconstruction PASS if non-target object bytes differ unexpectedly.

---

# 18. How to merge with work from another chat

This is essential because the exact info3–6 Mother already included parallel changes.

Before writing any future tutorial patch:

1. Ask for / obtain the **actual latest cumulative file** currently used by the user.
2. Hash it.
3. Do not assume the previous component output is still the Mother.
4. Parse the target PathIDs.
5. Verify whether the target objects themselves changed.
6. Verify known locked objects/components are still intact where applicable.
7. Build from that exact Mother.
8. Preserve every non-target object byte-for-byte.
9. After rebuild, independently replay and compare exact full-file SHA.
10. Only after hardware validation may the new output become the next trusted cumulative Mother.

If another chat modifies `resources.assets` after `20e0...`, do not apply the old `cb8c -> 20e0` package to it. Rebase the four target-object replacements against the new exact cumulative Mother.

Do not infer that M003 as a whole passed hardware simply because the file containing some M003 work also passed the info3–6 tutorial test. Component hardware acceptance remains scoped to what was actually exercised and confirmed.

---

# 19. Installer / Windows PowerShell pitfalls

Known permanent rules:

- CMD wrapper must be ASCII / no BOM; UTF-8 BOM once produced `´╗┐@echo off`.
- PowerShell helper names must be descriptive; avoid single-letter `H` hash functions.
- Never use `$Input` as a custom PowerShell variable/parameter because it collides case-insensitively with automatic `$input`.
- Use explicit `$InputStream` / `$OutputStream` style names.
- Windows PowerShell 5.1 may fail when directly wrapping `Generic.List` using `@($GenericList)` for JSON reports; explicitly copy into a normal array first.
- Report/hash generation should be independently recoverable after a large rebuild.
- Development patchers should fail closed on exact Mother SHA.
- Do not modify the source file in place; write output to a separate folder.

---

# 20. Fail-closed QC philosophy

A PASS requires evidence from the actual current file/raster/tool output.

Examples of automatic FAIL/INCOMPLETE:

- missing exact Mother hash evidence
- target PathID not found
- target expected to visibly change but visible RGBA change = 0
- non-target locked object changed unexpectedly
- line spacing only eyeballed
- overlay made after layout without feeding back into parameters
- SC text accidentally rendered through JP TTC face
- blue keyword missing or extra
- clean plate still has glyph residue
- hardware status inferred from offline QC

Offline QC PASS != Vita PASS.

Vita PASS/LOCKED components are frozen unless explicitly reopened.

---

# 21. Canonical project files to read first in a new chat

Before extending/rebuilding info1–6, read:

1. `manifests/v0.02-strategy-info1-6-vita-pass.json`
2. `docs/INFO1_6_TUTORIAL_RGBA32_HANDOFF.md`
3. `docs/TUTORIAL_TEXTURE_RENDERING_SOP.md`
4. `docs/CRITICAL_OVERLAY_LINE_SPACING_LAYOUT_RULE.md`
5. `docs/V002_M002_INFO3_6_TRANSLATION_SPEC.md`
6. `docs/M002_INFO3_6_OVERLAY_LAYOUT_LOCKS.md`
7. `docs/V002_DEVELOPMENT.md`
8. `PROJECT_PATCH_LEDGER.json`
9. `docs/M003_R4_HANDOFF_ADDENDUM.md` if parallel M003 work is still relevant

Do not rely on the numeric `M002` label in historical info3–6 filenames to determine component order.

---

# 22. Short answer to the most likely future questions

**Q: Which file contains info1–6?**  
A: `resources.assets`.

**Q: Which PathIDs?**  
A: info1=4363, info2=2180, info3=1420, info4=5059, info5=3028, info6=4413.

**Q: What format is final?**  
A: RGBA32 / TextureFormat 4.

**Q: Why not BC3?**  
A: Chinese antialiasing + BC3 4×4 color quantization caused hardware-visible mosaic artifacts; RGBA32 eliminated texture-codec loss.

**Q: What scaling does the game apply?**  
A: roughly X×0.93745, Y×1.12702, Y offset -12.53; use the full affine above.

**Q: How is typography laid out?**  
A: only by original-pixel measurement + overlay + line-spacing convergence. Never by eyeballing.

**Q: Which font face?**  
A: Noto Sans CJK SC, TTC index 2. JP index 0 prohibited for baked Chinese.

**Q: What supersampling?**  
A: SS8 text layer, one Lanczos mapping/downsample into source space.

**Q: How are clean plates made?**  
A: reuse real game texture. info1/2 final refinement uses A8/D0 glyph-local same-row RGBA interpolation; info3–6 use refined clean plates plus real V12 periodic/background donors and protected regions, not flat rectangles.

**Q: Does info4 ship-type list get translated?**  
A: No. Preserve original Japanese exactly.

**Q: Does info5 keep mips?**  
A: Yes, all 11. Generate each directly from final mip0 with Lanczos and flip each mip for Unity raw storage.

**Q: How do I continue after another chat changed resources.assets?**  
A: get the latest exact cumulative file, hash/audit it, and rebase the target-object replacements. Never assume the old Mother.

**Q: What is the latest exact validated info3–6 output in this branch?**  
A: `resources.assets` SHA-256 `20e0a0232c96eeba213fe09f65e3f1742302e50eec6fcb777e4952ad07c79311`.

**Q: Does that mean parallel M003 passed Vita?**  
A: No. It means the exact cumulative file containing that parallel work plus the info3–6 replacement ran successfully for the tested info3–6 scope. M003 keeps its own status.
