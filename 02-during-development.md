# 02 - During Development: Test Design, Execution & Collaboration

The goal during development is to create **fast feedback, shared ownership, and continuous validation**.

QA should not work as the final gate after everything is built. QA should help the team build the right thing, test the right risks, and detect problems while they are still cheap to fix.

---

## Outcomes expected during development

During implementation, the team should be able to:

- validate changes incrementally;
- review quality risks before merge;
- test critical behavior at the right level;
- automate stable and valuable checks;
- document evidence clearly;
- report defects in a way that accelerates resolution;
- keep product quality visible to the whole team.

---

## 1. Collaborate before the handoff

Avoid the pattern where development finishes and QA receives a surprise.

### Better practices

- QA reviews scenarios while development is still in progress.
- Developer and QA do quick pair testing before formal QA.
- QA asks for logs, test hooks, or test data improvements early.
- Developers share implementation notes that may affect testing.
- Product clarifies ambiguous behavior as soon as questions appear.

### Useful question

> What can we validate today instead of waiting until the entire feature is done?

---

## 2. Use the right test level for the risk

Not everything should be tested through the UI. Strong QA strategy uses different layers.

| Test level | Best for |
|---|---|
| Unit tests | Business rules, validators, calculations, small transformations |
| Component tests | Isolated service behavior |
| API tests | Contracts, status codes, payloads, errors, integration rules |
| Contract tests | Compatibility between providers and consumers |
| Integration tests | End-to-end communication between systems |
| UI tests | Critical user journeys and visual/user-facing behavior |
| Exploratory testing | Unknown risks, usability, edge cases, workflow quality |
| Regression tests | Protecting existing critical flows |

### Principle

Push tests as low as possible and as high as necessary.

---

## 3. Design tests around risk and value

For each story, prioritize:

1. Critical happy path
2. Most likely failure paths
3. Highest-impact edge cases
4. Integration and data risks
5. Regression around affected areas
6. User experience and clarity

### Test design prompts

- What input could break this?
- What user behavior could be unexpected?
- What system dependency could fail?
- What data could be missing, duplicated, outdated, or invalid?
- What existing flow could regress?
- What would be hard to troubleshoot later?

---

## 4. Automate strategically

Automation should reduce risk and shorten feedback loops.

### Good automation candidates

- Stable critical user journeys
- API contract validations
- Data transformation checks
- Regression-prone flows
- Repetitive setup or validation steps
- High-risk integrations
- Smoke tests for release and post-deploy validation

### Avoid automating first

- Unstable requirements
- Highly volatile UI
- One-time scenarios
- Tests with unclear expected results
- Flows that require heavy manual judgment

### Automation quality bar

Automated tests should be:

- readable;
- deterministic;
- independent where possible;
- easy to debug;
- tagged by scope and risk;
- connected to CI/CD when valuable;
- maintained as product behavior evolves.

---

## 5. Use AI as an assistant, not to take ownership

AI can support QA work, but it does not replace product understanding.

### Useful AI-assisted QA tasks

- Generate test ideas from requirements
- Identify edge cases
- Summarize logs
- Draft bug reports
- Review acceptance criteria
- Suggest automation structure
- Compare expected vs actual data
- Support exploratory testing charters

### Required human validation

- Confirm business context
- Check real user impact
- Validate expected results
- Protect sensitive data
- Review AI-generated tests for correctness
- Decide testing depth based on risk

### Principle

> AI accelerates analysis. QA provides judgment.

---

## 6. Report bugs with resolution in mind

A good bug report helps the team fix the issue faster.

### Include

- concise title;
- environment;
- build/version;
- preconditions;
- steps to reproduce;
- expected result;
- actual result;
- evidence;
- impact;
- severity and priority suggestion;
- logs, IDs, payloads, or screenshots when relevant;
- suspected area if known.

### Good bug title pattern

```text
[Area] Action fails when condition happens
```

Example:

```text
[Checkout] Payment confirmation is not displayed after an approved transaction
```

---

## 7. Collect evidence that proves behavior

Evidence should make validation clear and reusable.

### Examples

- Screenshots or short videos
- API requests and responses
- Logs with correlation IDs
- Test execution results
- Database record comparison when appropriate
- Input and output files
- Before/after behavior
- CI pipeline result
- Link to automated test

Good evidence reduces rework, improves trust, and helps future debugging.

---

## 8. Definition of Done

A change is done when:

- acceptance criteria are met;
- relevant positive and negative scenarios are validated;
- regression risk is covered;
- critical tests pass;
- automated tests were added or updated when valuable;
- logs and errors are useful for troubleshooting;
- documentation or release notes are updated when needed;
- known risks are communicated;
- evidence is attached;
- Product/QA/Dev agree the change is ready for the next step.

---

## During development checklist

- [ ] QA and Dev aligned before handoff
- [ ] Risk-based scenarios designed
- [ ] Right test levels selected
- [ ] Critical paths validated
- [ ] Negative and edge cases covered
- [ ] Automation opportunities reviewed
- [ ] Defects documented clearly
- [ ] Evidence attached
- [ ] Logs/observability checked when relevant
- [ ] Definition of Done met

---

## Key message

> QA is not only a tester.  
> QA is a quality strategist who helps the team make better technical and product decisions while the work is being built.
