# Robot Framework QA Skill

Use this skill to support Robot Framework automation with clean, maintainable, and readable tests.

---

## Project rule

Keep test cases as plain text documentation of behavior.

Put executable logic in Resource files.

This keeps tests readable and makes keywords reusable.

---

## Robot Framework principles

- Use clear test names.
- Keep test cases short and business-readable.
- Move implementation details to resource keywords.
- Avoid duplicated steps.
- Use meaningful setup and teardown.
- Prefer stable selectors, endpoints, and test data.
- Log useful context for troubleshooting.
- Keep assertions clear.
- Avoid over-engineering.

---

## Recommended structure

```text
/tests
  feature_name_tests.robot
/resources
  feature_name_keywords.resource
  api_keywords.resource
  data_keywords.resource
/variables
  test_data.yaml
```

---

## Test case style

Good test case:

```robot
*** Test Cases ***
User Can Create A Valid Order
    Given A Valid Customer Exists
    When The Customer Creates A New Order
    Then The Order Should Be Created Successfully
    And The Order Status Should Be Pending
```

The executable implementation should live in resource keywords.

---

## Keyword quality checklist

- [ ] Keyword name is clear.
- [ ] Keyword has one main responsibility.
- [ ] Arguments are explicit.
- [ ] Repeated logic is reused.
- [ ] Assertions are meaningful.
- [ ] Logs help troubleshooting.
- [ ] Errors are understandable.
- [ ] Sensitive data is not logged.

---

## Automation decision checklist

Automate when the scenario is:

- valuable;
- repeatable;
- stable;
- connected to regression risk;
- useful for fast feedback;
- maintainable.

Avoid automation when the scenario is unclear, unstable, or unlikely to be repeated.

---

## AI-assisted Robot review

When AI generates Robot Framework code, check:

- Does the keyword match the real project style?
- Are test cases still readable?
- Was executable logic kept in resource files?
- Are locators, endpoints, and data realistic?
- Are assertions correct?
- Are there hallucinated libraries or keywords?
- Is sensitive data protected?
