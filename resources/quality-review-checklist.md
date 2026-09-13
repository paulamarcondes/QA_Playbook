# Quality Review Checklist

The questions to ask out loud - in refinement, in PR review, in bug triage, in the release call, and after something goes wrong.

> **How this differs from the phase checklists:** the checklists at the end of [01](../01-before-development.md#before-development-checklist), [02](../02-during-development.md#during-development-checklist), and [03](../03-after-development.md#after-development-checklist) confirm the work was done. This page is what a reviewer asks to find out whether it was done *well*. Focus on outcomes, not checkbox theater.

## Before development

- [ ] What is the user or business problem, and who is the affected user or system?
- [ ] Are the acceptance criteria specific and observable enough to test without guessing?
- [ ] What are the negative paths and edge cases, and which did we deliberately leave out?
- [ ] Which systems, APIs, files, events, permissions, or configurations does this touch?
- [ ] What is the risk level, and does the planned test depth actually match it?
- [ ] Is the test data available, or is there a plan with an owner and a date?
- [ ] If this breaks in production, how would we find out?
- [ ] What would make us say this story is *not* ready?

## During development

- [ ] Which risks are protected by developer tests, and which still need QA validation?
- [ ] Can this be validated below the UI, or is the UI the only way in?
- [ ] What existing flows, contracts, permissions, or data could this change affect?
- [ ] Are failures explicit and safe, and would the team diagnose one from the logs alone?
- [ ] Were static analysis findings reviewed, or dismissed to keep the build green?
- [ ] Do user guides or how-to-test notes need updating?
- [ ] What did we choose not to test, and why is that acceptable?

## Bug classification

- [ ] Does the behavior violate a requirement, acceptance criterion, contract, user need, or quality standard?
- [ ] Is it a regression in something that used to work?
- [ ] Is it the product, or is it test data, environment, or setup?
- [ ] Is it expected behavior that is simply undocumented?
- [ ] Is it actually a feature request or a product decision?
- [ ] Is the impact clear enough to argue severity and priority *separately*?
- [ ] Could a developer start investigating from this report alone?

## Before release

- [ ] What is the residual risk, and who accepted it by name?
- [ ] Which critical flows are proven, and by what evidence?
- [ ] If this goes wrong, what is the rollback or mitigation, and who can trigger it?
- [ ] What will we watch after deploy, for how long, and who is watching?
- [ ] Does leadership have the risk picture, not just the test counts?

## After release

- [ ] What did production tell us that testing did not?
- [ ] Did a user detect something before we did?
- [ ] Which single change would have caught this earlier?
- [ ] Did each improvement action get an owner and a date, or just a nod in the retro?
