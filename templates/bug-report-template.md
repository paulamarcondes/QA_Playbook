# Bug Report Template

A good bug report helps the team reproduce, investigate, prioritize, and learn from the issue.

It should explain what happened, where to look, and why it matters.

---

## Summary

**Title:** `[Area] Action fails when condition happens`  
**Reported by:**  
**Date:**  
**Related story / release:**  

---

## Severity, priority, and risk

**Severity:** Low / Medium / High / Critical  
**Priority:** Low / Medium / High / Urgent  
**Risk Level:** Low / Medium / High / Critical  

**Why it matters:**  

- 

Reference: Core Principle #3 — Risk drives testing depth.

---

## Environment

| Item | Details |
|---|---|
| Environment | Dev / QA / Staging / Production |
| Build / Version |  |
| Browser / Device |  |
| User / Role |  |
| Test data |  |
| Feature flag |  |
| External system |  |

---

## Affected area

**Feature / Flow:**  
**API / Service / Component:**  
**Integration / External System:**  
**Data affected:**  

---

## Steps to reproduce or trigger condition

1. 
2. 
3. 

**Reproducibility:** Always / Sometimes / Once / Unknown  

---

## Expected result

- 

---

## Actual result

- 

---

## Evidence

Add useful evidence, not noise.

| Evidence type | Link / Details |
|---|---|
| Screenshot / Video |  |
| Logs |  |
| Trace ID / Correlation ID |  |
| Request / Response payload |  |
| Error message |  |
| Database record / ID |  |
| Automation report |  |

Do not include secrets, passwords, tokens, or sensitive personal data.

---

## Technical context

**Suspected area:**  
**Recent change related to this issue:**  
**Possible root cause:**  
**Workaround:**  

---

## User / business impact

Who is affected and what is the consequence?

- 

Examples:

- User cannot complete a critical journey.
- Incorrect data is sent to another system.
- Permission rules allow the wrong access.
- Production support cannot investigate due to missing logs.

---

## Resolution notes

**Fixed by:**  
**Fix version:**  
**Validation performed:**  
**Regression needed:** Yes / No  
**Automation candidate:** Yes / No  

---

## Critical / Blocker follow-up

For Critical or Blocker bugs:

- [ ] Update the [QA Metrics Dashboard](qa-metrics-dashboard-template.md) when relevant.
- [ ] Review whether a post-release learning discussion is needed.
- [ ] Check whether the [Test Strategy](test-strategy-template.md) or [Quality Review Checklist](../resources/quality-review-checklist.md) should be updated.
- [ ] Follow the learning process from [03 - After Development](../03-after-development.md).
