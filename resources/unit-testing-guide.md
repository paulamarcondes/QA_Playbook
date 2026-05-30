# Unit Testing Guide for QA

Unit tests are usually written by developers, but QAs can help define what should be protected.

The goal is not to chase coverage numbers. The goal is to protect important logic with fast, reliable feedback.

---

## Why QA should care about unit tests

Good unit tests help the team:

- catch logic defects early;
- reduce regression risk;
- validate edge cases faster;
- make refactoring safer;
- avoid relying only on slow E2E tests;
- increase confidence before QA validation starts.

---

## What deserves unit tests

Prioritize unit tests for:

- business rules;
- calculations;
- validations;
- status transitions;
- mapping logic;
- permission decisions;
- error handling;
- edge cases;
- conditions that are hard to reproduce manually.

---

## What QA can ask during refinement or PR review

Ask:

- What logic changed?
- What is the riskiest rule in this story?
- What should fail if this logic breaks?
- Are there negative and boundary cases?
- Are assertions meaningful?
- Is the test naming clear?
- Are mocks hiding too much risk?
- Is this better covered by unit, API, contract, or integration tests?

---

## Coverage is not enough

High coverage can still be weak if tests only check that code runs.

Good tests should:

- verify clear expected results;
- fail when behavior is wrong;
- cover meaningful paths;
- be easy to understand;
- avoid unnecessary dependency on external systems;
- support fast feedback in CI/CD.

---

## Unit test examples by risk

| Risk | Unit test focus |
|---|---|
| Permission logic | Allowed and denied roles. |
| Data mapping | Required fields, missing fields, invalid values. |
| Calculation | Normal, boundary, and invalid inputs. |
| Status transition | Valid transition, invalid transition, duplicate action. |
| Error handling | Dependency failure, timeout, invalid response. |

---

## QA checklist for unit testing

- [ ] Important business rules are covered.
- [ ] Edge cases are included.
- [ ] Negative paths are included.
- [ ] Assertions are meaningful.
- [ ] Tests are readable.
- [ ] Tests run fast.
- [ ] Coverage supports risk, not vanity metrics.
- [ ] Gaps are covered by another test level when needed.

---

## Related resources

- [Clean Code Guide](clean-code-guide.md)
- [Testing Guide](testing-guide.md)
- [Test Strategy Template](../templates/test-strategy-template.md)
