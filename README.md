# momo · 科研 Skills 集合

面向科研人员和研究生的通用 AI 辅助科研工作流。各技能独立安装，互相配合。

| Skill | 用途 |
| --- | --- |
| [循证式学术综述写作](evidence-based-academic-review/SKILL.md) | v1.2 · 研究方向探索、高质量文献推荐、证据核查、分节写作、全文统稿及可编辑科研配图 |
| [学术论文双栏精读](scholarly-bilingual-reader/SKILL.md) | 授权论文原文、逐段中文翻译、论证分析、五色英文标注及离线 HTML |

## 安装
点击 Code → Download ZIP，解压后将所需的独立 Skill 文件夹复制到兼容客户端的技能目录，例如 Codex 项目中的 `.agents/skills/`。具体可用性及网络权限取决于客户端。

## 使用示例
- 使用 $evidence-based-academic-review，先确定综述主线、核查证据，再分节撰写。
- 使用 $scholarly-bilingual-reader，将我提供的授权论文整理成逐段对应的双栏精读 HTML。

## 综述写作 v1.2
仅提供研究方向时，默认先推荐15–20篇代表性文献并提出候选论证主线，待确认后再写正文。已有题目或文献时，先核查证据并补充缺口。详见[文献检索与推荐规范](evidence-based-academic-review/references/literature-discovery.md)。

新增[科研配图与可编辑交付规范](evidence-based-academic-review/references/scientific-illustration.md)：绘图前明确配色，白底纯2D矢量风格，统一组件且保留独立可编辑对象，优先交付 SVG / 原生形状 PPTX 与预览；本地软件调用取决于实际权限与能力。

需要流程图、技术路线示意图或机制图时，可启用[科研绘图与可编辑交付规范](evidence-based-academic-review/references/scientific-figures.md)。默认白底扁平矢量、同类元素一致，优先独立可编辑 SVG/PPTX；根据用户偏好确认配色与格式。本地软件调用取决于实际访问权限。

## 配套工具
- [综述引用检查](evidence-based-academic-review/scripts/check_manuscript.py)：`python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md`
- [双栏精读工具与示例](scholarly-bilingual-reader/README.md)

脚本负责结构和格式检查或渲染，不替代模型翻译、原文核对及科学审查。须尊重版权、隐私、科研伦理和安全规则。仅发布通用工作流与虚构示例，不包含私人论文或研究资料。许可证尚未指定。

[English](README_EN.md)
