# QA Metrics Dashboard Template

Use this template to track quality trends and support better team decisions.

## Dashboard principles

- Use metrics to improve the system, not to blame people.
- Prefer trends over isolated numbers.
- Connect metrics to decisions and actions.
- Highlight risk, bottlenecks, and learning opportunities.
- Review metrics regularly with QA, Dev, Product, and leadership.

## Release confidence

| Metric | Current | Target | Status | Action |
|---|---:|---:|---|---|
| Critical tests passed |  |  |  |  |
| Open critical/high defects |  |  |  |  |
| Regression completion |  |  |  |  |
| Known release risks |  |  |  |  |
| Go/No-Go recommendation |  |  |  |  |

## Quality outcomes

| Metric | Formula / definition | Frequency | Data source | Action when red |
|---|---|---|---|---|
| Defect escape rate | Escaped defects / total defects | Sprint/month | Jira/TestRail/Support | Review test strategy and risk mapping |
| Production incidents | Count by severity | Sprint/month | Incident tool/logs | Run RCA and add prevention action |
| Change failure rate | Failed releases / total releases | Month | CI/CD/incident records | Improve release readiness and monitoring |
| Reopened defect rate | Reopened defects / closed defects | Sprint | Jira | Improve fix validation |
| Customer-reported defects | Defects reported by users/support | Month | Support tool | Prioritize user pain points |

## Process health

| Metric | Formula / definition | Frequency | Data source | Action when red |
|---|---|---|---|---|
| Requirement readiness | Stories meeting DoR / total stories | Sprint | Jira checklist | Improve refinement |
| Validation cycle time | Ready for QA to QA sign-off | Sprint | Jira | Remove testing bottlenecks |
| Defect resolution time | Bug created to verified fix | Sprint | Jira | Improve triage and ownership |
| Defects by origin | Requirement/code/test data/environment/etc. | Sprint/month | RCA labels | Target root causes |

## Automation health

| Metric | Formula / definition | Frequency | Data source | Action when red |
|---|---|---|---|---|
| Critical flow automation coverage | Automated critical flows / total critical flows | Month | Test inventory | Automate highest-risk gaps |
| Automated test pass rate | Passed tests / executed tests | Build/sprint | CI/CD | Investigate failures |
| Flaky test rate | Flaky failures / total failures | Sprint | CI/CD | Stabilize before expanding |
| Regression execution time | Time to complete regression | Release | CI/CD/TestRail | Optimize suite and scope |
| Automation maintenance effort | Time spent fixing tests | Sprint/month | Team tracking | Refactor brittle tests |

## Production signals

| Metric | What to watch | Action |
|---|---|---|
| Error rate | New or increasing failures | Investigate and classify impact |
| Latency | Slower critical operations | Check performance degradation |
| Traffic/volume | Abnormal spikes or drops | Compare with expected usage |
| Saturation | Resource limits or queue buildup | Prevent instability |
| MTTD | Time to detect failures | Improve alerts |
| MTTR | Time to restore service | Improve incident response |

## Monthly quality review

Answer these questions:

1. What improved?
2. What got worse?
3. Which risk repeated?
4. Which defect should have been caught earlier?
5. Which metric needs better data?
6. What is the smallest process, test, automation, or observability improvement we can make next?
