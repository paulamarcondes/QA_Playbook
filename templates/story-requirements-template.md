# Story / Requirements / Interface Document Template

Two templates in one file.

- **[Part 1 - The story version](#part-1---the-story-version)** covers a normal user story. It is what you will use almost every time.
- **[Part 2 - The interface and contract document](#part-2---the-interface-and-contract-document)** is for changes **other teams build against** - a shared API, a data contract, a file or event another system consumes - where this document *is* the deliverable and someone will hold you to it months later.

> QA rarely writes either one. QA reviews them, and the fastest way to use this template is as a list of what should already be there.

# Part 1 - The story version

## 1. The story

| Field | Value |
|---|---|
| Title |  |
| Jira / Work item |  |
| Owner |  |
| Risk level | Low / Medium / High / Critical |

```text
As a [user/system/persona],
I want [capability/change],
So that [value/outcome].
```

**Problem to solve:** the current gap, limitation, defect, manual effort, risk, or customer need.

**Success outcome:** how we will know this change worked.

## 2. Scope

**In scope:** [what this change covers]

**Out of scope:** [what it deliberately does not, so it is a decision rather than an oversight]

**Assumptions:** [believed true, not yet confirmed]

| Dependency | Owner | Status | Notes |
|---|---|---|---|
|  |  |  |  |

## 3. Acceptance criteria

Specific, observable, testable. Use BDD when behavior needs to be business-readable across Product, Dev, and QA; use the checklist form when the team needs something faster.

```gherkin
Given [context]
When [action]
Then [expected behavior]
And [observable result]
```

```text
- User can [complete action] when [condition]
- System prevents [invalid action] when [condition]
- Error message explains [problem] and [next step]
- Existing behavior [flow/component] is not impacted
- Logs include [ID/context] for troubleshooting
```

### Error and negative scenarios

- [ ] Invalid input fails safely.
- [ ] Missing required data returns a clear error.
- [ ] Duplicate requests/files/events are handled correctly.
- [ ] External dependency failure is handled correctly.
- [ ] Unauthorized access is blocked.

### Boundaries

State the actual values, not "within the limit".

| Boundary | Value | Behavior at the limit | Behavior one past it |
|---|---|---|---|
| Minimum / empty / zero |  |  |  |
| Maximum / length / size |  |  |  |
| Count, rate, or timeout |  |  |  |

### Existing data

What happens to records created before this change.

| Question | Answer |
|---|---|
| Are existing records affected? | Yes / No |
| Are they migrated, converted, backfilled, or left as they are? |  |
| What does the system do when it reads an old-format record? |  |
| Who owns the migration or cleanup, and is it in this story? |  |

## 4. QA notes

| Area | Notes |
|---|---|
| Critical happy path |  |
| Highest-risk negative scenarios |  |
| Regression areas |  |
| Test data and environment needed |  |
| Automation candidates |  |
| Post-deploy checks |  |

## 5. Open questions

| Question | Owner | Status |
|---|---|---|
|  |  |  |

A story is ready when scope is clear, acceptance criteria are testable, risks and dependencies are visible, test data needs are known, and open questions are resolved or explicitly accepted. Full bar: [Definition of Ready & Definition of Done](definition-of-ready-done-template.md).

---

# Part 2 - The interface and contract document

Add these sections **only** when other teams or systems build against this change. Everything in Part 1 still applies.

## 6. Document control

| Field | Value |
|---|---|
| Product / System |  |
| Status | Draft / In Review / Approved / Deprecated |
| Version |  |
| Last updated |  |
| Approvers | Product / Engineering / QA / Architecture |

## 7. Interface and contract details

| Field | Details |
|---|---|
| Contract name |  |
| Version |  |
| Source system |  |
| Target system |  |
| Primary user / system |  |
| Endpoint / File path / Topic / Queue |  |
| Method / Operation |  |
| Trigger | Manual / Scheduled / Event / API / File / Other |
| Direction | Inbound / Outbound / Bidirectional / Internal |
| Transport | UI / API / File / Queue / Database / Other |
| Format | JSON / XML / CSV / TXT / Image / Other |
| Schema / Layout reference |  |
| Authentication / Authorization |  |
| Frequency / Volume |  |
| Retention | How long the data is kept, and what happens when it expires |

### High-level flow

```text
Source -> Processing / Validation / Transformation -> Target -> Confirmation / Monitoring
```

### Data mapping

| Source field | Target field | Required? | Transformation / Rule | Default | Notes |
|---|---|---|---|---|---|
|  |  | Yes / No |  |  |  |

### Sample payload / file

```json
{
  "example": "replace with sanitized sample data"
}
```

### Compatibility expectations

- [ ] Backward compatibility required.
- [ ] New version required.
- [ ] Existing consumers/providers impacted.
- [ ] Migration or conversion required.
- [ ] Deprecated behavior documented.

## 8. Functional requirements

Use when the change needs numbered requirements someone can cite, beyond the acceptance criteria in Part 1.

| ID | Requirement | Priority | Acceptance / Validation Notes |
|---|---|---|---|
| FR-001 |  | Must / Should / Could |  |

## 9. Non-functional requirements

What breaks, the minimum bar, and how to test each of these: [Quality Attributes Guide](../resources/quality-attributes-guide.md).

| Area | Requirement | Validation approach |
|---|---|---|
| Performance |  |  |
| Security / Permissions |  |  |
| Reliability |  |  |
| Compatibility |  |  |
| Accessibility / UX |  |  |
| Audit / Compliance |  |  |
| Observability |  |  |

## 10. Observability requirements

A change is not ready if the team cannot understand and troubleshoot it after release.

- [ ] Correlation ID, plus the user, customer, tenant, or system identifier when applicable.
- [ ] Processing stage, and success, warning, or failure status with a clear reason.
- [ ] Input/output reference without exposing sensitive data.
- [ ] Dashboard, alert, or log query available.

```text
correlationId=  system=  stage=  status=  reason=  version=
```

## 11. User experience notes

For user-facing changes. Reference: [Nielsen Norman Group - 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/).

| Area | Notes |
|---|---|
| Primary user journey and expected outcome |  |
| Error, loading, and empty states |  |
| Possible confusion points |  |
| Accessibility considerations |  |
