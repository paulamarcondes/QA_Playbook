# 03 - After Development

Validate release confidence and learn from real outcomes.

This phase is about confirming that the change is ready to release, watching what happens after release, and improving the quality system based on evidence.

---

## Main goal

After development, the team should answer:

- Is the change ready for release?
- What risk remains?
- What evidence supports the release decision?
- What should be monitored after deployment?
- Did users or production behavior reveal anything we missed?
- What should improve in the next cycle?

---

## 1. Review release confidence

Release confidence should be based on evidence, not optimism.

Check:

- acceptance criteria status;
- test results;
- open bugs and known risks;
- regression impact;
- automation results;
- environment limitations;
- deployment or rollback concerns;
- monitoring readiness.

Useful template: [Deployment Validation Template](templates/deployment-validation-template.md)

---

## 2. Validate regression risk

Regression should be focused on what can realistically break.

Prioritize:

- critical user journeys;
- changed business rules;
- integrations and contracts;
- data transformations;
- permission-sensitive behavior;
- areas with recent bugs;
- high-value automated checks.

Useful resource: [Testing Guide](resources/testing-guide.md)

---

## 3. Check deployment readiness

Before release, confirm:

- build or version is known;
- scope is clear;
- smoke checks are defined;
- owner is identified;
- rollback or recovery path is understood;
- monitoring and logs are available for critical flows;
- stakeholders know known risks.

Useful template: [Deployment Validation Template](templates/deployment-validation-template.md)

---

## 4. Watch production signals

Post-deploy validation should check whether the system behaves as expected after release.

Look at:

- logs;
- errors;
- alerts;
- success and failure rates;
- latency or performance signals;
- support tickets;
- user complaints;
- data quality issues;
- integration queues or failed messages.

The goal is not to test everything again. The goal is to detect important issues quickly.

---

## 5. Use bugs as learning signals

A bug report is not only a fix request. It is also a signal about what the quality process missed.

For Critical or Blocker bugs, ask:

- Was the risk identified early?
- Were requirements or contracts unclear?
- Did tests miss an important scenario?
- Was automation missing or weak?
- Was observability enough to investigate quickly?
- Should the [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) be updated?

Useful template: [Bug Report Template](templates/bug-report-template.md)

---

## 6. Run a short quality retro

After important releases or production incidents, run a short quality retro.

Keep it practical. In 15 minutes, identify:

- what worked;
- what was missed;
- what risk should be added to the strategy;
- what checklist item should be improved;
- what automation or monitoring would help next time.

Update the [Quality Review Checklist](resources/quality-review-checklist.md), [Test Strategy Template](templates/test-strategy-template.md), or [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) when needed.

---

## 7. Track metrics that support decisions

Metrics should help the team improve quality, not blame people.

Track signals such as:

- escaped defects;
- change failure rate;
- time to restore service;
- release confidence;
- automation value;
- repeated defects by area;
- quality actions from retros.

The [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) is the single source for metric tracking and definitions.

---

## Output of this phase

At the end of this phase, the team should have:

- a clear release decision;
- known risks communicated;
- production signals reviewed;
- important defects captured with context;
- metrics updated when needed;
- practical improvements added to the quality process.
