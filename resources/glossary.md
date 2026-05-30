# Glossary

A short glossary for the concepts used across this playbook.

This file avoids basic testing definitions and focuses on terms that help teams make better quality decisions.

---

## Automation value

Automation value means an automated check provides useful, reliable, and maintainable feedback.

Good automation protects critical paths, contracts, integrations, and repetitive regression risks. It should not exist only to increase test count.

Reference: [Testing Guide](testing-guide.md)

---

## Change failure rate

The percentage of deployments that cause production failures, incidents, rollbacks, hotfixes, or degraded service.

This is one of the DORA metrics and should be tracked in the [QA Metrics Dashboard Template](../templates/qa-metrics-dashboard-template.md).

---

## Contract testing

Testing that validates whether a provider and consumer agree on the expected API, event, file, or data structure.

It helps prevent integration failures by checking expectations before or during development.

Reference: [01 - Before Development](../01-before-development.md)

---

## DORA metrics

A set of delivery performance metrics commonly used to understand software delivery health:

- deployment frequency;
- lead time for changes;
- change failure rate;
- time to restore service.

Use the [QA Metrics Dashboard Template](../templates/qa-metrics-dashboard-template.md) as the source of truth for tracking and interpreting these metrics in this playbook.

---

## Escaped defect

A defect found after the expected validation stage, especially after release to production or users.

Escaped defects should be reviewed as learning signals, not only as isolated bugs.

Reference: [03 - After Development](../03-after-development.md)

---

## Human-in-the-loop review

A required human review of AI-generated output before it is used.

It protects against hallucinated requirements, missing context, biased assumptions, weak expected results, and sensitive data exposure.

Reference: [AI Tools](../ai-tools/README.md)

---

## Lead time for changes

The time it takes for a code change to move from commit to production.

This is a DORA metric. Track it in the [QA Metrics Dashboard Template](../templates/qa-metrics-dashboard-template.md).

---

## Observability

The ability to understand what the system is doing through logs, metrics, traces, alerts, IDs, and other signals.

For QA, observability helps confirm whether failures are visible, traceable, and actionable after release.

Reference: [Technical Quality Reference](technical-quality-reference.md)

---

## Release confidence

The team’s evidence-based confidence that a change is ready to release.

It should consider risk, test results, known issues, regression impact, deployment readiness, and monitoring.

Reference: [03 - After Development](../03-after-development.md)

---

## Risk-based testing

A testing approach where testing depth is proportional to product, user, business, technical, or operational risk.

The risk framework should be defined in the [Test Strategy Template](../templates/test-strategy-template.md).

---

## Shift-left testing

The practice of moving quality activities earlier in the delivery process.

Examples include requirement review, contract definition, risk assessment, testability checks, and early technical review before full implementation is complete.

Reference: [01 - Before Development](../01-before-development.md)

---

## Testing in production

Using safe production signals such as monitoring, logs, alerts, feature flags, canary releases, or post-deploy checks to confirm real behavior.

This does not replace pre-release testing. It helps teams detect real issues faster.

Reference: [Deployment Validation Template](../templates/deployment-validation-template.md)
