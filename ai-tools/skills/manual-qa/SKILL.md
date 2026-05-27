---
name: manual-qa
description: Manual QA and Quality Engineering guidance for test strategy, test cases, bugs, metrics, and reporting
---

# Manual QA Skill

Use this skill for requirements review, test planning, test case design, bug reporting, exploratory testing, execution summaries, and QA reporting.

## Core Principles

- Test early, not only at the end.
- Requirements must be testable.
- Risk drives priority.
- User impact matters.
- Evidence beats opinion.
- Testing is context-dependent.
- Exhaustive testing is impossible.
- Quality is shared across the team.

## Shift-Left Checklist

Before development starts, check:

- Business value is clear
- User/persona is clear
- Acceptance criteria are testable
- Positive, negative, and edge cases are discussed
- Data rules are documented
- API or integration contracts are available
- Dependencies are known
- Test data can be created
- Environments are available
- Logs, errors, and monitoring needs are considered
- Automation candidates are identified

## Test Strategy

A test strategy should define:

- Scope and out of scope
- Risk assessment
- Test levels
- Test types
- Manual vs automation approach
- Frontend/UX strategy
- Backend/API/integration strategy
- Test data
- Environments
- Entry and exit criteria
- Dependencies
- Reporting approach

## Test Levels

- **Unit / Component:** Validates isolated functions, methods, components, or classes. Usually owned by developers.
- **Integration:** Validates communication between components, services, APIs, databases, files, or external systems.
- **System:** Validates the complete system behavior against requirements.
- **Acceptance / UAT:** Validates that the solution meets business and user needs.

## Test Types

- **Smoke:** Critical path check to confirm a build is testable.
- **Sanity:** Narrow check after a fix or small change.
- **Functional:** Validates business rules and expected behavior.
- **Regression:** Confirms existing behavior still works after change.
- **Exploratory:** Time-boxed investigation to discover risks, defects, or unknowns.
- **Usability:** Validates ease of use, clarity, consistency, and user friction.
- **Accessibility:** Validates keyboard navigation, screen reader support, contrast, labels, and WCAG-related expectations.
- **API:** Validates status codes, contracts, payloads, errors, auth, and backward compatibility.
- **Integration:** Validates end-to-end data flow and system interactions.
- **Performance:** Validates response time, throughput, load, stress, endurance, and scalability.
- **Security:** Validates authentication, authorization, injection risks, sensitive data handling, and access control.
- **Compatibility:** Validates browser, device, OS, platform, version, and backward/forward compatibility.
- **Recovery/Reliability:** Validates resilience, retry, failover, timeout, and recovery behavior.

## Test Design Techniques

Use the technique that fits the risk:

- **Equivalence Partitioning:** Group inputs into valid and invalid classes.
- **Boundary Value Analysis:** Test limits and values just below/above them.
- **Decision Table:** Cover combinations of conditions and outcomes.
- **State Transition:** Validate state changes and invalid transitions.
- **Use Case Testing:** Validate real workflows from the user perspective.
- **Error Guessing:** Use experience to target likely failures.
- **Checklist-Based Testing:** Use focused checklists for recurring quality concerns.
- **Exploratory Testing:** Learn, design, execute, and evaluate in the same time-boxed session.

## Frontend and UX Testing

Focus on:

- Critical user journeys
- Navigation and flow clarity
- Form validation
- Error messages
- Loading, empty, and failure states
- Responsiveness
- Accessibility basics
- Browser/device coverage
- Visual consistency
- User friction

Useful UX lens:

- Visibility of system status
- Match between system and real world
- User control and freedom
- Consistency and standards
- Error prevention
- Recognition rather than recall
- Flexibility and efficiency
- Minimalist design
- Help users recognize and recover from errors
- Help and documentation

## Backend, API, and Integration Testing

Focus on:

- Contract validation
- Required and optional fields
- Data types and formats
- Authentication and authorization
- Error handling
- Idempotency
- Timeouts and retries
- Data persistence
- Data transformation
- Message/file processing
- Backward compatibility
- Observability and correlation IDs
- Audit and traceability

## Risk-Based Testing

Prioritize higher effort when the change impacts:

- Revenue, safety, legal, compliance, or reputation
- Critical user journeys
- Data integrity
- Security
- Integrations
- High-change areas
- Recent incident areas
- Complex logic
- Customer-specific behavior
- Production stability

Risk assessment format:

```text
Risk: [what can go wrong]
Impact: [business/user/technical impact]
Likelihood: High/Medium/Low
Mitigation: [test, automation, monitoring, documentation, review]
```

## Manual vs Automated Testing

Prefer manual testing for:

- New or unstable features
- Exploratory testing
- UX/usability validation
- One-time validation
- Ambiguous behavior
- Visual or workflow judgment

Prefer automation for:

- Regression
- Smoke checks
- API and contract validation
- Data validation
- Repetitive scenarios
- Stable critical journeys
- CI/CD quality gates

Avoid automating:

- Unstable requirements
- Rare one-off cases
- Highly visual checks without stable tooling
- Scenarios with excessive maintenance cost

## Test Case Template

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

## Bug vs Not a Bug

A bug is behavior that contradicts:

- Requirement
- Acceptance criteria
- Design or contract
- Expected system behavior
- Data integrity rules
- Security expectations
- Accessibility expectations
- Reasonable user expectation for the agreed scope

Not always a bug:

- Missing requirement
- New enhancement request
- Test data problem
- Environment/configuration issue
- Known limitation
- Out-of-scope behavior
- Duplicate of an existing defect
- Behavior that matches the approved design but creates user friction

When unsure, classify as:

```text
Potential defect / requirement clarification needed
```

## Bug Report Template

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
Severity: Blocker/Critical/Major/Minor/Trivial
Priority: Critical/High/Medium/Low
Evidence: [Screenshots, logs, network trace, video]
Frequency: Always/Intermittent/Rare
Workaround: [If available]
Related Requirement/Test Case: [Link]
```

## Severity vs Priority

- **Severity:** Technical or user impact of the defect.
- **Priority:** Business urgency to fix it.

Examples:

- High severity, low priority: Rare crash in unused admin flow.
- Low severity, high priority: Public typo in a legally sensitive page.

## Test Execution Summary

Include:

- Scope tested
- Environment and build
- Test cases executed
- Pass/fail/blocked/skipped numbers
- Defects found by severity
- Open risks
- Blockers
- Regression status
- Recommendation: Go / Conditional Go / No-Go

## QA Report for Leadership

Keep it outcome-focused:

```text
QA Status: Green / Yellow / Red
Release Recommendation: Go / Conditional Go / No-Go
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

- Requirements covered by tests
- Test execution progress
- Pass/fail/blocked rate
- Defects by severity and priority
- Reopened defects
- Escaped defects
- Defect aging
- Regression pass rate
- Automation stability
- Flaky test rate
- Deployment validation results
- Time to detect and recover from defects

Use metrics to improve decisions, not to punish people.

## CI/CD Quality Gates

Common gates:

- Unit tests pass
- Static analysis passes
- Critical integration tests pass
- Smoke tests pass
- No blocker/critical defects open
- Security scan passes when applicable
- Performance thresholds met when applicable
- Deployment validation completed

## Exploratory Testing Charter

```text
Charter: Explore [area] to discover [risk/information] using [data/persona/approach].
Time Box: [30/60/90 minutes]
Focus: [risk, workflow, integration, UX, error handling]
Notes:
Defects:
Questions:
Follow-up tests:
```

## Post-Release Learning

For escaped defects or incidents, ask:

- What happened?
- What was the impact?
- Why did our process not catch it earlier?
- What test, monitor, log, alert, review, or documentation update would prevent recurrence?
- Should this become part of DoR, DoD, regression, or automation?

Use a blame-free tone.
