# QA SDLC Glossary

A concise glossary of QA, SDLC, testing, delivery, AI, and metrics terms used across this playbook.

The goal is to reduce ambiguity and help teams use the same language when discussing quality, risk, readiness, and release confidence.

## Quick index

- [Core QA and SDLC concepts](#core-qa-and-sdlc-concepts)
- [Requirements and planning](#requirements-and-planning)
- [Risk and strategy](#risk-and-strategy)
- [Testing types and techniques](#testing-types-and-techniques)
- [Test design and data](#test-design-and-data)
- [Development, review, and delivery](#development-review-and-delivery)
- [Observability and production quality](#observability-and-production-quality)
- [Bugs and defects](#bugs-and-defects)
- [Metrics and continuous improvement](#metrics-and-continuous-improvement)
- [AI-assisted QA](#ai-assisted-qa)
- [Team practices, tools, and documentation](#team-practices-tools-and-documentation)

## Core QA and SDLC concepts

| Term | Meaning |
|---|---|
| SDLC | Software Development Life Cycle: planning, building, testing, releasing, and improving software. |
| QA | Quality Assurance: preventing problems, validating behavior, and improving delivery confidence. |
| QC | Quality Control: detecting defects through inspection or testing. |
| Quality Engineering | Quality designed into requirements, architecture, code, tests, releases, observability, and improvement. |
| Quality Mindset | The habit of thinking about risk, user impact, testability, reliability, and maintainability in every phase. |
| Shift-Left Testing | Moving quality activities earlier into discovery, refinement, design, and development. |
| Shift-Right Testing | Validating after release through monitoring, production signals, feedback, logs, and controlled experiments. |
| Quality Standard | A shared expectation that helps the team decide whether work is ready or done. |
| Team Quality Agreement | A shared agreement on how quality will be planned, tested, reviewed, released, and measured. |
| QA as Strategist | A QA role focused on risk analysis, user impact, quality coaching, and release confidence. |

## Requirements and planning

| Term | Meaning |
|---|---|
| Requirement | A documented need, rule, behavior, constraint, or expectation the product must satisfy. |
| User Story | A short description of functionality from the user's perspective. |
| Acceptance Criteria | Conditions that must be true for a story to be accepted as complete. |
| Business Rule | Logic that defines how the product behaves based on policy, workflow, or domain constraints. |
| Functional Requirement | A requirement describing what the system must do. |
| Non-Functional Requirement | A requirement describing how the system should behave, such as security, performance, usability, reliability, or accessibility. |
| IFD | Interface Design Document: describes how systems exchange data, including flows, formats, mappings, and errors. |
| ICD | Interface Control Document: defines the technical contract between systems. |
| Data Contract | An agreement defining expected data structure, fields, formats, versions, and validation rules. |
| Testability | How easy it is to test, observe, isolate, mock, validate, and troubleshoot a feature or system. |
| Traceability | The ability to connect requirements, risks, test cases, bugs, evidence, and release decisions. |
| Definition of Ready | Minimum conditions a story or task must meet before development starts. |
| Definition of Done | Minimum conditions a story or task must meet before it can be considered complete. |
| Three Amigos | Product, Development, and QA aligning on behavior, risks, and examples before implementation. |

## Risk and strategy

| Term | Meaning |
|---|---|
| Risk-Based Testing | Testing effort and depth guided by likelihood and impact of failure. |
| Product Risk | Potential product failure that could harm users, business outcomes, compliance, reliability, or trust. |
| Technical Risk | Potential failure caused by architecture, code, dependencies, integrations, data, or environments. |
| User Impact | The effect a change or issue has on the user's ability to complete a real task. |
| Critical Flow | A user journey, business process, or system workflow that must work reliably because failure has high impact. |
| Golden Path | The single most important successful end-to-end journey through the product. If only one flow could be protected, this is it. Often used as a synonym for the critical path. |
| Happy Path | Any expected successful flow when inputs, dependencies, and conditions are valid. A feature can have several happy paths; it usually has one golden path. |
| Negative Scenario | A scenario validating invalid, missing, unavailable, or unexpected conditions. |
| Edge Case | A less common condition that may still cause failure, confusion, data issues, or unexpected behavior. |
| Assumption | Something believed to be true but not yet confirmed. |
| Out of Scope | A behavior, area, or scenario intentionally not covered by the current delivery or test effort. |

## Testing types and techniques

For fuller descriptions, ownership, and a practical selection guide, see the [Testing Types Reference](testing-types.md).

| Term | Meaning |
|---|---|
| Test Scenario | A high-level situation or behavior that needs validation. |
| Test Case | Plain-text documentation describing what to validate, conditions, expected results, and evidence. |
| Test Suite | A group of related test cases or automated tests. |
| Manual Testing | Human-led validation using judgment, exploration, domain knowledge, and product understanding. |
| Automated Testing | Programmatic validation that runs repeatable checks and provides faster feedback. |
| Exploratory Testing | Learning, test design, and execution happening together to discover risks. |
| Regression Testing | Testing to ensure existing behavior still works after changes. |
| Smoke Testing | A small set of high-value checks that confirms a build or deployment is stable enough for deeper validation. |
| Sanity Testing | A focused check to confirm a specific fix or change behaves as expected. |
| API Testing | Validation of APIs, including requests, responses, status codes, headers, payloads, errors, and contracts. |
| Integration Testing | Testing how components, services, systems, or external dependencies work together. |
| End-to-End Testing | Testing a complete workflow across multiple layers or systems. |
| Contract Testing | Testing whether a service or integration respects an agreed request/response or data contract. |
| UAT | User Acceptance Testing: business validation that the product meets real-world needs. |
| Accessibility Testing | Testing whether people with different abilities can use the product effectively. |
| Usability Testing | Testing whether users can complete tasks clearly, easily, and with low friction. |
| Performance Testing | Testing responsiveness, throughput, scalability, and stability. |
| Security Testing | Testing vulnerabilities, access control, data exposure, and misuse scenarios. |

## Test design and data

| Term | Meaning |
|---|---|
| Test Data | Data used to execute tests, such as users, records, files, payloads, or configurations. |
| Test Environment | The environment where testing happens, such as local, QA, staging, UAT, or production-like environments. |
| Mock | A controlled replacement for a dependency used to simulate behavior. |
| Stub | A simple implementation used to return predefined responses during testing. |
| Fixture | Reusable test data, configuration, or setup needed before a test runs. |
| Precondition | Something that must be true before a test or validation can start. |
| Expected Result | The behavior, output, data, or state expected after a test action. |
| Actual Result | The behavior, output, data, or state observed during execution. |
| Evidence | Proof of validation, such as screenshots, logs, payloads, files, videos, reports, or query results. |
| Automation Candidate | A scenario worth automating because it is critical, repetitive, stable, valuable, or expensive to test manually. |
| Flaky Test | A test that sometimes passes and sometimes fails without a real product change. |
| False Positive | A test failure that does not represent a real product issue. |
| False Negative | A test pass that hides a real product issue. |

## Development, review, and delivery

| Term | Meaning |
|---|---|
| Pull Request | A request to merge code changes into a branch after review. |
| Code Review | Review of code changes for correctness, maintainability, readability, security, test coverage, and risk. |
| CI | Continuous Integration: frequently merging and automatically validating code changes. |
| CD | Continuous Delivery or Continuous Deployment: automating release preparation or deployment. |
| Pipeline | An automated workflow that builds, tests, packages, deploys, or validates software. |
| Build | A packaged version of software created from source code and dependencies. |
| Artifact | A generated output from a build or process, such as a package, report, log, binary, or deployment file. |
| Deployment | Installing or applying a build or change to an environment. |
| Release | Making functionality available to users or customers. |
| Feature Flag | A switch used to enable or disable functionality without redeploying code. |
| Rollback | Returning the system to a previous stable version or state. |
| Hotfix | A fast targeted fix for a high-priority issue. |
| Change Freeze | A period when changes are restricted to reduce release or operational risk. |
| Go / No-Go Decision | A release decision based on readiness, risk, validation results, blockers, and stakeholder alignment. |

## Observability and production quality

| Term | Meaning |
|---|---|
| Observability | Understanding system behavior using logs, metrics, traces, alerts, and dashboards. |
| Logging | Recording useful system events, errors, and context to support debugging and monitoring. |
| Metric | A numerical signal used to understand behavior, delivery performance, or quality trends. |
| Trace | A record of a request or workflow as it moves across services or components. |
| Alert | A notification triggered when a defined condition suggests a problem or risk. |
| Monitoring | Watching system signals to detect issues, trends, failures, and degradation. |
| Correlation ID | A unique identifier used to trace the same transaction or request across systems. |
| Production Validation | Post-deployment checks that confirm critical workflows and system signals are healthy. |
| Incident | An unplanned event that affects users, systems, data, reliability, security, or operations. |
| RCA | Root Cause Analysis: investigation to understand why an issue happened and how to prevent recurrence. |
| Blameless Postmortem | A learning-focused incident review focused on systems, gaps, and improvements. |
| Action Item | A follow-up task created to reduce future risk or improve quality. |

## Bugs and defects

| Term | Meaning |
|---|---|
| Bug | Product behavior that does not match requirements, expectations, contracts, or user needs. |
| Defect | Another term for a bug, often used in formal quality processes. |
| Defect Leakage | Defects found after the phase where they should ideally have been detected. |
| Escaped Defect | A defect that reaches production or customers. |
| Severity | How serious the impact of a defect is. |
| Priority | How urgently the defect should be fixed. |
| Blocker | An issue that prevents progress, testing, deployment, or user completion of a critical flow. |
| Reopened Bug | A bug marked resolved that failed validation or returned later. |
| Workaround | A temporary way to avoid or reduce impact without fully fixing an issue. |
| Known Issue | A documented issue accepted temporarily, usually with impact, workaround, and follow-up tracked. |

## Metrics and continuous improvement

| Term | Meaning |
|---|---|
| QA Metric | A signal that helps the team understand quality, risk, delivery health, or improvement opportunities. |
| Leading Indicator | A metric that helps predict future quality or delivery risk. |
| Lagging Indicator | A metric that measures outcomes after they happen. |
| Deployment Frequency | How often the team successfully deploys changes. |
| Lead Time for Changes | How long it takes for a change to move from code committed to running in production. |
| Change Failure Rate | Percentage of changes that cause incidents, rollbacks, hotfixes, or degraded service. |
| MTTR | Mean Time to Restore: average time needed to recover after a production issue. |
| MTTD | Mean Time to Detect: average time needed to identify that an issue is happening. |
| Defect Density | Number of defects relative to size, scope, module, story count, or another baseline. |
| Defect Aging | How long defects remain open before being resolved. |
| Rework | Extra work caused by unclear requirements, defects, missed risks, poor implementation, or incomplete validation. |
| Automation Coverage | Portion of important scenarios, flows, contracts, or risks protected by automated tests. |
| Test Execution Status | Progress of test execution: passed, failed, blocked, not run, or skipped. |
| Quality Trend | A pattern over time showing whether quality is improving, stable, or declining. |
| Continuous Improvement | Using feedback, metrics, incidents, and retrospectives to improve product and delivery process. |

For metric tracking, use the [QA Metrics Dashboard Template](../templates/qa-metrics-dashboard-template.md).

## AI-assisted QA

| Term | Meaning |
|---|---|
| AI-Assisted Testing | Using AI to support QA activities such as test ideas, requirement review, log analysis, or risk summaries. |
| Prompt | The instruction or context given to an AI tool to produce a useful response. |
| Human Review | Required validation of AI-generated output by a person with product, technical, and risk context. |
| Hallucination | An AI-generated answer that sounds correct but is inaccurate, unsupported, or invented. |
| AI Guardrail | A rule, review step, or limitation used to reduce risk when using AI. |
| Sensitive Data | Information that should not be exposed to unauthorized tools, people, repositories, or public documentation. |

## Team practices, tools, and documentation

| Term | Meaning |
|---|---|
| QA Guild | A recurring community where QAs share practices, tools, learnings, standards, and improvement ideas. |
| SonarQube | Static analysis platform used to identify code quality, maintainability, security, duplication, and coverage issues. |
| Static Code Analysis | Automated inspection of code without executing it. |
| User Guide | Documentation that helps users understand how to use a feature or workflow. |
| How-to-Test Notes | Technical notes explaining setup, data, environment, expected logs, and troubleshooting tips. |
| QA Report | Concise report communicating scope, results, risks, defects, release recommendation, and improvement actions. |
| QA Assessment Survey | Lightweight survey to understand team quality maturity, culture, tooling, and improvement opportunities. |
| Nielsen Heuristics | Usability principles used to evaluate whether a UI is clear, consistent, recoverable, and easy to use. |
| WCAG | Web Content Accessibility Guidelines: the standard for making digital content usable by people with disabilities (covers perceivable, operable, understandable, and robust content). |
| CLI | Command Line Interface: text-based way to run commands, scripts, tests, searches, and file operations. |
| MCP | Model Context Protocol: a way for AI tools to connect with external systems. |

## Practical reminder

A glossary is not meant to make the process heavier. It is meant to help the team avoid confusion, align faster, and make better quality decisions with shared language.
