# momo · 科研 Skills 集合

面向科研人员和研究生的通用 AI 辅助科研工作流。各技能独立安装，互相配合。

| Skill | 用途 |
| --- | --- |
| [循证式学术综述写作](evidence-based-academic-review/SKILL.md) | 文献证据先行、科学问题驱动、分节写作、逐句审校及全文统稿 |
| [学术论文双栏精读](scholarly-bilingual-reader/SKILL.md) | 授权论文原文、逐段中文翻译、论证分析、五色英文标注及离线 HTML |

## 安装
点击 Code → Download ZIP，解压后将所需的独立 Skill 文件夹复制到兼容客户端的技能目录，例如 Codex 项目中的 `.agents/skills/`。具体可用性及网络权限取决于客户端。

## 使用示例
- 使用 $evidence-based-academic-review，先确定综述主线、核查证据，再分节撰写。
- 使用 $scholarly-bilingual-reader，将我提供的授权论文整理成逐段对应的双栏精读 HTML。

## 配套工具
- [综述引用检查](evidence-based-academic-review/scripts/check_manuscript.py)：`python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md`
- [双栏精读工具与示例](scholarly-bilingual-reader/README.md)

脚本负责结构和格式检查或渲染，不替代模型翻译、原文核对及科学审查。须尊重版权、隐私、科研伦理和安全规则。仅发布通用工作流与虚构示例，不包含私人论文或研究资料。许可证尚未指定。

[English](README_EN.md)
