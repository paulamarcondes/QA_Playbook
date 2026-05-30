# Unit Testing Guide for QA

A concise resource to help QAs collaborate with developers on unit testing strategy, coverage, and quality expectations.

QA does not own unit tests, but QA should understand what they protect, what they do not protect, and how they support the overall quality strategy.

## What unit tests are

Unit tests validate small pieces of code in isolation, such as:

- functions;
- methods;
- validators;
- business rules;
- calculations;
- data transformations;
- error handling logic.

They should be fast, isolated, repeatable, and easy to understand.

## Why unit tests matter

Unit tests help the team:

- catch defects early;
- protect critical business rules;
- reduce regression risk;
- support safe refactoring;
- provide fast feedback in CI/CD;
- reduce overdependence on slow UI tests.

Unit tests do not replace QA testing. They prevent avoidable defects before deeper validation starts.

## QA role in unit testing

QA should help confirm:

- critical rules are protected;
- positive, negative, and boundary scenarios are covered;
- tests align with requirements;
- coverage is meaningful, not only numeric;
- remaining gaps are covered by integration, API, UI, exploratory, or regression testing.

QA should ask for better tests, not simply more tests.

## What good unit tests look like

Good unit tests are:

- focused on one behavior;
- easy to read;
- independent;
- deterministic;
- fast to run;
- clear when they fail;
- connected to real product risk.

A good unit test should prove expected behavior, not just execute code.

## What unit tests should cover

### Business rules

Examples:

- required fields;
- allowed values;
- status transitions;
- permission rules;
- calculation rules;
- validation rules;
- mapping rules.

Ask:

- What rule must never break?
- What defect would impact users, data, or business?

### Boundary values

Examples:

- minimum and maximum values;
- empty and null values;
- one item and many items;
- values just below and above limits.

Ask:

- What happens exactly at the limit?
- What happens just outside the limit?

### Negative scenarios

Examples:

- invalid input;
- missing required data;
- unauthorized action;
- duplicated record;
- malformed payload;
- dependency failure.

Ask:

- Does the code fail safely?
- Is the error clear and expected?

### Data transformation

Examples:

- source fields map to correct destination fields;
- optional fields remain optional;
- defaults are applied correctly;
- version-specific behavior is respected.

Ask:

- Is the right data going to the right place?
- Are mandatory and optional fields handled correctly?

## Unit tests should avoid

Avoid tests that:

- validate too many behaviors at once;
- depend on execution order;
- depend on real external services;
- have weak or unclear assertions;
- test implementation details instead of behavior;
- pass without proving meaningful behavior;
- are flaky or hard to maintain.

## Unit test review checklist for QA

- [ ] Critical logic has unit tests.
- [ ] Business rules are covered.
- [ ] Positive and negative scenarios are included.
- [ ] Boundary values are tested.
- [ ] Error handling is tested.
- [ ] Assertions verify real outcomes.
- [ ] Tests are independent and repeatable.
- [ ] Mocks are used appropriately.
- [ ] Tests run automatically in CI.
- [ ] Failures would provide useful feedback.

## Useful QA questions

- Which unit tests protect this change?
- What business rules are covered?
- What edge cases did you include?
- What negative scenarios did you test?
- Would this test fail if the requirement was broken?
- Are we testing behavior or implementation details?
- Does this need a unit test, integration test, or both?

## Unit tests vs other test levels

| Use this level | For |
|---|---|
| Unit tests | Business rules, calculations, validation, isolated transformations, error handling logic. |
| Integration/API tests | Service communication, database interaction, API contracts, messaging, or event flows. |
| UI tests | User journeys, navigation, visual behavior, accessibility, and usability signals. |

Good quality strategy uses the right test at the right level.

## Quality standard

A story is stronger when:

- critical logic is protected by unit tests;
- tests run in CI;
- positive, negative, and boundary scenarios are covered;
- risky logic is not validated only through manual or UI tests;
- QA understands what is covered and what still needs validation.

Unit tests are part of the team's quality safety net.
