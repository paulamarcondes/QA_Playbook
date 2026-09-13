# Test Strategy Template

Use this as a lightweight test strategy for a feature, integration, release, or significant change.

This template includes risk assessment, test scope, test levels, manual vs automated strategy, tool/framework decisions, observability, and release confidence in one place.

> **How to use:** **Most stories need the one-pager below and nothing else.** Sections 1 to 14 are for integrations, migrations, release-level work, and regulated changes - the cases where someone will ask, months later, what was covered and why.

## The one-page version

For a normal story. Eight lines, written in the ticket, done in ten minutes.

| Field | Answer |
|---|---|
| What is changing |  |
| Risk level and why | Low / Medium / High / Critical |
| What must not break |  |
| How it will be validated | Levels, and manual vs automated |
| Test data and environment needs |  |
| What we are not testing |  |
| Evidence for sign-off |  |
| Post-deploy check needed? | Yes / No |

If every answer is easy, the story is low risk and you are done. If two or three are hard to answer, that is the signal to open the full version below.

---

## 1. Strategy summary

| Field | Value |
|---|---|
| Feature / Change |  |
| Jira / Work item |  |
| Product / System |  |
| Owner |  |
| Release / Sprint |  |
| Overall risk | Low / Medium / High / Critical |
| Recommendation | Ready / Ready with risk / Not ready |

### Objective

What confidence do we need before release?

## 2. Scope

### In scope

- [Add item]
- [Add item]
- [Add item]

### Out of scope

- [Add item]
- [Add item]
- [Add item]

### Systems / areas impacted

| Area | Impact | Notes |
|---|---|---|
| UI | None / Low / Medium / High |  |
| API | None / Low / Medium / High |  |
| Database | None / Low / Medium / High |  |
| Integration / Contract | None / Low / Medium / High |  |
| Files / Events / Queues | None / Low / Medium / High |  |
| Configuration | None / Low / Medium / High |  |
| Permissions / Security | None / Low / Medium / High |  |
| Reporting / Analytics | None / Low / Medium / High |  |

## 3. Risk assessment

Risk should guide testing depth and evidence expectations. Score each factor below, then derive the overall level from the [risk matrix in 01](../01-before-development.md#4-map-risk-before-defining-test-depth).

| Risk factor | Low | Medium | High | Notes |
|---|---|---|---|---|
| User impact |  |  |  |  |
| Business impact |  |  |  |  |
| Technical complexity |  |  |  |  |
| Integration impact |  |  |  |  |
| Data sensitivity |  |  |  |  |
| Security / permissions |  |  |  |  |
| Defect history |  |  |  |  |
| Observability gaps |  |  |  |  |
| Regression risk |  |  |  |  |

### Overall risk decision

| Field | Decision |
|---|---|
| Risk level | Low / Medium / High / Critical |
| Reason |  |
| Testing depth required | Matches the risk level - see the [risk levels table](../01-before-development.md#risk-levels) |

Individual factors are scored Low/Medium/High. **Critical** is reached through the matrix (high impact and high likelihood) or through the override: safety, money, personal data, or regulatory compliance.

## 4. Quality risks and mitigation

| Risk | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|
|  |  |  |  | Open / Mitigated / Accepted |

## 5. Test approach by area

Use different strategies for frontend/UX and backend/API risks.

| Area | Main risks | Validation approach | Evidence |
|---|---|---|---|
| Frontend / UX | Usability, accessibility, content, visual feedback, navigation, user errors | Exploratory, UI checks, accessibility, usability heuristics, critical UI automation | Screenshots, video, notes |
| Backend / API | Contracts, business rules, data integrity, permissions, performance, integrations | API, contract, integration, negative, data validation | Payloads, logs, reports |
| Data / Integration | Mapping, transformation, compatibility, duplicate handling, processing failures | Input/output validation, file/event checks, logs, reconciliation | Files, events, logs, DB checks |

Reference for UI review: [Nielsen Norman Group - 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

## 6. Test approach by level

| Test level | Required? | Purpose | Owner | Evidence |
|---|---|---|---|---|
| Unit | Yes / No | Business rules, validators, transformations | Dev | PR / CI results |
| Component | Yes / No | Isolated service behavior | Dev / QA | Test report |
| API | Yes / No | Contracts, payloads, status codes, errors | QA / Dev | API evidence |
| Contract | Yes / No | Provider/consumer compatibility | QA / Dev | Contract report |
| Integration | Yes / No | Cross-system flow | QA / Dev | Logs / payloads / files |
| UI | Yes / No | Critical user journey | QA | Screenshots / video |
| Exploratory | Yes / No | Unknown risks, usability, edge cases | QA / Team | Notes / findings |
| Regression | Yes / No | Existing behavior protection | QA / Automation | Test run |
| Post-deploy smoke | Yes / No | Production confidence | QA / DevOps | Monitoring / smoke result |

## 7. Test data and environment

| Need | Source | Owner | Status | Notes |
|---|---|---|---|---|
| Test data |  |  | Ready / Blocked / Pending |  |
| User / Role |  |  | Ready / Blocked / Pending |  |
| Environment |  |  | Ready / Blocked / Pending |  |
| External dependency |  |  | Ready / Blocked / Pending |  |
| Mock / Stub |  |  | Ready / Blocked / Pending |  |

## 8. Tool and framework strategy

| Decision | Selected option | Reason | Risks / Notes |
|---|---|---|---|
| Manual testing tools |  |  |  |
| API testing tool |  |  |  |
| Automation framework | Robot Framework / Playwright / Cypress / Selenium / Other |  |  |
| Programming language | Python / JavaScript / TypeScript / Java / Other |  |  |
| Test management |  |  |  |
| CI/CD integration |  |  |  |
| Reporting |  |  |  |

Choose tools based on product architecture, team skills, maintainability, CI/CD fit, debugging capability, and risk coverage.

## 9. Automation strategy

| Scenario | Automate? | Level | Reason | Location / Notes |
|---|---|---|---|---|
|  | Yes / No / Later | Unit / API / Integration / UI |  |  |

### Automation priority

1. Critical flows
2. High-risk regression
3. API/contracts/integrations
4. Repetitive manual checks
5. Stable behavior with clear expected results

Avoid automating unstable, unclear, or low-value scenarios before the behavior is mature. Full criteria: [02 - Automate strategically](../02-during-development.md#8-automate-strategically).

## 10. Observability and supportability

| Requirement | Status | Evidence / Notes |
|---|---|---|
| Clear error logs |  |  |
| Correlation / transaction ID |  |  |
| Dashboard or log query available |  |  |
| Alerts reviewed when relevant |  |  |
| Known failure modes documented |  |  |
| Support / troubleshooting notes updated |  |  |

## 11. Early test design

Create a draft test case outline before or during development for medium/high-risk changes.

| Area | Draft scenarios | Owner | Status |
|---|---|---|---|
| Critical happy path |  |  | Draft / Ready / N/A |
| Negative paths |  |  | Draft / Ready / N/A |
| Edge cases |  |  | Draft / Ready / N/A |
| Integration/API |  |  | Draft / Ready / N/A |
| UI/UX |  |  | Draft / Ready / N/A |
| Regression |  |  | Draft / Ready / N/A |
| Post-deploy smoke |  |  | Draft / Ready / N/A |

AI-assisted drafting may be used, but final review must be done by QA with product and technical context.

## 12. Entry criteria

- [ ] Requirements are clear and testable.
- [ ] Acceptance criteria are approved.
- [ ] Risks are classified.
- [ ] Test data is available or planned.
- [ ] Environment and dependencies are ready.
- [ ] Observability expectations are clear.

## 13. Exit criteria

- [ ] Critical scenarios passed.
- [ ] High-risk regression completed.
- [ ] Required automated tests passing.
- [ ] High-severity defects fixed or explicitly accepted.
- [ ] Evidence attached.
- [ ] Open risks communicated.
- [ ] Post-deploy validation defined.
- [ ] Release recommendation provided.

## 14. Final recommendation

| Field | Decision |
|---|---|
| Status | Ready / Ready with risk / Not ready |
| Reason |  |
| Known risks |  |
| Approver(s) |  |
