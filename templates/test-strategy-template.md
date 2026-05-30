# Test Strategy Template

Use this template to define the testing approach for a feature, project, epic, or release.

The strategy should be lightweight, risk-based, and useful for real decisions.

---

## Strategy information

**Project / Feature:**  
**Owner:**  
**Date:**  
**Version:**  
**Related tickets / links:**  

---

## 1. Goal

What quality decision should this strategy support?

- 

---

## 2. Scope

### In scope

- 

### Out of scope

- 

---

## 3. Risk framework

Use this section as the source of truth for risk-based testing decisions.

| Risk level | When to use | Expected testing depth |
|---|---|---|
| Low | Small, isolated, low-impact change | Lightweight validation and basic evidence |
| Medium | Normal feature change with limited dependencies | Positive, negative, and affected regression checks |
| High | Critical flow, integration, data, security, permissions, or production impact | Deeper test design, technical review, automation consideration, stronger evidence |
| Critical | Business-critical, customer-impacting, compliance, payment, safety, or major production risk | Full alignment, strong evidence, monitoring, rollback awareness, and leadership visibility when needed |

Risk drivers:

- user or business impact;
- production stability;
- integrations or external systems;
- data transformation or migration;
- security and permissions;
- accessibility or user access;
- compliance or audit needs;
- recent defects in the same area;
- complexity or uncertainty.

---

## 4. Testing approach

| Area / Risk | Testing approach | Owner | Notes |
|---|---|---|---|
|  | Unit / API / Contract / Integration / E2E / Exploratory / Regression |  |  |

Useful resource: [Testing Guide](../resources/testing-guide.md)

---

## 5. Automation approach

Automation should improve feedback, not only increase test count.

| Candidate | Why automate? | Level | Priority |
|---|---|---|---|
|  | Critical path / Contract / Regression / Repetitive check | Unit / API / Contract / E2E | Low / Medium / High |

Automation risks or limitations:

- 

---

## 6. Data and environments

| Need | Details | Owner |
|---|---|---|
| Test data |  |  |
| Accounts / roles |  |  |
| Environment |  |  |
| External systems |  |  |
| Feature flags / configs |  |  |

---

## 7. Observability and release confidence

| Signal | What should be visible? | Notes |
|---|---|---|
| Logs |  |  |
| Metrics |  |  |
| Alerts |  |  |
| IDs / traceability |  |  |
| Post-deploy checks |  |  |

---

## 8. Entry and exit criteria

### Entry criteria

- [ ] Requirements are testable.
- [ ] Risk level is known.
- [ ] Data and environment needs are clear.
- [ ] Dependencies are understood.

### Exit criteria

- [ ] Planned validation completed or risks accepted.
- [ ] Critical defects resolved or accepted.
- [ ] Evidence is available.
- [ ] Release risks are communicated.
- [ ] Monitoring or post-deploy checks are planned when needed.

---

## 9. Open risks and decisions

| Risk / Decision | Owner | Status | Notes |
|---|---|---|---|
|  |  | Open / Accepted / Mitigated |  |

---

## Summary

**Overall risk level:** Low / Medium / High / Critical  
**Release confidence:** Low / Medium / High  
**Main concern:**  
**Recommended next step:**
