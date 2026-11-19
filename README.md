# momo · 科研 Skills 集合

面向科研人员和研究生的通用 AI 辅助科研工作流。当前提供循证式学术综述写作 Skill。

| Skill | 用途 |
| --- | --- |
| [循证式学术综述写作](evidence-based-academic-review/SKILL.md) | v1.6 · 研究方向探索、高质量文献推荐、证据核查、分节写作、全文统稿及可编辑科研配图 |

## 安装
点击 Code → Download ZIP，解压后将所需的独立 Skill 文件夹复制到兼容客户端的技能目录，例如 Codex 项目中的 `.agents/skills/`。具体可用性及网络权限取决于客户端。

## 使用示例
- 使用 $evidence-based-academic-review，先确定综述主线、核查证据，再分节撰写。

## 综述写作 v1.6
仅提供研究方向时，默认先推荐15–20篇代表性文献并提出候选论证主线，待确认后设计正式框架，框架经用户确认后再写第一节。已有题目或文献时，先核查证据并补充缺口。详见[文献检索与推荐规范](evidence-based-academic-review/references/literature-discovery.md)。

**v1.4 强制审核节点：** 完整框架 → 用户审核（有修改则重新确认）→ 当前一节循证写作与证据核查 → 用户确认本节（有修改则重新确认）→ 下一节。全部主体章节确认后再总结、后写引言与摘要，确认后统稿。默认不自动跨越确认节点。

**v1.5 新增逐段原文对照核查文件：** Agent 完成综述后，默认额外交付独立可下载的 HTML 核查文件（也可按要求输出 DOCX 等），将最终正文每段与引用、实际查阅的必要原文证据短引或证据释义、中文释义、来源定位、匹配程度和未核实项对应；核查文件中的参考文献附已核实可点击入口。详见[证据审校规范](evidence-based-academic-review/references/evidence-audit.md)。

**v1.6 正式稿与核查文件分离：** 正式综述仅包含完整论文和规范参考文献（含正常文内引用及必要学术图表），不追加可点击的文献链接、审校记录或其他辅助材料。所有文献核查链接与证据对照集中在独立核查文件。著录规范要求的 DOI/URL 可作为普通文本保留。

需要流程图、技术路线示意图或机制图时，启用[科研绘图与可编辑交付规范](evidence-based-academic-review/references/scientific-figures.md)。默认白底扁平矢量、同类元素一致且独立，优先可编辑 SVG/PPTX。

**v1.3 新增：[19组科研配色库](evidence-based-academic-review/references/color-palettes.md)（[色卡预览](evidence-based-academic-review/references/color-palettes.svg)）。** 正式绘图前展示3–5组候选色卡供用户选择，支持自定义或授权AI代选；遵循白底纯色平涂规则。本地软件调用取决于实际访问权限。

## 配套工具
- [综述引用检查](evidence-based-academic-review/scripts/check_manuscript.py)：`python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md`

脚本负责结构和格式检查，不替代原文核对及科学审查。须尊重版权、隐私、科研伦理和安全规则。仅发布通用工作流与虚构示例，不包含私人论文或研究资料。许可证尚未指定。

[English](README_EN.md)
