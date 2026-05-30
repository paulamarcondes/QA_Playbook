# Quality Review Checklist

A quick checklist to support quality decisions before, during, and after development.

Use this as a lightweight reminder, not a heavy process.

---

## Before development

- [ ] User value is clear.
- [ ] Acceptance criteria are testable.
- [ ] Risk level is defined.
- [ ] Dependencies are known.
- [ ] Interface or contract expectations are documented when relevant.
- [ ] Security and permissions are considered.
- [ ] Accessibility is considered for user-facing changes.
- [ ] Test data and environment needs are clear.
- [ ] Testing approach is roughly agreed.
- [ ] Story meets Definition of Ready.

---

## During development

- [ ] PR review considers quality risks.
- [ ] Unit test strategy was reviewed when relevant.
- [ ] Contracts, payloads, and mappings were checked when relevant.
- [ ] Logs and errors support troubleshooting.
- [ ] Sensitive data is protected.
- [ ] Pair testing was used for high-risk work when useful.
- [ ] Automation was added or updated when it provides useful feedback.
- [ ] Bugs include technical context and impact.
- [ ] AI-generated output was reviewed by a human when used.

---

## Before release

- [ ] Acceptance criteria are met.
- [ ] Relevant regression risk was covered.
- [ ] Critical checks passed.
- [ ] Known issues are documented.
- [ ] Rollback or recovery plan is understood when needed.
- [ ] Monitoring or logs are available for important flows.
- [ ] Deployment validation plan is clear.
- [ ] Stakeholders understand remaining risks.

---

## After release

- [ ] Production signals were reviewed.
- [ ] Critical flows are behaving as expected.
- [ ] Incidents or high-severity bugs were reviewed.
- [ ] Metrics were updated when relevant.
- [ ] Missed risks were added to the strategy or checklist.
- [ ] Automation candidates were reviewed.
- [ ] One improvement action was captured.

---

## 15-minute quality retro

Use after releases or production incidents:

1. What went well?
2. What was missed?
3. What risk should have been clearer?
4. What test, log, automation, or checklist should improve?
5. What is the next action?
