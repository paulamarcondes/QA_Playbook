---
name: manual-qa
description: Manual QA and Quality Engineering guidance for test strategy, test cases, bugs, metrics, and reporting
---

# Manual QA Skill

Use this skill for requirements review, test planning, test case design, bug reporting, exploratory testing, execution summaries, and QA reporting.

## Core principles

- Test early, not only at the end.
- Requirements are the contract; they must be testable.
- Risk drives priority.
- Evidence beats opinion.
- Exhaustive testing is impossible.
- Quality is shared across the team.

## Shift-left checklist

Before development starts, check:

- business value is clear;
- user/persona is clear;
- acceptance criteria are testable;
- positive, negative, and edge cases are discussed;
- data rules are documented;
- API or integration contracts are available;
- dependencies are known;
- test data can be created;
- environments are available;
- logs, errors, and monitoring needs are considered;
- automation candidates are identified.

## Test strategy

A test strategy should define:

- scope and out of scope;
- risk assessment;
- test levels;
- test types;
- manual vs automation approach;
- frontend/UX strategy;
- backend/API/integration strategy;
- test data;
- environments;
- entry and exit criteria;
- dependencies;
- reporting approach.

## Test levels

| Level | Purpose |
|---|---|
| Unit / Component | Validates isolated functions, methods, components, or classes. Usually owned by developers. |
| Integration | Validates communication between components, services, APIs, databases, files, or external systems. |
| System | Validates complete system behavior against requirements. |
| Acceptance / UAT | Validates that the solution meets business and user needs. |

## Test types

| Type | Purpose |
|---|---|
| Smoke | Critical path check to confirm a build is testable. |
| Sanity | Narrow check after a fix or small change. |
| Functional | Validates business rules and expected behavior. |
| Regression | Confirms existing behavior still works after change. |
| Exploratory | Time-boxed investigation to discover risks, defects, or unknowns. |
| Usability | Validates ease of use, clarity, consistency, and user friction. |
| Accessibility | Validates keyboard navigation, screen reader support, contrast, labels, and WCAG-related expectations. |
| API | Validates status codes, contracts, payloads, errors, auth, and backward compatibility. |
| Integration | Validates end-to-end data flow and system interactions. |
| Performance | Validates response time, throughput, load, stress, endurance, and scalability. |
| Security | Validates authentication, authorization, injection risks, sensitive data handling, and access control. |
| Compatibility | Validates browser, device, OS, platform, version, and backward/forward compatibility. |
| Recovery/Reliability | Validates resilience, retry, failover, timeout, and recovery behavior. |

## Test design techniques

Use the technique that fits the risk:

- **Equivalence Partitioning:** group inputs into valid and invalid classes.
- **Boundary Value Analysis:** test limits and values just below/above them.
- **Decision Table:** cover combinations of conditions and outcomes.
- **State Transition:** validate state changes and invalid transitions.
- **Use Case Testing:** validate real workflows from the user perspective.
- **Error Guessing:** use experience to target likely failures.
- **Checklist-Based Testing:** use focused checklists for recurring quality concerns.
- **Exploratory Testing:** learn, design, execute, and evaluate in the same time-boxed session.

## Frontend and UX testing

Focus on:

- critical user journeys;
- navigation and flow clarity;
- form validation;
- error messages;
- loading, empty, and failure states;
- responsiveness;
- accessibility basics;
- browser/device coverage;
- visual consistency;
- user friction.

Useful UX lens:

- visibility of system status;
- match between system and real world;
- user control and freedom;
- consistency and standards;
- error prevention;
- recognition rather than recall;
- flexibility and efficiency;
- minimalist design;
- help users recognize and recover from errors;
- help and documentation.

## Backend, API, and integration testing

Focus on:

- contract validation;
- required and optional fields;
- data types and formats;
- authentication and authorization;
- error handling;
- idempotency;
- timeouts and retries;
- data persistence;
- data transformation;
- message/file processing;
- backward compatibility;
- observability and correlation IDs;
- audit and traceability.

## Risk-based testing

Prioritize higher effort when the change impacts:

- revenue, safety, legal, compliance, or reputation;
- critical user journeys;
- data integrity;
- security;
- integrations;
- high-change areas;
- recent incident areas;
- complex logic;
- customer-specific behavior;
- production stability.

Risk assessment format:

```text
Risk: [what can go wrong]
Impact: [business/user/technical impact]
Likelihood: High/Medium/Low
Mitigation: [test, automation, monitoring, documentation, review]
```

## Manual vs automated testing

### Prefer manual testing for

- New or unstable features
- Exploratory testing
- UX/usability validation
- One-time validation
- Ambiguous behavior
- Visual or workflow judgment

### Prefer automation for

- Regression
- Smoke checks
- API and contract validation
- Data validation
- Repetitive scenarios
- Stable critical journeys
- CI/CD quality gates

### Avoid automating

- Unstable requirements
- Rare one-off cases
- Highly visual checks without stable tooling
- Scenarios with excessive maintenance cost

## Test case template

```text
Title: [Feature] TC## - [Scenario]
Objective: [What this test validates]
Requirement: [Story/requirement/reference]
Priority: Critical/High/Medium/Low
Test Type: Functional/API/Integration/Regression/Smoke/etc.
Automation Candidate: Yes/No/Later
Environment: Dev/QA/Staging
Preconditions: [Setup/system state]
Test Data: [Specific data or dataset]
Steps:
1. [Action]
2. [Action]
3. [Action]
Expected Results:
- [Specific measurable result]
- [Data/log/UI/API validation]
Pass/Fail Criteria: [Objective rule]
Notes: [Risks, dependencies, questions]
```

Quality checks:

- Avoid vague steps like "test the feature".
- Expected results must be measurable.
- Include negative and boundary scenarios when relevant.
- Keep scenarios focused and maintainable.
- Link each test to a requirement or risk.

## Bug vs not a bug

A bug is behavior that contradicts:

- requirement;
- acceptance criteria;
- design or contract;
- expected system behavior;
- data integrity rules;
- security expectations;
- accessibility expectations;
- reasonable user expectation for the agreed scope.

Not always a bug:

- missing requirement;
- new enhancement request;
- test data problem;
- environment/configuration issue;
- known limitation;
- out-of-scope behavior;
- duplicate of an existing defect;
- behavior that matches the approved design but creates user friction.

When unsure, classify as:

```text
Potential defect / requirement clarification needed
```

## Bug report template

```text
Title: [Component] Specific defect summary
Summary: [One-line impact]
Environment: [Dev/QA/Staging/Prod read-only]
Build/Version: [Build, commit, release]
User/Role: [If relevant]
Steps to Reproduce:
1. [Step]
2. [Step]
3. [Step]
Expected Result: [Based on requirement]
Actual Result: [Observed behavior]
Impact: [User/business/technical impact]
Severity: Critical/High/Medium/Low
Priority: Critical/High/Medium/Low
Evidence: [Screenshots, logs, network trace, video]
Frequency: Always/Intermittent/Rare
Workaround: [If available]
Related Requirement/Test Case: [Link]
```

## Severity vs priority

- **Severity:** Technical or user impact of the defect.
- **Priority:** Business urgency to fix it.

Examples:

- High severity, low priority: rare crash in unused admin flow.
- Low severity, high priority: public typo in a legally sensitive page.

## Test execution summary

Include:

- scope tested;
- environment and build;
- test cases executed;
- pass/fail/blocked/skipped numbers;
- defects found by severity;
- open risks;
- blockers;
- regression status;
- release recommendation: Ready / Ready with risk / Not ready.

## QA report for leadership

Keep it outcome-focused:

```text
QA Status: Green / Yellow / Red
Release Recommendation: Ready / Ready with risk / Not ready
Scope Tested:
Key Risks:
Customer/User Impact:
Defect Summary:
Regression Status:
Automation/CI Status:
Open Decisions:
Next Actions:
```

## Metrics

Useful metrics:

- requirements covered by tests;
- test execution progress;
- pass/fail/blocked rate;
- defects by severity and priority;
- reopened defects;
- escaped defects;
- defect aging;
- regression pass rate;
- automation stability;
- flaky test rate;
- deployment validation results;
- time to detect and recover from defects.

Use metrics to improve decisions, not to punish people.

## CI/CD quality standards

Common standards:

- unit tests pass;
- static analysis passes;
- critical integration tests pass;
- smoke tests pass;
- no blocker/critical defects open;
- security scan passes when applicable;
- performance thresholds met when applicable;
- deployment validation completed.

## Exploratory testing charter

```text
Charter: Explore [area] to discover [risk/information] using [data/persona/approach].
Time Box: [30/60/90 minutes]
Focus: [risk, workflow, integration, UX, error handling]
Notes:
Defects:
Questions:
Follow-up tests:
```

## Post-release learning

For escaped defects or incidents, ask:

- What happened?
- What was the impact?
- Why did our process not catch it earlier?
- What test, monitor, log, alert, review, or documentation update would prevent recurrence?
- Should this become part of DoR, DoD, regression, or automation?

Use a blame-free tone.
