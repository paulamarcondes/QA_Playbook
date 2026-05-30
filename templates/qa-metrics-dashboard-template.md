# QA Metrics Dashboard Template

Use this template to track quality signals that help the team make better decisions.

Metrics should show risk, bottlenecks, confidence, and improvement opportunities. They should not be used to blame people.

---

## Dashboard information

**Team / Project:**  
**Period:**  
**Owner:**  
**Last updated:**  

---

## 1. Delivery speed and stability

These are inspired by DORA metrics.

| Metric | What it means | Current value | Trend | Notes / Action |
|---|---|---|---|---|
| Deployment frequency | How often the team releases successfully. |  | Up / Down / Stable |  |
| Lead time for changes | Time from code commit to production. |  | Up / Down / Stable |  |
| Change failure rate | Percentage of releases causing production failures. |  | Up / Down / Stable |  |
| Time to restore service | Time to recover from production failure. |  | Up / Down / Stable |  |

Use these metrics to understand delivery health, not individual performance.

---

## 2. Release quality

| Metric | Current value | Trend | Notes / Action |
|---|---|---|---|
| Defects found before release |  | Up / Down / Stable |  |
| Defects found after release |  | Up / Down / Stable |  |
| Critical / high severity defects |  | Up / Down / Stable |  |
| Escaped defects by area |  | Up / Down / Stable |  |
| Release confidence level | Low / Medium / High |  |  |

Useful question:

```text
Are we finding important issues before users do?
```

---

## 3. Risk and bottlenecks

| Signal | What to check | Notes / Action |
|---|---|---|
| High-risk stories without clear risk level | Are risky changes being identified early? |  |
| Stories blocked by unclear requirements | Is refinement strong enough? |  |
| Environment blockers | Are test environments slowing feedback? |  |
| Reopened bugs | Are fixes or requirements unclear? |  |
| Repeated defects in same area | Is there a deeper quality gap? |  |

---

## 4. Automation value

Do not track only number of automated tests. Track whether automation improves feedback.

| Metric | Current value | Notes / Action |
|---|---|---|
| Critical paths covered by automation |  |  |
| Contract/API checks in CI/CD |  |  |
| Useful regression checks automated |  |  |
| Flaky tests |  |  |
| Time saved or feedback improved |  |  |
| Automation gaps for high-risk areas |  |  |

Useful question:

```text
Is automation protecting important behavior with reliable feedback?
```

---

## 5. Product and user impact

| Signal | Current value | Notes / Action |
|---|---|---|
| User complaints related to quality |  |  |
| Support tickets by feature |  |  |
| Failed critical journeys |  |  |
| Accessibility or usability issues |  |  |
| Data quality issues |  |  |

---

## 6. Team improvement

| Signal | Current value | Notes / Action |
|---|---|---|
| QA maturity survey result |  |  |
| Retros with quality actions |  |  |
| Improvements added to checklist |  |  |
| Risks added to strategy after incidents |  |  |
| AI usage reviewed safely |  |  |

Reference: [QA Assessment Survey Template](qa-assessment-survey-template.md)

---

## Decisions from this dashboard

| Finding | Decision | Owner | Due date |
|---|---|---|---|
|  |  |  |  |

---

## Summary

**Main quality concern:**  
**Main improvement opportunity:**  
**Action for next cycle:**
