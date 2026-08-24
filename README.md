# Kancolle-Kai-Chinese-Translation

《舰队Collection 改》（艦これ改 / KanColle Kai）PlayStation Vita 简体中文汉化工程。

> 当前正式版本：**v0.01 — Pre-Game Translation Milestone**
>
> 截至 2026-08-23，正式进入游戏前的玩家可见内容已经完成汉化，并经过 PSV Vita 实机验证。

## 下载

**GitHub Release:**
https://github.com/meochan913/Kancolle-Kai-Chinese-Translation/releases/tag/v0.01

Release asset:

`Kancolle_Kai_CHS_v0.01.zip`

SHA-256:

`2d7df4bcdfbe011e5b0f2ce0090226ab4db1fcfdb5375f1b5c80a8f173c34269`

Release 页面同时提供 `Kancolle_Kai_CHS_v0.01_SHA256SUMS.txt`。

## 当前进度

| 模块 | 状态 |
| --- | --- |
| 标题画面 / 初次就任 / 归任 | ✅ 已完成 |
| 标题版本信息 | ✅ 已完成 |
| 简体中文字库 / GB2312 基础覆盖 | ✅ 已集成 |
| 初始模式选择 | ✅ Vita PASS |
| 11 艘初始舰介绍 | ✅ 已完成 |
| 初始舰注音清理 | ✅ 已完成 |
| 提督名输入相关 UI | ✅ 已完成 |
| 确认按钮 | ✅ 已完成 |
| 教程三页正文 | ✅ FINAL / Vita PASS |
| 教程妖精气泡 | ✅ FINAL / Vita PASS |
| ReceiveShip「续」按钮 | ✅ FINAL / Vita PASS |
| 正式进入母港后的游戏内容 | 🚧 下一阶段 |

## 项目原则

本仓库**不分发原始游戏、完整修改版游戏文件、完整 `.assets`、原始 DLL、固件或其他专有游戏内容**。

公开内容只包含：

- 差分 patch / patch metadata
- 校验哈希
- 可复现工具
- 工程记录与 QC
- 汉化文本及本项目原创工作

使用者必须自行提供与本项目支持版本完全一致、合法获得的游戏文件。

## 支持版本

- Platform: PlayStation Vita
- Title: 艦これ改 / KanColle Kai
- Title ID: `PCSG00684`
- Game version targeted by this project: `1.02`

## 仓库结构

```text
docs/                    工程文档、安装说明、QC 规则
patches/                 差分 patch（不包含完整游戏文件）
tools/                   patch 制作、应用与 hash 工具
PROJECT_PATCH_LEDGER.json
                         项目级 single source of truth
release-notes/           各版本 Release Notes
release-status/          GitHub Release 可审计发布回执
screenshots/             实机截图（后续导入）
```

## 安装

v0.01 使用 **clean 1.02 → FINAL Vita-validated** 单步 patch。当前版本包含 8 个 `.kckpatch` 差分文件及 fail-closed 安装工具。

详见 [`docs/INSTALL.md`](docs/INSTALL.md)；干净 1.02 输入哈希见 [`docs/SOURCE_BASELINE.md`](docs/SOURCE_BASELINE.md)。

## QC

本项目采用 fail-closed QC：任一关键 gate 失败、关键输入缺失、或视觉目标未实际改善时，不允许标记为 PASS。

v0.01 的 8 个 patch 已从 clean 1.02 独立 replay，生成结果与 Vita 验证后的累计 `rePatch` 文件逐字节一致。仓库端 payload 也已完成独立完整性核验。

## 当前阶段

**v0.01 已正式发布。**

下一阶段将进入正式母港后的游戏 UI 汉化，版本线进入 `v0.02` 开发阶段。

## Credits

- Chinese localization / project author: **Meo**
- Engineering assistance: OpenAI ChatGPT

## Disclaimer

本项目为非官方粉丝汉化工程，与 C2机关、KADOKAWA、DMM GAMES、SEGA、Sony Interactive Entertainment 或其他权利方无关联。

所有原游戏商标、角色、美术、音频与其他原始内容均属于其各自权利人。
