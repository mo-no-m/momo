# Evidence-Based Academic Review Skill

A reusable workflow for evidence-grounded narrative reviews and academic manuscript revision.

## Workflow

Define the research question and tentative thesis; verify literature; plan section-level arguments; draft and audit each section; evaluate external feedback; synthesize conclusions; write the introduction and abstract; revise the complete manuscript and check references.

## Setup

Download or clone this repository, and copy the `evidence-based-academic-review/` directory into the skills directory of a compatible client, for example `.agents/skills/` in a Codex project. Availability and access to research databases depend on the client.

Example: "Use $evidence-based-academic-review to help me plan an academic narrative review. Verify evidence before drafting and work one section at a time."

The Python 3 checker can be run with:

```bash
python evidence-based-academic-review/scripts/check_manuscript.py manuscript.md
```

It checks numeric citation order, matching bibliography entries, and character counts, not scientific validity. Always verify primary sources, report inaccessible evidence, and respect academic integrity, copyright, ethics, and safety requirements.

[中文说明](README.md)
