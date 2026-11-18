---
name: scholarly-bilingual-reader
description: 将用户提供的学术论文 PDF、授权全文、DOI、PMID、PMCID 或标题转换为可离线浏览的中英双栏精读 HTML；逐段对应翻译与论证分析、五色英文高亮、来源定位、章节导航、图表说明与完整性核查。Use for scholarly paper close reading, bilingual annotated HTML, and evidence-grounded argument analysis.
---

# Scholarly Bilingual Reader — 学术论文双栏精读

## 目标
输出真实可打开的单文件 HTML，不以文章摘要、导读、虚构原文或占位模板冒充全文。左栏保留原英文并附对应中文译文，右栏逐段提供中文论证注释。以用户提供的 PDF 或依法可用全文为权威来源。

## 范围与前提
- 接受 PDF、合法全文、DOI、PMID、PMCID、论文标题；确认准确版本、作者、年份及许可。可用联网工具或 scripts/pubmed_lookup.py 检索元数据；仅获取摘要时明确说明，索取合法全文，不补造内容。
- 尊重版权、访问控制、隐私和生物安全。仅在授权及适用安全规则允许的范围内提供原文和译文；对不宜复述的内容提供安全的高层概述并明确缺口，不将阅读任务转为高风险实验操作、工程设计或优化指南。不自动发布论文或附件到公共网站。
- 阅读 references/STRUCTURE.md、references/ANALYSIS_GUIDE.md、references/QUALITY.md。优先使用提供的 PDF；双栏排版、脚注、图像、扫描页须视觉核对，自动提取不可代替原文检查。

## 工作流
1. **全文清点**：核对论文题名、作者、摘要、原有章节顺序、正文、Methods、表图与图注、原有结论（若存在）、致谢、披露及参考文献。用 scripts/reader.py inventory --pdf PAPER.pdf --out inventory.json 辅助检查文字块及页码；不要假定块顺序就是阅读顺序。全文不明时不得宣称完整。
2. **逐段对齐**：按原文顺序建立 P001、P002…稳定 ID；处理跨页、跨栏断段，保留原始词句、数字、限定词、单位、引文及定位。记录实质性修订，不重新编造原始章节。
3. **逐段翻译**：每个可处理阅读单元都有准确、流畅、完整且对应的中文译文；术语统一，保留否定、统计量和不确定性。把翻译与概述明确区分，不以简短摘要代替翻译。
4. **逐段分析**：右栏固定为段落功能、逻辑位置、论证分析；说明该段回答什么、承接什么、证据支持什么、不能推出什么。区分作者判断、直接证据、读者综合观点。
5. **五色标注**：只对英文原文的确切片段用黄（核心论点）、红（关键概念）、蓝（证据）、绿（让步/反驳/局限）、紫（方法）。中文译文不高亮，不整段涂色；使用 Python Unicode 字符位置，不重叠。
6. **论证全景**：另设分析区，概括核心问题、中心论点、完整论证路径、章节作用、方法与证据边界、强弱论点、隐含假设及三个后续问题。不存在的反驳或结论不伪造。
7. **导出和验收**：填充 article.json。先执行 python scripts/reader.py validate --input article.json --strict，再执行 python scripts/reader.py render --input article.json --output reader.html --strict；必要且有权时加 --pdf PAPER.pdf 嵌入 PDF。图片采用本地许可素材和 data URI；不依赖外部 CSS/JS/字体 CDN。检查桌面与移动端排版、导航、搜索、完整性和显示。
8. 交付可下载 HTML，报告原文、译文、注释、图表、参考文献数量、审计范围及未解决事项。机械验证通过不等于科学审核或全文无漏。

## 使用方式
默认由 Agent 阅读、翻译和分析，Python 负责整理、校验、渲染，不负责大模型推理。模型额度、数据库访问和可用工具取决于宿主。不可声称已联网、已全文核查或已永久安装，除非实际证实。
