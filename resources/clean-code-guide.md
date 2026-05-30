# Clean Code Review Guide for QA

A concise resource to help QAs review code and PRs with a quality, risk, and user-impact mindset.

QA does not need to rewrite the code. QA helps the team identify risk earlier and confirm that the change is clear, testable, observable, secure, and aligned with the expected behavior.

## QA focus in PR review

Review the change to understand:

- what changed;
- what could break;
- what needs to be tested;
- whether the implementation matches the requirement;
- whether the change is easy to test, maintain, and troubleshoot.

## What QA should look for

### Clear intent

Look for:

- meaningful names aligned with the domain;
- logic that is easy to understand;
- functions/classes with one clear responsibility.

Ask:

- Can I understand the purpose of this change?
- Does the code reflect the requirement clearly?

### Focused change

Look for:

- one main purpose in the PR;
- no unrelated refactoring or formatting noise;
- regression impact that is easy to identify.

Ask:

- Is this PR too large?
- Are unrelated changes increasing risk?

### Simple and testable logic

Look for:

- conditions that are not overly complex;
- edge cases handled explicitly;
- business logic that can be tested without relying only on the UI.

Ask:

- Can this be validated at unit, API, or integration level?
- Is the logic deterministic and easy to isolate?

### Error handling

Look for:

- invalid, missing, duplicated, or unexpected data handled safely;
- no silent failures or empty catch blocks;
- useful and actionable error messages.

Ask:

- What happens when this fails?
- Would the team understand the failure quickly?

### Observability

Look for:

- useful logs or signals for critical flows;
- logs that help identify the affected user, record, request, or transaction;
- no sensitive data exposed.

Ask:

- If this breaks after release, how will we know?
- Is there enough information to troubleshoot?

### Security and data safety

Look for:

- input validation;
- backend authorization;
- no hardcoded secrets;
- no sensitive data exposed in logs, UI, URLs, or errors.

Ask:

- Can a user access something they should not?
- Can invalid input corrupt or expose data?

## QA PR review checklist

- [ ] Requirement and acceptance criteria are reflected in the change.
- [ ] Critical paths and risks are clear.
- [ ] Unit, API, or integration tests exist where expected.
- [ ] UI validation is not the only protection for critical logic.
- [ ] Error scenarios are handled.
- [ ] Logs/observability are sufficient.
- [ ] No sensitive data is exposed.
- [ ] Regression impact is understood.
- [ ] Documentation or how-to-test notes were updated if needed.

## Common red flags

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

## Useful QA questions

- What is the riskiest part of this change?
- Which tests protect this logic?
- What happens with invalid or missing data?
- What existing behavior could be affected?
- Can we validate this without relying only on the UI?
- What logs or signals confirm success or failure?

## Quality standard

A PR is healthier when:

- the intent is clear;
- the change is focused;
- the logic is testable;
- failures are explicit;
- critical paths are protected by tests;
- logs support troubleshooting;
- risk and regression impact are understood.

Clean code is not about perfection. It is about reducing risk and making the system easier to understand, test, and evolve.
