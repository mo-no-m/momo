# momo · 科研 Skills 集合

面向科研人员和研究生的通用 AI 辅助科研工作流。当前提供循证式学术综述写作 Skill。

| Skill | 用途 |
| --- | --- |
| [循证式学术综述写作](evidence-based-academic-review/SKILL.md) | v1.4 · 研究方向探索、高质量文献推荐、证据核查、分节写作、全文统稿及可编辑科研配图 |

## 安装
点击 Code → Download ZIP，解压后将所需的独立 Skill 文件夹复制到兼容客户端的技能目录，例如 Codex 项目中的 `.agents/skills/`。具体可用性及网络权限取决于客户端。

## 使用示例
- 使用 $evidence-based-academic-review，先确定综述主线、核查证据，再分节撰写。

## 综述写作 v1.4
仅提供研究方向时，默认先推荐15–20篇代表性文献并提出候选论证主线，待确认后设计正式框架，框架经用户确认后再写第一节。已有题目或文献时，先核查证据并补充缺口。详见[文献检索与推荐规范](evidence-based-academic-review/references/literature-discovery.md)。

**v1.4 强制审核节点：** 完整框架 → 用户审核（有修改则重新确认）→ 当前一节循证写作与证据核查 → 用户确认本节（有修改则重新确认）→ 下一节。全部主体章节确认后再总结、后写引言与摘要，确认后统稿。默认不自动跨越确认节点。

需要流程图、技术路线示意图或机制图时，启用[科研绘图与可编辑交付规范](evidence-based-academic-review/references/scientific-figures.md)。默认白底扁平矢量、同类元素一致且独立，优先可编辑 SVG/PPTX。

**v1.3 新增：[19组科研配色库](evidence-based-academic-review/references/color-palettes.md)（[色卡预览](evidence-based-academic-review/references/color-palettes.svg)）。** 正式绘图前展示3–5组候选色卡供用户选择，支持自定义或授权AI代选；遵循白底纯色平涂规则。本地软件调用取决于实际访问权限。

## 配套工具
- [综述引用检查](evidence-based-academic-review/scripts/check_manuscript.py)：`python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md`

脚本负责结构和格式检查，不替代原文核对及科学审查。须尊重版权、隐私、科研伦理和安全规则。仅发布通用工作流与虚构示例，不包含私人论文或研究资料。许可证尚未指定。

[English](README_EN.md)
