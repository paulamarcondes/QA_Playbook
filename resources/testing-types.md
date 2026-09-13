# Testing Types Reference

Use this reference to clarify common testing levels, methods, types, and techniques used across the QA Playbook.

Companion visual: the author's own [Software Testing QA mind map](https://mm.tt/map/3489122534?t=03NPIthAMR), which maps the same material as a single picture. It is a personal artifact rather than a standard, so treat this page as the source of truth.

> **Key idea:** Testing is not only execution. It includes planning, analysis, design, implementation, execution, monitoring, reporting, and completion.

> **Dijkstra:** "Program testing can be used to show the presence of bugs, but never to show their absence." This is why QA prioritizes by risk instead of chasing exhaustive coverage. Source: [Notes on Structured Programming, EWD249 (1970)](https://en.wikiquote.org/wiki/Edsger_W._Dijkstra).

## Seven testing principles (ISTQB)

1. Testing shows the presence of defects, not their absence.
2. Exhaustive testing is impossible - guide effort with risk and priorities.
3. Early testing saves time and money (shift-left).
4. Defects cluster - a few areas usually hold most of them.
5. Pesticide paradox - repeated tests stop finding new bugs; vary and refresh them.
6. Testing is context-dependent.
7. Absence-of-errors fallacy - a defect-free build can still fail user needs.

Reference: [ISTQB Glossary](https://glossary.istqb.org/).

## Verification vs validation

Two words used interchangeably in daily conversation that mean different things, and QA needs both.

| | Verification | Validation |
|---|---|---|
| The question | Are we building the product **right**? | Are we building the **right** product? |
| Checks against | Spec, contract, design, standard, acceptance criteria | Real user **value**: the user need, the business outcome, actual use |
| Typical activities | Requirement and design review, static analysis, unit and component tests, contract tests, PR review | Exploratory testing, usability and accessibility testing, UAT, bug bash, production behavior and user feedback |
| It fails when | The build does not match what was agreed | The build matches what was agreed, and what was agreed was wrong |

A feature can pass every verification check and still fail validation. That is the absence-of-errors fallacy (principle 7 above) in practice: a defect-free build that solves the wrong problem.

Across this playbook, the two run in parallel rather than in sequence:

| Phase | Verification | Validation |
|---|---|---|
| [01 - Before](../01-before-development.md) | Contracts, testability, acceptance criteria that can be checked | User value, user journey, the problem actually worth solving |
| [02 - During](../02-during-development.md) | PR review, unit/API/contract tests, static analysis | Exploratory testing, UX and error clarity, does the flow make sense |
| [03 - After](../03-after-development.md) | Regression, release readiness gate, smoke tests | Bug bash, production behavior, support signals, user feedback |

> **Practical reminder:** Verification is mostly answerable from documents and code. Validation usually requires a human using the product the way a real person would.

## Testing levels

| Level | Purpose | Typical ownership |
|---|---|---|
| Unit / Component Testing | Validates functions, classes, components, validators, calculations, or rules in isolation. | Developers |
| Integration Testing | Validates interactions between components, services, APIs, databases, queues, files, or external systems. | Developers + QA |
| System Testing | Validates end-to-end behavior of the complete system or product. | QA |
| Acceptance Testing / UAT | Validates whether the product satisfies business needs and is ready for real use. | Business + Product + QA |

## Testing methods

| Method | Best for |
|---|---|
| Manual Testing | Human judgment, exploration, usability, product understanding, and context. |
| Automated Testing | Repeatable checks, regression, APIs, contracts, critical paths, and fast feedback. |

A mature strategy usually combines both. Manual testing is strong for exploration, usability, and judgment. Automation is strong for regression, APIs, contracts, repetitive checks, and fast feedback.

## Functional testing types

| Type | Purpose |
|---|---|
| Functional Testing | Confirms that features behave according to requirements. |
| Smoke Testing | Confirms that a build or deployment is stable enough for deeper testing. |
| Sanity Testing | Quickly validates a specific change, fix, or area. |
| Regression Testing | Confirms that existing behavior still works after changes. |
| System Testing | Validates complete product behavior. |
| End-to-End Testing | Validates a full workflow across multiple layers or systems. |
| User Acceptance Testing | Confirms real-world business readiness. |
| Exploratory Testing | Combines learning, test design, and execution to discover risks scripted tests may miss. |

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
| Accessibility Testing | Validates usability for people with different abilities, against the Web Content Accessibility Guidelines (WCAG). |
| Usability Testing | Checks whether users can complete tasks clearly, efficiently, and with low friction. |
| Reliability Testing | Evaluates whether the system performs consistently over time. |
| Maintainability Testing | Evaluates whether the system is easy to change, support, and troubleshoot. |

## API, backend, and integration-focused testing

| Type | Purpose |
|---|---|
| API Testing | Validates requests, responses, status codes, headers, payloads, authentication, and error handling. |
| Contract Testing | Confirms that providers and consumers respect agreed contracts. |
| Data Validation Testing | Confirms required fields, values, mappings, transformations, persistence, and integrity. |
| Backward Compatibility Testing | Confirms that existing consumers or behaviors still work after a change. |
| Error Handling Testing | Confirms that invalid, missing, duplicate, or failed inputs are handled safely and clearly. |

## UI and user-focused testing

| Type | Purpose |
|---|---|
| UI Testing | Validates visible behavior, navigation, fields, buttons, messages, states, and layout. |
| UX Testing | Validates whether the journey is clear, intuitive, useful, and low-friction. |
| Accessibility Testing | Validates keyboard navigation, contrast, screen reader support, labels, and inclusive usage. |
| Cross-Browser Testing | Validates behavior across browsers such as Chrome, Safari, Firefox, or Edge. |
| Cross-Platform Testing | Validates behavior across web, mobile, desktop, or operating systems. |
| Network Testing | Validates behavior under Wi-Fi, 5G, 4G, 3G, slow, or unstable network conditions. |

> **Mobile:** native and hybrid mobile apps add risks this playbook does not cover in depth - app store review and staged rollout, OS version fragmentation, device permissions, background and offline behavior, battery and data usage, push notifications, and the fact that users can decline an update indefinitely, so several versions of your app run at once. Treat the practices here as the base and add mobile-specific coverage on top.

## Test design techniques

| Technique | Use when |
|---|---|
| Equivalence Partitioning | Inputs can be grouped into valid and invalid classes. |
| Boundary Value Analysis | Values have limits, ranges, minimums, or maximums. |
| Decision Table Testing | Multiple conditions combine into different outcomes. |
| State Transition Testing | Behavior depends on states and transitions. |
| Use Case Testing | Real user or system workflows need validation. |
| Error Guessing | Experience suggests likely failures or edge cases. |
| Checklist-Based Testing | A focused list can guide repeatable validation. |
| Exploratory Testing | The team needs to learn and test at the same time using a time-boxed charter. |

## Severity and priority

| Term | Meaning |
|---|---|
| Severity | How much damage the defect does. Critical / High / Medium / Low. |
| Priority | How soon it gets fixed. Critical / High / Medium / Low. |

They move independently. Data loss in a deprecated admin tool two people still use is high severity but low priority. A typo on a legally sensitive public page is low severity but high priority. For the full four-corner view, see [02 - Severity vs priority](../02-during-development.md#severity-vs-priority).

## Practical selection guide

Use the risk and context to choose the right validation approach.

| Context | Useful validation |
|---|---|
| New critical user flow | Functional, UI/UX, API/integration, regression, accessibility when relevant. |
| API or integration change | API, contract, data validation, error handling, backward compatibility. |
| Bug fix | Sanity, regression around affected area, root cause validation. |
| Release candidate | Smoke, risk-based regression, deployment validation, post-deploy checks. |
| Legacy or unstable area | Exploratory, regression, observability, defect history review. |
| High data risk | Data validation, transformation checks, reconciliation, negative testing. |
| User-facing interface | Usability, accessibility, compatibility, error clarity. |

## Practical reminder

The goal is not to use every testing type. The goal is to choose the right validation for the risk, user impact, and delivery context.
