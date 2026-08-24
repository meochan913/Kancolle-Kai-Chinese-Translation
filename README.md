# Kancolle-Kai-Chinese-Translation

《舰队Collection 改》（艦これ改 / KanColle Kai）PlayStation Vita 简体中文汉化工程。

> 当前里程碑：**v0.01 — Pre-Game Translation Milestone**
>
> 截至 2026-08-23，正式进入游戏前的玩家可见内容已经完成汉化，并经过阶段性 PSV Vita 实机验证。

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
screenshots/              实机截图（后续导入）
```

## 安装

v0.01 的公开一键 patch 包将在所有 FINAL 文件与原始 1.02 Mother 文件重新导入并生成 clean-base → v0.01 差分后发布。

详见 [`docs/INSTALL.md`](docs/INSTALL.md)；干净 1.02 输入哈希见 [`docs/SOURCE_BASELINE.md`](docs/SOURCE_BASELINE.md)。

## QC

本项目采用 fail-closed QC：任一关键 gate 失败、关键输入缺失、或视觉目标未实际改善时，不允许标记为 PASS。

详见 [`docs/QC_POLICY.md`](docs/QC_POLICY.md)。

## 当前阶段

目前仓库骨架与工程 ledger 已建立。下一步是把项目当前 FINAL 文件和 pristine 1.02 Mother 文件配对，生成**从干净 1.02 直接到 v0.01 的单步差分**。

## Credits

- Chinese localization / project author: **Meo**
- Engineering assistance: OpenAI ChatGPT

## Disclaimer

本项目为非官方粉丝汉化工程，与 C2机关、KADOKAWA、DMM GAMES、SEGA、Sony Interactive Entertainment 或其他权利方无关联。

所有原游戏商标、角色、美术、音频与其他原始内容均属于其各自权利人。
