# 02 - During Development

Build quality while the change is being implemented.

This phase is about fast feedback, technical collaboration, useful tests, observable behavior, and early risk reduction.

---

## Main goal

During development, QA should help the team answer:

- Is the implementation matching the requirement?
- Are important risks being covered?
- Are unit tests meaningful?
- Are contracts and payloads still correct?
- Are failures visible and easy to investigate?
- Is automation adding useful feedback?
- Is the feature moving toward Done with confidence?

---

## Team habit: review quality before the end

Do not wait for a finished build to start quality review.

QA can add value during development by:

- reviewing acceptance criteria with the developer;
- reviewing payloads, contracts, and mappings;
- discussing unit test coverage;
- checking logs and error handling;
- pair-testing high-risk flows;
- identifying automation candidates early;
- raising defects with useful technical context.

---

## 1. Review PRs with a QA mindset

QA does not need to review code like a developer. QA should review code for quality signals.

Look for:

- changed business rules;
- missing edge cases;
- unclear error handling;
- risky data transformations;
- permission or access gaps;
- missing or weak tests;
- logging and traceability gaps;
- hardcoded values or fragile logic;
- possible accessibility or usability issues.

Useful resource: [Clean Code Guide](resources/clean-code-guide.md)

---

## 2. Review unit test strategy

Unit tests should protect important logic, not only increase coverage numbers.

Discuss with developers:

- What logic changed?
- Which rules should be protected by unit tests?
- Are negative and edge cases covered?
- Are assertions meaningful?
- Would these tests fail if the logic was broken?

Useful resource: [Unit Testing Guide](resources/unit-testing-guide.md)

---

## 3. Validate contracts and payloads early

For APIs, files, events, or integrations, review examples before full testing starts.

Check:

- required fields;
- optional fields;
- valid and invalid payloads;
- error responses;
- status transitions;
- backward compatibility;
- consumer expectations;
- data mapping rules.

Early contract review prevents expensive integration bugs.

---

## 4. Use pair testing for high-risk changes

Pair testing is useful when the change is complex, risky, or hard to understand.

Use it for:

- critical flows;
- integration changes;
- data transformations;
- permission-sensitive features;
- confusing defects;
- unstable areas;
- changes with unclear behavior.

Keep it short and focused. The goal is fast shared understanding.

---

## 5. Review observability and monitoring

Modern QA should help ensure failures are visible after release.

Ask during review:

- Are important failures logged?
- Do logs include useful IDs, status, and context?
- Can support or engineering trace what happened?
- Are sensitive values protected?
- Are metrics or alerts needed for this change?
- Would we know if this broke in production?

Checklist item:

```text
Does this change include enough logs, metrics, or traceability to make failures visible in production?
```

---

## 6. Test continuously

Start with the fastest useful feedback.

Depending on the change, use:

- local validation;
- unit test review;
- API checks;
- contract checks;
- integration checks;
- targeted exploratory testing;
- regression checks;
- accessibility or security checks;
- automation updates.

Useful resource: [Testing Guide](resources/testing-guide.md)

---

## 7. Automate for feedback

Automation should protect valuable feedback loops.

Prioritize automation for:

- critical paths;
- API contracts;
- stable regression flows;
- integration checks;
- repetitive checks;
- high-risk scenarios that must be retested often.

Avoid automating unstable, unclear, low-value, or one-time scenarios.

Checklist item:

```text
Are critical paths and contracts protected by automated checks when valuable?
```

---

## 8. Report bugs with context

A good bug report helps the team fix the issue faster.

Include:

- clear title;
- environment and build;
- affected area;
- steps or trigger condition;
- expected and actual result;
- evidence;
- logs, IDs, traces, or payloads when relevant;
- risk level;
- business or user impact;
- suspected area if known.

Useful template: [Bug Report Template](templates/bug-report-template.md)

---

## 9. Validate AI-generated output

If AI was used for test design, code, scripts, summaries, or bug analysis, a human must review it.

Check for:

- hallucinated requirements;
- generic or unrealistic tests;
- missing edge cases;
- biased assumptions;
- sensitive data exposure;
- mismatch with business risk;
- incorrect expected results.

AI supports QA. It does not own quality decisions.

---

## 10. Definition of Done

A story is Done when the team has enough evidence that the change is safe, useful, and maintainable.

Minimum checks:

- [ ] Acceptance criteria are met.
- [ ] Risk level was considered.
- [ ] Relevant positive and negative scenarios were validated.
- [ ] Unit tests and code quality were reviewed when relevant.
- [ ] Contracts, payloads, logs, and errors were reviewed when relevant.
- [ ] Security and accessibility expectations were validated when relevant.
- [ ] Automation was added or updated when it provides useful feedback.
- [ ] Evidence is attached or documented.
- [ ] Known risks are communicated.

Full template: [Definition of Ready / Done Template](templates/definition-of-ready-done-template.md)

---

## Output of this phase

At the end of this phase, the team should have:

- fewer surprises in QA validation;
- stronger implementation quality;
- clearer evidence;
- better automation decisions;
- better logs and troubleshooting signals;
- higher confidence before release.
