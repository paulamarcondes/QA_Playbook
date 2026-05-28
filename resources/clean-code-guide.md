# Clean Code Review Guide for QA

A concise resource to help QAs review code and PRs with a quality, risk, and user-impact mindset.

QA does not need to rewrite the code. QA helps the team identify risk earlier and confirm that the change is clear, testable, observable, secure, and aligned with the expected behavior.

---

## QA Focus in PR Review

Review the change to understand:

- What changed
- What could break
- What needs to be tested
- Whether the implementation matches the requirement
- Whether the change is easy to test, maintain, and troubleshoot

---

## What QA Should Look For

### Clear Intent

- Names are meaningful and aligned with the domain
- Logic is easy to understand
- Functions/classes have one clear responsibility

Ask:

- Can I understand the purpose of this change?
- Does the code reflect the requirement clearly?

### Focused Change

- The PR has one main purpose
- No unrelated refactoring or formatting noise
- Regression impact is easy to identify

Ask:

- Is this PR too large?
- Are unrelated changes increasing risk?

### Simple and Testable Logic

- Conditions are not overly complex
- Edge cases are handled explicitly
- Business logic can be tested without relying only on the UI

Ask:

- Can this be validated at unit, API, or integration level?
- Is the logic deterministic and easy to isolate?

### Error Handling

- Invalid, missing, duplicated, or unexpected data is handled safely
- No silent failures or empty catch blocks
- Error messages are useful and actionable

Ask:

- What happens when this fails?
- Would the team understand the failure quickly?

### Observability

- Critical flows have useful logs or signals
- Logs help identify the affected user, record, request, or transaction
- Sensitive data is not exposed

Ask:

- If this breaks after release, how will we know?
- Is there enough information to troubleshoot?

### Security and Data Safety

- Input validation exists
- Authorization is handled on the backend
- No hardcoded secrets
- Sensitive data is not exposed in logs, UI, URLs, or errors

Ask:

- Can a user access something they should not?
- Can invalid input corrupt or expose data?

---

## QA PR Review Checklist

- [ ] Requirement and acceptance criteria are reflected in the change.
- [ ] Critical paths and risks are clear.
- [ ] Unit, API, or integration tests exist where expected.
- [ ] UI validation is not the only protection for critical logic.
- [ ] Error scenarios are handled.
- [ ] Logs/observability are sufficient.
- [ ] No sensitive data is exposed.
- [ ] Regression impact is understood.
- [ ] Documentation or how-to-test notes were updated if needed.

---

## Common Red Flags

- Large PR with mixed concerns
- No tests for changed logic
- Only happy path covered
- Hardcoded values
- Silent failures
- Generic error messages
- Missing authorization checks
- Business rules duplicated in multiple places
- UI-only validation for critical behavior
- Logs missing for important flows
- Logs exposing sensitive data

---

## Useful QA Questions

- What is the riskiest part of this change?
- Which tests protect this logic?
- What happens with invalid or missing data?
- What existing behavior could be affected?
- Can we validate this without relying only on the UI?
- What logs or signals confirm success or failure?

---

## Quality Gate

A PR is healthier when:

- The intent is clear
- The change is focused
- The logic is testable
- Failures are explicit
- Critical paths are protected by tests
- Logs support troubleshooting
- Risk and regression impact are understood

Clean code is not about perfection. It is about reducing risk and making the system easier to understand, test, and evolve.
