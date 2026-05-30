# Technical Quality Reference

Use this reference when QA collaborates with developers during implementation, PR review, unit test review, and technical risk discussions.

This is not a developer checklist. It is a QA guide for asking better questions and finding quality risks earlier.

---

## 1. What QA should look for in PRs

Review changes for quality signals such as:

- changed business rules;
- missing edge cases;
- unclear error handling;
- risky data transformation;
- permission or access gaps;
- weak or missing tests;
- logging and traceability gaps;
- fragile logic or hardcoded values;
- sensitive data exposure;
- accessibility or usability risks.

Useful workflow: [02 - During Development](../02-during-development.md)

---

## 2. Clean code signals for QA

QA does not need to judge code style deeply, but should notice when code makes quality harder.

Good signs:

- logic is readable and not overly complex;
- names explain business intent;
- responsibilities are separated;
- duplicated logic is avoided;
- validation and error handling are clear;
- configuration is not hardcoded;
- sensitive data is protected;
- logs help troubleshooting without exposing secrets.

Warning signs:

- business rules are hidden in unclear conditions;
- one change affects many unrelated areas;
- tests are hard to understand or maintain;
- errors are swallowed or too generic;
- logs do not include useful IDs or states;
- code depends on unstable data, timing, or environment behavior.

---

## 3. Unit testing expectations

Unit tests should protect important logic, not only increase coverage numbers.

Discuss with developers:

- Which business rules changed?
- Which edge cases can break the logic?
- Which negative scenarios matter?
- Are assertions meaningful?
- Would the test fail if the behavior was wrong?
- Are tests isolated from unnecessary external dependencies?
- Are test names clear enough to explain the behavior?

Useful unit test targets:

- calculations;
- validations;
- mapping logic;
- status transitions;
- permission rules;
- error handling;
- boundary values;
- data transformation rules.

Avoid relying only on high coverage percentage. Coverage is useful only when the tests assert meaningful behavior.

---

## 4. Contract and integration quality

For APIs, files, events, or integrations, check whether the implementation respects the agreed contract.

Review:

- required and optional fields;
- request and response examples;
- valid and invalid payloads;
- error responses;
- status codes or status transitions;
- data mapping rules;
- backward compatibility;
- provider and consumer expectations;
- authentication and authorization.

Contract changes should be visible in the story and considered in the test strategy.

---

## 5. Observability and troubleshooting

A feature is safer when failures are visible and actionable.

Check:

- important failures are logged;
- logs include useful IDs, status, and context;
- sensitive data is not logged;
- support or engineering can trace what happened;
- metrics or alerts are considered for critical flows;
- error messages help investigation without exposing internal details.

Good question:

```text
If this fails in production, how will we know and where will we look first?
```

---

## 6. Security, permissions, and data safety

Review security as part of normal quality work.

Ask:

- Are roles and permissions respected?
- Is least privilege followed?
- Are unauthorized scenarios considered?
- Is sensitive data masked, encrypted, or protected when needed?
- Are audit or traceability needs clear?
- Are secrets, tokens, or credentials kept out of code and logs?

---

## 7. AI-generated code or test review

When AI helps generate code, tests, or scenarios, QA should validate the output before trusting it.

Check:

- Did AI invent requirements, fields, APIs, or keywords?
- Are expected results aligned with the real product?
- Are edge cases, permissions, accessibility, and negative paths missing?
- Is the logic biased, generic, or unrelated to the user context?
- Is sensitive data protected?
- Is the automation maintainable and valuable?

Useful guide: [AI Tools](../ai-tools/README.md)

---

## 8. Practical PR questions for QA

Use these questions when reviewing high-risk changes:

- What behavior changed?
- What can break because of this change?
- What tests protect the most important logic?
- What contract, payload, or mapping changed?
- What happens when input is invalid or missing?
- What permissions apply?
- What will we see in logs if this fails?
- What should be automated because it will matter again?

---

## Related documents

- [02 - During Development](../02-during-development.md)
- [Testing Guide](testing-guide.md)
- [Definition of Ready / Done Template](../templates/definition-of-ready-done-template.md)
- [Bug Report Template](../templates/bug-report-template.md)
