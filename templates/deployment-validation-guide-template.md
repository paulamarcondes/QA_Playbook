# Deployment Validation Guide Template

Use this template as a QA-focused guide for release readiness, deployment validation, rollback awareness, and post-deployment monitoring.

It is not a full DevOps runbook. Its purpose is to make QA expectations clear before, during, and after a deployment.

## 1. Release information

| Field | Value |
|---|---|
| Release / Version |  |
| Date / Time |  |
| Environment | QA / UAT / Staging / Production |
| Product / System |  |
| Deployment owner |  |
| QA owner |  |
| Related tickets |  |
| Release notes |  |

## 2. Deployment scope

### Included changes

- [Add item]
- [Add item]
- [Add item]

### Not included

- [Add item]
- [Add item]
- [Add item]

### Impacted areas

| Area | Impact | Validation needed? | Notes |
|---|---|---|---|
| UI / User journey | None / Low / Medium / High | Yes / No |  |
| API / Service | None / Low / Medium / High | Yes / No |  |
| Database / Migration | None / Low / Medium / High | Yes / No |  |
| Integrations | None / Low / Medium / High | Yes / No |  |
| Configuration | None / Low / Medium / High | Yes / No |  |
| Monitoring / Alerts | None / Low / Medium / High | Yes / No |  |
| Documentation / Support | None / Low / Medium / High | Yes / No |  |

## 3. Release readiness checklist

Use this section before approving the deployment.

### Functional readiness

- [ ] Critical acceptance criteria passed.
- [ ] Main user journeys validated.
- [ ] Negative scenarios validated.
- [ ] Edge cases reviewed.
- [ ] Known defects triaged.
- [ ] User-facing behavior changes documented when relevant.

### Regression readiness

- [ ] Risk-based regression completed.
- [ ] Critical automated tests passing.
- [ ] Manual regression evidence attached when needed.
- [ ] Impacted APIs/integrations validated.
- [ ] Permissions and roles checked when relevant.
- [ ] Data migration or transformation validated when relevant.

### Technical readiness

- [ ] Deployment version/build confirmed.
- [ ] Configuration reviewed.
- [ ] Environment dependencies confirmed.
- [ ] Logs are clear and useful.
- [ ] Monitoring/alerts reviewed.
- [ ] Rollback or mitigation plan understood.

### Product and support readiness

- [ ] Product owner aware of release status.
- [ ] Support team informed of relevant changes.
- [ ] Release notes updated when needed.
- [ ] Known risks documented and accepted.
- [ ] Go / No-Go decision recorded.

## 4. Go / No-Go decision

| Question | Answer |
|---|---|
| Is the release ready to deploy? | Ready / Ready with risk / Not ready |
| What are the known risks? |  |
| Who accepted the risks? |  |
| What is the final decision? | Go / No-Go |
| Approver(s) |  |

## 5. Deployment validation steps

| Step | Validation | Expected result | Owner | Evidence | Status |
|---|---|---|---|---|---|
| 1 | Confirm deployed version/build | Correct version is live |  |  | Not Run / Pass / Fail |
| 2 | Validate application/service health | Services are available |  |  | Not Run / Pass / Fail |
| 3 | Run critical smoke test | Main flow works |  |  | Not Run / Pass / Fail |
| 4 | Validate API/integration processing | Expected response/data flow |  |  | Not Run / Pass / Fail |
| 5 | Check logs and monitoring | No unexpected errors |  |  | Not Run / Pass / Fail |
| 6 | Confirm known risk areas | No release-blocking behavior |  |  | Not Run / Pass / Fail |

## 6. Smoke test scenarios

| Scenario | Priority | Steps / Reference | Expected result | Evidence | Status |
|---|---|---|---|---|---|
|  | Critical / High / Medium |  |  |  | Not Run / Pass / Fail |

## 7. Data / integration validation

Use this section when deployment affects APIs, files, events, queues, transformations, or downstream systems.

| Check | Expected result | Evidence | Status |
|---|---|---|---|
| Message/file/API request processed |  |  | Not Run / Pass / Fail |
| Required fields populated |  |  | Not Run / Pass / Fail |
| Data mapping correct |  |  | Not Run / Pass / Fail |
| Error handling correct |  |  | Not Run / Pass / Fail |
| Duplicate/retry behavior correct |  |  | Not Run / Pass / Fail |
| Downstream confirmation available |  |  | Not Run / Pass / Fail |
| Logs contain correlation/trace ID |  |  | Not Run / Pass / Fail |

## 8. Rollback / mitigation awareness

| Question | Answer |
|---|---|
| What issue would trigger rollback? |  |
| Who can approve rollback? |  |
| What is the rollback path? |  |
| What data/configuration needs special care? |  |
| What is the customer/user communication path? |  |
| What temporary mitigation is available if rollback is not possible? |  |

## 9. Post-deployment monitoring

| Signal | Where to check | Expected behavior | Monitoring window | Owner |
|---|---|---|---|---|
| Error rate |  |  |  |  |
| Latency / performance |  |  |  |  |
| Failed jobs/messages/files |  |  |  |  |
| Support tickets / user reports |  |  |  |  |
| Business/system transactions |  |  |  |  |
| Logs/traces for known risk areas |  |  |  |  |

## 10. Final QA sign-off

| Field | Value |
|---|---|
| Deployment validation result | Passed / Passed with risk / Failed |
| Known risks |  |
| Follow-up actions |  |
| QA sign-off |  |
| Release owner sign-off |  |
| Date/time |  |

## 11. Post-release learning

Use this section after the release to capture improvements. For more guidance, see [03 - After Development](../03-after-development.md).

| Question | Notes |
|---|---|
| Did any issue escape to production? |  |
| What did our tests miss? |  |
| What should be automated or monitored next? |  |
| What should be added to the test strategy or regression suite? |  |
| What should be improved in requirements, development, or deployment? |  |
