# Definition of Ready / Definition of Done Template

Use this template as a shared quality standard for stories, tasks, and team agreements.

Avoid treating DoR and DoD as QA gates. They are team standards that help everyone reduce risk and deliver better software.

---

## Basic information

**Team / Project:**  
**Feature / Area:**  
**Date:**  
**Owner:**  

---

## Risk level

**Risk Level:** Low / Medium / High / Critical

Testing depth, evidence, review effort, and automation expectations should match the documented risk.

Reference: [Test Strategy Template](test-strategy-template.md)

---

## Definition of Ready

A story is Ready when the team has enough clarity to start development safely.

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Scope and out-of-scope are clear.
- [ ] Risk level is defined.
- [ ] Dependencies are known.
- [ ] Test data and environment needs are understood.
- [ ] API, file, data, or interface contract is documented when relevant.
- [ ] Security and permission expectations are clear when relevant.
- [ ] Accessibility expectations are clear when relevant.
- [ ] Observability or logging needs are considered when relevant.
- [ ] Testing approach is roughly agreed.
- [ ] Story aligns with [01 - Before Development](../01-before-development.md) standards for testability, risk, and contracts.
- [ ] Story follows the [Story / Requirements Template](story-requirements-template.md) when applicable.

---

## Definition of Done

A story is Done when the team has enough evidence that the change is correct, safe, useful, and maintainable.

- [ ] Acceptance criteria are met.
- [ ] Relevant positive, negative, and edge scenarios were validated.
- [ ] Risk level was considered in testing depth.
- [ ] Unit test strategy was reviewed when relevant.
- [ ] Code quality, maintainability, and testability were reviewed when relevant.
- [ ] Contracts, payloads, mappings, and backward compatibility were validated when relevant.
- [ ] Security and permissions were validated when relevant.
- [ ] Accessibility expectations were validated when relevant.
- [ ] Logs, errors, and troubleshooting signals were reviewed when relevant.
- [ ] Critical paths and contracts are protected by automated checks when valuable.
- [ ] AI-generated output was reviewed by a human when AI was used.
- [ ] Documentation, how-to-test notes, or release notes were updated when needed.
- [ ] Evidence is attached or linked.
- [ ] Known risks are communicated.
- [ ] Product, QA, and Development agree the change is ready for the next step.

Useful resources:

- [Clean Code Guide](../resources/clean-code-guide.md)
- [Unit Testing Guide](../resources/unit-testing-guide.md)
- [Testing Guide](../resources/testing-guide.md)

---

## Deployment validation reference

Story-level Done is not the same as deployment readiness.

If the change requires release or environment validation:

- [ ] Deployment validation needs are identified.
- [ ] Smoke checks are clear.
- [ ] Rollback or recovery plan is understood.
- [ ] Monitoring or post-deploy checks are planned.

Use the [Deployment Validation Template](deployment-validation-template.md).

---

## Risk-based flexibility

Not every story needs the same level of process.

| Risk | DoR / DoD expectation |
|---|---|
| Low | Keep it lean. Clear requirement, simple validation, basic evidence. |
| Medium | Validate key scenarios, affected regression, and relevant risks. |
| High | Stronger review, deeper testing, better evidence, automation consideration. |
| Critical | Full alignment, strong evidence, automation where valuable, release and monitoring awareness. |
