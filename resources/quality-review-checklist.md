# Quality Review Checklist

Use this checklist during refinement, development, PR review, bug triage, release conversations, and post-release learning.

> **How to use:** Focus on outcomes, not checkbox theater. The goal is to reveal risk, improve decisions, and make quality visible.

This checklist mirrors the core guides: [01 - Before Development](../01-before-development.md), [02 - During Development](../02-during-development.md), and [03 - After Development](../03-after-development.md).

## Before development

- [ ] Is the user or business problem clear?
- [ ] Is the impacted user, system, or journey known?
- [ ] Are acceptance criteria clear and testable?
- [ ] Did the team choose BDD or practical checklist criteria?
- [ ] Is the happy path understood?
- [ ] Are negative paths and edge cases discussed?
- [ ] Are impacted systems, APIs, files, events, permissions, or configurations identified?
- [ ] Are frontend/UX and backend/API risks visible?
- [ ] Is regression impact understood?
- [ ] Is required test data available or planned?
- [ ] Are observability needs clear for risky flows?
- [ ] Is a test strategy or draft test case outline needed before development?
- [ ] Are tool/framework decisions clear for testing or automation?
- [ ] Is the story ready for development?

## During development

- [ ] Has QA reviewed scenarios before formal handoff?
- [ ] Did QA and Dev review unit tests, integration tests, and static analysis when relevant?
- [ ] Are SonarQube or similar static analysis findings reviewed?
- [ ] Has QA reviewed the PR from a risk and testability perspective when relevant?
- [ ] Are unit/API/integration/UI tests added at the right level?
- [ ] Are errors handled clearly and safely?
- [ ] Is the feature observable in production through logs, traces, metrics, or alerts when relevant?
- [ ] Is the implementation testable without relying only on the UI?
- [ ] Are critical paths protected?
- [ ] Are environment differences between Dev, QA/Test, Staging, and Production understood?
- [ ] Are known risks communicated?
- [ ] Is evidence attached?
- [ ] Are user guide or how-to-test notes updated when needed?

## Bug classification

- [ ] Does the behavior violate a requirement, acceptance criteria, contract, user need, or quality standard?
- [ ] Is it a regression?
- [ ] Is it caused by invalid test data or environment setup?
- [ ] Is it expected behavior but poorly documented?
- [ ] Is it actually a feature request or product decision?
- [ ] Is impact clear enough to define severity and priority?
- [ ] Is the bug report actionable enough for a developer to investigate quickly?

## Before release

- [ ] Did critical tests pass?
- [ ] Was risk-based regression completed?
- [ ] Are high-severity defects closed or explicitly accepted?
- [ ] Is rollback or mitigation understood?
- [ ] Are monitoring/logs available for critical areas?
- [ ] Was production smoke validation planned when needed?
- [ ] Is the release recommendation clear?
- [ ] Is a QA report or release summary needed for leadership visibility?

## After release

- [ ] Were production signals reviewed?
- [ ] Were escaped defects or incidents analyzed without blame?
- [ ] Was the root cause added to the test strategy, checklist, automation, monitoring, or documentation when relevant?
- [ ] Were quality metrics updated when the release created measurable impact?
- [ ] Are follow-up actions owned and visible?
