# Quality Review Checklist

Use this checklist to confirm quality outcomes across the delivery flow.

It is intentionally short. The goal is to reveal risk and missing evidence, not to create process for its own sake.

---

## 1. Before development

Expected outcome: the team can start development with clear value, known risk, and testable requirements.

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Risk level is documented.
- [ ] API, file, data, or interface contract is clear when relevant.
- [ ] Security and permissions expectations are clear when relevant.
- [ ] Accessibility expectations are clear for user-facing changes.
- [ ] Test data and environment needs are known.
- [ ] Testing approach is roughly agreed.

Useful guide: [01 - Before Development](../01-before-development.md)

---

## 2. During development

Expected outcome: quality risks are reviewed while the change is still easy to adjust.

- [ ] PR review considers risk, testability, permissions, and edge cases.
- [ ] Important business logic is protected by meaningful tests.
- [ ] Contracts, payloads, mappings, or schemas are reviewed when relevant.
- [ ] Failures will be visible through useful logs, IDs, metrics, or traces.
- [ ] Sensitive data is not exposed in logs, errors, test data, or AI prompts.
- [ ] Automation protects valuable feedback loops when it makes sense.
- [ ] AI-generated output is reviewed by a human before use.

Useful resource: [Technical Quality Reference](technical-quality-reference.md)

---

## 3. Before release

Expected outcome: release confidence is based on evidence and known risk.

- [ ] Critical and high-risk scenarios were validated.
- [ ] Open defects and known risks are understood.
- [ ] Regression impact was reviewed.
- [ ] Deployment validation is planned when needed.
- [ ] Rollback or recovery path is understood for risky releases.
- [ ] Monitoring or post-deploy checks are clear for critical flows.
- [ ] Evidence is attached or linked.

Useful template: [Deployment Validation Template](../templates/deployment-validation-template.md)

---

## 4. After release

Expected outcome: the team learns from production behavior and improves the next cycle.

- [ ] Production signals were reviewed for critical flows.
- [ ] Critical or Blocker bugs updated the metrics dashboard when relevant.
- [ ] Missed risks were added to the test strategy or checklist.
- [ ] Repeated defects triggered an improvement action.
- [ ] A short quality retro happened when a release or incident justified it.

Useful guide: [03 - After Development](../03-after-development.md)

---

## 5. Final question

```text
Do we have enough evidence to make a good quality decision?
```

If the answer is no, clarify the risk, gather better evidence, or agree on the known risk before moving forward.
