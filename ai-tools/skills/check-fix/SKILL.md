---
name: check-fix
description: Reviews a code fix against the ticket it claims to resolve, for completeness, root cause, regression risk, and the gaps fixes usually leave behind
---

# QA Checker - Code Fix

Reads a code change next to the ticket it claims to resolve, and answers: **does it fix what was asked**, **does it fix the cause or only the symptom**, and **what might it break**.

> **This is a preliminary check, not a retest.** It reads a diff. The fix still has to be verified against the original reproduction steps, and the regression risk it flags still has to be tested. Nothing here shortens that.

## Required inputs

| Input | Without it |
|---|---|
| The code change, a diff preferred over whole files | Nothing can be checked |
| **The ticket or request description** | There is no standard for "fixed" |
| The original bug report and steps to reproduce | Cannot tell whether the failing case is actually addressed |
| What calls this code, or where it is used | Blast radius is a guess |
| The test that now covers it, if one was added | Cannot tell whether the bug can return unnoticed |

A diff without a ticket is a style review. Say so and stop.

## Check 1 - Does it do what was asked

Restate in one sentence what the ticket asked for, and in one sentence what the change actually does, then put them side by side. Most disagreements are visible in that comparison alone.

Flag when the change does **less** than asked, **more** than asked, or something adjacent to what was asked.

## Check 2 - Symptom or cause

The question that decides whether this bug comes back.

| Pattern | What it looks like in a diff |
|---|---|
| **Symptom patched** | A null check added where the null should never have arrived. A try/catch around the failure. A value corrected on the way out. |
| **Cause fixed** | The code that produced the bad value is corrected. |
| **Both** | The cause is fixed and a guard is added for safety. |

Symptom-only is sometimes the right call under incident pressure. It is only wrong when nobody says out loud that it is what happened. Report which pattern this is, and if it is symptom-only, ask whether a follow-up ticket exists.

## Check 3 - The data already broken

**The most frequently missed thing in any fix.**

If the defect corrupted, skipped, or mis-wrote data, then the fix stops *new* bad data. It usually does nothing about the records already wrong.

Ask every time:

- Did this defect produce bad data, incomplete records, missed events, or wrong values?
- Does anything in this change clean them up, or is there a separate migration or script?
- If not, **who knows those records are wrong**, and what happens to them?

If the answer is "nobody has looked", that is a finding, and often a bigger one than the fix.

## Check 4 - Scope and blast radius

- Changes in the diff that the ticket did not ask for. Each one is untested risk arriving under cover of a fix.
- What else calls the changed function, reads the changed data, or depends on the changed behavior.
- Shared components, shared utilities, shared configuration.
- Changed defaults. A changed default silently changes behavior for every existing caller.
- Contract changes: a field, a type, a status code, an error shape.

## Check 5 - Regression risk signals

| Signal | Why it matters |
|---|---|
| A condition was inverted or widened | The cases that used to take the other branch now behave differently |
| A shared helper changed | Every caller inherits the change, tested or not |
| A guard clause was removed | Something upstream is now trusted that was not trusted before |
| Error handling changed | A failure that used to be caught may now propagate, or the reverse |
| A value is now cached, batched, or made async | Timing behavior changed, which tests rarely cover |

## Check 6 - Will it come back

- **Was a test added that would have failed before this fix?** If not, say so plainly. The bug can return and nothing will notice.
- Does the test cover the actual reported case, or a simplified version of it?
- Are the neighbouring cases covered - the same bug with a different input, a different role, a different record state?

## Check 7 - Proportionality

Compare the size of the fix to the severity of the ticket.

A one-line change on a Critical data-loss defect is either very elegant or does not address the real problem. Say which you think it is, and why. The same applies in reverse: a 400-line change on a cosmetic ticket is scope creep wearing a bug fix as a disguise.

## How to report

Label each finding **Confirmed** (visible in the diff provided - quote the file and line), **Likely** (strong signal, but something needed to confirm it was not provided), or **Needs human check** (cannot be determined by reading the diff).

Never invent a ticket key, a file path, a line number, or a quote.

## Output format

```text
FIX CHECK - [ticket] - [date]
Preliminary only. The fix still needs retesting against the original reproduction steps.

Ticket asked for: [one sentence]
The change does:   [one sentence]
Addresses the request: Fully / Partially / Not clearly / Does something else

ROOT CAUSE: Symptom patched / Cause fixed / Both
[reasoning]

ALREADY-BROKEN DATA
[whether bad data exists, and whether anything cleans it up]

REGRESSION RISK
- [what could break] | [file:line] | [confidence] | Retest: [specific scenario]

OUT OF SCOPE IN THIS DIFF
- [change unrelated to the ticket] | [file:line]

TEST COVERAGE
[whether a test was added that would have failed before the fix]

WHAT A HUMAN MUST STILL TEST
- Original reproduction steps, confirmed fixed
- [each regression scenario above]
- [anything reading a diff cannot answer]
```

## Then what

Take the regression list into the retest, not into a comment thread. If the fix is symptom-only or leaves broken data behind, that is a new ticket before the current one closes, and it belongs in the [post-release review](../../../03-after-development.md#10-run-blame-free-post-release-reviews) if it already reached production. For hotfixes specifically, see [what gets deferred rather than dropped](../../../03-after-development.md#6-validate-a-hotfix-without-a-full-regression).
