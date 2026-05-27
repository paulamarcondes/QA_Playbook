---
name: robot-qa
description: Robot Framework automation guidance for clean, maintainable, robust test automation
---

# Robot Framework QA Skill

Use this skill for Robot Framework test creation, review, refactoring, debugging, and manual-to-automated conversion.

## Core Rule

Analyze -> Propose -> Get approval -> Execute.

Do not modify test code without approval.

## Automation Philosophy

- Minimal changes
- Clear test intent
- Readable keywords
- Stable execution
- Strong assertions
- Useful failure messages
- Low maintenance cost
- Consistent project structure

Prefer the simplest reliable solution.

## Tool Guidance

Use the best available tool for the task:

- Use Robot Framework MCP when available and useful for structured Robot analysis.
- Use CLI for local execution, quick searches, git diffs, and test runs.
- Use file search/read tools for repository inspection.
- Avoid complex tooling when a local read or command is enough.

## Robot Framework Standards

Use Robot Framework 6.x+ conventions where possible.

Recommended style:

- Space-separated format
- 4-space indentation for continuation lines
- Descriptive test names
- Descriptive keyword names
- Business-readable steps
- Meaningful tags
- Short documentation
- No hard-coded environment data
- No duplicated setup logic

Example:

```robot
*** Test Cases ***
Verify User Can Submit Valid Request
    [Documentation]    Validates the critical happy path for request submission.
    [Tags]    smoke    regression    request
    Given A Valid User Is Authenticated
    When The User Submits A Valid Request
    Then The Request Should Be Created Successfully
```

## Project Structure Guidance

Keep executable automation code in resource files and supporting libraries.

Recommended separation:

- Test cases: readable scenario flow
- Resource files: reusable business and technical keywords
- Variables: environment, test data references, constants
- Libraries: custom Python/Java logic only when necessary
- Test data: external files when data is large or reused

Avoid putting complex logic directly inside test cases.

## Keyword Design

Good keywords are:

- Single-purpose
- Named by behavior, not implementation
- Reusable
- Easy to read
- Easy to debug
- Validated with meaningful assertions

Examples:

```robot
Submit Valid Booking Request
Verify Booking Status Should Be Confirmed
Create Test User With Default Permissions
```

Avoid:

```robot
Click Button 1
Do Stuff
Validate Data
```

## Keyword Layers

Use layers to keep tests readable:

1. **Test case layer:** business scenario
2. **Business keyword layer:** user or system action
3. **Technical keyword layer:** UI/API/DB/file operation
4. **Library/helper layer:** custom logic when needed

## Robustness Rules

Always consider:

- Preconditions
- Cleanup
- Test independence
- Explicit waits
- Retry only when justified
- Meaningful failure messages
- Logs for debugging
- Deterministic test data
- Avoiding fixed sleeps

Example retry pattern:

```robot
Wait Until Keyword Succeeds    60s    5s    Verify Request Status    ${request_id}    COMPLETED
```

Use retries for asynchronous behavior, not to hide unstable tests.

## Assertions

Assertions should validate values, not just existence.

Weak:

```robot
Should Not Be Empty    ${response}
```

Better:

```robot
Should Be Equal As Strings    ${response.status}    APPROVED    msg=Expected APPROVED but got ${response.status}
```

Validate:

- Status
- Data values
- Required fields
- Error messages
- Logs or events when relevant
- Side effects
- Persistence
- Downstream outputs

## Test Data

Use:

- Synthetic data
- Anonymized data when realism is required
- Clear naming
- Cleanup after test execution
- External files for large datasets
- Versioned datasets for regression

Avoid:

- Production personal data
- Customer-sensitive data
- Credentials in code
- Environment-specific hardcoding
- Shared mutable data without cleanup

## Manual to Automated Conversion

Steps:

1. Understand the manual test objective.
2. Identify the real validation points.
3. Remove vague or duplicate steps.
4. Decide the best automation layer: API, integration, UI, database, file, or hybrid.
5. Define preconditions and cleanup.
6. Create business-readable test flow.
7. Implement reusable keywords.
8. Add strong assertions and failure messages.
9. Run locally.
10. Check stability before adding to CI/CD.

Not every manual test should be automated. Automate high-value, stable, repeatable checks.

## Automation Candidate Criteria

Good candidates:

- Critical paths
- Smoke checks
- Regression scenarios
- API contract checks
- Data transformation checks
- Repetitive validations
- Stable requirements
- High business impact

Poor candidates:

- Unstable requirements
- One-time checks
- Highly subjective UX judgment
- Visual-only validation without proper tooling
- Scenarios requiring excessive maintenance

## PR Review Checklist for Robot Tests

- Test name clearly states behavior
- Test can run independently
- Tags are useful
- Setup and teardown are correct
- No hard-coded credentials or secrets
- No fixed sleeps unless justified
- Assertions are meaningful
- Failure messages help debugging
- Keywords are reusable and not over-engineered
- Test data is controlled and cleaned up
- Existing style is respected
- CI impact is acceptable

## Debugging Guidance

When a Robot test fails:

1. Read the failure message.
2. Check `log.html` and `report.html`.
3. Identify whether the failure is product, test data, environment, timing, selector, or automation logic.
4. Reproduce locally if possible.
5. Fix the root cause, not only the symptom.
6. Add logging or better assertions if failure is hard to diagnose.

Useful commands:

```bash
robot --test "Test Name" tests/
robot --include smoke tests/
robot --rerunfailed output.xml tests/
rebot --merge output.xml rerun.xml
```

## CI/CD Guidance

Recommended pipeline split:

- Pull request: lint, static checks, small smoke suite
- Merge/main: smoke and critical regression
- Nightly: broader regression
- Pre-release: full regression and integration checks

Track:

- Pass rate
- Failure reasons
- Flaky tests
- Execution time
- Coverage of critical flows

Do not let flaky tests become ignored noise. Fix, quarantine, or remove them from blocking gates until stable.

## Refactoring Rules

When refactoring:

- Keep behavior unchanged unless requested
- Change the smallest safe scope
- Preserve existing naming patterns when reasonable
- Improve readability without over-engineering
- Extract repeated logic only when it reduces maintenance
- Run affected tests after changes

## Output Format When Reviewing Code

Use this concise format:

```text
Summary:
- [Main finding]

Recommended change:
- [Specific action]

Risk:
- [Low/Medium/High and why]

Validation:
- [Command or test to run]
```

Show diffs or snippets only when useful. Avoid pasting full files unless requested.
