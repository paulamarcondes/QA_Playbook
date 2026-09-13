---
name: check-requirements
description: Reviews a new feature or product requirements document against its template and against what development actually needs to build it
---

# QA Checker - Requirements

Reads a requirements document and answers two questions: **does it follow the agreed template**, and **is anything missing that development will need**.

> **This is a preliminary check, not an approval.** It reads documents. It cannot know your product history, your customers, or the decision someone made in a meeting. Every finding is a question to take to a person, not a verdict.

## Required inputs

Ask for all of these. If any are missing, say which and stop:

| Input | Why |
|---|---|
| The requirements document | The thing being checked |
| **The template it should follow** | Without it there is no standard to check against, only opinion |
| Related files: mappings, schemas, sample payloads, interface docs | Most contradictions hide between the prose and the data |
| What the product does today, if the change touches existing behavior | To spot requirements that conflict with what already exists |

Never assume a template. If the user has no template, say so and offer to check against the [Story / Requirements / Interface Document Template](../../../templates/story-requirements-template.md) instead, as an explicit substitution.

## Check 1 - Template conformance

- Which required sections are **missing**.
- Which are present but **empty**, or still hold placeholder text: `[Add item]`, `TBD`, `N/A` with no reason given.
- Which are filled but say nothing: "standard behavior", "as usual", "same as before".

An empty section is a decision nobody made yet, not a formatting problem.

## Check 2 - Testability

For each acceptance criterion, ask: **could two people independently agree whether this passed?**

Flag any criterion that:

- describes an intention rather than an observable result;
- has no stated input, or no stated expected output;
- depends on a value nobody wrote down ("within the timeout", "the configured limit");
- cannot be verified without reading the source code.

## Check 3 - Completeness

Development needs more than the happy path. Report which of these the document does not answer:

| Area | The question it must answer |
|---|---|
| Negative paths | What happens on invalid, missing, duplicate, or unauthorized input |
| Boundaries | Minimum, maximum, empty, zero, one, many, one past the limit |
| Permissions | Who can do this, and what a user without that permission sees |
| Data rules | Required vs optional, types, formats, defaults, validation |
| Contracts | Version, backward compatibility, sample valid and invalid payloads, error responses |
| Failure behavior | Retry, roll back, skip, fail fast, or partial success - and which one |
| Existing data | What happens to records created before this change |
| Non-functional | Accessibility, locales and time zones, security, performance targets, personal data |
| Observability | What gets logged, with what identifier, and what an alert would look like |
| Volumes | How much, how often, how long it is kept |

Not every requirement needs every row. Report what is missing **and whether it matters for this change**, so the list stays usable.

## Check 4 - Contradictions

The highest-value findings, and the ones a human reading linearly misses:

- A field is required in the mapping table and optional in the schema.
- The sample payload does not match the field list.
- The summary promises something no acceptance criterion covers.
- Two criteria cannot both be true.
- A stated goal has **zero** acceptance criteria attached to it.
- The document contradicts the interface doc or schema it references.

Quote both sides of every contradiction. A contradiction reported without both quotes gets argued instead of fixed.

## Check 5 - Ambiguity

Words that hide an unmade decision. Flag each with the question it is avoiding:

`fast` · `quickly` · `user-friendly` · `intuitive` · `appropriate` · `properly` · `gracefully` · `reasonable` · `large` · `some` · `various` · `as needed` · `if applicable` · `etc.` · `and so on` · `should` where it means `must`

> "Errors are handled gracefully" -> Ask: shown where, saying what, and what can the user do next?

## How to report

Label each finding **Confirmed** (the evidence is in the files provided - quote it), **Likely** (strong signal, but something needed to confirm it was not provided), or **Needs human check** (cannot be determined from documents alone).

Never soften "not found" into "probably fine". Never invent a section, field name, or quote.

## Output format

```text
REQUIREMENTS CHECK - [document] - [date]

Ready for development: Yes / Not yet / No
Template: [name] - [n] required sections missing

BLOCKING - development should not start
- [finding] | [where, quoted] | [confidence] | Ask [role]: [the question]

SHOULD FIX BEFORE BUILD
- [finding] | [where] | [confidence] | Ask [role]: [the question]

WORTH CLARIFYING
- [finding]

NOT CHECKED
- [what could not be assessed, and what would be needed to assess it]
```

Lead with what the document does well when there is something real to say. A review that is only failures gets defended against instead of used.

## Then what

Findings become questions in refinement, not comments in a document nobody reopens. Take the blocking list to the [Three Amigos conversation](../../../01-before-development.md#2-run-a-lightweight-three-amigos-review) and the readiness call to the [Definition of Ready](../../../01-before-development.md#11-definition-of-ready).
