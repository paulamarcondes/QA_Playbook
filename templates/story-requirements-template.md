# Story / Requirements Template

Use this template to make stories clear, testable, and risk-aware before development starts.

---

## Story summary

**Title:**  
**Owner:**  
**Feature / Area:**  
**Related ticket / link:**  
**Date:**  

---

## User value

**Who needs this?**  

**What problem does it solve?**  

**What user or business outcome should improve?**  

---

## Scope

### In scope

- 

### Out of scope

- 

---

## Risk level

**Risk Level:** Low / Medium / High / Critical

Reason:

- 

Consider higher risk when the story affects critical flows, integrations, data, permissions, security, accessibility, payments, compliance, or production stability.

Reference: [Test Strategy Template](test-strategy-template.md)

---

## Requirements

| Requirement | Notes |
|---|---|
| Main behavior |  |
| Business rules |  |
| Validation rules |  |
| Error handling |  |
| Dependencies |  |
| Data needed |  |

---

## Acceptance criteria

Use clear, testable examples.

```gherkin
Given ...
When ...
Then ...
```

Acceptance criteria:

1. 
2. 
3. 

---

## Interface / contract details

Use when the story involves APIs, files, events, integrations, data mappings, or external systems.

| Item | Details |
|---|---|
| Provider |  |
| Consumer |  |
| Request / input |  |
| Response / output |  |
| Required fields |  |
| Optional fields |  |
| Error responses |  |
| Authentication / authorization |  |
| Backward compatibility risk |  |
| Example payload / file |  |

Checklist:

- [ ] API, file, data, or interface contract is documented.
- [ ] Required and optional fields are clear.
- [ ] Valid and invalid examples are available when useful.
- [ ] Consumer expectations are understood.
- [ ] Contract test need was considered.

---

## Security and permissions

- [ ] Roles and permissions are clear.
- [ ] Least privilege is considered.
- [ ] Sensitive data is protected.
- [ ] Audit or traceability needs are clear when relevant.
- [ ] Unauthorized access scenarios are considered.

Notes:

- 

---

## Accessibility and user experience

Use when the story affects UI, content, navigation, forms, messages, or user interaction.

- [ ] Labels and messages are clear.
- [ ] Error feedback is understandable.
- [ ] Keyboard navigation is considered when relevant.
- [ ] Color or visual-only feedback is not the only signal when relevant.
- [ ] User friction or confusion risks were discussed.

Notes:

- 

---

## Observability

- [ ] Important failures should be logged.
- [ ] Useful IDs or status values should be available for troubleshooting.
- [ ] Sensitive data should not appear in logs.
- [ ] Monitoring or alert needs were considered when relevant.

Notes:

- 

---

## Testing notes

| Area | Notes |
|---|---|
| Positive scenarios |  |
| Negative scenarios |  |
| Edge cases |  |
| Regression areas |  |
| Automation candidates |  |
| Test data |  |
| Environment needs |  |

---

## Definition of Ready checklist

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Risk level is defined.
- [ ] Dependencies are known.
- [ ] Interface or contract is documented when relevant.
- [ ] Security, permissions, and accessibility were considered when relevant.
- [ ] Test data and environment needs are understood.
- [ ] Story aligns with [01 - Before Development](../01-before-development.md) standards.
