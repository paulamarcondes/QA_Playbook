# Testing Guide

Use this guide to choose the right testing approach.

This is the knowledge base: it explains how to think about testing options. The [Test Strategy Template](../templates/test-strategy-template.md) is the project plan: it defines what a specific project will use.

---

## Simple decision flow

Before choosing tests, ask:

1. What changed?
2. What can break?
3. Who or what is affected?
4. How risky is the change?
5. What is the fastest useful feedback?
6. What evidence do we need to trust the release?
7. What should be automated because it will matter again?

---

## Testing by risk and layer

| Change type | Useful testing approach |
|---|---|
| Business rule | Unit tests, API checks, targeted exploratory testing |
| API or contract | Contract tests, API tests, negative scenarios, backward compatibility checks |
| Integration | Integration tests, payload validation, error handling, monitoring review |
| Data mapping or transformation | Input/output validation, edge cases, schema checks, sample files or payloads |
| UI or user flow | Exploratory testing, accessibility checks, usability review, regression checks |
| Permissions or roles | Authorization checks, negative access scenarios, audit/log review |
| Critical production flow | Automated regression, monitoring, rollback awareness, post-deploy validation |
| Low-risk text or cosmetic change | Lightweight review, smoke check, accessibility when relevant |

---

## Unit testing

Use unit tests when logic can be validated close to the code.

Good targets:

- calculations;
- validations;
- mapping rules;
- status transitions;
- permission logic;
- error handling;
- boundary conditions.

Unit testing expectations are covered in the [Technical Quality Reference](technical-quality-reference.md).

---

## API and contract testing

Use API and contract checks when systems exchange data.

Validate:

- required and optional fields;
- valid and invalid payloads;
- response codes;
- error messages;
- authentication and authorization;
- backward compatibility;
- provider and consumer expectations.

---

## Integration testing

Use integration testing when the risk is between systems, services, files, queues, databases, or external providers.

Focus on:

- data movement;
- transformations;
- retries and failures;
- missing or malformed data;
- timing and dependencies;
- observability and troubleshooting.

---

## Exploratory testing

Use exploratory testing when human judgment adds value.

Good targets:

- unclear behavior;
- new user journeys;
- complex flows;
- usability risks;
- edge cases;
- areas with recent bugs;
- behavior that is hard to capture in scripts.

Use the [Test Cases Template](../templates/test-cases-template.md) for concise scenario notes and exploratory charters.

---

## Regression testing

Regression testing should focus on what can realistically break.

Prioritize:

- critical paths;
- areas touched by the change;
- recent bug areas;
- integrations;
- permissions;
- data transformations;
- stable automated checks.

Avoid running large regression suites without risk focus.

---

## Automation decision

Automate when the scenario is:

- valuable;
- repeatable;
- stable;
- connected to regression risk;
- useful for fast feedback;
- maintainable.

Avoid automation when the scenario is unclear, unstable, one-time, or cheaper to explore manually.

---

## Quick rule

```text
Use the smallest test that gives reliable confidence for the risk.
```
