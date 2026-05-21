# Academic Email JP Skill

A practical ChatGPT Skill for drafting concise, natural Japanese academic emails to professors, supervisors, collaborators, university offices, and research labs.

This skill is designed for students and researchers who need Japanese academic email drafts that are clear, appropriately polite, and not overly template-like.

## Use Cases

- Asking a supervisor to check a revised manuscript
- Requesting an appointment or research meeting
- Contacting a professor for a lab visit
- Asking for a recommendation letter
- Writing a late-reply apology
- Sending a thank-you note after a meeting
- Contacting a university office about an administrative procedure

## What This Skill Optimizes For

- Clear subject lines
- Appropriate addressee and greeting
- Relationship-aware tone
- Concrete requested action
- Minimal but sufficient background
- No exaggerated humility
- No self-proving language such as "this is a natural and polite email"
- No invented attachments, deadlines, prior meetings, or affiliations

## Example

Input:

```text
我想给导师发邮件，说我根据他的意见改了论文，想请他有空时确认一下。
```

Output:

```text
件名：論文修正稿のご確認のお願い

〇〇先生

お世話になっております。
〇〇です。

先日いただいたご指摘を踏まえ、論文の修正稿を作成いたしました。
お時間のある際にご確認いただけますと幸いです。

どうぞよろしくお願いいたします。
```

## Files

```text
academic-email-jp-skill/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── docs/
│   └── references.md
├── quality-checklist.md
└── examples/
    ├── manuscript-check/
    ├── appointment-request/
    ├── lab-visit-first-contact/
    └── recommendation-request/
```

## Privacy

All examples in this repository are synthetic. Do not publish real professor emails, student IDs, unpublished paper content, recommendation details, or private lab/company information.

## Status

Public v0.1. The skill is usable as a focused drafting aid and will be improved with more synthetic examples and scenario checks.

## References

The writing rules are based on Japanese university email guidance, research-lab contact pages, recommendation-letter request guidance, business email conventions, and Japanese learner pragmatics research. See [docs/references.md](docs/references.md).
