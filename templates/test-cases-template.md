# Test Cases Template

Use this template to document manual, exploratory, API, integration, regression, and automation candidate scenarios.

Test cases should be readable as plain text documentation. Keep executable automation logic in test/resource files, reusable keywords, fixtures, helpers, or framework-specific resources.

---

## 1. Test Suite Information

| Field | Value |
|---|---|
| Feature / Story |  |
| Jira / Work item |  |
| Product / System |  |
| Test owner |  |
| Environment |  |
| Version / Build |  |
| Date |  |

---

## 2. Scope

### In scope

- 
- 
- 

### Out of scope

- 
- 
- 

### Main risks covered

- 
- 
- 

---

## 3. Coverage Matrix

| Requirement / AC | Scenario | Type | Priority | Automated? | Test Case ID |
|---|---|---|---|---|---|
| AC-001 |  | Positive / Negative / Regression / Integration | High / Medium / Low | Yes / No / Candidate | TC-001 |

---

## 4. Test Cases

### TC-001 - [Scenario title]

| Field | Details |
|---|---|
| Priority | Critical / High / Medium / Low |
| Type | Positive / Negative / API / Integration / UI / Regression / Exploratory |
| Automation | Automated / Candidate / Manual only |
| Preconditions |  |
| Test data |  |
| Steps | 1. <br>2. <br>3. |
| Expected result |  |
| Evidence | Screenshot / logs / payload / file / database record / report |
| Status | Not Run / Passed / Failed / Blocked |
| Defect link |  |

---

### TC-002 - [Scenario title]

| Field | Details |
|---|---|
| Priority | Critical / High / Medium / Low |
| Type | Positive / Negative / API / Integration / UI / Regression / Exploratory |
| Automation | Automated / Candidate / Manual only |
| Preconditions |  |
| Test data |  |
| Steps | 1. <br>2. <br>3. |
| Expected result |  |
| Evidence | Screenshot / logs / payload / file / database record / report |
| Status | Not Run / Passed / Failed / Blocked |
| Defect link |  |

---

## 5. BDD Scenario Option

Use this format when the scenario benefits from business-readable behavior.

```gherkin
Scenario: [short scenario name]
  Given [context]
  When [action]
  Then [expected result]
  And [additional validation]
```

---

## 6. API / Integration Validation Notes

Use this section when validating APIs, files, events, queues, data transformations, or integrations.

| Check | Expected result | Evidence |
|---|---|---|
| Status code / response |  |  |
| Required fields |  |  |
| Optional fields |  |  |
| Data mapping |  |  |
| Error handling |  |  |
| Duplicate handling |  |  |
| Backward compatibility |  |  |
| Logs / traceability |  |  |

---

## 7. Exploratory Testing Charter

| Field | Details |
|---|---|
| Mission | What are we trying to learn or challenge? |
| Area | Feature, flow, integration, or risk area |
| Timebox | 30 / 60 / 90 minutes |
| Data |  |
| Heuristics | Boundary values, invalid data, permissions, interruptions, usability, performance, consistency |
| Notes / Findings |  |
| Follow-up actions |  |

---

## 8. Automation Notes

| Scenario | Automate? | Reason | Suggested level | Notes |
|---|---|---|---|---|
|  | Yes / No / Later |  | Unit / API / Contract / Integration / UI |  |

Automation guidance:

- Automate stable, valuable, and repetitive checks.
- Prioritize critical flows, contracts, integrations, and regression-prone areas.
- Avoid automating unclear or unstable behavior too early.
- Keep test case documentation readable; keep executable logic in the automation framework.
- In Robot Framework, keep Test Cases high-level and place reusable executable keywords in Resource files.

---

## 9. Execution Summary

| Result | Count |
|---|---:|
| Passed |  |
| Failed |  |
| Blocked |  |
| Not Run |  |

### Release recommendation

Ready / Ready with risk / Not ready

### Notes

- 
- 
- 
