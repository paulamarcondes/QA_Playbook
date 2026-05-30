# Test Cases Template

Use this template to document manual, exploratory, API, integration, regression, and automation candidate scenarios.

Keep test documentation useful and easy to maintain. Avoid long click-by-click scripts unless they are truly needed.

---

## When to use detailed steps

Use detailed steps when the flow requires:

- repeated manual regression;
- audit or compliance evidence;
- complex setup;
- onboarding support;
- handoff to another tester;
- a fragile or high-risk flow.

For most scenarios, prefer concise scenario notes or exploratory charters.

---

## Test charter

**Feature / Area:**  
**Tester:**  
**Date:**  
**Risk Level:** Low / Medium / High / Critical  
**Related story / bug:**  

### Mission

What are we trying to learn or validate?

- 

### Target areas

- 

### Risks to explore

- 

### Test data

- 

### Environment

- 

---

## Scenario list

| ID | Scenario | Type | Priority | Result | Evidence |
|---|---|---|---|---|---|
| TC-001 |  | Positive / Negative / Edge / Regression / Exploratory | Low / Medium / High | Pass / Fail / Blocked |  |

---

## Scenario notes

### Scenario ID

**Goal:**  
**Preconditions:**  
**Data:**  
**Steps or actions:**  
**Expected result:**  
**Actual result:**  
**Evidence:**  
**Notes / findings:**  

---

## Exploratory notes

Use this section for observations that do not fit scripted steps.

| Observation | Risk / Impact | Follow-up |
|---|---|---|
|  |  |  |

---

## Automation candidates

| Scenario | Why automate? | Suggested level | Priority |
|---|---|---|---|
|  |  | Unit / API / Contract / E2E | Low / Medium / High |

Automation should be considered when the scenario is stable, valuable, repeatable, and protects a meaningful risk.

---

## Summary

**Overall result:** Pass / Fail / Blocked  
**Main risks found:**  
**Bugs opened:**  
**Recommended next steps:**
