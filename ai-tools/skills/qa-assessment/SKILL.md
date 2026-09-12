---
name: qa-assessment
description: Scoring rubric for assessing a team's QA maturity against the playbook, with evidence rules, grade bands, and report formats
---

# QA Assessment Skill

The measuring stick. Use this to score a team's real practices against the QA Playbook and turn the result into a grade, a gap list, and an action plan.

Paired with [`qa-assessment.agent.md`](../../agents/qa-assessment.agent.md), which owns the workflow. This file owns the rubric.

## The eight areas

Scored against the [QA Assessment Survey Template](../../../templates/qa-assessment-survey-template.md), so an AI assessment and a team self-assessment produce comparable numbers.

| # | Area | Playbook reference |
|---|---|---|
| 1 | Requirements and refinement | [01 §1-§3, §13](../../../01-before-development.md) |
| 2 | User focus and product quality | [01 §1, §8](../../../01-before-development.md) |
| 3 | Test strategy and coverage | [01 §4-§5](../../../01-before-development.md), [02 §4-§5](../../../02-during-development.md) |
| 4 | Automation and tooling | [01 §9](../../../01-before-development.md), [02 §7](../../../02-during-development.md) |
| 5 | Development collaboration | [02 §1-§3, §9-§13](../../../02-during-development.md) |
| 6 | Environments and test data | [01 §10](../../../01-before-development.md), [02 §6](../../../02-during-development.md) |
| 7 | Observability and release confidence | [03 §1-§4](../../../03-after-development.md) |
| 8 | Metrics and improvement culture | [03 §6-§8](../../../03-after-development.md) |

Equal weight by default. A team may reweight for its context, as long as the weighting is stated in the report.

## Scoring scale

| Score | Meaning | What it takes |
|---:|---|---|
| 1 | Not in place | No evidence the practice exists. |
| 2 | Inconsistent or informal | Happens when someone remembers, depends on individuals. |
| 3 | Defined but not reliable | Documented or agreed, but skipped under pressure. |
| 4 | Working well | Consistently applied, visible in artifacts. |
| 5 | Strong, measured, improved | Applied, measured, and actively refined over time. |

**Half points are not allowed.** Force the decision; a 3 that wants to be a 3.5 is a 3.

## Evidence rules

Non-negotiable. A QA assessment that cannot survive a "how do you know?" is an opinion.

- **Every score cites evidence**: a file path, a ticket key, a pipeline run, a commit, a document link, or a quoted interview answer.
- **No evidence means "Not observed", not 1.** A team can be doing something well that leaves no trace the assessment could reach. Score it `N/O` and list what to ask for.
- **Absence of a document is not absence of a practice.** Verify before scoring down.
- **Never invent a finding, a metric, or a ticket key.** If access was denied or a tool failed, say so in the Coverage section.
- **Distinguish "we have the template" from "we use the template".** A DoR nobody applies scores 2, not 4.
- Prefer three recent examples over one perfect one. Recency beats volume: the last 2-3 sprints reflect how the team works now.

## Grade bands

Total the scored areas, convert to a percentage, then band it.

**Areas scored `N/O` are excluded from the total, not counted as zero:**

```text
grade % = total score / (assessed areas x 5)
```

Always report **coverage** next to the grade: *"68% - Defined, coverage 6 of 8 areas."*

- Below 6 of 8 areas assessed, the grade is **indicative only** and the band must never be quoted without the coverage figure.
- Below 4 of 8, do not publish a grade at all. Report the evidence gaps and what access is needed.

This cuts both ways. It stops a team being punished for access the assessment could not get, and it stops weak areas being quietly parked as "not observed" to lift the percentage. If an area is unscoreable, the report says what was missing and who can provide it.

| Band | Score | % | What it means |
|---|---|---:|---|
| **Optimizing** | 37-40 | 90-100% | Quality is measured and continuously improved. Rare. |
| **Managed** | 30-36 | 75-89% | Practices are consistent and visible. Gaps are known and owned. |
| **Defined** | 24-29 | 60-74% | Practices exist and are agreed, but bend under delivery pressure. |
| **Developing** | 16-23 | 40-59% | Quality depends on individuals rather than the system. |
| **Initial** | 8-15 | 20-39% | Testing happens late, informally, and reactively. |

Score ranges above assume all eight areas were assessed. With fewer, use the percentage.

Report the band and the percentage together. A percentage alone invites false precision; a band alone hides movement between assessments.

> **Never** present the grade as a verdict on people. It describes a system the whole team built, usually under constraints nobody in the room chose.

## Where to look for evidence

CLI and repository access answer most of this faster than asking.

| Area | Signals worth gathering |
|---|---|
| Requirements | Ticket templates, AC in recent stories, DoR checklist use, refinement notes |
| User focus | Accessibility checks, UX review notes, support ticket themes, usability findings |
| Test strategy | Test plans, test case repositories, risk assessments, coverage of critical flows |
| Automation | Test folder structure, test counts by level, CI config, pass and flake rates, run duration |
| Collaboration | PR review comments, QA participation in PRs, unit test presence in diffs, static analysis config |
| Environments | Environment docs, test data setup scripts, fixture or seeding code, blocked-ticket reasons |
| Observability | Logging in critical paths, correlation IDs, dashboards, alert definitions, runbooks |
| Metrics | Escaped defect tracking, incident records, reopened bug rates, retro action follow-through |

> **Read the shape, not just the count.** A repo with 900 UI tests and 40 unit tests is not a 5 in automation. Test distribution reveals strategy more honestly than any document.

## Report format

```text
QA MATURITY ASSESSMENT - [Team / Product] - [Date]

Overall: [XX]% - [Band] · Coverage: [n] of 8 areas
Assessed by: [who] · Sources: [repo, Jira, Confluence, CI, interviews]
Not assessed: [area - what was missing - who can provide it]

SCORES
| # | Area | Score | Band contribution | Evidence |

TOP STRENGTHS (3)
- [Area] [what is genuinely working, with evidence]

TOP GAPS (3, ranked by risk)
- [Area] [gap] -> [risk it creates] -> [smallest fix that moves it]

QUICK WINS (under 2 weeks)
STRUCTURAL WORK (a quarter or more)

RECOMMENDED NEXT ASSESSMENT: [date]
```

## Action plan rules

- **Three improvement actions maximum per cycle.** A plan with fifteen actions is a wish list, and the team will deliver none of them.
- Each action names an owner, a target score change, and a review date.
- Prefer the action that raises the lowest score over the one that perfects the highest.
- Tie every action to the risk it reduces, not to the score it raises. Scores are the proxy, not the goal.
- An action nobody can start this sprint belongs in the structural list, not the quick wins.

## Reassessment

Reassess after 6 to 12 weeks. Report movement per area, not only the overall number, since one area jumping from 2 to 4 while another slips from 4 to 3 nets to zero and hides both stories.

> **Practical reminder:** the grade exists to start a conversation the team can act on. If the report produces defensiveness instead of a next step, the assessment failed regardless of how accurate the number was.
