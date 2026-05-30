# Clean Code Guide for QA

QAs do not need to review code like developers. But QAs can review code changes with a quality mindset.

The goal is to identify risk, testability issues, missing scenarios, weak error handling, and maintainability concerns before defects reach users.

---

## What QA should look for in code review

### 1. Requirement fit

Ask:

- Does the code match the acceptance criteria?
- Are all expected paths handled?
- Are negative paths considered?
- Is there any behavior not described in the story?

---

### 2. Readability and maintainability

Ask:

- Is the logic easy to understand?
- Are names clear?
- Is the change smaller than it could be?
- Is duplicated logic being introduced?
- Would another developer understand this later?

Clean code reduces future bugs.

---

### 3. Testability

Ask:

- Can this logic be tested easily?
- Is important logic isolated enough for unit tests?
- Are dependencies mocked or controlled where needed?
- Are there clear inputs and outputs?

Poor testability usually means higher regression risk.

---

### 4. Error handling

Ask:

- What happens when input is invalid?
- What happens when a dependency fails?
- Are error messages useful?
- Are failures handled safely?
- Are retry, timeout, or fallback behaviors clear when relevant?

---

### 5. Logs and observability

Ask:

- Are important failures logged?
- Do logs include useful IDs or context?
- Can support or engineering trace what happened?
- Are sensitive values protected?
- Are metrics or alerts needed?

Good logs help the team investigate production issues faster.

---

### 6. Security and data safety

Ask:

- Are permissions checked correctly?
- Is least privilege respected?
- Is sensitive data protected?
- Are secrets or credentials exposed?
- Are logs free from personal or confidential data?

Security should be reviewed early, not only tested at the end.

---

### 7. Accessibility and user impact

For UI changes, ask:

- Are labels and messages clear?
- Are errors understandable?
- Is keyboard navigation relevant?
- Could visual-only feedback create a problem?
- Could this change make the flow harder for users?

---

### 8. AI-generated code or tests

If AI helped generate code or tests, check:

- Does it match the real requirement?
- Are expected results correct?
- Are edge cases missing?
- Is the logic generic or hallucinated?
- Are there biased assumptions?
- Was sensitive data used in the prompt?

AI output must always be reviewed by a human.

---

## PR review checklist for QA

- [ ] Acceptance criteria are reflected in the implementation.
- [ ] Important edge cases are handled.
- [ ] Risky logic has meaningful tests.
- [ ] Errors are handled clearly.
- [ ] Logs support troubleshooting.
- [ ] Security and permissions are respected.
- [ ] Sensitive data is protected.
- [ ] Accessibility and user impact were considered when relevant.
- [ ] Automation was added or updated when it provides useful feedback.
- [ ] Known risks are communicated.

---

## Related resources

- [Unit Testing Guide](unit-testing-guide.md)
- [Testing Guide](testing-guide.md)
- [Definition of Ready / Done Template](../templates/definition-of-ready-done-template.md)
