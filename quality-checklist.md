# Quality Checklist

Use this checklist before publishing an example or release.

## Required

- [ ] The output starts directly with `件名：` or the email body. No meta preface.
- [ ] The subject is specific enough to identify the purpose.
- [ ] The addressee matches the recipient relationship.
- [ ] The sender identifies themself when needed.
- [ ] The requested action is explicit.
- [ ] Deadlines and attachments are included only if user-provided.
- [ ] The draft does not invent prior meetings, affiliations, or document status.
- [ ] The tone is not over-humble for a low-burden request.
- [ ] The draft contains no self-proving language.
- [ ] The draft contains no real personal data.
- [ ] `python scripts/validate_examples.py` passes.

## Red Flags

Avoid:

```text
以下は自然で丁寧なメール文です。
尊敬する〇〇先生
〇〇教授様
先生の素晴らしいご研究に深く感銘を受けました。
失礼のないよう、丁寧にご連絡いたします。
もし差し支えなく、ご都合がよろしければ、可能な範囲で...
```

## High-Burden Requests

For recommendation letters, urgent exceptions, or special support, confirm:

- [ ] destination or purpose,
- [ ] deadline,
- [ ] format or submission method,
- [ ] materials attached,
- [ ] why this recipient is being asked,
- [ ] enough lead time is acknowledged.
