# Bug Report Template

Use this format to make defects clear, reproducible, and easier to fix.

> **Goal:** A good bug report helps the team understand what failed, why it matters, where to investigate, and what evidence supports the finding.

## Title

```text
[Area] Short description of the problem
```

## Description

Describe the issue in 1-2 sentences.

## Impact

One line: who is affected and what they cannot do. Not "the endpoint returns 500", but "a dispatcher cannot close an incident, so the record stays open in the queue". This line is what severity and priority get argued from.

## Environment

| Field | Value |
|---|---|
| Environment |  |
| Build/version |  |
| Browser/device |  |
| User/role |  |
| Test data |  |
| Affected flow/API/component |  |
| Risk level | Low / Medium / High / Critical |

## Preconditions

The state the system had to be in before step 1: existing records, configuration, feature flags, permissions, prior transactions. The field most often missing from a bug report, and the one that most often blocks reproduction.

## Expected result

What should happen, and which requirement, acceptance criterion, or contract says so.

## Actual result

What actually happened.

## Steps to reproduce

1. [Step]
2. [Step]
3. [Step]

## Severity / Priority suggestion

| Field | Value |
|---|---|
| Severity | Critical / High / Medium / Low |
| Priority | Critical / High / Medium / Low |
| Rationale |  |

## Evidence

Attach or link relevant evidence:

- screenshots or video;
- logs or traces;
- correlation IDs;
- API payloads;
- files;
- database record IDs;
- related test case or automated test result.

## Technical context

| Field | Notes |
|---|---|
| Suspected area |  |
| Related requirement / AC |  |
| Related test case |  |
| Regression? | Yes / No / Unknown |
| Frequency | Always / Intermittent / Rare |
| Workaround |  |

## Follow-up for high-impact bugs

For Critical or High bugs, consider whether the issue should trigger:

- update to the [QA Metrics Dashboard Template](qa-metrics-dashboard-template.md);
- post-release learning in [03 - After Development](../03-after-development.md);
- new regression coverage;
- improved logs, alerts, or monitoring;
- update to Definition of Ready or Definition of Done.
