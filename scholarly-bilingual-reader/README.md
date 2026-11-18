# 学术论文双栏精读 / Scholarly Bilingual Reader

安装时保留目录名 scholarly-bilingual-reader。使用支持 Agent Skills 的客户端调用 $scholarly-bilingual-reader，提供有权使用的论文 PDF 或全文，或者 DOI、PMID、PMCID、题名用于定位来源。仅有摘要时不会声称完成全文精读。

左栏：英文原文及对应中文翻译；右栏：段落功能、逻辑位置、论证分析。英文高亮：黄—核心论点，红—关键概念，蓝—证据，绿—局限，紫—方法。输出自包含 HTML，含章节导航和搜索。

## Quick start

Python 3; PDF inventory additionally requires Poppler's pdftotext. The metadata utility requires internet access.

```bash
python scripts/pubmed_lookup.py "paper title"
python scripts/reader.py inventory --pdf paper.pdf --out inventory.json
python scripts/reader.py validate --input examples/demo.json --strict
python scripts/reader.py render --input examples/demo.json --output demo.html --strict
```

Run commands from this skill directory. Open demo.html in a browser. The demo contains fictional text, not a real publication. For actual documents, the agent prepares article.json according to references/STRUCTURE.md; verify source fidelity and translations before rendering. The scripts do not translate text or call a model. PDF inventory is not a guarantee of reading order. Respect copyright and safety; never automatically publish reading outputs. The PubMed utility fetches metadata, not full text.
