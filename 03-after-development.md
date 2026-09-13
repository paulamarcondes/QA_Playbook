# 03 - After Development

Release confidence, metrics, and continuous improvement after implementation.

The goal after development: **release with confidence, detect issues quickly, and learn from what happens next.** Quality does not end when QA testing is complete - release readiness, production validation, observability, metrics, and retrospectives are part of QA.

> **Key idea:** A release is not finished when the code ships. It is finished when the team can see how it behaves, explain the risk it carries, and act on what it learns.

Companion reference: [Quality Review Checklist - After release](resources/quality-review-checklist.md#after-release).

## Outcomes expected after development

After implementation, the team understands release risk, validates key flows before and after deploy, releases in a way that limits blast radius, detects failures quickly, communicates QA status to stakeholders, measures quality trends, and learns from incidents to improve the next cycle - recapped in the [after development checklist](#after-development-checklist).

## 1. Define release readiness

Before release, the team should confirm that the change is functionally correct, technically safe, and operationally observable.

### Release readiness checklist

- [ ] Critical acceptance criteria passed.
- [ ] High-risk regression executed and critical automated tests passing.
- [ ] Known defects reviewed and accepted or fixed.
- [ ] Rollback or mitigation plan understood.
- [ ] Logs and monitoring available for critical flows.
- [ ] Support/Product informed, with release notes or documentation updated when needed.
- [ ] Test evidence attached.
- [ ] Go/No-Go decision made with visible risk.

The checklist feeds one clear decision - release, release with mitigation, or hold:

```mermaid
flowchart TD
    R["`**Release readiness review**
AC · regression · automation
defects · rollback · observability`"]:::step --> Q{"`Risk visible
and acceptable?`"}
    Q -->|Yes| GO["`**Go**
release, then smoke-test
and monitor`"]:::go
    Q -->|Residual risk| COND["`**Ready with risk**
release with mitigation
+ heightened monitoring`"]:::cond
    Q -->|No| NOGO["`**No-go**
fix blockers,
then re-review`"]:::nogo
    NOGO -.-> R
    classDef step fill:#d6deea,stroke:#3f4f68,color:#222a38;
    classDef go   fill:#d4e4d8,stroke:#2f5a43,color:#1f3329;
    classDef cond fill:#ecdcb8,stroke:#6e5418,color:#3d3115;
    classDef nogo fill:#e6c2c4,stroke:#7a3338,color:#38191b;
```

The expanded version of this gate - functional, regression, technical, and product/support readiness, plus deployment steps and rollback - is in the [Deployment Validation Guide Template](templates/deployment-validation-guide-template.md).

## 2. Run focused regression

Regression should protect what matters most, not blindly repeat everything.

### Regression should prioritize

- critical user journeys;
- high-traffic areas;
- revenue, compliance, safety, or trust-related flows;
- recently changed components;
- historically unstable areas;
- integrations and contracts;
- permissions and data-sensitive flows.

### Good regression questions

- What could this change break?
- Which users would be most affected?
- Which integrations depend on this behavior?
- Which automated tests already protect this?
- What still needs manual judgment?

### Prune the suite, not only grow it

Regression suites only ever get added to, and an hour of tests that nobody trusts protects nothing. The [pesticide paradox](resources/testing-types.md#seven-testing-principles-istqb) is not just an observation, it is an instruction to maintain.

Review the suite on a regular cadence - quarterly, or at every major release - and act on four questions:

| Question | Action |
|---|---|
| Has this test ever failed for a real defect? | A test that has never caught anything, over years, is documentation with a run cost. Demote or delete. |
| Does it duplicate a cheaper test? | If a unit test already covers the rule, the UI test covering it again is paying twice for one risk. |
| Does it still match how the product works? | Tests for retired flows quietly pass forever and hide that nothing is being checked. |
| Is it flaky? | Apply the quarantine policy in [02 - When tests go flaky](02-during-development.md#when-tests-go-flaky). Flaky tests spend trust, not just time. |

> **Balance the ledger.** When a post-release review adds a regression test, that is the moment to ask which one it replaces. A suite that only grows eventually gets skipped wholesale, and then it protects nothing at all.

## 3. Run a bug bash before big releases

Regression protects the risks you already know about. A **bug bash** is a time-boxed session where the whole team attacks a release-candidate build at the same time, looking for the risks nobody wrote a test for. Developers, Product, Support, UX, and QA each break software differently, and the people closest to the code are the least likely to use it the wrong way.

Worth running before a major release, a high-risk integration, a migration, or the first version of a customer-facing flow. Not worth running for routine changes.

> **Real world:** invite people from close teams - a neighboring squad, Support, Ops, a QA from the Guild. They ask the questions a new user would, and they are not protecting anything they built.

| Step | What it takes |
|---|---|
| 1. Prepare | A build stable enough to explore, ready test data and accounts, and a clear scope: which areas are in, which are out. |
| 2. Bash | 60-90 minutes, everyone at once, areas or charters assigned so coverage does not collapse onto the same happy path, and one shared place to log findings. |
| 3. Triage | Same day, while context is fresh: dedupe, separate bugs from feature requests and test data noise, then set severity and priority. |
| 4. Feed back | Fix, accept, or defer; turn valuable findings into regression tests or automation candidates; hand residual risk to the Go/No-Go decision. |

### What makes a bug bash fail

- An unstable build, so the session finds environment noise instead of product risk.
- No scope, so everyone retests the same happy path.
- Running it too late for anything found to be fixed.
- No triage, so findings become a backlog nobody reads.

> **Real world:** the hard part is not the session, it is protecting the hour on other people's calendars. Tie it to a release date and keep it short - a focused 60 minutes with six people beats a vague afternoon with two.

To classify what the session surfaces, see [02 - Define what is a bug and what is not](02-during-development.md#10-define-what-is-a-bug-and-what-is-not).

## 4. Release progressively

A release does not have to be a single moment where all the risk lands at once. Progressive delivery separates **deploying** code from **releasing** behavior, so that if something is wrong, fewer people meet it and the reversal is a switch rather than a rebuild.

This changes what QA is asked for. The question stops being "is it perfect?" and becomes "is it safe to expose to 1% of users while we watch?", which is a far easier question to answer honestly.

| Technique | What it does | What QA validates |
|---|---|---|
| **Feature flag** | Code ships off, switched on separately | That the feature works **off** as well as on, and that switching it off mid-session recovers cleanly |
| **Canary** | A small share of traffic gets the new version first | The comparison signals: error rate, latency, and business metrics for canary versus the rest |
| **Blue-green** | Two full environments, traffic switched between them | That the idle environment is genuinely production-equivalent, and the switch back works |
| **Dark launch** | New code runs on real traffic, output discarded | That the real output matches the old system, without users seeing either |
| **Ring / phased rollout** | Internal users, then a pilot market, then everyone | That each ring has a defined stop condition, not just a schedule |

### What QA must insist on

- **An off switch that was actually tested.** A rollback path nobody has exercised is a plan, not a capability. Test the disable, not only the enable.
- **A stop condition agreed before rollout.** "Error rate above X, or latency p95 above Y, and we stop." Decided in advance, because nobody makes that call well at 23:00 with a graph climbing.
- **A named watcher and a time box.** Progressive rollout with nobody watching is a slow release, not a safe one.
- **Flag cleanup.** Every flag is a branch in behavior and a combination somebody has to test. Flags left behind become permanent, untested configuration. Give each one an expiry.

> **Real world:** most teams reach for feature flags long before they have the monitoring to use them well. A flag without a metric to watch just moves the moment of discovery, it does not shrink the blast radius. Get the signal first.

## 5. Validate production behavior

Post-deploy validation confirms that real systems are healthy after release.

### Recommended post-deploy checks

- Smoke test critical journeys.
- Confirm deployment version.
- Check error logs.
- Review monitoring dashboards.
- Validate API/file/event processing when relevant.
- Confirm expected data is created or transformed correctly.
- Check alerts or support channels for early signals.
- Track known risks during the stabilization window.

> **Principle:** A release is not fully complete until the team confirms that production behavior is healthy.

> **Real world:** many QAs have no production access, especially in regulated or enterprise systems. If you cannot touch prod, partner with Ops, SRE, or on-call to run these checks and share the signals - the validation still has to happen, even if you do not run it yourself.

## 6. Validate a hotfix without a full regression

A production incident is the one moment where the playbook's normal answer - test by risk, take the time it needs - meets a clock. Pretending otherwise is how teams end up abandoning process entirely under pressure, which is exactly when they need it most.

The honest position: a hotfix gets **less** validation than a normal change, deliberately, and the team accepts that trade knowingly rather than quietly.

### The minimum that is never skipped

However urgent it is:

1. **Reproduce the original failure**, so you can prove the fix addresses the real problem and not a plausible-looking one.
2. **Verify the fix on the failing case**, with evidence.
3. **Check the blast radius:** what else calls this code, reads this data, or depends on this behavior. Ten minutes of asking beats a second incident.
4. **Smoke the critical journeys the change could touch.** Not all of them - the ones downstream of the change.
5. **Confirm the rollback path** before deploying, not after.

### What gets deferred, not dropped

Deferred work with no ticket is dropped work with better manners. Before the incident closes, raise:

- the full regression pass the hotfix skipped;
- the automated test that would have caught this;
- the monitoring or alert that should have detected it sooner;
- the root cause fix, if the hotfix was a mitigation rather than a cure.

### Watch the fix, not just the deploy

Hotfixes carry a higher change failure rate than planned releases, because they are written fast, reviewed fast, and tested less. Treat the first hour after one as part of the fix:

- Confirm the original failure signal stops.
- Confirm no new error signature appears.
- Confirm the fix reached every instance, region, or tenant, not only the first one.

> **Principle:** speed is a legitimate trade against coverage. Silence is not. Say out loud what was not tested, and write down what still has to be.

## 7. Create a QA report for leadership visibility

QA reporting should make quality visible without overwhelming stakeholders.

### A strong QA report includes

- Scope tested and not tested
- Release recommendation: Ready / Ready with risk / Not ready
- Key risks and mitigations
- Test execution summary
- Critical defects and current status
- Escaped defects or production concerns when relevant
- Automation and regression coverage for critical flows
- Environment or test data blockers
- User impact and business impact
- Metrics trend and improvement actions

### Recommended format

Use a concise one-page document or short presentation for leadership and a more detailed dashboard for the team.

> **Principle:** Leadership does not need every test step. They need the risk picture, release confidence, business impact, and decisions required.

### Name the lever, not only the risk

A report that raises a risk without saying what would reduce it leaves leadership with a worry and no way to act on it. That is how QA reporting becomes background noise.

For each significant risk, say what it would take: time, a decision, a person, an environment, or an accepted trade-off. Then say what you recommend.

> "Regression on the payments path is manual and takes two days, which is why we cannot release twice a week. Automating the six critical scenarios is roughly one sprint. Recommendation: do it before the Q4 volume, or accept single weekly releases until then."

That is a decision someone can make. "Regression coverage is a risk" is not.

Most of what limits quality is decided above the team - deadlines, staffing, environments, tolerance for technical debt. Reporting is where those decisions get made with the information rather than without it. See [what quality needs from leadership](resources/qa-operating-model.md#2-what-quality-needs-from-leadership).

## 8. Use metrics that drive decisions

Metrics should help the team improve quality, not create blame. Start small: a strong QA metric set covers five complementary signal types, and every metric in it has a target and an agreed action.

> **Rule:** If a metric has no target and no agreed action when it breaches, do not track it.

| Signal type | Starter metric | What it shows | Action when it moves the wrong way |
|---|---|---|---|
| **Outcome** | Escaped defects | What reached users or production | Review risk analysis and regression strategy; when defects trace back to requirements, strengthen refinement and the Definition of Ready |
| **Outcome** | Production incidents | Real stability and operational impact | Run root cause analysis; if incidents repeat in one area, add targeted regression there |
| **Outcome** | Change failure rate | How release quality connects to delivery performance | Strengthen release readiness and post-deploy monitoring |
| **Outcome** | Support ticket trend | Real user friction | Prioritize the user pain points behind the tickets |
| **Delivery health** | Reopened defect rate | Unclear fixes, weak validation, or poor communication | Improve fix validation and acceptance criteria |
| **Delivery health** | Validation cycle time | QA blockers, test data gaps, or environment problems | Review test data, environment stability, and automation opportunities |
| **Automation health** | Critical-flow automation coverage | Whether automation protects what matters most | Automate the highest-risk uncovered flow next |
| **Automation health** | Flaky test rate | Trust in automation results | Stabilize the suite before expanding coverage |
| **Observability** | MTTD / MTTR | How fast the team detects and recovers from issues | Add logs, alerts, correlation IDs, or dashboard visibility |
| **Culture and maturity** | Team QA maturity trend | Whether quality practices improve over time | Build a focused improvement plan with the team |

For a detailed dashboard format, formulas, and data sources, see [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md).

## 9. Avoid vanity metrics

Some metrics look impressive but do not prove quality by themselves. Use these with context:

- total number of test cases;
- raw test coverage percentage;
- number of bugs found by QA;
- number of automated tests;
- number of executed scenarios.

These can be useful only when connected to risk, critical-flow coverage, defect trends, release outcomes, and user impact.

> **Better question:** What decision will this metric help us make?

## 10. Run blame-free post-release reviews

After important releases or incidents, the team should learn without blame.

### Questions to ask

- What happened?
- What was the user or business impact?
- **What did the person on the other end actually experience** - what were they trying to do, what did they see, and what did it cost them in time, work, or trust?
- How was it detected, and did a user find it before we did?
- Could we have detected it earlier?
- Why did our process or tests miss it?
- What small change would prevent a similar issue?
- Do we need a new test, monitor, alert, checklist item, or documentation update?
- Who owns the follow-up action?

### Output

Every review should produce one or more practical improvements.

Examples:

- add an automated regression test;
- improve logs;
- add a contract validation;
- update Definition of Ready;
- improve test data;
- add a monitoring alert;
- clarify ownership.

## After development checklist

- [ ] Regression completed based on risk, and the suite pruned as well as extended.
- [ ] Bug bash run and triaged when the release is big or high-risk.
- [ ] Critical automated tests passing.
- [ ] Release risks documented.
- [ ] Rollout approach chosen, with a stop condition and a named watcher.
- [ ] QA report or release summary prepared when relevant.
- [ ] Production smoke validation planned.
- [ ] Observability checked.
- [ ] Known defects reviewed.
- [ ] Metrics updated.
- [ ] Post-release feedback reviewed.
- [ ] Lessons learned captured.
- [ ] Follow-up actions assigned.

## Key message

> Quality after development is not about proving that QA tested.  
> It is about proving that the team can release, observe, communicate, learn, and improve.

---

**Playbook:** [01 - Before Development](01-before-development.md) · [← 02 - During Development](02-during-development.md) · **03 - After Development**  
[↑ Back to README](README.md)
