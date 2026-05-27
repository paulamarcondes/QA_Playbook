# 01 - Before Development: Quality Planning & Risk Prevention

The goal before development is simple: **make the work clear, testable, valuable, and safe to build**.

QA should be involved early enough to prevent ambiguity, expose risk, and align the team on what quality means for that change.

---

## Outcomes expected before coding starts

A story or feature should enter development only when the team understands:

- what user or business problem it solves;
- which flows, systems, data, and users are impacted;
- what could fail and how serious the impact would be;
- how success and failure will be validated;
- what evidence will prove the change is working;
- what needs to be observable after release.

---

## 1. Run a lightweight Three Amigos review

Use a short conversation with **Product + Development + QA** before implementation.

### Questions to answer

- What problem are we solving?
- Who is the user or system consuming this change?
- What is the expected happy path?
- What are the most important negative paths?
- What edge cases are likely?
- What should never break?
- How will we validate this in test and production?
- What logs, metrics, or traces will help us troubleshoot it later?

### Output

A story should leave refinement with clear acceptance criteria, known risks, test data needs, dependencies, and a shared understanding of done.

---

## 2. Write acceptance criteria that are testable

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

### Recommended format

```gherkin
Given a valid user or system context
When the action is performed
Then the expected result should happen
And the system should provide clear feedback or traceability
```

### Add quality criteria, not only functional criteria

Examples:

- Error messages must be clear and actionable.
- Invalid data must fail explicitly, not silently.
- The system must log the correlation ID for troubleshooting.
- The API response must keep backward compatibility.
 - The API response must maintain backward compatibility.
- The critical flow must be covered by automated regression.

---

## 3. Map risk before defining test depth

Not every change deserves the same testing effort. Testing depth should follow risk.

| Risk factor | Questions |
|---|---|
| User impact | Could this block a critical user journey? |
| Business impact | Could this affect revenue, compliance, safety, or trust? |
| Technical complexity | Does it involve integrations, async flows, data transformation, permissions, or configuration? |
| Change size | Is the change touching shared components or legacy areas? |
| Defect history | Has this area failed before? |
| Observability | Can failures be detected and diagnosed quickly? |

### Risk levels

| Level | Testing approach |
|---|---|
| Low | Focused functional validation and basic regression |
| Medium | Functional, negative, integration, and targeted regression |
| High | Full risk-based validation, automation review, logs/monitoring checks, rollback awareness, and release follow-up |

---

## 4. Validate testability before implementation

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

---

## 5. Treat contracts as quality assets

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

---

## 6. Prepare test data and environments early

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

---

## 7. Definition of Ready

A story is ready for development when:

- the goal and value are clear;
- acceptance criteria are testable;
- main risks are identified;
- dependencies are known;
- test data needs are understood;
- UX/API/contract expectations are documented;
- non-functional expectations are clear when relevant;
- observability needs are defined for risky flows;
- QA, Dev, and Product share the same understanding.

---

## Before development checklist

- [ ] User/business value is clear
- [ ] Acceptance criteria are testable
- [ ] Happy path and negative paths are known
- [ ] Risks are classified
- [ ] Test data needs are identified
- [ ] Dependencies are visible
- [ ] Integration/API/data contracts are documented
- [ ] Observability needs are considered
- [ ] Definition of Ready is met

---

## Key message

> QA does not need to wait for code to create value.  
> The earlier QA exposes ambiguity and risk, the cheaper and safer the delivery becomes.
