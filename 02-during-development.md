# 02 - During Development: Test Design, Execution & Collaboration

The goal during development is to create **fast feedback, shared ownership, and continuous validation**.

QA should not work as the final gate after everything is built. QA should help the team build the right thing, test the right risks, and detect problems while they are still cheap to fix.

---

## Outcomes expected during development

During implementation, the team should be able to:

- validate changes incrementally;
- review quality risks before merge;
- test critical behavior at the right level;
- check developer quality signals, such as unit tests and static analysis;
- automate stable and valuable checks;
- use environments intentionally;
- document evidence and how-to-test guidance clearly;
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

## 2. Check developer quality signals

QA does not need to own unit testing, but QA should understand whether the change is protected at the right technical level.

### Signals to review with developers

- Unit tests added or updated for business rules, validators, calculations, and transformations
- Integration or component tests added when behavior crosses boundaries
- Static analysis reviewed, such as SonarQube issues, code smells, duplication, and security hotspots
- CI pipeline passing
- Code coverage meaningful for the changed area, not only globally high
- Error handling and logs included for risky flows

### Practical question

> Which risks are protected by developer tests, and which risks still need QA validation?

---

## 3. Participate in PR review as a QA task

Pull request review is not only a developer activity. QA can review changes through a risk and testability lens.

### QA PR review focus

- Does the change match the requirement and acceptance criteria?
- Are edge cases and negative paths considered?
- Are unit/API/integration tests included at the right level?
- Are logs, errors, and validation messages useful?
- Does the change affect existing flows, contracts, permissions, or data?
- Are feature flags, configs, migrations, or environment differences clear?
- Are documentation, user guide, or how-to-test notes needed?

QA does not need to approve implementation style, but can raise risks that affect validation and release confidence.

---

## 4. Use the right test level for the risk

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

For a broader reference, see [Testing Types Reference](testing-types.md).

---

## 5. Design tests around risk and value

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

## 6. Use environments intentionally

Environment strategy affects test reliability and release confidence.

| Environment | Purpose | QA focus |
|---|---|---|
| Dev | Fast developer feedback and early checks | Pair testing, early API checks, obvious defects, testability feedback |
| QA / Test | Dedicated validation environment | Functional, integration, regression, exploratory, test data validation |
| Staging / Pre-prod | Production-like release validation | Final smoke, configuration, deployment validation, high-risk regression |
| Production | Real user/system behavior | Smoke validation, monitoring, logs, alerts, incident signals |

### Release reminder

A feature moving between environments should have clear build/version information, deployment notes, known risks, and rollback or mitigation awareness when needed.

---

## 7. Automate strategically

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

## 8. Use AI as an assistant, not as ownership

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

For reusable assistant configuration, see [AI Tools](ai-tools/README.md).

---

## 9. Define what is a bug and what is not

A bug is a product behavior that conflicts with a requirement, acceptance criteria, contract, expected user outcome, security rule, data integrity rule, or agreed quality standard.

### Usually a bug

- Requirement or acceptance criteria not met
- Incorrect data, missing data, or data corruption
- Broken integration, API, file, event, or workflow
- Security, permission, or access control issue
- Critical user journey blocked
- Error handling is missing, misleading, or unsafe
- Regression in existing behavior
- Significant usability problem that prevents task completion

### Usually not a bug

- New feature request
- Product decision that works as designed
- Cosmetic preference without user or brand impact
- Environment issue unrelated to the product change
- Known limitation already documented and accepted
- Test data setup issue caused by invalid preconditions

### When unsure

Document the observation, impact, evidence, and question. Then align with Product, Dev, and QA before classifying it.

---

## 10. Report bugs with resolution in mind

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
[Checkout] Payment confirmation is not displayed after approved transaction
```

---

## 11. Collect evidence that proves behavior

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

## 12. Document user guides and how-to-test notes

Documentation is part of quality when it helps users, support, QA, and developers validate or operate the feature correctly.

### User guide updates

Update user-facing or support-facing documentation when the change affects:

- user workflow;
- permissions or roles;
- configuration;
- error messages;
- expected behavior;
- operational steps;
- known limitations.

### How-to-test notes

Add lightweight technical notes when the feature needs specific validation context:

- environment setup;
- test users and roles;
- required data;
- API payloads or files;
- feature flags or configuration;
- expected logs;
- troubleshooting tips.

A good how-to-test note makes future regression faster and reduces knowledge loss.

---

## 13. Definition of Done

A change is done when:

- acceptance criteria are met;
- relevant positive and negative scenarios are validated;
- unit/static analysis/pipeline quality signals are reviewed;
- regression risk is covered;
- critical tests pass;
- automated tests were added or updated when valuable;
- logs and errors are useful for troubleshooting;
- documentation, user guide, how-to-test notes, or release notes are updated when needed;
- known risks are communicated;
- evidence is attached;
- Product/QA/Dev agree the change is ready for the next step.

---

## During development checklist

- [ ] QA and Dev aligned before handoff
- [ ] Unit tests and static analysis reviewed when relevant
- [ ] QA reviewed PR risk/testability when relevant
- [ ] Risk-based scenarios designed
- [ ] Right test levels selected
- [ ] Correct environment used for the validation purpose
- [ ] Critical paths validated
- [ ] Negative and edge cases covered
- [ ] Automation opportunities reviewed
- [ ] Defects classified and documented clearly
- [ ] Evidence attached
- [ ] User guide or how-to-test notes updated when needed
- [ ] Logs/observability checked when relevant
- [ ] Definition of Done met

---

## Key message

> QA is not only a tester.  
> QA is a quality strategist who helps the team make better technical and product decisions while the work is being built.
