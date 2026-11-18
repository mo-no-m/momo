# 循证式学术综述写作 Skill
**Evidence-Based Academic Review · v1.0**

面向科研人员、研究生及学术写作者的通用 Agent Skill。以科学问题为主线，先核查证据，再逐节写作、审校和统稿。

## 工作流

确定科学问题 → 检索与核查文献 → 设计章节及分观点 → 逐节写作 → 逐句证据核查 → 评估审校反馈 → 总结与展望 → 后写引言、摘要、关键词 → 全文统稿与引用检查。

## 文件

- [SKILL.md](evidence-based-academic-review/SKILL.md)：核心工作流程。
- [文献核查规范](evidence-based-academic-review/references/evidence-audit.md)：证据账本、核查深度与审校模板。
- [写作和交付规范](evidence-based-academic-review/references/style-and-delivery.md)：自然过渡、论证结构及定稿清单。
- [引用检查脚本](evidence-based-academic-review/scripts/check_manuscript.py)：检查数字引用、参考文献编号及字符数。

## 使用

通过 GitHub 的 Code → Download ZIP 下载仓库并解压。将其中的 `evidence-based-academic-review/` 文件夹放入支持 Agent Skills 的客户端技能目录（例如 Codex 项目的 `.agents/skills/`，或用户级技能目录）。客户端是否支持技能安装以及网络、数据库访问权限，请以其当前配置为准。也可以直接提供 SKILL.md 和配套文件作为写作指令。

示例指令：

> 使用 $evidence-based-academic-review，协助我完成一篇学术综述。先确定科学问题和论证主线，核查文献，再分节撰写和审校；暂时不要直接生成全文。

运行机械检查（Python 3，无第三方依赖）：

```bash
python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md
```

脚本只检查数字型引文和文本计数，不验证文献真实性、科学结论或 Word 字数。文献核查需具备实际来源访问权限。科研写作必须遵循学术诚信、版权、伦理与安全规范。

## English

See [English README](README_EN.md). This skill supports evidence-grounded narrative reviews, claim-by-claim citation audits, and coherent manuscript revision. It does not replace primary-source verification or domain expertise.

本仓库仅发布通用写作工作流，不包含私人研究资料或课程论文。许可证尚未指定。
