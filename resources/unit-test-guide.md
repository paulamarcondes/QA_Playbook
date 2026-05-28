# Unit Testing Guide for QA

A concise resource to help QAs collaborate with developers on unit testing strategy, coverage, and quality expectations.

QA does not own unit tests, but QA should understand what they protect, what they do not protect, and how they support the overall quality strategy.

---

## What Unit Tests Are

Unit tests validate small pieces of code in isolation, such as:

- Functions
- Methods
- Validators
- Business rules
- Calculations
- Data transformations
- Error handling logic

They should be fast, isolated, repeatable, and easy to understand.

---

## Why Unit Tests Matter

Unit tests help the team:

- Catch defects early
- Protect critical business rules
- Reduce regression risk
- Support safe refactoring
- Provide fast feedback in CI/CD
- Reduce overdependence on slow UI tests

Unit tests do not replace QA testing. They prevent avoidable defects before deeper validation starts.

---

## QA Role in Unit Testing

QA should help confirm:

- Critical rules are protected
- Positive, negative, and boundary scenarios are covered
- Tests align with requirements
- Coverage is meaningful, not only numeric
- Remaining gaps are covered by integration, API, UI, exploratory, or regression testing

QA should ask for better tests, not simply more tests.

---

## What Good Unit Tests Look Like

Good unit tests are:

- Focused on one behavior
- Easy to read
- Independent
- Deterministic
- Fast to run
- Clear when they fail
- Connected to real product risk

A good unit test should prove expected behavior, not just execute code.

---

## What Unit Tests Should Cover

### Business Rules

Examples:

- Required fields
- Allowed values
- Status transitions
- Permission rules
- Calculation rules
- Validation rules
- Mapping rules

Ask:

- What rule must never break?
- What defect would impact users, data, or business?

### Boundary Values

Examples:

- Minimum and maximum values
- Empty and null values
- One item and many items
- Values just below and above limits

Ask:

- What happens exactly at the limit?
- What happens just outside the limit?

### Negative Scenarios

Examples:

- Invalid input
- Missing required data
- Unauthorized action
- Duplicated record
- Malformed payload
- Dependency failure

Ask:

- Does the code fail safely?
- Is the error clear and expected?

### Data Transformation

Examples:

- Source fields map to correct destination fields
- Optional fields remain optional
- Defaults are applied correctly
- Version-specific behavior is respected

Ask:

- Is the right data going to the right place?
- Are mandatory and optional fields handled correctly?

---

## Unit Tests Should Avoid

Avoid tests that:

- Validate too many behaviors at once
- Depend on execution order
- Depend on real external services
- Have weak or unclear assertions
- Test implementation details instead of behavior
- Pass without proving meaningful behavior
- Are flaky or hard to maintain

---

## Unit Test Review Checklist for QA

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

---

## Useful QA Questions

- Which unit tests protect this change?
- What business rules are covered?
- What edge cases did you include?
- What negative scenarios did you test?
- Would this test fail if the requirement was broken?
- Are we testing behavior or implementation details?
- Does this need a unit test, integration test, or both?

---

## Unit Tests vs Other Test Levels

Use unit tests for:

- Business rules
- Calculations
- Validation
- Isolated transformations
- Error handling logic

Use integration/API tests for:

- Service communication
- Database interaction
- API contracts
- Messaging or event flows

Use UI tests for:

- User journeys
- Navigation
- Visual behavior
- Accessibility and usability signals

Good quality strategy uses the right test at the right level.

---

## Quality Gate

A story is stronger when:

- Critical logic is protected by unit tests
- Tests run in CI
- Positive, negative, and boundary scenarios are covered
- Risky logic is not validated only through manual or UI tests
- QA understands what is covered and what still needs validation

Unit tests are part of the team’s quality safety net.
