# QA Playbook

A practical Quality Engineering playbook for building reliable software **before, during, and after development**.

This repository is a portfolio project that documents how modern QA can support delivery through shift-left practices, risk-based testing, automation, release confidence, AI-assisted workflows, and continuous improvement.

> Quality is not a final checkpoint. It is a system property built through clear requirements, technical collaboration, smart testing, user focus, and measurable learning.

---

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

---

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

---

## Playbook structure

### Core guides

- **[01 - Before Development](01-before-development.md)**  
  Build quality into requirements, risks, contracts, testability, tool decisions, user focus, and early test design.

- **[02 - During Development](02-during-development.md)**  
  Collaborate with developers, validate continuously, review quality signals, support PR review, and automate smartly.

- **[03 - After Development](03-after-development.md)**  
  Measure release confidence, production quality, leadership visibility, post-release learning, and continuous improvement.

### Resources

- **[Testing Types Reference](resources/testing-types.md)**  
  Clarifies testing levels, methods, types, techniques, and practical selection criteria.

- **[QA SDLC Glossary](resources/qa-sdlc-glossary.md)**  
  Defines common QA, SDLC, testing, release, AI, and metrics terms used across the playbook.

- **[Quality Review Checklist](resources/quality-review-checklist.md)**  
  Quick quality questions for refinement, development, PR review, environments, documentation, and release.

- **[Clean Code Review Guide for QA](resources/clean-code-guide.md)**  
  Practical guidance for QAs reviewing code and PRs with a quality, risk, testability, observability, and user-impact mindset.

- **[Unit Testing Guide for QA](resources/unit-test-guide.md)**  
  Concise guidance to help QAs collaborate with developers on unit testing strategy, meaningful coverage, and quality expectations.

### AI tools

- **[AI Tools](ai-tools/README.md)**  
  Reusable AI assistant instructions, agents, and skills for QA workflows.

### Templates

- **[Story / Requirements / Interface Document Template](templates/story-requirements-template.md)**  
  Structure for user stories, requirements, interfaces, contracts, user focus, and testability expectations.

- **[Test Strategy Template](templates/test-strategy-template.md)**  
  Lightweight strategy with risk assessment, test scope, tool/framework choices, automation, observability, and release confidence.

- **[Test Cases Template](templates/test-cases-template.md)**  
  Plain-text test case documentation for manual, exploratory, API, integration, regression, UX, and automation candidate scenarios.

- **[Definition of Ready & Definition of Done Template](templates/definition-of-ready-done-template.md)**  
  Practical DoR/DoD quality gates for stories, tasks, and team working agreements.

- **[QA Assessment Survey Template](templates/qa-assessment-survey-template.md)**  
  Team survey to measure QA maturity, culture, tooling, collaboration, and improvement over time.

- **[Bug Report Template](templates/bug-report-template.md)**  
  Clear and reproducible bug documentation.

- **[Deployment Validation Guide Template](templates/deployment-validation-guide-template.md)**  
  QA-focused guide for release readiness, deployment validation, rollback awareness, and post-deploy monitoring.

- **[QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md)**  
  Metrics model for quality visibility and team decisions.


---

## Recommended use

Use this playbook as:

- a GitHub portfolio project;
- a reference for QA interviews;
- a team working agreement;
- a starting point for QA process improvement;
- a lightweight quality governance model;
- a foundation for AI-assisted QA workflows.

---

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

---

## Author

Created by **Paula Marcondes**  

[Connect with me on LinkedIn](https://www.linkedin.com/in/paulamarcondes/)
