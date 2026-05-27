# Testing Types Reference

Use this reference to clarify common testing levels, methods, types, and techniques used across the QA Playbook.

This reference is also connected to my original Software Testing QA mind map: [Software Testing QA Mind Map](https://mm.tt/map/3489122534?t=03NPIthAMR).

Testing is not only execution. It includes planning, analysis, design, implementation, execution, monitoring, reporting, and completion.

---

## Testing levels

| Level | What it validates | Typical owner |
|---|---|---|
| Unit / Component Testing | Individual functions, classes, components, validators, calculations, or rules in isolation | Dev |
| Integration Testing | Interactions between components, services, APIs, databases, queues, files, or external systems | Dev / QA |
| System Testing | End-to-end behavior of the complete system or product | QA |
| Acceptance Testing / UAT | Whether the product satisfies business needs and is ready for real use | Business / Product / QA |

---

## Testing methods

| Method | Definition |
|---|---|
| Manual Testing | Human-led validation using judgment, exploration, product understanding, and context. |
| Automated Testing | Programmatic validation of repeatable checks to provide faster and more consistent feedback. |

A mature strategy usually combines both. Manual testing is strong for exploration, usability, and judgment. Automation is strong for regression, APIs, contracts, repetitive checks, and fast feedback.

---

## Functional testing types

| Type | Purpose |
|---|---|
| Functional Testing | Confirms that features behave according to requirements. |
| Smoke Testing | Confirms that the build or deployment is stable enough for deeper testing. |
| Sanity Testing | Quickly validates a specific change, fix, or area. |
| Regression Testing | Confirms that existing behavior still works after changes. |
| System Testing | Validates the complete product behavior. |
| End-to-End Testing | Validates a full workflow across multiple layers or systems. |
| User Acceptance Testing | Confirms real-world business readiness. |
| Exploratory Testing | Simultaneous learning, test design, and execution to discover risks. |

---

## Non-functional testing types

| Type | Purpose |
|---|---|
| Performance Testing | Evaluates response time, throughput, scalability, and stability. |
| Load Testing | Checks behavior under expected or high user/system load. |
| Stress Testing | Pushes the system beyond expected limits to identify breaking points. |
| Volume Testing | Validates behavior with large amounts of data. |
| Scalability Testing | Checks whether the system can grow with demand. |
| Endurance Testing | Validates stability over a long period. |
| Recovery Testing | Checks whether the system can recover after failure. |
| Security Testing | Validates access control, data protection, vulnerabilities, and misuse scenarios. |
| Compatibility Testing | Checks behavior across browsers, devices, operating systems, versions, or platforms. |
| Accessibility Testing | Validates usability for people with different abilities. |
| Usability Testing | Checks whether users can complete tasks clearly, efficiently, and with low friction. |
| Reliability Testing | Evaluates whether the system performs consistently over time. |
| Maintainability Testing | Evaluates whether the system is easy to change, support, and troubleshoot. |

---

## API, backend, and integration-focused testing

| Type | Purpose |
|---|---|
| API Testing | Validates requests, responses, status codes, headers, payloads, authentication, and error handling. |
| Contract Testing | Confirms that providers and consumers respect agreed contracts. |
| Data Validation Testing | Confirms required fields, values, mappings, transformations, persistence, and integrity. |
| Backward Compatibility Testing | Confirms that existing consumers or behaviors still work after a change. |
| Error Handling Testing | Confirms that invalid, missing, duplicate, or failed inputs are handled safely and clearly. |

---

## UI and user-focused testing

| Type | Purpose |
|---|---|
| UI Testing | Validates visible behavior, navigation, fields, buttons, messages, states, and layout. |
| UX Testing | Validates whether the journey is clear, intuitive, useful, and low-friction. |
| Accessibility Testing | Validates keyboard navigation, contrast, screen reader support, labels, and inclusive usage. |
| Cross-Browser Testing | Validates behavior across browsers such as Chrome, Safari, Firefox, or Edge. |
| Cross-Platform Testing | Validates behavior across web, mobile, desktop, or operating systems. |
| Network Testing | Validates behavior under different network conditions, such as Wi-Fi, 5G, 4G, 3G, slow, or unstable connections. |

---

## Test design techniques

| Technique | When to use |
|---|---|
| Equivalence Partitioning | Group inputs into valid and invalid classes to reduce redundant testing. |
| Boundary Value Analysis | Test values at, below, and above limits. |
| Decision Table Testing | Validate combinations of conditions and expected outcomes. |
| State Transition Testing | Validate behavior across states and transitions. |
| Use Case Testing | Validate real user or system workflows. |
| Error Guessing | Use experience to anticipate likely mistakes, failures, and edge cases. |
| Checklist-Based Testing | Use a checklist to guide repeatable validation. |
| Exploratory Testing | Learn and test at the same time using a time-boxed charter. |

---

## Severity and priority

| Concept | Meaning |
|---|---|
| Severity | How serious the technical or user impact is. |
| Priority | How urgently the issue should be fixed. |

Example: A rare crash may have high severity but lower priority if almost no users are affected. A public typo in a critical legal message may have low technical severity but high business priority.

---

## Practical selection guide

| Situation | Good testing focus |
|---|---|
| New critical user flow | Functional, UI/UX, API/integration, regression, accessibility when relevant |
| API or integration change | API, contract, data validation, error handling, backward compatibility |
| Bug fix | Sanity, regression around affected area, root cause validation |
| Release candidate | Smoke, risk-based regression, deployment validation, post-deploy checks |
| Legacy or unstable area | Exploratory, regression, observability, defect history review |
| High data risk | Data validation, transformation checks, reconciliation, negative testing |
| User-facing interface | Usability, accessibility, compatibility, error clarity |

---

## Practical reminder

The goal is not to use every testing type. The goal is to choose the right validation for the risk, user impact, and delivery context.
