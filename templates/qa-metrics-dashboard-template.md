# QA Metrics Dashboard Template

The tracking sheet for the metric set defined in [03 - Use metrics that drive decisions](../03-after-development.md#8-use-metrics-that-drive-decisions). That page says *which* metrics and *why*; this one is where you record them.

## Principles

- Metrics improve the system. They are never used to rank people.
- Trends over isolated numbers.
- **If a metric has no target and no agreed action when it breaches, do not track it.**
- Review with QA, Dev, Product, and leadership together. Most of what limits quality is decided above the team, and this is the conversation where that gets decided with the data rather than without it.

## Release confidence

A snapshot per release, not a trend.

| Check | Current | Target | Status |
|---|---:|---:|---|
| Critical tests passed |  |  |  |
| Open critical/high defects |  |  |  |
| Regression completion |  |  |  |
| Known release risks |  |  |  |
| Go/No-Go recommendation |  |  |  |

## The metric set

Ten metrics across five signal types. Start with three, not ten.

| Signal | Metric | Formula | Frequency | Source | Target | Action when it breaches |
|---|---|---|---|---|---|---|
| Outcome | Escaped defects | Found in production / total found | Sprint | Jira, Support |  | Review risk analysis and regression scope |
| Outcome | Production incidents | Count by severity | Month | Incident tool |  | RCA, then targeted regression where they repeat |
| Outcome | Change failure rate | Failed releases / total releases | Month | CI/CD |  | Strengthen release readiness and post-deploy checks |
| Outcome | Support ticket trend | Tickets by theme | Month | Support tool |  | Prioritize the user pain behind the tickets |
| Delivery health | Reopened defect rate | Reopened / closed | Sprint | Jira |  | Improve fix validation and acceptance criteria |
| Delivery health | Validation cycle time | Ready for QA to sign-off | Sprint | Jira |  | Review test data, environments, automation |
| Automation health | Critical-flow coverage | Automated critical flows / total | Month | Test inventory |  | Automate the highest-risk uncovered flow next |
| Automation health | Flaky test rate | Flaky failures / total failures | Sprint | CI/CD |  | Stabilize before expanding coverage |
| Observability | MTTD / MTTR | Detect and restore times | Month | Incident tool |  | Add logs, alerts, correlation IDs, dashboards |
| Culture | QA maturity trend | Assessment score per area | Quarter | [Survey](qa-assessment-survey-template.md) |  | Three improvement actions, with time allocated |

Post-deploy production signals - error rate, latency, traffic, saturation - are tracked per release in the [Deployment Validation Guide](deployment-validation-guide-template.md#9-post-deployment-monitoring).

## Monthly review

1. What improved, and what got worse?
2. Which risk repeated?
3. Which defect should have been caught earlier?
4. Which metric needs better data, or should be dropped?
5. What is the smallest improvement we can make next, and who owns it?
