# Definition of Ready / Done Template

Use this template to define shared quality standards for stories, tasks, and team agreements.

DoR and DoD are not QA gates. They are team standards that help everyone understand when work is clear enough to start and safe enough to move forward.

Reference: [Core Principles](../README.md#core-principles)

---

## Definition of Ready

A story is Ready when the team has enough clarity to start development with controlled risk.

### Story information

**Story / Task:**  
**Owner:**  
**Feature / Area:**  
**Risk Level:** Low / Medium / High / Critical  

Risk should be assessed using the framework in the [Test Strategy Template](test-strategy-template.md).

### Ready checklist

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Risk level is defined.
- [ ] Dependencies are known.
- [ ] Data and environment needs are understood.
- [ ] Interface or contract expectations are documented when relevant.
- [ ] Security, permissions, and accessibility needs are considered when relevant.
- [ ] Testing approach is roughly agreed.
- [ ] Story aligns with [01 - Before Development](../01-before-development.md) standards.
- [ ] Story details are captured in the [Story / Requirements Template](story-requirements-template.md) when needed.

---

## Definition of Done

A story is Done when the team has enough evidence to trust the change based on its risk.

### Done checklist

- [ ] Acceptance criteria are met.
- [ ] Risk-based scenarios were validated.
- [ ] Positive, negative, and edge cases were covered according to risk.
- [ ] Contracts, payloads, mappings, and backward compatibility were validated when relevant.
- [ ] Security and permissions were validated when relevant.
- [ ] Accessibility expectations were validated when relevant.
- [ ] Logs, errors, and troubleshooting signals were reviewed when relevant.
- [ ] Code and tests meet the [Technical Quality Reference](../resources/technical-quality-reference.md) standards.
- [ ] Critical paths and contracts are protected by automated checks when valuable.
- [ ] AI-generated output was reviewed by a human when AI was used.
- [ ] Documentation, how-to-test notes, or release notes were updated when needed.
- [ ] Evidence is attached or linked.
- [ ] Known risks are communicated.
- [ ] Product, QA, and Development agree the change is ready for the next step.

Useful resources:

- [Technical Quality Reference](../resources/technical-quality-reference.md)
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
