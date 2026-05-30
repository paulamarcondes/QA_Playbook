# Definition of Ready & Definition of Done Template

Use this template to define clear, practical quality standards for stories, tasks, features, integrations, and releases.

The goal is not to create bureaucracy. The goal is to reduce rework, prevent unclear handoffs, and make quality a shared team responsibility.

> **Real world:** most teams that succeed with DoR/DoD use a 3–5 item subset, not the full list. Treat everything below as a menu to pick from, not a mandate — start small and add only what repeatedly bites you.

## 1. Purpose

This document defines the minimum quality expectations for:

- **Definition of Ready (DoR):** when work is clear enough to start.
- **Definition of Done (DoD):** when work is complete enough to be considered delivered.

A story should not start with major unanswered questions, and it should not be marked as done just because code was written.

## 2. How to use this template

Teams should adapt this checklist based on product risk, system complexity, regulatory needs, customer impact, and delivery model.

Recommended approach:

1. Keep a **global minimum DoR/DoD** for all stories.
2. Add **extra criteria for high-risk work**, such as payments, security, permissions, integrations, data transformation, migrations, production incidents, or customer-critical flows.
3. Review this template during retrospectives when defects, rework, or unclear handoffs happen.
4. Avoid checkbox theater. Each item should help the team make a better delivery decision.

---

# Definition of Ready (DoR)

A story is **Ready** when the team has enough shared understanding to start development with confidence.

## 3. Minimum DoR checklist

| Area | Ready criteria | Status / Notes |
|---|---|---|
| Business value | The problem, goal, or user/business outcome is clear. |  |
| User / stakeholder | The affected user, client, system, or stakeholder is identified. |  |
| Scope | In-scope and out-of-scope items are clear. |  |
| Acceptance criteria | Acceptance criteria are testable and written in clear language. |  |
| Happy path | The expected successful flow is understood. |  |
| Negative paths | Expected error, validation, and failure scenarios are identified. |  |
| Edge cases | Relevant boundaries, exceptions, permissions, configurations, or data variations are discussed. |  |
| Dependencies | External systems, APIs, files, environments, teams, or approvals are identified. |  |
| Test data | Required test data, accounts, files, payloads, or configurations are available or planned. |  |
| Testability | The team knows how the change can be validated. |  |
| Observability | Logs, monitoring, correlation IDs, or traceability needs are defined when relevant. |  |
| Non-functional needs | Performance, security, accessibility, privacy, compatibility, or reliability expectations are defined when relevant. |  |
| Risk level | The story has a risk classification: Low / Medium / High / Critical. |  |
| Estimation | The team has enough clarity to estimate the work. |  |
| Open questions | Critical open questions are resolved or explicitly documented as assumptions. |  |

## 4. High-risk story add-ons

Use these additional DoR checks when the change has high customer, business, technical, or production risk.

- [ ] Data contracts, schemas, mappings, payload examples, or interface documents are available.
- [ ] Backward compatibility expectations are clear.
- [ ] Migration, configuration, or feature flag needs are understood.
- [ ] Failure behavior is defined: retry, rollback, alert, block, skip, or fail fast.
- [ ] Expected logs and troubleshooting signals are defined.
- [ ] Impacted regression areas are identified.
- [ ] Support, operations, or customer-facing impacts are considered.
- [ ] Security, privacy, audit, or compliance risks are reviewed when applicable.

## 5. Signs a story is not ready

A story should usually not enter the sprint when:

- acceptance criteria are vague or not testable;
- expected behavior depends on assumptions nobody confirmed;
- test data or environments are not available and no plan exists;
- external dependencies are unknown or unmanaged;
- the team cannot explain how the feature will be validated;
- the risk is high but no extra validation strategy was discussed;
- the story is too large to test, review, or deliver safely.

---

# Definition of Done (DoD)

A story is **Done** when it meets the agreed quality bar and can be released or handed off with confidence.

Done means the team has validated that the change works, does not create unacceptable risk, and is understandable after delivery.

## 6. Minimum DoD checklist

| Area | Done criteria | Status / Evidence |
|---|---|---|
| Acceptance criteria | All agreed acceptance criteria were implemented and validated. |  |
| Code quality | Code was reviewed, is maintainable, and follows team standards. |  |
| Unit tests | Unit tests were added or updated where applicable. |  |
| API / integration tests | API, contract, or integration checks were added or updated when applicable. |  |
| Manual validation | Relevant happy path, negative path, and edge cases were validated. |  |
| Regression impact | Impacted regression areas were checked based on risk. |  |
| Automation | Critical or repetitive scenarios were automated, or automation was documented as future work. |  |
| Test evidence | Evidence was attached: screenshots, logs, payloads, test results, or notes. |  |
| Defects | No open critical/high defects remain unless explicitly accepted. |  |
| Observability | Logs, monitoring, alerts, or traceability are available when relevant. |  |
| Error handling | Expected failures are handled clearly and safely. |  |
| Documentation | User, technical, support, or QA documentation was updated when needed. |  |
| Deployment readiness | Configuration, feature flags, migration steps, rollback needs, or release notes are clear. |  |
| Product approval | PO, stakeholder, or QA acceptance was completed when required. |  |

## 7. High-risk story add-ons

Use these additional DoD checks for high-risk work.

- [ ] Data transformation, mapping, or contract outputs were validated against expected results.
- [ ] Backward compatibility was tested or consciously accepted as not applicable.
- [ ] Failure scenarios were tested: invalid data, timeout, unavailable dependency, duplicate message/file, retry, or partial failure.
- [ ] Logs include enough context to troubleshoot without manual guessing.
- [ ] Monitoring or alerting is available for critical failures.
- [ ] Rollback, mitigation, or feature disablement path is known.
- [ ] Production smoke validation is planned.
- [ ] Support or operations teams received relevant notes when needed.
- [ ] Risk acceptance is documented for anything intentionally deferred.

## 8. Suggested DoD by test level

| Test level | Expected use |
|---|---|
| Unit tests | Business rules, validators, calculations, transformations, and isolated logic. |
| API / contract tests | Field validation, status codes, required/optional fields, error responses, and backward compatibility. |
| Integration tests | Communication between systems, files, queues, workflows, services, databases, or third-party dependencies. |
| UI tests | Critical user journeys, permissions, high-value flows, and usability-sensitive paths. |
| Exploratory testing | New behavior, complex workflows, edge cases, user experience, and areas with high uncertainty. |
| Regression testing | Existing critical paths that could be impacted by the change. |

## 9. Practical team agreement

Use this section to define how the team will apply DoR and DoD in daily work.

| Agreement | Team decision |
|---|---|
| Where is DoR checked? | Refinement / planning / backlog review |
| Who confirms DoR? | Product + Dev + QA / Three Amigos |
| Where is DoD checked? | Pull request / QA validation / Jira transition / release review |
| Who confirms DoD? | Dev + QA + Product when required |
| What requires high-risk add-ons? |  |
| What evidence is required? |  |
| Where is evidence stored? | Jira / TestRail / GitHub / Confluence / other |
| How are exceptions approved? |  |
| How often is this template reviewed? | Monthly / quarterly / after incidents |

## 10. Recommended Jira fields

For stronger traceability, teams may add or standardize these fields:

- Business value / user outcome
- Acceptance criteria
- Risk level: Low / Medium / High / Critical
- Impacted systems / modules
- Test data needed
- Test strategy notes
- Automation candidate: Yes / No
- Regression scope
- Observability notes
- Release notes needed: Yes / No
- QA evidence link
- Known risks / accepted risks

## 11. Final quality questions

Before starting work:

> Do we understand the value, the risk, and how to validate success?

Before closing work:

> Would we be comfortable releasing this, supporting it, and explaining how it behaves in production?

## 12. Guiding principle

Definition of Ready protects the team from unclear work. Definition of Done protects the user, the product, and the business from incomplete delivery.
