# 01 - Before Development

Quality planning and risk prevention before coding starts.

The goal before development is simple: **make the work clear, testable, valuable, and safe to build**. QA should be involved early enough to prevent ambiguity, expose risk, align the team on user value, and define how the change will be validated before code is written.

> **Key idea:** A story is not ready just because it has a description. It is ready when the team understands value, risk, contracts, testability, and expected evidence.

## Outcomes expected before coding starts

A story or feature should enter development only when the team understands:

- what user or business problem it solves;
- which users, systems, flows, data, and environments are impacted;
- what could fail and how serious the impact would be;
- how success and failure will be validated;
- what test strategy, test data, and evidence will be needed;
- what should be automated, manually validated, or explored;
- what needs to be observable after release.

## 1. Start with user value

Quality starts by understanding the real user journey, not only the technical change.

### Questions to ask

- Who is the user, customer, support team, or system consuming this change?
- What problem are we solving for them?
- What task must they complete successfully?
- What could frustrate, block, confuse, or mislead them?
- What would make this change feel reliable and easy to use?
- How will we know this improved the product experience?

> **Principle:** A feature can be technically correct and still fail in practice if the user journey is unclear, slow, confusing, or hard to recover from.

## 2. Run a lightweight Three Amigos review

Use a short conversation with **Product + Development + QA** before implementation.

### Questions to answer

- What problem are we solving?
- Who is the user or system consuming this change?
- What is the expected happy path?
- What are the most important negative paths?
- What edge cases are likely?
- What should never break?
- How will we validate this in Dev, QA/Test, Staging, and Production?
- What logs, metrics, or traces will help us troubleshoot it later?

### Output

A story should leave refinement with clear acceptance criteria, known risks, test data needs, dependencies, and a shared understanding of done.

## 3. Write acceptance criteria that are testable

Good acceptance criteria are specific, observable, and connected to behavior.

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

Use this when behavior needs to be business-readable and shared across Product, Dev, and QA.

```gherkin
Given a valid user or system context
When the action is performed
Then the expected result should happen
And the system should provide clear feedback or traceability
```

### Option B - Practical checklist format

Use this when the team needs a faster, simpler format.

```text
- User can complete [main action] when [condition]
- System prevents [invalid action] when [condition]
- Error message explains [problem] and [next step]
- Existing behavior [flow/component] is not impacted
- Logs include [ID/context] for troubleshooting
```

### Add quality criteria, not only functional criteria

Examples:

- Error messages must be clear and actionable.
- Invalid data must fail explicitly, not silently.
- The system must log the correlation ID for troubleshooting.
- The API response must keep backward compatibility.
- The critical flow must be covered by automated regression when valuable.

## 4. Map risk before defining test depth

Not every change deserves the same testing effort. Testing depth should follow risk.

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

## 5. Create the test strategy and draft test cases early

For medium or high-risk work, QA should start the **test strategy and test cases before development**, not after handoff.

### What to define early

- Scope and out-of-scope areas
- Main risks and mitigation
- Test levels: unit, API, integration, UI, regression, exploratory, UAT
- Manual vs automated validation
- Test data and environment needs
- Frontend/UX and backend/API validation approach
- Evidence expected for sign-off
- Post-deploy checks when needed

Use the [Test Strategy Template](templates/test-strategy-template.md) and [Test Cases Template](templates/test-cases-template.md) to define risks, scope, validation approach, and early scenarios before development starts.

### Why this helps

- Developers see expected validations before implementation.
- Missing requirements are discovered earlier.
- Automation candidates are identified sooner.
- QA execution becomes faster and less reactive.

### AI-assisted option

AI agents, skills, and instructions can speed up test strategy and test case drafting when used with human review. See [AI Tools](ai-tools/README.md).

Useful prompts:

```text
Review this story for ambiguity, risk, missing acceptance criteria, and testability gaps.
```

```text
Create a lightweight test strategy and risk-based test case outline for this feature.
```

Human QA still owns the final judgment, expected results, risk priority, and product context.

## 6. Validate testability before implementation

A feature is easier to test when testability is designed in.

### Testability questions

- Can this be tested independently?
- Can we prepare reliable test data?
- Can we mock or simulate external dependencies?
- Can we validate the result through API, database, logs, UI, files, or events?
- Can failures be reproduced?
- Can the team identify which step failed?
- Do we need feature flags, test hooks, or better logs?

If the answer is unclear, the story needs more design discussion before development starts.

## 7. Treat contracts as quality assets

For APIs, files, events, schemas, data mappings, or integrations, the contract is part of the product.

### A good contract defines

- version;
- required and optional fields;
- data types and formats;
- default values;
- allowed values;
- backward compatibility expectations;
- sample valid and invalid payloads;
- error responses;
- ownership and change process.

QA should review contracts with the same seriousness as UI behavior.

## 8. Separate frontend/UX and backend/API strategies

Frontend and backend testing protect different risks. A strong strategy covers both without overusing one layer.

### Frontend / UX focus

Validate the user journey, usability, accessibility, clarity, visual feedback, error recovery, permissions, and state changes.

Useful validation:

- exploratory testing;
- UI checks;
- accessibility checks;
- usability review;
- critical UI automation;
- copy, labels, empty states, errors, loading states, and recovery paths.

Use usability heuristics to support structured review. Reference: [Nielsen Heuristics Workshop](https://youtu.be/OtyM8dGKLUU?si=Fu3HYPjSQG3NDAoG)

### Backend / API focus

Validate business rules, contracts, data integrity, security, performance, integrations, error handling, and system behavior beyond the UI.

Useful validation:

- API tests;
- contract tests;
- integration tests;
- logs and correlation IDs;
- data validation;
- negative testing;
- authorization checks;
- duplicate requests, timeouts, retries, and idempotency when relevant.

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
- Valid and invalid input data
- Boundary values
- Existing records needed for regression
- External system availability
- Files, payloads, or events needed for integrations
- Data cleanup strategy

### Good practice

Keep a small, reusable set of **golden test data** for critical flows.

## 11. Assess QA maturity when joining a team

When QA joins a new team, start by understanding how quality currently works before proposing changes.

### Run a simple team survey

Measure the current state of:

- requirement quality;
- Definition of Ready and Definition of Done;
- test strategy and test coverage;
- automation health;
- environment and test data stability;
- defect management;
- observability;
- release confidence;
- user focus;
- quality culture.

Repeat the same survey after a few sprints or months to show improvement, gaps, and culture change.

For a reusable model, see [QA Assessment Survey Template](templates/qa-assessment-survey-template.md).

## 12. Build QA community through a QA Guild

A QA Guild is a recurring space where QAs from different teams share knowledge, patterns, failures, tools, and standards.

### Useful guild topics

- testing techniques;
- automation patterns;
- flaky tests;
- accessibility and UX testing;
- API and contract testing;
- AI-assisted QA;
- quality metrics;
- incident learnings;
- framework/tool decisions.

> **Principle:** QA maturity grows faster when knowledge is shared across teams instead of staying isolated inside one squad.

## 13. Definition of Ready

A story is ready for development when:

- the goal and value are clear;
- acceptance criteria are testable;
- main risks are identified;
- dependencies are known;
- test data needs are understood;
- UX/API/contract expectations are documented;
- frontend and backend validation needs are understood;
- non-functional expectations are clear when relevant;
- observability needs are defined for risky flows;
- QA, Dev, and Product share the same understanding.

For a full template, see [Definition of Ready & Definition of Done Template](templates/definition-of-ready-done-template.md).

## Before development checklist

- [ ] User/business value is clear.
- [ ] User journey and expected experience are understood.
- [ ] Acceptance criteria are testable.
- [ ] BDD or practical checklist format was chosen.
- [ ] Happy path and negative paths are known.
- [ ] Risks are classified.
- [ ] Test strategy and test case outline started when relevant.
- [ ] Test data needs are identified.
- [ ] Dependencies are visible.
- [ ] Integration/API/data contracts are documented.
- [ ] Frontend/UX and backend/API strategies are considered.
- [ ] Tool/framework choices are aligned with product risk and team context.
- [ ] Observability needs are considered.
- [ ] Definition of Ready is met.

## Key message

> QA does not need to wait for code to create value.  
> The earlier QA exposes ambiguity, user risk, and testability gaps, the cheaper and safer the delivery becomes.
