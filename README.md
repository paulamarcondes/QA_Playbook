# QA Playbook

A practical QA Engineering playbook for building quality before, during, and after software development.

> Quality is not a final checkpoint. It is built through clear requirements, smart risk decisions, technical collaboration, useful automation, and continuous learning.

This repository is intentionally concise and practical. It can be used by junior, mid-level, and senior QAs, as well as developers, product owners, tech leads, and teams that want a shared quality standard.

---

## Why this playbook exists

Modern QA is more than executing test cases. A strong QA practice helps the team:

- prevent defects early;
- understand user and business risk;
- define clear requirements and contracts;
- choose the right testing depth;
- improve release confidence;
- use automation where it brings value;
- use AI responsibly;
- learn from bugs, releases, and production feedback.

---

## Core principles

1. **Prevention beats detection**  
   The best bug is the one removed during refinement, design, code review, or early testing.

2. **User value drives quality**  
   A feature is not successful only because it works technically. Users must be able to complete the journey with clarity, trust, and low friction.

3. **Risk drives testing depth**  
   Critical flows, integrations, data transformations, security, permissions, payments, and customer-impacting changes deserve deeper validation.

4. **Quality is a team responsibility**  
   QA leads quality thinking, but quality depends on Product, Developers, UX, Support, and Engineering leaders.

5. **Automation should improve feedback**  
   Automated tests should protect critical paths, contracts, integrations, and repetitive checks. Automation is not a goal by itself.

6. **Humans protect context**  
   AI can support analysis, test design, log review, and documentation, but human judgment remains responsible for business risk, ethics, usability, and real user impact.

7. **Metrics should improve decisions**  
   Good metrics reveal risks, bottlenecks, learning opportunities, and product impact. They should never be used to blame people.

---

## Playbook structure

### Core workflow guides

| Guide | Purpose |
|---|---|
| [01 - Before Development](01-before-development.md) | Build quality into requirements, risks, contracts, security, accessibility, and testability before coding starts. |
| [02 - During Development](02-during-development.md) | Collaborate during implementation through PR review, unit test discussions, pair testing, observability checks, and smart automation. |
| [03 - After Development](03-after-development.md) | Validate release confidence, deployment readiness, production signals, metrics, and post-release learning. |

### Resources

| Resource | Purpose |
|---|---|
| [Testing Guide](resources/testing-guide.md) | Knowledge base for choosing the right testing approach based on risk, layer, speed, and confidence. |
| [Technical Quality Reference](resources/technical-quality-reference.md) | One place for clean code review, unit testing expectations, PR review, observability, maintainability, and QA-Dev collaboration. |
| [Quality Review Checklist](resources/quality-review-checklist.md) | Outcome-based checklist for refinement, development, release, and improvement. |
| [Glossary](resources/glossary.md) | Short definitions for the most important QA, delivery, AI, and metrics concepts used in this playbook. |

### Templates

| Template | Purpose |
|---|---|
| [Story / Requirements Template](templates/story-requirements-template.md) | Captures user value, requirements, contracts, risk, security, accessibility, and testability. |
| [Test Strategy Template](templates/test-strategy-template.md) | Defines project-level scope, risk, test levels, automation, tools, data, environments, and release confidence. |
| [Test Cases Template](templates/test-cases-template.md) | Supports practical scenario notes and exploratory charters without forcing outdated click-by-click scripts. |
| [Bug Report Template](templates/bug-report-template.md) | Captures reproducibility, technical context, logs, risk, impact, and follow-up learning. |
| [Definition of Ready / Done Template](templates/definition-of-ready-done-template.md) | Defines shared quality standards before work starts and before it is considered done. |
| [Deployment Validation Template](templates/deployment-validation-template.md) | Supports release checks, rollback awareness, monitoring, and post-deploy validation. |
| [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) | Single source for DORA, quality, risk, automation, and improvement metrics. |
| [QA Assessment Survey Template](templates/qa-assessment-survey-template.md) | Helps teams assess QA maturity, collaboration, tooling, and improvement opportunities. |

### AI tools

| File | Purpose |
|---|---|
| [AI Tools](ai-tools/README.md) | Practical guidance for using AI in QA without losing human judgment. |
| [Basic AI Instructions](ai-tools/BASICS.instructions.md) | Reusable base instructions for QA-focused AI assistants. |
| [Manual QA Agent](ai-tools/manual-qa.agent.md) | Agent instructions for manual QA support. |
| [Manual QA Skill](ai-tools/manual-qa/SKILL.md) | Practical skill file for manual QA workflows. |
| [Robot QA Skill](ai-tools/robot-qa/SKILL.md) | Practical skill file for Robot Framework QA workflows. |

---

## How the documents connect

This playbook works as a simple quality loop:

1. **Before development**, define value, risk, contracts, data, security, accessibility, and testability.
2. **During development**, review implementation quality, unit tests, logs, contracts, and automation value.
3. **After development**, validate release confidence, observe production behavior, learn from bugs, and improve the process.
4. **Templates and resources** keep the standards practical and repeatable.

Clear separation:

- The [Testing Guide](resources/testing-guide.md) explains **how to choose testing approaches**.
- The [Test Strategy Template](templates/test-strategy-template.md) defines **what a specific project will use**.
- The [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) is the single place for metric tracking and interpretation.

---

## Recommended use

Use this playbook as:

- a GitHub portfolio project;
- a QA interview reference;
- a team working agreement;
- a starting point for improving QA practices;
- a lightweight quality guide for real delivery teams;
- a foundation for responsible AI-assisted QA workflows.

---

## References and inspiration

This playbook is inspired by Quality Engineering, shift-left testing, risk-based testing, DevOps, usability practices, AI-assisted QA, and continuous improvement.

Useful references:

- [DORA Metrics](https://dora.dev/)
- [Google SRE Book - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [IBM - Shift-left testing](https://www.ibm.com/think/topics/shift-left-testing)
- [Atlassian - User Stories](https://www.atlassian.com/agile/project-management/user-stories)

---

## Author

Created by Paula Marcondes  
[Connect with me on LinkedIn](https://www.linkedin.com/in/paulamarcondes/)
