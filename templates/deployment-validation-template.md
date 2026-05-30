# Deployment Validation Template

Use this template to plan release checks, post-deploy validation, rollback awareness, and production monitoring.

Deployment validation supports the release learning flow described in [03 - After Development](../03-after-development.md).

---

## Deployment information

**Release / Version:**  
**Environment:**  
**Date / Time:**  
**Owner:**  
**Related stories / bugs:**  
**Risk Level:** Low / Medium / High / Critical  

---

## Pre-deployment checks

- [ ] Release scope is clear.
- [ ] Known risks are documented.
- [ ] Critical bugs are resolved or accepted.
- [ ] Smoke checks are defined.
- [ ] Required data and configuration are ready.
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

References:

- [03 - After Development](../03-after-development.md)
- [QA Metrics Dashboard Template](qa-metrics-dashboard-template.md)
- [Bug Report Template](bug-report-template.md)
