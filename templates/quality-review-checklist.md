# Quality Review Checklist

Use this checklist during refinement, development, PR review, and release conversations.

---

## Before development

- [ ] What user or business problem are we solving?
- [ ] Who is impacted and what journey must work?
- [ ] Are acceptance criteria clear and testable?
- [ ] Did we choose BDD or practical checklist criteria?
- [ ] What is the happy path?
- [ ] What are the most important negative paths?
- [ ] What edge cases could matter?
- [ ] What systems, APIs, files, events, permissions, or configurations are impacted?
- [ ] What frontend/UX and backend/API risks exist?
- [ ] What could break existing behavior?
- [ ] What test data is required?
- [ ] What needs to be observable after release?
- [ ] Do we need a test strategy or draft test cases before development?
- [ ] Are tool/framework decisions clear for testing or automation?
- [ ] Is the story ready for development?

---

## During development

- [ ] Has QA reviewed scenarios before handoff?
- [ ] Did QA and Dev review unit tests, integration tests, and static analysis results when relevant?
- [ ] Are SonarQube or similar static analysis findings reviewed?
- [ ] Has QA reviewed the PR from a risk and testability perspective when relevant?
- [ ] Are unit/API/integration/UI tests added at the right level?
- [ ] Are errors handled clearly?
- [ ] Are logs useful for troubleshooting?
- [ ] Is the implementation testable?
- [ ] Are critical paths protected?
- [ ] Are environment differences between Dev, QA/Test, Staging, and Production understood?
- [ ] Are known risks communicated?
- [ ] Is evidence attached?
- [ ] Are user guide or how-to-test notes updated when needed?

---

## Bug classification

- [ ] Does the behavior violate a requirement, acceptance criteria, contract, user need, or quality standard?
- [ ] Is it a regression?
- [ ] Is it caused by invalid test data or environment setup?
- [ ] Is it expected behavior but poorly documented?
- [ ] Is it actually a feature request or product decision?
- [ ] Is impact clear enough to define severity and priority?

---

## Before release

- [ ] Did critical tests pass?
- [ ] Was risk-based regression completed?
- [ ] Are high-severity defects closed or accepted?
- [ ] Is rollback or mitigation understood?
- [ ] Are monitoring/logs available?
- [ ] Was production smoke validation planned?
- [ ] Is the release recommendation clear?
- [ ] Is a QA report or release summary needed for leadership visibility?
