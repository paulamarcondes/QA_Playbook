# QA Operating Model

How quality work is organized: who owns what, how QA works when the team is spread across time zones or contracts, how a QA joining a team finds out where they have landed, and how QA practice spreads beyond one squad.

The three phase guides describe what happens to *a change*. This page describes what happens to *a team*. Its practices run over weeks and months, not per story.

> **Key idea:** A practice only survives if someone owns it. Most QA improvements fail not because the idea was wrong, but because it belonged to everyone and therefore to no one.

## 1. Who owns what

"Quality is a team responsibility" is true and, on its own, useless. It is the sentence teams say right before nobody does the thing.

The table below is a starting point, not a rule. Adapt it, then write the result down somewhere the team can point at during a disagreement.

**A** = accountable, one person or role, the one who answers for it. **R** = responsible, does the work. **C** = consulted before the decision. **I** = informed after.

| Activity | Product | Dev | QA | UX | Ops / SRE |
|---|---|---|---|---|---|
| Business value and priority | **A** | C | C | C | I |
| Acceptance criteria are testable | R | R | **A** | C | - |
| Risk level of a change | C | R | **A** | I | C |
| Unit and component tests | I | **A** | C | - | - |
| Test strategy and depth | C | C | **A** | C | I |
| API and contract tests | I | **A/R** | R | - | I |
| Exploratory testing | R | R | **A** | R | - |
| Accessibility | C | R | R | **A** | - |
| Performance targets | **A** | R | C | I | C |
| Security testing | I | R | R | - | **A** |
| Severity of a defect | C | C | **A** | C | C |
| Priority of a defect | **A** | C | C | C | C |
| Release Go/No-Go | **A** | C | C | I | C |
| Production monitoring | I | C | C | - | **A** |
| Incident response | I | R | C | - | **A** |
| Post-release learning | R | R | **A** | I | R |

Two rows deserve their own argument, because they are where most defect disputes actually come from:

- **QA is accountable for severity.** Severity is a factual judgment about damage, and QA holds the evidence.
- **Product is accountable for priority.** Priority is a business trade-off against everything else in the backlog, and Product holds that context.

When QA owns both, QA becomes a bottleneck people route around. When Product owns both, severity quietly drifts to match whatever is convenient this sprint.

### Where QA does not belong

A QA who owns everything is a QA who is the reason nothing ships. Say this out loud, early:

- QA does not write the unit tests. QA checks that the right risks have them.
- QA does not approve implementation style in a PR. QA raises risk and testability.
- QA is not the last gate before release. The team decides together, with QA supplying the risk picture.
- QA does not own "quality". QA owns the visibility of quality, so the team can decide with its eyes open.

## 2. What quality needs from leadership

Quality is a team responsibility, and the team does not control most of what decides whether quality is *possible*: the deadline, the staffing, the environment budget, how much technical debt is tolerated, and whether careful work is rewarded or quietly penalized. Those are leadership decisions, and no amount of QA craft overrides them.

This is not a complaint, and it is not an excuse. It is the most useful thing a QA can understand, because it changes what you ask for and who you ask.

### What only leadership can do

| Lever | What it looks like in practice |
|---|---|
| Protect the practice under pressure | When the date is at risk, the Definition of Done holds and the scope moves. A DoD waived every quarter is not a standard, it is a suggestion. |
| Fund the unglamorous things | Test environments, test data, automation maintenance. None of these win a roadmap argument on their own, and none of them stop costing when they are missing. |
| Ask for risk, not for "is it done" | The question a leader asks becomes the thing teams optimize for. "What is the risk if we ship this Friday?" produces a different conversation than "will it be ready Friday?". |
| Make prevention visible | If only firefighting gets recognized, the team learns that being needed during an incident pays better than preventing one. |
| Sponsor the improvement plan | Three actions, with time actually allocated. An improvement plan with no time behind it is a document, not a plan. |

### Where top-down is the right answer

Most of this playbook works bottom-up, because practices a team chooses tend to survive and practices imposed on it tend to be performed. Some things still cannot be left to each squad:

- **Security, privacy, and accessibility standards.** A per-team opinion on WCAG, or on personal data in logs, is a compliance gap with extra steps.
- **What "done" means at the organization level.** Teams can add to it. They should not each invent it.
- **Severity definitions and escalation.** If Critical means something different on every team, incident response cannot work.

The pattern that holds: **the standard is set centrally, and how a team meets it is the team's to design.** Mandating the standard and the method together produces compliance theater, and everyone involved can tell.

### How QA earns the support

Support is rarely granted because quality is important. It is granted because someone made the cost legible.

- **Translate quality into delivery terms.** "Our validation takes four days because test data takes three" lands where "we need better test data" does not.
- **Bring evidence, not impressions.** A trend beats an anecdote, and one named escaped defect beats both.
- **Ask for one thing at a time.** Fifteen gaps read as a complaint. Three ranked actions read as a plan.
- **Say what you will stop doing.** Capacity is the honest currency, and offering the trade is what makes the ask credible.

> **Principle:** QA rarely has authority. QA almost always has evidence. Over time, evidence is the more durable of the two.

## 3. QA across time zones and contracts

Distributed delivery is the normal case in a large company, not the exception. Two situations change how QA has to work.

### Spread across time zones

The cost is not the hours. It is that every question becomes a round trip, and a question asked at 16:00 in one place is answered at 09:00 the next day in another. Three exchanges become three days.

| Problem | What actually helps |
|---|---|
| Clarifications cost a day each | Batch questions into one message rather than drip-feeding. Answer with options, not just "which one?", so the reply can be a decision instead of another question. |
| The overlap window gets spent on status | Protect the overlap for decisions and pairing. Status belongs in writing, read asynchronously. |
| "Follow the sun" becomes "throw it over the wall" | Hand over written state: what was tested, what was found, what is blocked, what needs a decision. A handover with no open questions named is not a handover. |
| Defects sit a full day before triage | Agree a severity that pages immediately, and one that waits for the next triage. Write the rule down before the first argument about it. |
| Refinement happens without QA | If QA cannot attend, QA reviews the story in writing before it enters the sprint, and the team treats that review as a gate rather than a comment. |

> **Real world:** the fix for time zones is almost always *writing things down*, and the reason teams resist is that writing feels slower in the moment. It is slower in the moment. It is much faster across the week.

### Working with vendor, contract, or offshore QA

The failure mode is predictable: the contract measures test cases executed, so the partner optimizes for test cases executed, and nobody is measuring escaped defects.

- **Never measure a QA partner on volume.** Test case count and execution count are vanity metrics ([03 - Avoid vanity metrics](../03-after-development.md#9-avoid-vanity-metrics)). Measure escaped defects, critical-flow coverage, and reopened defect rate.
- **Give them the risk picture, not just the scripts.** A partner told what to click finds what you already knew to look for.
- **Product context is the real deliverable to transfer.** Domain knowledge, user behavior, incident history. Without it a partner cannot judge severity, and every judgment call escalates to you.
- **Expect the same bug report quality.** One field set for everyone: see the [Bug Report Template](../templates/bug-report-template.md).
- **Decide who owns severity.** Usually the partner proposes and the internal QA confirms. Decide it explicitly rather than discovering it during an incident.
- **Onboard them into the guild.** A partner excluded from the community stays a supplier and never becomes a team.

## 4. Assess QA maturity when joining a team

When QA joins a new team, understand how quality currently works before proposing changes. The first ninety days spent diagnosing beat the first ninety days spent installing your previous team's process.

### Run a simple team survey

Score the current state with the [QA Assessment Survey Template](../templates/qa-assessment-survey-template.md), which defines the areas to measure, then repeat it after a few sprints to show improvement, gaps, and culture change. To run the same assessment with an AI assistant, evidence rules and grade bands included, see the [QA Assessment Skill](../ai-tools/skills/qa-assessment/SKILL.md).

Whatever the scores say, commit to **three actions maximum per cycle**, and pick the one that raises the lowest score rather than the one that perfects the highest.

## 5. Build QA community through a QA Guild

A QA Guild is a recurring space where QAs from different teams share knowledge, patterns, failures, tools, and standards.

### What makes a guild survive

Most guilds die the same way: a recurring meeting with no agenda, attendance drifting, quietly cancelled after four months.

- One owner who prepares the session. Rotating "whoever has something" means nobody does.
- One topic per session, chosen a week ahead.
- Bring real artifacts: an actual flaky test, an actual escaped defect, an actual PR. Abstract discussion produces abstract agreement and no change.
- Produce something that outlives the meeting: a decision, a shared helper, a checklist item, a standard.
- Keep it short. Forty-five focused minutes beats a vague ninety.

> **Principle:** QA maturity grows faster when knowledge is shared across teams instead of staying isolated inside one squad. The guild is also where a single QA on a squad stops being professionally alone.

## Related

- [QA Assessment Survey Template](../templates/qa-assessment-survey-template.md) - the maturity survey itself
- [Definition of Ready & Definition of Done Template](../templates/definition-of-ready-done-template.md) - includes the team agreement section on who confirms what
- [03 - Use metrics that drive decisions](../03-after-development.md#8-use-metrics-that-drive-decisions) - what to measure instead of volume
