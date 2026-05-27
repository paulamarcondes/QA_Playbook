# Test Strategy Template

Use this as a lightweight test strategy for a feature, integration, release, or significant change.

This template includes risk assessment, test scope, test levels, automation direction, observability, and release confidence in one place.

---

## 1. Strategy Summary

| Field | Value |
|---|---|
| Feature / Change |  |
| Jira / Work item |  |
| Product / System |  |
| Owner |  |
| Release / Sprint |  |
| Overall risk | Low / Medium / High / Critical |
| Recommendation | Proceed / Proceed with risk / Do not proceed |

### Objective

What confidence do we need before release?

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

### Systems / areas impacted

| Area | Impact | Notes |
|---|---|---|
| UI | None / Low / Medium / High |  |
| API | None / Low / Medium / High |  |
| Database | None / Low / Medium / High |  |
| Integration / Contract | None / Low / Medium / High |  |
| Files / Events / Queues | None / Low / Medium / High |  |
| Configuration | None / Low / Medium / High |  |
| Permissions / Security | None / Low / Medium / High |  |
| Reporting / Analytics | None / Low / Medium / High |  |

---

## 3. Risk Assessment

Risk should guide testing depth and evidence expectations.

| Risk factor | Low | Medium | High | Notes |
|---|---|---|---|---|
| User impact |  |  |  |  |
| Business impact |  |  |  |  |
| Technical complexity |  |  |  |  |
| Integration impact |  |  |  |  |
| Data sensitivity |  |  |  |  |
| Security / permissions |  |  |  |  |
| Defect history |  |  |  |  |
| Observability gaps |  |  |  |  |
| Regression risk |  |  |  |  |

### Overall risk decision

**Risk level:** Low / Medium / High / Critical  
**Reason:**  
**Testing depth required:** Light / Standard / Deep / Release-blocking validation

---

## 4. Quality Risks and Mitigation

| Risk | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|
|  |  |  |  | Open / Mitigated / Accepted |

---

## 5. Test Approach by Level

| Test level | Required? | Purpose | Owner | Evidence |
|---|---|---|---|---|
| Unit | Yes / No | Business rules, validators, transformations | Dev | PR / CI results |
| Component | Yes / No | Isolated service behavior | Dev / QA | Test report |
| API | Yes / No | Contracts, payloads, status codes, errors | QA / Dev | API evidence |
| Contract | Yes / No | Provider/consumer compatibility | QA / Dev | Contract report |
| Integration | Yes / No | Cross-system flow | QA / Dev | Logs / payloads / files |
| UI | Yes / No | Critical user journey | QA | Screenshots / video |
| Exploratory | Yes / No | Unknown risks, usability, edge cases | QA / Team | Notes / findings |
| Regression | Yes / No | Existing behavior protection | QA / Automation | Test run |
| Post-deploy smoke | Yes / No | Production confidence | QA / DevOps | Monitoring / smoke result |

---

## 6. Test Data and Environment

| Need | Source | Owner | Status | Notes |
|---|---|---|---|---|
| Test data |  |  | Ready / Blocked / Pending |  |
| User / Role |  |  | Ready / Blocked / Pending |  |
| Environment |  |  | Ready / Blocked / Pending |  |
| External dependency |  |  | Ready / Blocked / Pending |  |
| Mock / Stub |  |  | Ready / Blocked / Pending |  |

---

## 7. Automation Strategy

| Scenario | Automate? | Level | Reason | Location / Notes |
|---|---|---|---|---|
|  | Yes / No / Later | Unit / API / Integration / UI |  |  |

Automation priority:

1. Critical flows
2. High-risk regression
3. API/contracts/integrations
4. Repetitive manual checks
5. Stable behavior with clear expected results

Avoid automating unstable, unclear, or low-value scenarios before the behavior is mature.

---

## 8. Observability and Supportability

| Requirement | Status | Evidence / Notes |
|---|---|---|
| Clear error logs |  |  |
| Correlation / transaction ID |  |  |
| Dashboard or log query available |  |  |
| Alerts reviewed when relevant |  |  |
| Known failure modes documented |  |  |
| Support / troubleshooting notes updated |  |  |

---

## 9. Entry Criteria

- [ ] Requirements are clear and testable
- [ ] Acceptance criteria are approved
- [ ] Risks are classified
- [ ] Test data is available or planned
- [ ] Environment and dependencies are ready
- [ ] Observability expectations are clear

---

## 10. Exit Criteria

- [ ] Critical scenarios passed
- [ ] High-risk regression completed
- [ ] Required automated tests passing
- [ ] High-severity defects fixed or explicitly accepted
- [ ] Evidence attached
- [ ] Open risks communicated
- [ ] Post-deploy validation defined
- [ ] Release recommendation provided

---

## 11. Final Recommendation

**Status:** Ready / Ready with risk / Not ready  
**Reason:**  
**Known risks:**  
**Approver(s):**  
