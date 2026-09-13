# 01 - Before Development

Quality planning and risk prevention before coding starts.

The goal: **make the work clear, testable, valuable, and safe to build**. Involve QA early enough to expose ambiguity and risk, align on user value, and define how the change will be validated before code is written.

> **Key idea:** A story is not ready just because it has a description. It is ready when the team understands value, risk, contracts, testability, and expected evidence.

Companion reference: [Quality Review Checklist - Before development](resources/quality-review-checklist.md#before-development).

## Outcomes expected before coding starts

By the end of this phase, the team can explain what to build and why, what could fail, how success and failure will be validated, and what must be observable after release - captured formally in the [Definition of Ready](#11-definition-of-ready).

## 1. Start with user value

Quality starts with the real user journey, not only the technical change.

> **Real world:** This user-first instinct often comes from experience-driven backgrounds - service, support, UX, customer success - where you learn to see the product through the user's eyes. QA that keeps that lens catches problems a spec never mentions.

### Questions to ask

- Who consumes this change - user, customer, support team, or system?
- What problem are we solving, and what task must they complete?
- What could frustrate, block, confuse, or mislead them?
- What would make it feel reliable and easy to use?
- How will we know the experience improved?

### Ask how it fails them, not only how it works

Service industries learned this long before software did: people forgive failure, and they remember how the failure was handled. A refund handled well keeps a customer. A refund handled badly loses ten.

Most acceptance criteria describe success. The recovery path is where trust is actually won or lost, so ask it explicitly:

- When this fails, does the person understand **what happened**, in their words rather than the system's?
- Do they know **what to do next**, or are they left guessing?
- Can they **recover without contacting support**, and if they do contact support, does Support have what they need to help?
- Does the failure lose their work, their data, or their time?
- How long will they be stuck before anyone notices?

> **Principle:** A feature can be technically correct and still fail if the user journey is unclear, slow, confusing, or hard to recover from. Design the recovery, not only the success.

## 2. Run a lightweight Three Amigos review

Hold a short **Product + Development + QA** conversation before implementation.

> **Real world:** a formal Three Amigos is rare, and QA is often pulled in late. If that is your situation, start small - ask one or two of the questions below in refinement, or directly to the developer. Influence beats ceremony.

### Questions to answer

- What is the expected happy path?
- What are the most important negative paths and likely edge cases?
- What should never break?
- How will we validate this across Dev, Staging, and Production?
- What logs, metrics, or traces will help troubleshoot it later?

### Output

A story should leave refinement with clear acceptance criteria, known risks, test data needs, dependencies, and a shared definition of done.

## 3. Write acceptance criteria that are testable

Good acceptance criteria are specific, observable, and tied to behavior.

### Strong acceptance criteria include

- expected behavior;
- user or system action;
- input data;
- output/result;
- error handling;
- permission or role rules;
- integration or contract expectations;
- audit/logging expectations when relevant.

### Option A - BDD format

Use when behavior needs to be business-readable across Product, Dev, and QA.

```gherkin
Given a valid user or system context
When the action is performed
Then the expected result should happen
And the system should provide clear feedback or traceability
```

### Option B - Practical checklist format

Use when the team needs a faster, simpler format.

```text
- User can complete [main action] when [condition]
- System prevents [invalid action] when [condition]
- Error message explains [problem] and [next step]
- Existing behavior [flow/component] is not impacted
- Logs include [ID/context] for troubleshooting
```

### Weak vs strong, in practice

> **Weak:** "Login works."
> **Strong:** "Given an invalid password, login is rejected, the user sees error X, and the attempt is logged with a correlation ID."

The strong version names the condition, the observable result, and the troubleshooting signal, so it is testable without guessing.

### Add quality criteria, not only functional criteria

Cover failure and operability, not just the happy path:

- Invalid data fails explicitly, not silently.
- Errors are clear, actionable, and logged with a correlation ID.
- The API response keeps backward compatibility.
- Critical flows are covered by automated regression when valuable.

## 4. Map risk before defining test depth

Testing depth should follow risk; not every change deserves the same effort.

> **Shortcut:** Score **Impact** and **Likelihood** as Low, Medium, or High, then read the risk level off the matrix. Impact weighs more than likelihood: a rare failure that hurts badly still deserves attention.

### Risk matrix

| | Likelihood: Low | Likelihood: Medium | Likelihood: High |
|---|---|---|---|
| **Impact: High** | Medium | High | **Critical** |
| **Impact: Medium** | Low | Medium | High |
| **Impact: Low** | Low | Low | Medium |

> **Override:** anything touching safety, money, personal data, or regulatory compliance never sits below **High**, whatever the likelihood says.

```mermaid
flowchart TD
    Start["`**Assess the change**
Score Impact and Likelihood
as Low · Medium · High`"] --> Q{"`Read the level from
the risk matrix`"}
    Q -->|Low| L["`**Low**
Focused functional
+ basic regression`"]
    Q -->|Medium| M["`**Medium**
Functional · negative
integration · targeted regression`"]
    Q -->|High| H["`**High**
Risk-based validation
automation review
observability · rollback`"]
    Q -->|Critical| C["`**Critical**
Release-blocking validation
mandatory automation
post-release monitoring`"]
    classDef low  fill:#d4e4d8,stroke:#2f5a43,color:#1f3329;
    classDef med  fill:#ecdcb8,stroke:#6e5418,color:#3d3115;
    classDef high fill:#ecc9b0,stroke:#8a4423,color:#3f2614;
    classDef crit fill:#e6c2c4,stroke:#7a3338,color:#38191b;
    class L low
    class M med
    class H high
    class C crit
```

For full risk assessment, use the [Test Strategy Template](templates/test-strategy-template.md).

### Risk factors to review

- **User impact:** Could this block a critical user journey?
- **Business impact:** Could this affect revenue, compliance, safety, or trust?
- **Technical complexity:** Does it involve integrations, async flows, data transformation, permissions, or configuration?
- **Change size:** Is the change touching shared components or legacy areas?
- **Defect history:** Has this area failed before?
- **Observability:** Can failures be detected and diagnosed quickly?

### Risk levels

| Risk level | Typical testing depth |
|---|---|
| Low | Focused functional validation and basic regression. |
| Medium | Functional, negative, integration, and targeted regression. |
| High | Full risk-based validation, automation review, observability checks, rollback awareness, and release follow-up. |
| Critical | Release-blocking validation: full risk-based coverage, mandatory automated regression, observability and rollback verification, and post-release monitoring. |

> **Example:** A change to the payment-confirmation email. Impact = High (revenue and trust), Likelihood = Medium -> the matrix gives **High** risk: risk-based validation, automation review, and post-release monitoring. The override would have reached the same level on its own, because money is involved.

> **Data point:** **~20% of defects cause ~80% of avoidable rework** - and teams lose 40-50% of their effort to it (Boehm & Basili, 2001). Test the risky few deeply, not everything evenly.

## 5. Create the test strategy and draft test cases early

For medium or high-risk work, start the **test strategy and test cases before development**, not after handoff.

### What to define early

- Scope and out-of-scope areas
- Main risks and mitigation
- Test levels: unit, API, integration, UI, regression, exploratory, UAT
- Manual vs automated validation
- Test data and environment needs
- Frontend/UX and backend/API validation approach
- Evidence expected for sign-off
- Post-deploy checks when needed

Use the [Test Strategy Template](templates/test-strategy-template.md) and [Test Cases Template](templates/test-cases-template.md) to define risks, scope, validation approach, and early scenarios.

### Why this helps

- Developers see expected validations before implementation.
- Missing requirements and automation candidates surface earlier.
- QA execution becomes faster and less reactive.

> **Real world:** requirements move, and test cases written in full detail before the build get rewritten. That teaches a team the effort was wasted, and they stop doing it. Draft **scenarios and risks** early, because those survive a change of design. Leave detailed steps and expected values until the behavior is settled.

### AI-assisted option

AI agents, skills, and instructions can speed up strategy and test-case drafting, with human review. See [AI Tools](ai-tools/README.md).

Useful prompts:

```text
Review this story for ambiguity, risk, missing acceptance criteria, and testability gaps.
```

```text
Create a lightweight test strategy and risk-based test case outline for this feature.
```

Human QA still owns final judgment, expected results, risk priority, and product context.

## 6. Validate testability before implementation

A feature is easier to test when testability is designed in.

### Testability questions

- Can this be tested independently?
- Can we prepare reliable test data?
- Can we mock or simulate external dependencies?
- Can we validate the result through API, database, logs, UI, files, or events?
- Can failures be reproduced, and can the team identify which step failed?
- Do we need feature flags, test hooks, or better logs?

If the answer is unclear, the story needs more design discussion before development starts.

## 7. Treat contracts as quality assets

For APIs, files, events, schemas, data mappings, or integrations, the contract is part of the product.

### A good contract defines

- version;
- required and optional fields;
- data types and formats;
- default and allowed values;
- backward compatibility expectations;
- sample valid and invalid payloads;
- error responses;
- ownership and change process.

QA should review contracts with the same seriousness as UI behavior.

## 8. Separate frontend/UX and backend/API strategies

Frontend and backend testing protect different risks. A strong strategy covers both without overusing one layer.

### Frontend / UX focus

Validate the user journey, usability, accessibility, clarity, visual feedback, error recovery, permissions, and state changes.

Useful validation: exploratory testing, UI and accessibility checks, usability review, critical UI automation, and a pass over copy, labels, empty states, errors, loading states, and recovery paths.

Use usability heuristics to support structured review. Reference: [Nielsen Norman Group - 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

### Backend / API focus

Validate business rules, contracts, data integrity, security, performance, integrations, error handling, and system behavior beyond the UI.

Useful validation: API, contract, and integration tests, data validation, negative testing, authorization checks, logs and correlation IDs, plus duplicate requests, timeouts, retries, and idempotency when relevant.

For the full catalogue of testing types and a context-to-validation map, see the [Testing Types Reference](resources/testing-types.md#practical-selection-guide). For accessibility, locale, security, performance, and privacy - the qualities that fail silently on both sides - see the [Quality Attributes Guide](resources/quality-attributes-guide.md).

## 9. Choose tools, languages, and frameworks intentionally

Tooling should match the product, risk, team skills, architecture, and maintenance cost.

### Questions before choosing tools

- Is the product mainly UI, API, data, mobile, backend, integration, or hybrid?
- Which layer gives the fastest reliable feedback?
- What does the team already know and maintain well?
- Will this tool work in CI/CD and local development?
- Does it support the required reporting, debugging, retries, and test data strategy?
- Is it stable for the application architecture?

> **Principle:** The best tool is not the trendiest one. It is the one the team can use reliably to protect critical behavior over time.

## 10. Prepare test data and environments early

Late test data is a common reason for blocked QA.

### Plan ahead

- Required users, roles, permissions, and accounts
- Valid and invalid input data, plus boundary values
- Existing records needed for regression
- External system availability
- Files, payloads, or events needed for integrations
- Data cleanup strategy

### Good practice

Keep a small, reusable set of **golden test data** for critical flows.

> **Never a production copy.** Generate synthetic data first, and mask irreversibly only when realism is genuinely required. A production dump sitting in a lower environment is a breach waiting for a date. See [Quality Attributes Guide - Privacy and test data](resources/quality-attributes-guide.md#5-privacy-and-test-data).

> **Team-level practices:** assessing QA maturity when joining a team, and building a QA Guild, run over weeks and months rather than per story. Both moved to the [QA Operating Model](resources/qa-operating-model.md), alongside role ownership and how QA works across time zones and vendor teams.

## 11. Definition of Ready

A story is ready when the goal and value are clear, the acceptance criteria are testable, risks and dependencies are identified, test data and environment needs are understood, and QA, Dev, and Product share the same understanding of what is being built.

Contracts, non-functional expectations ([Quality Attributes Guide](resources/quality-attributes-guide.md)) and observability needs join that bar when the change is risky enough to warrant them.

The full checklist, the high-risk add-ons, and where the team confirms each one live in the [Definition of Ready & Definition of Done Template](templates/definition-of-ready-done-template.md). Agree 3-5 items there and apply them consistently, rather than adopting the whole list.

## Before development checklist

The work items of this phase. The readiness gate itself lives in the [Definition of Ready](#11-definition-of-ready) and is not repeated here.

- [ ] User journey and expected experience are understood.
- [ ] BDD or practical checklist format was chosen for acceptance criteria.
- [ ] Happy path and negative paths are known.
- [ ] Risk level is classified and testing depth follows it.
- [ ] Test strategy and test case outline started when relevant.
- [ ] Tool/framework choices are aligned with product risk and team context.
- [ ] Definition of Ready is met.

## Key message

> QA does not need to wait for code to create value.  
> The earlier QA exposes ambiguity, user risk, and testability gaps, the cheaper and safer the delivery becomes.

---

**Playbook:** **01 - Before Development** · [02 - During Development →](02-during-development.md) · [03 - After Development](03-after-development.md)  
[↑ Back to README](README.md)
