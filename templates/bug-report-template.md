# Bug Report Template

Use this template to report bugs with enough context to help the team fix the issue faster and learn from it.

A good bug report explains what happened, where to investigate, who is affected, and why it matters.

---

## Bug summary

**Title:**  
**Reported by:**  
**Date:**  
**Related story / release:**  
**Severity:** Low / Medium / High / Critical  
**Priority:** Low / Medium / High / Urgent  
**Risk Level:** Low / Medium / High / Critical  

Risk should align with the framework in the [Test Strategy Template](test-strategy-template.md).

---

## Affected area

**Feature / flow:**  
**Component / service / API / integration:**  
**Environment:**  
**Build / version:**  
**User role / permission:**  
**Data used:**  

---

## Issue description

Describe the issue clearly and concisely.

```text
What happened?
Where did it happen?
How often does it happen?
```

---

## Steps or trigger condition

Use steps when reproduction is clear. Use trigger condition when the issue depends on data, integration, timing, or environment state.

1. 
2. 
3. 

---

## Expected result

What should happen?

- 

---

## Actual result

What happened instead?

- 

---

## Evidence

Attach or link relevant evidence.

| Evidence type | Link / details |
|---|---|
| Screenshot / video |  |
| Logs |  |
| Trace ID / correlation ID |  |
| Request / response payload |  |
| File / message sample |  |
| Console / network error |  |

Do not include sensitive data unless it is sanitized or approved.

---

## Technical context

Add anything that helps investigation.

| Item | Details |
|---|---|
| Suspected area |  |
| Last known working version |  |
| Recent related change |  |
| Environment state |  |
| External dependency |  |
| Frequency | Always / Intermittent / Once |
| Workaround |  |

---

## Impact

Explain why this matters.

| Impact area | Notes |
|---|---|
| User impact |  |
| Business impact |  |
| Data impact |  |
| Security / permission impact |  |
| Release impact |  |

---

## Resolution notes

Use after investigation or fix.

**Root cause:**  
**Fix summary:**  
**Validation completed:**  
**Regression added or updated:**  
**Automation added or updated:**  
**Monitoring or alert updated:**  

---

## Critical / Blocker follow-up

For Critical or Blocker bugs:

- [ ] Update the [QA Metrics Dashboard](qa-metrics-dashboard-template.md) when relevant.
- [ ] Review whether Change Failure Rate or escaped defect metrics were affected.
- [ ] Trigger post-release learning according to [03 - After Development](../03-after-development.md).
- [ ] Update the [Test Strategy Template](test-strategy-template.md) if a risk was missed.
- [ ] Update the [Quality Review Checklist](../resources/quality-review-checklist.md) if a process gap was found.
