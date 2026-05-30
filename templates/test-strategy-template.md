# Test Strategy Template

Use this template to define how the team will test a feature, epic, release, or project.

Keep it lightweight. The goal is clarity, not documentation volume.

---

## Overview

**Project / Feature:**  
**Owner:**  
**Date:**  
**Related links:**  

**Goal:**  

---

## Scope

### In scope

- 

### Out of scope

- 

---

## Risk assessment

| Area / Flow | Risk Level | Why it matters | Testing depth | Mitigation |
|---|---|---|---|---|
|  | Low / Medium / High / Critical |  |  |  |

Risk guidance:

| Risk Level | Suggested depth |
|---|---|
| Low | Lightweight validation or smoke check. |
| Medium | Positive, negative, and affected regression scenarios. |
| High | Deeper testing, contract/API checks, exploratory testing, automation review. |
| Critical | Strong evidence, automation for critical paths, release visibility, monitoring, rollback awareness. |

Reference: Core Principle #3 — Risk drives testing depth.

---

## Test approach

| Test area | Approach | Owner | Notes |
|---|---|---|---|
| Unit testing |  |  |  |
| API testing |  |  |  |
| Contract testing |  |  |  |
| Integration testing |  |  |  |
| UI / UX testing |  |  |  |
| Exploratory testing |  |  |  |
| Regression testing |  |  |  |
| Security / permissions |  |  |  |
| Accessibility |  |  |  |
| Performance / reliability |  |  |  |

Useful resource: [Testing Guide](../resources/testing-guide.md)

---

## Automation strategy

Automate where it improves feedback.

| Candidate | Why automate? | Level | Priority | Notes |
|---|---|---|---|---|
|  |  | Unit / API / Contract / E2E | Low / Medium / High |  |

Do not automate only to increase test count. Prioritize critical paths, contracts, integrations, and stable regression checks.

---

## Data and environments

| Need | Details |
|---|---|
| Test data |  |
| Accounts / roles |  |
| Environment |  |
| External systems |  |
| Feature flags |  |
| Mocks / stubs |  |
| Known limitations |  |

---

## Observability

- Logs needed:
- IDs or traceability needed:
- Metrics or alerts needed:
- Sensitive data restrictions:
- Production signals to review after release:

---

## Entry and exit criteria

### Entry criteria

- [ ] Requirements are clear enough.
- [ ] Risk level is defined.
- [ ] Test data and environments are available or limitations are known.
- [ ] Contracts are documented when relevant.

### Exit criteria

- [ ] High-risk scenarios are validated.
- [ ] Critical checks pass.
- [ ] Known defects are documented.
- [ ] Automation is updated when valuable.
- [ ] Release risks are communicated.
- [ ] Evidence is available.

---

## Evidence and reporting

| Evidence | Location |
|---|---|
| Test results |  |
| Screenshots / videos |  |
| Logs / traces |  |
| Automation reports |  |
| Known issues |  |

---

## Open questions

-
