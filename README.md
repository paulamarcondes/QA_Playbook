# QA Playbook

A practical Quality Engineering playbook for building reliable software **before, during, and after development**.

This repository is a portfolio project that documents how modern QA can support delivery through shift-left practices, risk-based testing, automation, release confidence, and continuous improvement.

> Quality is not a final checkpoint. It is a strategy built through clear requirements, technical collaboration, smart testing, and measurable learning.

---

## Why this playbook exists

Modern software teams need more than test execution. They need quality practices that help them:

- prevent defects before implementation starts;
- validate what matters most to users and the business;
- reduce regression and production risk;
- make failures visible, traceable, and actionable;
- use automation and AI responsibly to improve feedback loops;
- learn from releases, incidents, and metrics.

This playbook is intentionally concise and practical. It is designed to be reused by QA Engineers, Developers, Product Owners, Tech Leads, and teams that want to make quality part of the delivery system.

---

## Core principles

1. **Prevention beats detection**  
   The best bug is the one removed during refinement, design, or code review.

2. **Risk drives testing depth**  
   Critical flows, integrations, data transformations, security, payments, permissions, and customer-impacting changes deserve deeper validation.

3. **Quality is a team responsibility**  
   QA leads quality thinking, but Developers, Product, UX, Support, and Engineering leaders all contribute to product confidence.

4. **Automation accelerates feedback**  
   Automated tests should protect critical paths, contracts, integrations, and repetitive checks. Automation is not a goal by itself.

5. **Humans protect context**  
   AI can help generate ideas, analyze logs, summarize requirements, and speed up test design, but human judgment remains essential for product risk, usability, ethics, and real user impact.

6. **Metrics should improve decisions**  
   Good QA metrics reveal risk, bottlenecks, learning opportunities, and product impact. They should never be used to blame people.

---

## Playbook structure

| Phase | Goal | Guide |
|---|---|---|
| Before Development | Build quality into requirements, risks, contracts, and testability | [01 - Before Development](01-before-development.md) |
| During Development | Collaborate with developers, validate continuously, and automate smartly | [02 - During Development](02-during-development.md) |
| After Development | Measure release confidence, production quality, and continuous improvement | [03 - After Development](03-after-development.md) |

---

## Templates

| Template | Purpose |
|---|---|
| [Story / Requirements / Interface Document Template](templates/story-requirements-template.md) | Clean structure for user stories, requirements, interfaces, contracts, and testability expectations |
| [Test Strategy Template](templates/test-strategy-template.md) | Lightweight strategy with risk assessment, test scope, automation, observability, and release confidence |
| [Test Cases Template](templates/test-cases-template.md) | Plain-text test case documentation for manual, exploratory, API, integration, regression, and automation candidate scenarios |
| [Quality Review Checklist](templates/quality-review-checklist.md) | Quick quality questions for refinement, development, and release |
| [Bug Report Template](templates/bug-report-template.md) | Clear and reproducible bug documentation |
| [Deployment Validation Guide Template](templates/deployment-validation-guide-template.md) | QA-focused guide for release readiness, deployment validation, rollback awareness, and post-deploy monitoring |
| [QA Metrics Dashboard Template](templates/qa-metrics-dashboard-template.md) | Metrics model for quality visibility and team decisions |

---

## Recommended use

Use this playbook as:

- a reference for QA interviews;
- a team working agreement;
- a starting point for QA process improvement;
- a QA team assessment;
- a quality governance model.

---

## References and inspiration

This playbook is inspired by modern Quality Engineering practices, shift-left testing, risk-based testing, DevOps, observability, and continuous improvement. Useful references include:

- [DORA Metrics](https://dora.dev/guides/dora-metrics/)
- [Google SRE Book - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [IBM - Shift-left testing](https://www.ibm.com/think/topics/shift-left-testing)
- [ISTQB Glossary](https://glossary.istqb.org/)
- [Atlassian - User Stories](https://www.atlassian.com/agile/project-management/user-stories)

---

## Author

Created by **Paula Marcondes**
