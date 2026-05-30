# AI Tools for QA

This folder contains practical AI instructions, agents, and skills to support QA work.

AI can help QA move faster, but it should not replace human judgment.

---

## Good uses for AI in QA

AI can help with:

- summarizing requirements;
- finding missing acceptance criteria;
- suggesting positive and negative scenarios;
- improving bug reports;
- reviewing logs;
- creating exploratory test ideas;
- identifying automation candidates;
- refactoring Robot Framework keywords;
- improving documentation clarity.

---

## Human validation rule

Every AI-generated output must be reviewed by a human before use.

Check for:

- hallucinated requirements;
- incorrect expected results;
- missing edge cases;
- generic scenarios that do not fit the product;
- biased assumptions;
- sensitive or confidential data exposure;
- mismatch with real user impact;
- automation that creates maintenance without value.

---

## Data safety

Do not paste into AI tools:

- passwords;
- tokens;
- secrets;
- customer personal data;
- production confidential data;
- private business information not approved for AI use.

Use sanitized examples whenever possible.

---

## Files in this folder

| File | Purpose |
|---|---|
| [BASICS.instructions.md](BASICS.instructions.md) | Base instructions for QA-focused AI assistants. |
| [manual-qa.agent.md](agent/manual-qa.agent.md) | Agent instructions for manual QA support. |
| [manual-qa/SKILL.md](manual-qa/SKILL.md) | Skill guidance for manual QA workflows. |
| [robot-qa/SKILL.md](robot-qa/SKILL.md) | Skill guidance for Robot Framework workflows. |

---

## Simple prompt pattern

```text
Act as a QA Engineer.
Review the requirement below.
Identify risks, missing acceptance criteria, negative scenarios, test data needs, automation candidates, and questions for the team.
Keep the answer concise and practical.
```

---

## Reminder

AI should make QA thinking faster, clearer, and more complete.

It should not make quality decisions without human review.
