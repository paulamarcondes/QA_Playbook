---
name: check-deliverables
description: Reviews feature and release deliverables from QA and from development - test plans, test cases, deployment and delivery guides, release notes, interface docs, migration plans - against their templates and quality bar
---

# QA Checker - Deliverables

Reads the documents a feature or release produces, from **QA and from development**, and answers: **do they follow the template**, **do they meet the quality bar**, and **do they contradict each other**.

Development owns most of the operational documents here - deployment and delivery guides, release notes, interface docs, migration plans, runbooks. QA still reviews them, because they are what Support, Ops, and the next person on call will depend on.

> **This is a document review, not a coverage guarantee.** A deliverable can pass every check here and still miss the defect that reaches production. This finds what is absent or inconsistent on paper.

## Required inputs

| Input | Why |
|---|---|
| The deliverables to check, from either side | The thing being checked |
| **The template each one should follow** | Without it there is no standard, only preference |
| The requirements or acceptance criteria they cover | The only way to check coverage rather than just completeness |

If the acceptance criteria are not provided, say so. Coverage cannot be checked, and the output must say that rather than skip it silently.

Never assume a template. If the user has none for a given document, say so and offer to check against the playbook equivalent instead, as an explicit substitution: [Test Strategy](../../../templates/test-strategy-template.md) · [Test Cases](../../../templates/test-cases-template.md) · [Bug Report](../../../templates/bug-report-template.md) · [Deployment Validation Guide](../../../templates/deployment-validation-guide-template.md). Where no template exists on either side, check against the quality bar below and label the finding as such.

## Check 1 - Template conformance

- Required sections missing.
- Placeholder text still in place: `[Add item]`, `TBD`, `[Scenario title]`, empty table rows.
- Sections filled with something that says nothing: "as per standard", "see Jira".

## Check 2 - Quality bar by artifact

### QA deliverables

| Artifact | Playbook template | Passes when |
|---|---|---|
| **Test strategy** | [Test Strategy](../../../templates/test-strategy-template.md) | Risk level stated **and justified** · in-scope and out-of-scope both filled · exit criteria measurable · test data has a named owner and a status |
| **Test cases** | [Test Cases](../../../templates/test-cases-template.md) | Expected results measurable, not "works correctly" · negative and boundary scenarios present · each case traces to an acceptance criterion · evidence named per case · no click-by-click scripting where it adds nothing |
| **Bug reports** | [Bug Report](../../../templates/bug-report-template.md) | Preconditions present · impact written as what a person cannot do · evidence attached · severity and priority rated separately, with a reason |
| **QA report** | Format in the [Manual QA Skill](../manual-qa/SKILL.md#qa-report-for-leadership) | Scope tested **and not tested** · a release recommendation · each risk paired with what would reduce it |

### Development deliverables

| Artifact | Playbook template | Passes when |
|---|---|---|
| **Deployment / delivery guide** | [Deployment Validation Guide](../../../templates/deployment-validation-guide-template.md) | Steps in execution order · prerequisites and config changes listed · migration steps with expected duration · **a rollback path someone has actually exercised** · a step confirming the deployed version · who to contact when it goes wrong |
| **Interface / API documentation** | [Story / Requirements / Interface Document](../../../templates/story-requirements-template.md#7-interface-and-contract-details) | Version · required vs optional fields · data types and formats · error responses · sample valid and invalid payloads · an explicit backward compatibility statement |
| **Release notes** | None - quality bar only | Written in user terms, not commit messages · breaking changes called out · known issues listed · any action required by users or admins stated |
| **Migration plan** | None - quality bar only | What data, in what order · how long it takes · **whether it is reversible** · what happens to records created mid-migration · a verification step that proves it worked |
| **Runbook / operations notes** | None - quality bar only | What each alert means · the common failures and the response to each · escalation path |
| **How-to-test notes** | None - quality bar only | Environment setup · test users and roles · required data · feature flags · the logs to expect |
| **Configuration guide** | None - quality bar only | Every setting, its default, and what differs per environment |

"None" means this playbook has no template for it. Check it against the team's own template if one exists, otherwise against the quality bar, and say which standard was used.

The two rows that fail most often: **a rollback path nobody has tested**, and **a migration plan with no verification step**.

## Check 3 - Coverage

Map every acceptance criterion to the test cases that cover it.

Report:

- **Acceptance criteria with zero test cases.** The single most valuable finding in this whole check.
- Criteria covered only by a happy-path case, where the criterion describes an error or a rule.
- Test cases that trace to nothing, which usually means the requirement changed and the case was never updated.

## Check 4 - Contradictions between documents

Each document can be individually fine and collectively wrong. This is where QA reviewing development's documents earns its place:

- Strategy says **High** or **Critical** risk, and the test cases cover only the happy path.
- Strategy names automation candidates; no case is flagged as one.
- Something is **out of scope** in the strategy and has a test case anyway, or **in scope** with no case at all.
- The deployment guide has **no smoke scenario for the critical flow** the strategy named.
- The deployment guide changes a configuration value the interface doc still documents with the old default.
- Release notes do not mention a **breaking change** the interface doc declares.
- The migration plan and the deployment guide disagree on **order** - migration before or after the deploy.
- How-to-test notes reference a feature flag the deployment guide never sets.
- Risk level in the strategy does not match the risk level on the story.

Quote both sides. A contradiction without both quotes becomes a debate.

## Check 5 - Evidence and traceability

- Is the evidence named specific enough to collect? "Logs" is not evidence. "API response plus correlation ID from the payment log" is.
- Could someone else re-run this in six months from the document alone?
- Are the ticket, build, and environment recorded?

## How to report

Label each finding **Confirmed** (the evidence is in the documents provided - quote it), **Likely** (strong signal, but something needed to confirm it was not provided), or **Needs human check** (cannot be determined from the documents alone).

Never invent a test case ID, a section, a config key, or a quote.

## Output format

```text
DELIVERABLES CHECK - [release or feature] - [date]

Reviewed: [QA documents] + [development documents]
Coverage: [n] of [n] acceptance criteria have at least one test case

UNCOVERED ACCEPTANCE CRITERIA
- [AC] - no test case found

CONTRADICTIONS BETWEEN DOCUMENTS
- [document A says X] vs [document B says Y] | [confidence]

OPERATIONAL GAPS
- [missing rollback, verification step, escalation path, breaking change note]

TEMPLATE AND QUALITY GAPS
- [document] | [gap] | [confidence]

NOT CHECKED
- [what could not be assessed, and what would be needed]
```

## Then what

Fix in this order: uncovered acceptance criteria, operational gaps, contradictions, then template tidiness. A missing rollback path is a release risk. A missing section heading is housekeeping.
