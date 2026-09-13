# Unit Testing Guide for QA

Unit tests are a **developer responsibility**. QA does not write them and does not own them. QA reads them, because they decide how much risk is left for every test level above.

This guide is about that reading: why it matters to you, how to judge whether a suite protects anything, and what to ask for when it does not.

## Why this matters to QA

- **Every rule proven here is a rule you do not have to re-test through the UI.** Weak unit coverage does not remove work, it pushes it up to the slowest, most fragile level, where it lands on you.
- **A defect caught here is nearly free.** The same defect found in exploratory testing costs a cycle; in production it costs an incident.
- **Coverage percentage is not coverage of risk.** 85% coverage with weak assertions is more dangerous than 40% honest coverage, because it buys confidence nobody verified.
- **Refactoring safety is your regression safety.** When developers can change code without fear, the change you validate is smaller and cleaner.

> Unit tests do not replace QA testing. They decide what is *left* for QA to test, which is why reading them is worth your time.

## What they cover, and how to analyze it

Unit tests validate small pieces of code in isolation: functions, validators, business rules, calculations, transformations, error handling. Fast, isolated, repeatable.

Four areas are worth checking, and each has one question that exposes the gap faster than reading the tests line by line.

| Area | What should be covered | The question that finds the gap |
|---|---|---|
| **Business rules** | Required fields, allowed values, status transitions, permission rules, calculations, mapping rules | "Which rule here must never break, and what happens to users or data if it does?" |
| **Boundaries** | Minimum and maximum, empty and null, one item and many, just below and just above a limit | "What happens exactly at the limit, and one past it?" |
| **Negative paths** | Invalid input, missing required data, unauthorized action, duplicate record, malformed payload, dependency failure | "Does it fail safely, with an error someone can act on?" |
| **Data transformation** | Source field to target field, optional fields staying optional, defaults applied, version-specific behavior | "Is the right data going to the right place, in the right format?" |

**Ask for better tests, not more tests.** A count is easy to raise and proves nothing.

## Judging test quality

You do not need to write the code to see whether a test is worth anything.

| Signs it protects something | Signs to distrust it |
|---|---|
| Tests one behavior, named so the failure is obvious | Validates several behaviors at once, so a failure is ambiguous |
| Asserts a real outcome: a value, a state, an error | Asserts that the code ran, or that nothing threw |
| Independent of other tests and of order | Depends on execution order or leftover state |
| Deterministic and fast | Flaky, slow, or reaching a real external service |
| Tied to a requirement or a known risk | Tests implementation details, so a safe refactor breaks it |

> **The test that matters:** would this test fail if the requirement were broken? If not, it is executing code, not protecting behavior.

## Review checklist

- [ ] Critical business logic has tests.
- [ ] Assertions verify real outcomes, not that the code ran.
- [ ] Boundary values are covered.
- [ ] Negative paths and error handling are covered.
- [ ] Tests are independent, deterministic, and free of real external dependencies.
- [ ] A failure message would tell you what broke.
- [ ] Tests run automatically in CI.
- [ ] Whatever is not covered here is named, and picked up at a higher level.

## Questions to ask the developer

- Which unit tests protect this change?
- What business rules are covered, and which are not?
- What happens at the boundaries?
- Would this test fail if the requirement were broken?
- Does this need a unit test, an integration test, or both?

These are collaboration questions, asked in refinement or in the pull request, not an audit.

## Where unit tests stop

Unit tests cover business rules, calculations, validation, isolated transformations, and error handling logic. Anything that crosses a boundary - service calls, databases, contracts, messaging, events - and anything the user actually sees needs a higher level.

The full map of levels to risks is in [02 - Use the right test level for the risk](../02-during-development.md#4-use-the-right-test-level-for-the-risk). How QA reviews the rest of a pull request is in the [Clean Code Review Guide for QA](clean-code-guide.md).
