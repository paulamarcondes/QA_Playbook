# QA SDLC Glossary

A concise glossary of QA, SDLC, testing, delivery, and metrics terms used across this playbook.

The goal is to reduce ambiguity and help teams use the same language when discussing quality, risk, readiness, and release confidence.

---

## Core QA & SDLC Concepts

| Term | Simple definition |
|---|---|
| SDLC | Software Development Life Cycle. The full process of planning, building, testing, releasing, and improving software. |
| QA | Quality Assurance. The discipline of preventing problems, validating product behavior, and improving confidence in delivery. |
| QC | Quality Control. Activities focused on detecting defects in a product, usually through inspection or testing. |
| Quality Engineering | A broader approach where quality is designed into requirements, architecture, code, tests, releases, observability, and continuous improvement. |
| Quality Mindset | The habit of thinking about risk, user impact, testability, reliability, and maintainability in every phase of delivery. |
| Shift-Left Testing | Moving quality activities earlier in the SDLC, especially into discovery, refinement, design, and development. |
| Shift-Right Testing | Validating quality after release through monitoring, production signals, feedback, logs, and controlled experiments. |
| Quality Gate | A minimum set of checks that must pass before work moves to the next phase. |
| Team Quality Agreement | A shared team agreement on how quality will be planned, tested, reviewed, released, and measured. |
| QA as Strategist | A QA role focused not only on test execution, but also on risk analysis, user impact, quality coaching, and release confidence. |

---

## Requirements & Planning

| Term | Simple definition |
|---|---|
| Requirement | A documented need, rule, behavior, constraint, or expectation that the product must satisfy. |
| User Story | A short description of functionality from the user's perspective, usually explaining who needs what and why. |
| Acceptance Criteria | Clear conditions that must be true for a story to be accepted as complete. |
| Business Rule | A rule that defines how the product must behave based on business logic, policy, workflow, or domain constraints. |
| Functional Requirement | A requirement describing what the system must do. |
| Non-Functional Requirement | A requirement describing how the system should behave, such as performance, security, usability, reliability, or accessibility. |
| IFD | Interface Design Document. A document describing how systems exchange data, including flows, formats, validations, mappings, and errors. |
| ICD | Interface Control Document. A document defining the technical contract between systems, often including protocols, schemas, fields, versions, and responsibilities. |
| Data Contract | An agreement that defines the expected data structure, required fields, formats, versions, and validation rules exchanged between systems. |
| Testability | How easy it is to test, observe, isolate, mock, validate, and troubleshoot a feature or system. |
| Traceability | The ability to connect requirements, risks, test cases, bugs, evidence, and release decisions. |
| Definition of Ready | The minimum conditions a story or task must meet before development starts. |
| Definition of Done | The minimum conditions a story or task must meet before it can be considered complete. |
| Three Amigos | A collaboration practice where Product, Development, and QA align on requirements, risks, and examples before implementation. |

---

## Risk & Strategy

| Term | Simple definition |
|---|---|
| Risk-Based Testing | A testing approach where effort and depth are guided by the likelihood and impact of failure. |
| Product Risk | The possibility that a product failure could harm users, business outcomes, compliance, reliability, or trust. |
| Technical Risk | The possibility that architecture, code, dependencies, integrations, data, or environments could cause failure. |
| User Impact | The effect a change, issue, or limitation has on the user's ability to complete a real task. |
| Critical Flow | A user journey, business process, or system workflow that must work reliably because failure has high impact. |
| Golden Path | The most important successful end-to-end path that represents expected system behavior. |
| Edge Case | A less common condition that may still cause failure, confusion, data issues, or unexpected behavior. |
| Negative Scenario | A test scenario designed to validate how the system behaves when something is invalid, missing, unavailable, or unexpected. |
| Happy Path | The expected successful flow when all inputs, dependencies, and conditions are valid. |
| Assumption | Something believed to be true but not yet confirmed. Assumptions should be made visible because they create risk. |
| Out of Scope | A behavior, area, or scenario intentionally not covered by the current delivery or test effort. |

---

## Testing Types & Techniques

| Term | Simple definition |
|---|---|
| Test Scenario | A high-level situation or behavior that needs to be validated. |
| Test Case | A plain-text documentation item describing what to validate, under which conditions, with expected results and evidence. |
| Test Suite | A group of related test cases or automated tests. |
| Manual Testing | Human-led validation using judgment, exploration, domain knowledge, and product understanding. |
| Automated Testing | Programmatic validation that runs repeatable checks and provides faster feedback. |
| Exploratory Testing | Simultaneous learning, test design, and execution to discover risks not fully covered by scripted tests. |
| Regression Testing | Testing performed to ensure existing behavior still works after changes. |
| Smoke Testing | A small set of high-value checks that confirms the build or deployment is stable enough for deeper validation. |
| Sanity Testing | A focused check to confirm a specific fix or change behaves as expected. |
| API Testing | Validation of APIs, including requests, responses, status codes, headers, payloads, errors, and contracts. |
| Integration Testing | Testing how components, services, systems, or external dependencies work together. |
| End-to-End Testing | Testing a complete workflow across multiple layers or systems from start to finish. |
| Contract Testing | Testing whether a service or integration respects an agreed request/response or data contract. |
| UAT | User Acceptance Testing. Validation by business users or stakeholders to confirm the product meets real-world needs. |
| Accessibility Testing | Testing whether people with different abilities can use the product effectively. |
| Usability Testing | Testing whether users can complete tasks easily, clearly, and with low friction. |
| Performance Testing | Testing responsiveness, throughput, scalability, and stability under expected or stress conditions. |
| Security Testing | Testing for vulnerabilities, access control issues, data exposure, and misuse scenarios. |

---

## Test Design & Data

| Term | Simple definition |
|---|---|
| Test Data | Data used to execute tests, such as users, records, files, payloads, configurations, or database values. |
| Test Environment | The environment where testing happens, such as local, QA, staging, UAT, or production-like environments. |
| Mock | A controlled replacement for a dependency used to simulate specific behavior. |
| Stub | A simple implementation used to return predefined responses during testing. |
| Fixture | A reusable set of test data, configuration, or setup needed before a test runs. |
| Precondition | Something that must be true before a test or validation can start. |
| Expected Result | The behavior, output, data, or system state expected after a test action. |
| Actual Result | The behavior, output, data, or system state observed during test execution. |
| Evidence | Proof of validation, such as screenshots, logs, payloads, files, videos, test reports, or query results. |
| Automation Candidate | A scenario worth automating because it is critical, repetitive, stable, valuable, or expensive to test manually. |
| Flaky Test | A test that sometimes passes and sometimes fails without a real product change. |
| False Positive | A test failure that does not represent a real product issue. |
| False Negative | A test pass that hides a real product issue. |

---

## Development, Review & Delivery

| Term | Simple definition |
|---|---|
| Pull Request | A request to merge code changes into a branch after review. |
| Code Review | A review of code changes for correctness, maintainability, readability, security, test coverage, and risk. |
| CI | Continuous Integration. A practice where code changes are frequently merged and automatically validated. |
| CD | Continuous Delivery or Continuous Deployment. A practice that automates release preparation or production deployment. |
| Pipeline | An automated workflow that builds, tests, packages, deploys, or validates software. |
| Build | A packaged version of the software created from source code and dependencies. |
| Artifact | A generated output from a build or process, such as a package, report, log, binary, or deployment file. |
| Deployment | The process of installing or applying a build or change to an environment. |
| Release | Making functionality available to users or customers. A release may include one or more deployments. |
| Feature Flag | A configuration switch used to enable or disable functionality without redeploying code. |
| Rollback | Returning the system to a previous stable version or state after a release problem. |
| Hotfix | A fast, targeted fix for a high-priority issue, often released outside the normal delivery cycle. |
| Change Freeze | A period when changes are restricted to reduce release or operational risk. |
| Go / No-Go Decision | A release decision based on readiness, risk, validation results, blockers, and stakeholder alignment. |

---

## Observability & Production Quality

| Term | Simple definition |
|---|---|
| Observability | The ability to understand system behavior using logs, metrics, traces, alerts, and dashboards. |
| Logging | Recording useful system events, errors, and context to support debugging and monitoring. |
| Metric | A numerical signal used to understand system behavior, delivery performance, or quality trends. |
| Trace | A record of a request or workflow as it moves across services or components. |
| Alert | A notification triggered when a defined condition suggests a problem or risk. |
| Monitoring | Watching system signals to detect issues, trends, failures, and degradation. |
| Correlation ID | A unique identifier used to trace the same transaction or request across systems. |
| Production Validation | Post-deployment checks that confirm critical workflows and system signals are healthy in production. |
| Incident | An unplanned event that affects users, systems, data, reliability, security, or operations. |
| RCA | Root Cause Analysis. A structured investigation to understand why an issue happened and how to prevent recurrence. |
| Blameless Postmortem | A learning-focused review of an incident that focuses on systems, gaps, and improvements instead of blaming people. |
| Action Item | A specific follow-up task created to reduce future risk or improve quality after a finding or incident. |

---

## Bugs & Defects

| Term | Simple definition |
|---|---|
| Bug | A product behavior that does not match requirements, expectations, contracts, or user needs. |
| Defect | Another term for a bug, often used in formal quality processes. |
| Defect Leakage | Defects found after the phase where they should ideally have been detected. |
| Escaped Defect | A defect that reaches production or customers. |
| Severity | How serious the impact of a defect is. |
| Priority | How urgently the defect should be fixed. |
| Blocker | An issue that prevents progress, testing, deployment, or user completion of a critical flow. |
| Reopened Bug | A bug that was marked resolved but failed validation or returned later. |
| Workaround | A temporary way to avoid or reduce the impact of an issue without fully fixing it. |
| Known Issue | A documented issue that is accepted temporarily, usually with impact, workaround, and follow-up tracked. |

---

## Metrics & Continuous Improvement

| Term | Simple definition |
|---|---|
| QA Metric | A signal that helps the team understand quality, risk, delivery health, or improvement opportunities. |
| Leading Indicator | A metric that helps predict future quality or delivery risk before problems occur. |
| Lagging Indicator | A metric that measures outcomes after they happen, such as production bugs or incidents. |
| Deployment Frequency | How often the team successfully deploys changes. |
| Lead Time for Changes | How long it takes for a change to move from code committed to running in production. |
| Change Failure Rate | The percentage of changes that cause incidents, rollbacks, hotfixes, or degraded service. |
| MTTR | Mean Time to Restore. The average time needed to recover after a production issue. |
| Defect Density | Number of defects relative to size, scope, module, story count, or another baseline. |
| Defect Aging | How long defects remain open before being resolved. |
| Rework | Extra work caused by unclear requirements, defects, missed risks, poor implementation, or incomplete validation. |
| Automation Coverage | The portion of important scenarios, flows, contracts, or risks protected by automated tests. |
| Test Execution Status | Current progress of test execution, usually shown as passed, failed, blocked, not run, or skipped. |
| Quality Trend | A pattern over time that shows whether quality is improving, stable, or declining. |
| Continuous Improvement | The habit of using feedback, metrics, incidents, and retrospectives to improve the product and delivery process. |

---

## AI-Assisted QA

| Term | Simple definition |
|---|---|
| AI-Assisted Testing | Using AI to support QA activities such as brainstorming scenarios, reviewing requirements, generating test ideas, analyzing logs, or summarizing risks. |
| Prompt | The instruction or context given to an AI tool to produce a useful response. |
| Human Review | The required validation of AI-generated output by a person with product, technical, and risk context. |
| Hallucination | An AI-generated answer that sounds correct but is inaccurate, unsupported, or invented. |
| AI Guardrail | A rule, review step, or limitation used to reduce risk when using AI. |
| Sensitive Data | Information that should not be exposed to unauthorized tools, people, repositories, or public documentation. |

---

## Practical reminder

A glossary is not meant to make the process heavier. It is meant to help the team avoid confusion, align faster, and make better quality decisions with shared language.
