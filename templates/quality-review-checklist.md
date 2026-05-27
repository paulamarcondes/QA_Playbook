# Quality Review Checklist

Use this checklist during refinement, development, and release conversations.

---

## Before development

- [ ] What user or business problem are we solving?
- [ ] Are acceptance criteria clear and testable?
- [ ] What is the happy path?
- [ ] What are the additional Use Cases?
- [ ] What are the most important negative paths?

- [ ] What edge cases could matter?
- [ ] What systems, APIs, files, events, permissions, or configurations are impacted?
- [ ] What could break existing behavior?
- [ ] What test data/file is required?
- [ ] How errors will be identified/logged?
- [ ] What needs to be observable after release?
- [ ] What are performance or security expectations?
- [ ] Is the story ready for development?

---

## During development

- [ ] Has QA reviewed scenarios before handoff?
- [ ] Are unit/API/integration/UI tests added at the right level?
- [ ] Are errors handled clearly?
- [ ] Are logs useful for troubleshooting?
- [ ] Is the implementation testable?
- [ ] Are critical paths protected?
- [ ] Are known risks communicated?
- [ ] Is evidence attached?
- [ ] Are the release notes ready?

---

## Before release

- [ ] Did critical tests pass?
- [ ] Was risk-based regression completed?
- [ ] Are high-severity defects closed or accepted?
- [ ] Is rollback or mitigation understood?
- [ ] Are monitoring/logs available?
- [ ] Was production smoke validation planned?
- [ ] Is the release recommendation clear?
