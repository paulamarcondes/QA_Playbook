---
name: check-code
description: Preliminary review of developed code against the requirements, mappings, and schemas it was built from. Never a replacement for hands-on testing!
---

# QA Checker - Code Against Requirements

Reads developed code next to the requirements it was built from, and reports where they do not line up.

> ## This never replaces testing
>
> This check reads source code. It cannot run the system, call a real integration, process a real file, or watch a user. **Everything it finds is a hypothesis to verify by testing, and everything it misses is still out there.** A clean result means "no contradiction found on paper", never that the feature works, and it is never a reason to shorten the hands-on testing that must happen before anything reaches production.
>
> Every report must end with the **What a human must still test** section. A report without it is incomplete.

## Required inputs

### Always

| Input | Without it |
|---|---|
| The code, or where to find it | Nothing can be checked |
| **Requirements and acceptance criteria** | There is nothing to check the code *against*, only style opinions |
| What the code depends on and what depends on it | Blast radius is a guess |

If requirements are missing, stop. A code review without a requirement is a style review.

### Only when the change moves data between systems

Skip these when they do not apply. A UI-only or single-service change has none of them, and demanding them stalls the check for no reason.

| Input | Without it |
|---|---|
| Field mappings | Transformation errors become invisible |
| Schemas and contracts | Type, format, and required-field mismatches cannot be seen |
| Sample payloads or files, valid and invalid | Error handling cannot be traced |

Name whichever inputs are missing, and say what that costs, before starting.

## Check 1 - Requirement trace

The core of this check. One row per acceptance criterion.

| AC | Where in the code | Status | Note |
|---|---|---|---|
| AC-01 | `OrderValidator.java:48` | Implemented | |
| AC-02 | `OrderMapper.java:112` | **Partial** | Handles null, not empty string |
| AC-03 | not found | **Not found** | No code path matches this criterion |
| AC-04 | - | **Cannot tell** | Logic is in a service not provided |

Four statuses only. **"Not found" is never softened to "probably handled elsewhere".** If it is not in the code provided, it is not found, and say what would be needed to check.

## Check 2 - Data mapping against schema against code

**Skip this check entirely when the change does not move data between systems.** Where it does apply, this is where most integration defects live, and where reading three sources side by side beats testing at finding them.

For each mapped field, compare all three sources:

- Field present in the mapping but **not written by the code**.
- Required in the schema, **optional in the code**, or the reverse.
- Type or format mismatch: string where the schema says number, date format not the one specified.
- A default applied in code that differs from the documented default.
- Truncation: a target field shorter than the source.
- A field the code writes that no mapping mentions.

## Check 3 - Error handling against the specification

For each failure the requirements describe, find what the code actually does:

- Invalid input, missing required data, duplicate record or message, unauthorized caller, dependency unavailable, timeout, partial failure.
- Does it fail the way the spec says - retry, roll back, skip, fail fast, or partial success?
- **Silent failures:** empty catch blocks, swallowed exceptions, errors logged and then ignored.
- Does the error reaching the user say what the requirement says it should?

## Check 4 - Boundaries, permissions, and observability

| Area | What to look for |
|---|---|
| Boundaries | The limits stated in the requirements, actually enforced in code. Off-by-one at min and max. Empty and zero handled. |
| Permissions | Authorization checked **server-side**, not only hidden in the UI. Every protected action, every role. |
| Observability | Correlation ID present and passed through. Logs at the stages the requirement names. **No personal data or secrets in the logs.** |
| Compatibility | If a contract changed, is the old shape still accepted for existing consumers? |

## Check 5 - Risk smells

Not defects on their own, but where defects concentrate:

- Business rules duplicated in more than one place, now able to drift apart.
- Validation only in the UI for logic that matters.
- Hardcoded environment-specific values that should be configuration.

## How to report

Label each finding **Confirmed** (visible in the code provided - quote the file and line), **Likely** (strong signal, but something needed to confirm it was not provided), or **Needs human check** (cannot be determined by reading; most timing, integration, and data-quality questions land here).

Never invent a file path, a line number, a function name, or a quote. If a path was not provided, say the code was not provided.

## Output format

```text
PRELIMINARY CODE CHECK - [feature] - [date]
Preliminary only. Not a test pass. Hands-on testing still required!

REQUIREMENT TRACE
[n] implemented · [n] partial · [n] not found · [n] cannot tell
| AC | Where | Status | Note |

LIKELY DEFECTS
- [what breaks, and the input that would break it] | [file:line] | [confidence]

CONTRADICTIONS WITH THE SPEC
- [code does X] vs [requirement says Y] | [file:line] | [quote from the requirement]

RISK AREAS
- [area] | [why it concentrates risk] | [file:line]

WHAT A HUMAN MUST STILL TEST
- [specific scenario, and why reading the code cannot answer it]

NOT CHECKED
- [what was not provided, and what it would have shown]
```

## What a human must still test

This section is required in every report. Reading code cannot see runtime behavior, what a real integration actually returns, timing and concurrency, performance at real volume, what production data really looks like, user experience, what differs between environments, or anything in code that was not provided.

Write this list as **specific scenarios for this change**, not as the generic list above. "Submit two identical import files three seconds apart and confirm only one record is created" is useful. "Test concurrency" is not.

## Then what

Findings become test scenarios and questions for the developer, not a verdict on the code. Feed them into the [test design](../../../02-during-development.md#5-design-tests-around-risk-and-value) and the [exploratory session](../../../02-during-development.md#6-run-exploratory-testing-with-a-charter), and raise the contradictions as [defects or requirement clarifications](../../../02-during-development.md#10-define-what-is-a-bug-and-what-is-not).
