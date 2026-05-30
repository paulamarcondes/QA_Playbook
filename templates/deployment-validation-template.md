# Deployment Validation Template

Use this template to plan release checks, post-deploy validation, rollback awareness, and production monitoring.

This is different from Definition of Done. DoD is story-level completion. Deployment validation is environment-level release confidence.

---

## Release information

**Release / Version:**  
**Date:**  
**Environment:**  
**Owner:**  
**Related tickets:**  

---

## Release scope

### Included changes

- 

### Out of scope

- 

### Known risks

- 

---

## Pre-deployment checks

- [ ] Release scope is confirmed.
- [ ] Required approvals are complete.
- [ ] Critical defects are reviewed.
- [ ] Known issues are documented.
- [ ] Test evidence is available.
- [ ] Dependencies are ready.
- [ ] Test data or configuration needs are clear.
- [ ] Rollback or recovery plan is understood.
- [ ] Monitoring and logs are available for critical flows.

---

## Smoke validation

| Check | Expected result | Owner | Result | Evidence |
|---|---|---|---|---|
|  |  |  | Pass / Fail / Blocked |  |

---

## Post-deploy monitoring

Check production or target environment signals after deployment.

| Signal | What to check | Result / Notes |
|---|---|---|
| Logs | Errors, exceptions, warnings, correlation IDs |  |
| Metrics | Failures, latency, volume, success rate |  |
| Alerts | New or unusual alerts |  |
| User flow | Critical journey works as expected |  |
| Integrations | Data is moving correctly |  |
| Support | New tickets or user complaints |  |

---

## Rollback awareness

- Rollback owner:
- Rollback trigger:
- Rollback steps location:
- Communication channel:
- Known rollback risks:

---

## Final release status

**Status:** Approved / Approved with risks / Blocked / Rolled back  

**Summary:**  

**Known risks:**  

**Follow-up actions:**  

---

## Learning follow-up

If issues happened after deployment:

- [ ] Bug report created or updated.
- [ ] QA Metrics Dashboard updated when relevant.
- [ ] Test Strategy updated when a risk was missed.
- [ ] Quality Review Checklist updated when a process gap was found.
- [ ] 15-minute quality retro completed when needed.
