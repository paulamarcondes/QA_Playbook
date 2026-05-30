# 03 - After Development

Use release validation, production feedback, metrics, and learning to improve future quality.

This phase is not only about confirming that a release happened. It is about understanding whether the change is safe, useful, observable, and ready for continuous improvement.

---

## Main goal

After development, QA helps the team answer:

- Are we confident enough to release?
- What risks remain?
- Is deployment validation clear?
- Would we notice if the feature failed in production?
- Did production behavior match expectations?
- What should we improve next time?

---

## 1. Confirm release confidence

Release confidence should be based on evidence, not feelings.

Review:

- scope delivered;
- risks covered;
- tests executed;
- defects found and fixed;
- known issues;
- environment limitations;
- automation results;
- deployment risks;
- rollback awareness;
- monitoring readiness.

Useful template: [Deployment Validation Template](templates/deployment-validation-template.md)

---

## 2. Review regression risk

Regression testing should be risk-based.

Ask:

- What existing flows could be affected?
- Which critical paths need retesting?
- Which integrations or contracts changed?
- What data or permissions could be impacted?
- Which automation results matter for this release?
- Is exploratory testing needed for confidence?

Useful resource: [Testing Guide](resources/testing-guide.md)

---

## 3. Validate deployment readiness

Before or during deployment, confirm:

- release scope is clear;
- deployment steps are known;
- smoke checks are defined;
- rollback or recovery plan is understood;
- logs and monitoring are available;
- responsible people are aligned;
- known risks are communicated.

Do not confuse story-level Done with deployment readiness. A story can be Done while the release still needs environment-level validation.

---

## 4. Observe production signals

After release, check whether the system behaves as expected.

Look at:

- errors;
- logs;
- alerts;
- support tickets;
- user complaints;
- key business flows;
- performance or availability signals;
- integration failures;
- data issues.

Testing does not stop when code is merged.

---

## 5. Learn from bugs

A bug is not only a fix request. It is also a learning signal.

For high-severity defects, review:

- why the issue was missed;
- whether requirements were unclear;
- whether risk was underestimated;
- whether tests were missing;
- whether logs were insufficient;
- whether automation should be added;
- whether the checklist or strategy should change.

Useful template: [Bug Report Template](templates/bug-report-template.md)

---

## 6. Use metrics for decisions

Metrics should help the team improve quality, not blame individuals.

Useful questions:

- Are production defects increasing?
- Are releases becoming safer?
- Where are bottlenecks happening?
- Are automated checks giving useful feedback?
- Are high-risk areas getting enough attention?
- Are incidents generating improvements?

Useful template: [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md)

---

## 7. Run a 15-minute quality retro

After a release or production incident, run a short quality retro.

Keep it practical:

1. What went well?
2. What was missed?
3. What risk should have been clearer?
4. What test, log, automation, or checklist should be improved?
5. What is one action for the next cycle?

Checklist item:

```text
Was the root cause or missed risk added to the Quality Review Checklist or Test Strategy?
```

Useful resource: [Quality Review Checklist](resources/quality-review-checklist.md)

---

## Output of this phase

At the end of this phase, the team should have:

- release evidence;
- clear known risks;
- production visibility;
- better metrics;
- improved checklists;
- stronger test strategy for the next cycle.
