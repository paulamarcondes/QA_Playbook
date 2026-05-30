# Testing Guide

Use this guide to choose the right testing approach for each change.

The goal is not to run every possible test. The goal is to get the right confidence at the right speed.

---

## Start with these questions

Before choosing tests, ask:

- What changed?
- What can break?
- Who is affected?
- What is the risk level?
- What is the fastest useful feedback?
- What needs human exploration?
- What should be automated for future feedback?

---

## Risk-based testing depth

| Risk level | Recommended depth |
|---|---|
| Low | Lightweight review, smoke check, or focused validation. |
| Medium | Positive and negative scenarios, affected area regression, basic evidence. |
| High | Deeper scenario coverage, contract/API checks, regression, exploratory testing, automation review. |
| Critical | Full risk review, strong evidence, automation for critical paths, monitoring, rollback awareness, stakeholder alignment. |

Risk should be defined in the [Test Strategy Template](../templates/test-strategy-template.md).

---

## Choose testing by change type

| Change type | Useful testing approach |
|---|---|
| Business rule | Unit tests, API checks, scenario testing, edge cases. |
| API change | Contract checks, API tests, negative responses, backward compatibility. |
| Integration change | Contract tests, integration tests, data mapping checks, failure scenarios. |
| Data transformation | Input/output validation, boundary cases, invalid data, regression. |
| UI change | Exploratory testing, accessibility checks, UX review, regression. |
| Permission change | Role-based scenarios, negative access tests, audit/log review. |
| Security-sensitive change | Permission checks, data exposure review, error handling, logs without sensitive data. |
| Critical flow | Automated regression, exploratory testing, monitoring, rollback awareness. |
| Low-risk content change | Review, smoke check, visual confirmation. |

---

## Choose testing by level

| Level | Best used for | Watch out for |
|---|---|---|
| Unit | Business rules, calculations, small logic decisions. | Passing unit tests do not prove the full flow works. |
| API | Service behavior, status codes, payloads, validations. | API tests may miss UI or end-to-end user issues. |
| Contract | Provider/consumer expectations, required fields, compatibility. | Contracts must be agreed before they can protect the team. |
| Integration | Data flow between systems, mappings, external dependencies. | Environments and test data can make results noisy. |
| E2E | Critical user journeys and release confidence. | Expensive and fragile if overused. |
| Exploratory | Unknown risks, usability, edge cases, human judgment. | Needs a clear mission and evidence. |
| Regression | Existing behavior that must not break. | Should be risk-based, not everything every time. |
| Smoke | Basic health after build or deployment. | Not enough for deep confidence. |

---

## What to automate

Good automation candidates:

- critical paths;
- stable regression checks;
- API contracts;
- repetitive checks;
- high-risk flows that run often;
- scenarios that give fast feedback in CI/CD.

Poor automation candidates:

- unclear requirements;
- unstable UI flows;
- one-time checks;
- low-risk scenarios rarely repeated;
- tests that require heavy maintenance with low value.

Automation should answer:

```text
Will this test give useful, reliable feedback faster than manual testing?
```

---

## What to keep exploratory

Use exploratory testing when the team needs human judgment.

Good areas:

- new flows;
- unclear behavior;
- UX issues;
- accessibility concerns;
- edge cases;
- production-like scenarios;
- defects that need investigation;
- risk areas not fully covered by automation.

Use the [Test Cases Template](../templates/test-cases-template.md) to document charters and findings.

---

## Practical rule

Start small, test what matters, and increase depth based on risk.

Do not create test volume. Create confidence.
