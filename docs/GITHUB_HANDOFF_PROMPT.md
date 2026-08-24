# 《舰队Collection 改》汉化工程 — GitHub 跨会话接力提示词

你正在继续维护我的《舰队Collection 改》（KanColle Kai / 艦これ改）简体中文汉化工程。请把下面内容视为“接力索引”，但不要只相信这段提示词里的静态信息：**开始任何 GitHub 写操作前，必须先使用已连接的 GitHub connector 读取仓库中的 `PROJECT_PATCH_LEDGER.json`、`release-status/`、`manifests/`、README 和当前 main tree，以 GitHub 当前内容为最终事实源。**

## GitHub 仓库

Repository:
`meochan913/Kancolle-Kai-Chinese-Translation`

Public repo:
`https://github.com/meochan913/Kancolle-Kai-Chinese-Translation`

GitHub connector 已经成功连接，之前确认用户对该 repo 有 admin/push 权限。以后涉及这个仓库的读取、commit、文件修改、issue/PR 等操作，优先直接使用 GitHub connector，不要让我手工重复操作，除非 connector 的具体接口不支持二进制上传或 Release 动作。

## 当前正式版本

当前正式 Release:
`v0.01 — Pre-Game Translation Milestone`

Release URL:
`https://github.com/meochan913/Kancolle-Kai-Chinese-Translation/releases/tag/v0.01`

Release asset:
`Kancolle_Kai_CHS_v0.01.zip`

Release ZIP SHA-256:
`2d7df4bcdfbe011e5b0f2ce0090226ab4db1fcfdb5375f1b5c80a8f173c34269`

Checksum asset:
`Kancolle_Kai_CHS_v0.01_SHA256SUMS.txt`

v0.01 source/repository QC commit:
`a9a0ddf7bd0059751178dd062620d7209f4581e6`

GitHub Actions publication run:
`32681364998`

Release publication receipt:
`release-status/v0.01.json`

v0.01 的 GitHub Actions `publish` job 已确认 completed/success；其中 payload verification、deterministic ZIP build、Release create/verify、status receipt 和 status commit 全部 success。

## v0.01 已完成范围

v0.01 表示“正式进入游戏之前的玩家可见内容”已经完成汉化并阶段性收口，包括：

- 标题画面 / 初次就任 / 归任
- 标题版本信息
- 简体中文字库基础
- 初始模式选择
- 11 艘初始舰介绍
- 初始舰注音清理
- 提督名输入相关 UI
- 确认按钮
- 教程三页正文
- 教程妖精气泡
- ReceiveShip「续」按钮

教程三页正文 VisibleBlue 修复已 PSV Vita 实机 PASS。
三只教程妖精气泡已 PSV Vita PASS / LOCKED。
ReceiveShip PathID 224 的最终「续」为 game-space 左移 1px + 上移 1px，已 PSV Vita 实机 PASS。
这些已接受组件以后默认冻结，除非我明确要求重新打开。

下一阶段进入正式母港后的游戏 UI，开发版本线应进入 `v0.02`。

## Clean 1.02 正式 Mother 基线

公开 patch 不是从历史 RC / 中间 Mother 起算，而是从：
`1.00 本体 + 官方 1.02 Update 覆盖后的 clean source`

完整 57 文件 source manifest:
`manifests/clean-1.02.sha256.json`

v0.01 实际修改并要求 patcher preflight 校验的 8 个 clean Mother：

`level2`
SHA-256 `1baf870b0bfded8c6298c133ccd63aba434009d88deeabba7333fd1f7b07ed07`

`level5`
SHA-256 `c2739e6fd7440b200d44b46a492c3e9bb337302a1cc9ba92a01963f971be093b`

`Managed/Assembly-CSharp.dll`
SHA-256 `cb74f8991c7d80f7519b028581753acd006b488f8d160613dc6b215015362327`

`resources.assets`
SHA-256 `7845a58df2c72ff15fe72ebf134050bb4cc660e5de10274b317da4e9f62c72f4`

`sharedassets2.assets`
SHA-256 `7a799248d4e73c87d56fc047026921161ed1f2eb3b9bd57afe33afa0a4e643fc`

`sharedassets3.assets`
SHA-256 `dc1ee9c49058fb7f582c6c36ba076e2dfc4c50107f2d6350f026d0e4c25d9ec1`

`sharedassets5.assets`
SHA-256 `1c483cf3f68ddf7bf4693094a21468c95ca3287815204f8fdf1ced8a23b5aae0`

`sharedassets6.assets`
SHA-256 `914b586adcb0f28cbb7cc127d4032d8b0728c5d64e15ac85b20781533ed8a2a0`

历史开发阶段出现过的 `518f...`、`84ea...`、`a908...` 等 hash 是中间累计 Mother / RC 基线，**不能**作为公开 clean v0.01/v0.02 安装器的官方输入条件。

## v0.01 FINAL 输出 hash

`level2`
`e4620fba82e4b50124c412d5a885ca9255be9e8590b3db0ec080122762bb2e73`

`level5`
`9d83c6183e0cb4d064d2bc69199059396c0f5d06e970c335777a37749ee9fff5`

`Managed/Assembly-CSharp.dll`
`ae2b1f2a6c008f05f19ad10dd4a7c963ef8b5294d2e8d3b538b387370149d90e`

`resources.assets`
`f19fbcf5f2be01bd386ff4f126688ab7685f3df3426881924797863348f7fce8`

`sharedassets2.assets`
`7cde6cf01ae29fa4a31d72c1d2865016e30ddf4809d7d699cb3b7d415568ee61`

`sharedassets3.assets`
`05474b778394a89e3f11f3081418a6256fda1a7a16ff23d702279713fa83638b`

`sharedassets5.assets`
`c43eed5af97a0f8b2feb826759fa5cbbca1641e47d65928f2fde91e554f1fa23`

`sharedassets6.assets`
`f67cbd9f3cc8752a32e7383c2d04578c466ae9f5913ca7bcc34570f5ac78a487`

这些结果已经通过 clean 1.02 → v0.01 FINAL 独立 replay，生成结果与 Vita 实机使用的最终累计 `rePatch` 文件逐字节一致。

## Patch 架构

仓库不允许上传完整原版/修改版游戏 `.assets`、完整 `Assembly-CSharp.dll` 或其他版权游戏二进制。

公开版本只保存：
- `.kckpatch` 差分 payload
- patch/source/final SHA-256 manifests
- patcher / scripts
- `PROJECT_PATCH_LEDGER.json`
- QC 文档
- release notes
- 必要截图

v0.01 当前有 8 个 patch：
`patches/v0.01/Assembly-CSharp.dll.kckpatch`
`patches/v0.01/level2.kckpatch`
`patches/v0.01/level5.kckpatch`
`patches/v0.01/resources.assets.kckpatch`
`patches/v0.01/sharedassets2.assets.kckpatch`
`patches/v0.01/sharedassets3.assets.kckpatch`
`patches/v0.01/sharedassets5.assets.kckpatch`
`patches/v0.01/sharedassets6.assets.kckpatch`

payload SHA-256 manifest:
`manifests/v0.01-patch-payloads.sha256.json`

release manifest:
`manifests/v0.01.json`

安装器：
`APPLY_V001.cmd`
`tools/apply_v001.py`

安装器必须 fail-closed：
先一次性验证所有涉及 Mother 的 SHA-256；
任何一个错误立即停止；
再验证每条 patch old bytes；
应用完成后再次验证 FINAL SHA-256；
只有全部精确命中才允许 PASS。

## GitHub / Release 操作 SOP

`PROJECT_PATCH_LEDGER.json` 是项目级 single source of truth。正式组件必须记录 Mother SHA-256、Output SHA-256、patch 路径、QC/Vita 状态、superseded/locked 信息。

未来新版本（例如 v0.02）不要把 RC1→RC2→RC3 的开发链直接给用户。开发可以用累计 Mother，但正式 Release 必须重新整理成：
`clean 1.02 Mother → 当前版本 FINAL Vita-accepted output`
的单步 deterministic delta。

每次 Release 前必须：
- 从 GitHub 重新读取 ledger / manifests；
- 导入当前 FINAL Vita-accepted 文件；
- 对照 clean source；
- 生成单步 patch；
- 独立 replay；
- 确认 replay output 与 FINAL 逐字节一致；
- 确认 repo tree 没有误上传完整游戏 binary；
- 对 repo 里的 patch payload 做 size/hash QC；
- 再创建 Release。

GitHub connector 当前没有直接的 `create release + upload local binary asset` 动作。因此 v0.01 采用仓库内 GitHub Actions：
`.github/workflows/publish-v001.yml`

workflow 在 GitHub runner 上：
1. 验证 8 个 patch payload SHA-256；
2. deterministic 构建 Release ZIP；
3. 创建/验证 GitHub Release；
4. 上传 ZIP + SHA256SUMS；
5. 写回 `release-status/v0.01.json`；
6. commit status receipt。

今后如果 connector 仍没有 Release write action，可沿用这种 “GitHub Actions + auditable status receipt” 的发布方式，但每个正式版本最好使用自己的 workflow/tag，避免误覆盖旧 Release。
**不要修改或覆盖 v0.01 Release 资产，除非我明确要求修复 v0.01。**

## QC 硬规则

本项目 QC 必须 fail-closed。

- 任一关键 gate FAIL / unknown / missing evidence => 总体 FAIL 或 INCOMPLETE，绝不能 PASS。
- 不得因为文件名、旧记录、脚本“理论上应该正确”就宣称 PASS。
- visible fix 必须有真实可见像素变化；Before/After 如果该变却没变，立即 FAIL。
- BC3/DXT5 binary integrity 不能代替 visual QC。
- 用户可见 Atlas QC 必须正常 game-space orientation。
- Vita PASS 和 Offline QC PASS 必须分开。
- Vita PASS / LOCKED component 默认绝对冻结。
- GitHub repo / Release 的 hash、commit、asset 状态必须从当前 GitHub 实际读取或实际构建结果得出，不能凭提示词静态数据猜。

## 新会话开始时你应该怎么做

当我在新聊天里贴这段提示词并说“继续 GitHub / 继续汉化工程”时：

先连接并读取 `meochan913/Kancolle-Kai-Chinese-Translation`，至少读取：
`PROJECT_PATCH_LEDGER.json`
`README.md`
`release-status/v0.01.json`
`manifests/v0.01.json`
`manifests/clean-1.02.sha256.json`
以及当前 `main` tree / 最近 commits。

确认当前事实后，再告诉我仓库当前状态并继续任务。
不要要求我重新解释 v0.01 的整个历史，除非 GitHub 数据本身出现冲突或缺失。

当前方向：**v0.01 已正式发布；下一开发阶段是 v0.02，开始汉化正式进入游戏后的母港与游戏 UI。**
