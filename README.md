# QA Playbook

A practical Quality Engineering playbook for building reliable software **before, during, and after development**.

This repository is a portfolio project that documents how modern QA can support delivery through shift-left practices, risk-based testing, automation, release confidence, AI-assisted workflows, and continuous improvement.

> **Key idea:** Quality is not a final checkpoint. It is a system property built through clear requirements, technical collaboration, smart testing, user focus, and measurable learning.

## Why this playbook exists

Modern software teams need more than test execution. They need quality practices that help them:

- prevent defects before implementation starts;
- validate what matters most to users and the business;
- reduce regression and production risk;
- make failures visible, traceable, and actionable;
- choose the right test strategy, tools, and automation approach;
- use AI responsibly to improve feedback loops;
- learn from releases, incidents, metrics, and team maturity signals.

This playbook is intentionally concise and practical. It is designed to be reused by QA Engineers, Developers, Product Owners, Tech Leads, and teams that want to make quality part of the delivery system.

## Quick navigation

| Section | Purpose |
|---|---|
| [01 - Before Development](01-before-development.md) | Build quality into requirements, risks, contracts, testability, user focus, and early test design. |
| [02 - During Development](02-during-development.md) | Validate continuously, review technical quality signals, support PR review, and automate smartly. |
| [03 - After Development](03-after-development.md) | Measure release confidence, production quality, post-release learning, and continuous improvement. |
| [Resources](resources/) | Practical QA references for testing, clean code, unit testing, glossary, and review checklists. |
| [Templates](templates/) | Reusable templates for stories, strategy, test cases, bugs, DoR/DoD, deployment, metrics, and maturity assessment. |
| [AI Tools](ai-tools/) | Reusable AI instructions, agents, and skills for QA workflows. |

## Core principles

1. **Prevention beats detection**  
   The best bug is the one removed during refinement, design, or code review.

2. **User value drives quality**  
   A technically correct feature still fails if users cannot complete the journey with clarity, trust, and low friction.

3. **Risk drives testing depth**  
   Critical flows, integrations, data transformations, security, payments, permissions, and customer-impacting changes deserve deeper validation.

4. **Quality is a team responsibility**  
   QA leads quality thinking, but Developers, Product, UX, Support, and Engineering leaders all contribute to product confidence.

5. **Automation accelerates feedback**  
   Automated tests should protect critical paths, contracts, integrations, and repetitive checks. Automation is not a goal by itself.

6. **Humans protect context**  
   AI can help generate ideas, analyze logs, summarize requirements, and speed up test design, but human judgment remains essential for product risk, usability, ethics, and real user impact.

7. **Metrics should improve decisions**  
   Good QA metrics reveal risk, bottlenecks, learning opportunities, and product impact. They should never be used to blame people.

## Playbook structure

### Core guides

| Guide | Focus |
|---|---|
| [01 - Before Development](01-before-development.md) | Quality planning, risk prevention, contracts, testability, tool decisions, and early scenarios. |
| [02 - During Development](02-during-development.md) | Collaboration, PR review, technical signals, test design, execution, evidence, and bug reporting. |
| [03 - After Development](03-after-development.md) | Release confidence, metrics, production validation, reporting, and learning. |

### Resources

| Resource | Purpose |
|---|---|
| [Testing Types Reference](resources/testing-types.md) | Testing levels, types, techniques, and practical selection guidance. |
| [QA SDLC Glossary](resources/qa-sdlc-glossary.md) | Shared terminology for QA, SDLC, testing, delivery, AI, and metrics. |
| [Quality Review Checklist](resources/quality-review-checklist.md) | Outcome-based quality questions for refinement, development, PRs, bugs, and releases. |
| [Clean Code Review Guide for QA](resources/clean-code-guide.md) | How QA can review code and PRs from a risk, testability, and observability perspective. |
| [Unit Testing Guide for QA](resources/unit-test-guide.md) | How QA can collaborate with developers on meaningful unit testing strategy. |

### Templates

| Template | Purpose |
|---|---|
| [Story / Requirements / Interface Template](templates/story-requirements-template.md) | Structure for clear, testable, user-focused requirements and contracts. |
| [Test Strategy Template](templates/test-strategy-template.md) | Risk assessment, scope, approach, tools, automation, observability, and release confidence. |
| [Test Cases Template](templates/test-cases-template.md) | Plain-text scenario documentation for manual, exploratory, API, integration, regression, and automation candidate scenarios. |
| [DoR / DoD Template](templates/definition-of-ready-done-template.md) | Practical quality standards for readiness and completion. |
| [QA Assessment Survey Template](templates/qa-assessment-survey-template.md) | Team survey for quality maturity, collaboration, tooling, and improvement. |
| [Bug Report Template](templates/bug-report-template.md) | Clear defect documentation focused on reproduction, impact, evidence, and technical context. |
| [Deployment Validation Template](templates/deployment-validation-guide-template.md) | Release readiness, validation, rollback awareness, monitoring, and post-release learning. |
| [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) | Quality visibility model for trends, risks, bottlenecks, and decisions. |

### AI tools

| File | Purpose |
|---|---|
| [AI Tools README](ai-tools/README.md) | Navigation and usage guidance for the AI tools folder. |
| [BASICS.instructions.md](ai-tools/BASICS.instructions.md) | Always-on QA context and AI safety rules. |
| [Manual QA Agent](ai-tools/agents/manual-qa.agent.md) | End-to-end QA workflow agent behavior. |
| [Manual QA Skill](ai-tools/skills/manual-qa/SKILL.md) | QA knowledge base for planning, tests, bugs, reporting, and metrics. |
| [Robot QA Skill](ai-tools/skills/robot-qa/SKILL.md) | Robot Framework automation guidance. |

## Recommended use

Use this playbook as:

- a GitHub portfolio project;
- a reference for QA interviews;
- a team working agreement;
- a starting point for QA process improvement;
- a lightweight quality governance model;
- a foundation for AI-assisted QA workflows.

## References and inspiration

This playbook is inspired by modern Quality Engineering practices, shift-left testing, risk-based testing, DevOps, usability heuristics, AI-assisted QA, and continuous improvement.

Useful references include:

- [DORA Metrics](https://dora.dev/guides/dora-metrics/)
- [Google SRE Book - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [IBM - Shift-left testing](https://www.ibm.com/think/topics/shift-left-testing)
- [ISTQB Glossary](https://glossary.istqb.org/)
- [Atlassian - User Stories](https://www.atlassian.com/agile/project-management/user-stories)
- [Nielsen Heuristics Workshop](https://youtu.be/OtyM8dGKLUU?si=Fu3HYPjSQG3NDAoG)
- [Software Testing QA Mind Map](https://mm.tt/map/3489122534?t=03NPIthAMR)

## Author

Created by **Paula Marcondes**  
[Connect with me on LinkedIn](https://www.linkedin.com/in/paulamarcondes/)
