# 01 - Before Development

Build quality before coding starts.

This phase is about alignment. The goal is not to document everything twice, but to make sure the team has enough clarity to start with controlled risk.

---

## Main goal

Before development starts, the team should understand:

- what problem is being solved;
- who is affected;
- what can go wrong;
- what needs to be tested;
- which contracts, data, roles, and environments are involved;
- what “Ready” means for this work.

Use the [Story / Requirements Template](templates/story-requirements-template.md) to capture the details.

---

## Team habit: interface-first for high-risk work

For high-risk stories, do not start coding until the key interface or data expectations are clear.

Use a short Three Amigos conversation with Product, Development, and QA to confirm:

- user value and expected behavior;
- API, file, event, data, or UI contract;
- permissions and access rules;
- important positive, negative, and edge cases;
- observability needs;
- testing approach.

Checklist item:

```text
Is the API, file, data, or interface contract documented and agreed in the story?
```

---

## 1. Confirm user value

A requirement should clearly explain the user or business outcome.

Ask:

- Who needs this change?
- What problem does it solve?
- What user journey or business process is affected?
- What would make this change unsuccessful, even if it technically works?

Useful template: [Story / Requirements Template](templates/story-requirements-template.md)

---

## 2. Identify risk early

Risk drives testing depth.

Every meaningful story should have a simple risk level:

```text
Low / Medium / High / Critical
```

Use the detailed risk framework in the [Test Strategy Template](templates/test-strategy-template.md). This guide only defines when the risk conversation should happen.

Risk should be discussed during refinement when the change affects:

- critical user flows;
- integrations or external systems;
- data transformation or migration;
- security or permissions;
- payments or financial data;
- accessibility or user access;
- production stability;
- legal, compliance, or audit needs.

---

## 3. Make requirements testable

A story is testable when QA can clearly identify:

- expected result;
- acceptance criteria;
- input and output data;
- positive and negative scenarios;
- dependencies;
- evidence needed for validation.

Avoid vague acceptance criteria such as:

```text
The system should work correctly.
```

Prefer:

```text
Given an active user with permission X,
when they submit Y,
then the system should return Z and save the status as Approved.
```

---

## 4. Define contracts before implementation

For APIs, integrations, files, events, or data flows, define the contract before coding.

Confirm enough detail for the team to avoid late integration surprises:

- provider and consumer;
- request and response expectations;
- required and optional fields;
- valid and invalid examples;
- error handling;
- backward compatibility;
- authentication and authorization;
- logging and traceability;
- contract test needs.

Detailed contract fields should live in the [Story / Requirements Template](templates/story-requirements-template.md).

---

## 5. Include security, permissions, and accessibility early

Security and accessibility are requirement-level quality concerns, not late testing extras.

Ask during refinement:

- Who should access this feature or data?
- Who should not access it?
- Are roles and permissions clear?
- Is sensitive data protected?
- Does the change follow least privilege?
- Can users understand, navigate, and recover from errors?
- Are accessibility expectations clear for UI, forms, messages, or content changes?

Capture the details in the story when relevant.

---

## 6. Plan data and environments

Before development starts, clarify:

- test data needed;
- data setup and cleanup;
- environment dependencies;
- external systems;
- feature flags;
- test accounts and permissions;
- mocked or real integrations;
- known environment limitations.

Bad environments create false confidence or false failures.

---

## 7. Choose the first testing approach

Do not wait until the end to decide how to test.

Ask:

- What is the fastest useful feedback?
- What should be covered by unit tests?
- What needs API, contract, integration, or E2E validation?
- What needs exploratory testing?
- What should become an automation candidate?

Useful resource: [Testing Guide](resources/testing-guide.md)

---

## 8. Definition of Ready

A story is ready when the team has enough clarity to start development with controlled risk.

Minimum checks:

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Risk level is defined.
- [ ] Dependencies are known.
- [ ] Data and environment needs are understood.
- [ ] Interface or contract expectations are documented when relevant.
- [ ] Security, permissions, and accessibility needs are considered when relevant.
- [ ] Testing approach is roughly agreed.
- [ ] Story aligns with this guide and the [Story / Requirements Template](templates/story-requirements-template.md).

Full template: [Definition of Ready / Done Template](templates/definition-of-ready-done-template.md)

---

## Output of this phase

At the end of this phase, the team should have:

- clearer requirements;
- known risks;
- documented contracts when relevant;
- better testability;
- fewer late surprises;
- a shared understanding of what quality means for the story.
