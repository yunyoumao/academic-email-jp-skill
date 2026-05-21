---
name: academic-email-jp
description: Write, rewrite, or diagnose concise natural Japanese academic emails for professors, supervisors, collaborators, university offices, research-lab visits, manuscript checks, meeting requests, recommendation requests, apologies, and thank-you notes. Use when the user asks for Japanese professor email wording, 日语/日本語メール, 先生へのメール, 研究室訪問メール, 添削依頼, 面談依頼, 推薦状依頼, お礼メール, or wants to avoid AI-like or overly template-like Japanese email.
---

# Academic Email JP

## Goal

Produce Japanese academic email drafts that are concise, relationship-aware, and sendable. Optimize for recipient clarity: who is writing, what is requested, by when, and what the recipient needs to do.

Do not aim for maximum politeness. Politeness should reduce friction, not make a simple request look ceremonial.

## Default Output

- Default to `draft_only`: output the subject and Japanese email body without preface or explanation.
- If the user asks for diagnostics, provide a short Chinese or Japanese note after the draft.
- Do not write meta-introductions such as `以下は自然で丁寧なメール文です` or `AIらしさを抑えた文面です`.
- Do not claim the draft is natural, polite, native-like, or appropriate. The draft must demonstrate that through wording.

## Quick Workflow

1. Identify the relationship: current supervisor, unknown professor, collaborator, university office, lab member, HR/company, or unknown.
2. Identify the task: request, report, confirmation, apology, thank-you, follow-up, or reply.
3. Select subject, addressee, opening, self-introduction, request body, closing, and signature.
4. Include only user-provided facts. Do not invent attachments, deadlines, meetings, affiliations, or prior discussions.
5. If missing information is low risk, use `〇〇` placeholders. If missing information changes the request, ask one concise question.
6. For high-burden requests, verify that the draft gives the recipient enough information to act without asking back for basics.
7. Run the final anti-AI and anti-self-proving check before answering.

## Information To Preserve Or Ask For

Use or ask for:

- recipient name and relationship,
- sender name, affiliation, grade/status, or lab,
- purpose,
- first contact or ongoing thread,
- deadline or date options,
- attachment status,
- expected action from recipient,
- student ID, course name, report title, or procedure name when the email is administrative or submission-related,
- destination, deadline, required format, and materials when requesting a recommendation letter or similar high-burden support,
- desired output mode: Japanese only, Chinese explanation plus Japanese draft, rewrite only, subject only, or tone diagnosis.

If the user gives Chinese notes, convert intent into Japanese. Do not translate literally.

## Subject Lines

Make the subject concrete. Include the object and action.

Good patterns:

```text
論文修正稿のご確認のお願い（〇〇）
面談日程のご相談（〇〇）
研究室訪問のお願い（〇〇大学 〇〇）
推薦状作成のお願い（〇〇）
〇月〇日ゼミ欠席のご連絡（〇〇）
```

Avoid vague subjects:

```text
お願い
質問があります
ご相談
こんにちは
至急
重要
```

For report submission or administrative emails, exact routing information is more important than elegant wording. Preserve user-provided conventions such as course name, student ID, deadline, or report number.

For replies, usually keep the existing subject with `Re:`. Change the subject only when the topic has materially changed or the original subject is misleading.

## Tone By Relationship

| Relationship | Tone |
|---|---|
| Current supervisor | concise, familiar-formal, minimal self-introduction |
| Unknown professor | formal, clear self-introduction, specific reason for contact |
| University office | administrative, direct, no academic flattery |
| Collaborator | professional, task-oriented |
| HR/company | business email format, not professor format |

## Burden-Aware Request Strategy

Match the amount of explanation to the burden placed on the recipient.

| Burden | Examples | Strategy |
|---|---|---|
| Low | simple confirmation, schedule reply | short request, minimal apology |
| Medium | manuscript check, appointment request | reason, concrete action, optional date/deadline |
| High | recommendation letter, special exception, urgent request | context, why this recipient, required materials, deadline, submission method, and an escape option |

For high-burden requests, do not draft a vague polite email. Ask for missing essentials or use placeholders:

```text
提出先：
締切：
提出方法：
必要書類：
添付資料：
```

## Phrase Rules

Default addressee for professors:

```text
〇〇先生
```

Avoid:

```text
尊敬する〇〇先生
〇〇教授様
〇〇先生様
〇〇教授:
〇〇先生:
```

Opening:

| Situation | Use |
|---|---|
| First contact | `初めてご連絡いたします。` |
| Existing relationship | `お世話になっております。` |
| Reply | `ご返信ありがとうございます。` |
| After meeting | `先日はお時間をいただき、ありがとうございました。` |
| Sudden first contact | `突然のご連絡失礼いたします。` |

Avoid `こんにちは` for first-contact formal academic mail.

## Administrative And Submission Emails

For university offices, report submissions, certificates, or procedures:

- keep the required identifiers,
- make the subject searchable,
- write the purpose before details,
- avoid academic flattery,
- do not use `先生` unless the recipient is actually a teacher.

Good:

```text
〇〇課 ご担当者様

お世話になっております。
〇〇研究科〇〇専攻の〇〇です。

〇〇の手続きについて確認したく、ご連絡いたしました。
```

## Anti-AI And Anti-Self-Proving Check

Before final output, remove:

- prefaces explaining that the email is natural, polite, or non-AI-like,
- self-proving language such as `失礼のないよう、丁寧にご連絡いたします`,
- empty praise such as `先生の素晴らしいご研究に深く感銘を受けました`,
- repeated `お忙しいところ` or multiple apologies for a simple request,
- over-humble chains such as `もし差し支えなく、ご都合がよろしければ、可能な範囲で`,
- fake details: nonexistent attachment, deadline, prior conversation, publication status, or affiliation.

## Scenario Patterns

### Manuscript check

```text
先日いただいたご指摘を踏まえ、論文の修正稿を作成いたしました。
お時間のある際にご確認いただけますと幸いです。
```

Only mention attachments if the user says an attachment exists.

### Appointment request

```text
来週、研究計画について一度ご相談させていただけないでしょうか。
以下の時間帯でしたら対応可能です。
```

### Lab visit or first contact

```text
先生の研究室で扱われている〇〇に関心があり、
研究室訪問についてご相談させていただきたく、ご連絡いたしました。
```

Show fit with the lab's actual research. Do not write generic praise.

### Recommendation letter

Before drafting, make sure the email contains or asks for destination, purpose, deadline, required format, submission method, and attached materials.

```text
〇〇への出願にあたり、推薦状の提出が必要となりました。
先生にご推薦をお願いできないかと思い、ご連絡いたしました。

提出締切は〇月〇日で、提出方法は〇〇です。
必要書類と参考資料を添付しております。
```

### Late reply

```text
ご返信が遅くなり、申し訳ございません。
```

Apologize once, then answer the matter.

### Thank-you after meeting

```text
本日はお時間をいただき、ありがとうございました。
ご説明いただいた〇〇について、今後の研究計画を考えるうえで大変参考になりました。
```

## Final Output Format

For draft requests:

```text
件名：...

〇〇先生

...
```

For diagnosis requests, prioritize:

1. unnatural addressee,
2. vague subject,
3. missing self-introduction,
4. unclear requested action,
5. over-politeness or self-proving wording,
6. literal Chinese-to-Japanese phrasing,
7. invented or risky details.

