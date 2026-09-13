---
name: manual-qa
description: Manual QA and Quality Engineering guidance for test strategy, test cases, bugs, metrics, and reporting
---

# Manual QA Skill

Use this skill for requirements review, test planning, test case design, bug reporting, exploratory testing, execution summaries, and QA reporting.

This file holds the **output formats and team standards** an assistant cannot infer. General testing knowledge is deliberately not repeated here.

## Where the knowledge lives

When the playbook is available, read the source rather than guessing:

| Need | Source |
|---|---|
| Testing levels, types, techniques, selection guide | [Testing Types Reference](../../../resources/testing-types.md) |
| Risk levels and test depth | [01 - Map risk before defining test depth](../../../01-before-development.md#4-map-risk-before-defining-test-depth) |
| Which test level for which risk | [02 - Use the right test level](../../../02-during-development.md#4-use-the-right-test-level-for-the-risk) |
| What to automate, pipeline stages, flaky tests | [02 - Automate strategically](../../../02-during-development.md#8-automate-strategically) |
| Bug or not a bug | [02 - Define what is a bug and what is not](../../../02-during-development.md#10-define-what-is-a-bug-and-what-is-not) |
| Accessibility, locale, security, performance, privacy | [Quality Attributes Guide](../../../resources/quality-attributes-guide.md) |
| Metrics worth tracking | [03 - Use metrics that drive decisions](../../../03-after-development.md#8-use-metrics-that-drive-decisions) |

## Core principles

- Test early, not only at the end.
- Requirements are the contract; they must be testable.
- Risk drives priority.
- Evidence beats opinion.
- Exhaustive testing is impossible.
- Quality is shared across the team, and leadership decides how much of it is possible.

## Risk assessment format

```text
Risk: [what can go wrong]
Impact: [business/user/technical impact]
Likelihood: High/Medium/Low
Level: Low/Medium/High/Critical
Mitigation: [test, automation, monitoring, documentation, review]
```

Safety, money, personal data, and regulatory compliance never sit below High, whatever the likelihood.

## Test case template

The compact chat version of the [Test Cases Template](../../../templates/test-cases-template.md). Same fields, written as plain text. When the output goes into a document, use the template; when it goes into a ticket or a chat reply, use this. If the two ever disagree, the template wins.

```text
Title: [Feature] TC## - [Scenario]
Objective: [what this test validates]
Requirement: [story/requirement/reference]
Priority: Critical/High/Medium/Low
Test Type: Functional/API/Integration/Regression/Smoke/etc.
Automation Candidate: Yes/No/Later
Environment: Dev/Staging
Preconditions: [setup/system state]
Test Data: [specific data or dataset]
Steps:
1. [Action]
2. [Action]
3. [Action]
Expected Results:
- [specific measurable result]
- [data/log/UI/API validation]
Pass/Fail Criteria: [objective rule]
Notes: [risks, dependencies, questions]
```

Quality checks:

- No vague steps like "test the feature".
- Expected results must be measurable.
- Include negative and boundary scenarios when relevant.
- Link each test to a requirement or a risk.

## Bug report template

The compact chat version of the [Bug Report Template](../../../templates/bug-report-template.md); the template wins if the two disagree. Preconditions, impact, evidence, and suspected area are the fields most often missing and most often needed.

```text
Title: [Area] Action fails when condition happens
Summary: [one line: who is affected and what they cannot do]
Environment: [Dev / Staging / Production read-only]
Build/Version: [build, commit, or release]
User/Role: [if relevant]
Preconditions: [the state the system had to be in before step 1]
Test Data: [accounts, records, payloads used]
Steps to Reproduce:
1. [Step]
2. [Step]
3. [Step]
Expected Result: [from the requirement, AC, or contract]
Actual Result: [observed behavior]
Impact: [user, business, or technical impact]
Severity: Critical/High/Medium/Low
Priority: Critical/High/Medium/Low
Rationale: [why those two ratings]
Frequency: Always / Intermittent / Rare
Regression: Yes / No / Unknown
Suspected Area: [where to start investigating, if known]
Evidence: [screenshots, logs, correlation IDs, payloads, files]
Workaround: [if available]
Related Requirement / Test Case: [link]
```

When it is unclear whether something is a defect, label it and move on rather than arguing:

```text
Potential defect / requirement clarification needed
```

## Severity vs priority

- **Severity:** how much damage the defect does. Critical / High / Medium / Low.
- **Priority:** how soon it gets fixed. Critical / High / Medium / Low.

They move independently:

- High severity, low priority: data loss in a deprecated admin tool two people still use.
- Low severity, high priority: typo on a legally sensitive public page.

QA proposes severity with evidence. Product owns priority. State who is affected and what they cannot do before proposing either.

## Exploratory testing charter

```text
Charter: Explore [area] with [data/persona/condition] to discover [risk/information].
Time Box: [30/60/90 minutes]
Notes:
Findings:
Questions:
Coverage gaps:
Follow-up tests:
```

## Test execution summary

```text
Scope tested:
Environment and build:
Executed / Passed / Failed / Blocked / Not run:
Defects by severity:
Open risks:
Blockers:
Regression status:
Release recommendation: Ready / Ready with risk / Not ready
```

## QA report for leadership

Outcome-focused. Name the lever next to each risk, not only the risk.

```text
QA Status: Green / Yellow / Red
Release Recommendation: Ready / Ready with risk / Not ready
Scope Tested:
Key Risks: [risk -> what would reduce it -> recommendation]
Customer/User Impact:
Defect Summary:
Regression Status:
Automation/CI Status:
Open Decisions:
Next Actions:
```

## Post-release learning

For escaped defects or incidents, blame-free:

- What happened, and what did the person on the other end experience?
- Why did our process not catch it earlier?
- What test, monitor, log, alert, review, or documentation update would prevent recurrence?
- Should this become part of DoR, DoD, regression, or automation?
- Who owns the follow-up, and by when?
