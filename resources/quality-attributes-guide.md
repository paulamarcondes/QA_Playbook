# Quality Attributes Guide

Accessibility, internationalization, security, performance, and privacy are not extra testing. They are the qualities a product either has or does not, and they fail in ways functional testing never sees: a form that works perfectly and cannot be reached by keyboard, a date that reads 03/04 in two countries and means two different days, an endpoint that returns the right data to the wrong user.

They are grouped here because they share a shape. Each one is cheap to design in, expensive to retrofit, invisible on a happy-path demo, and increasingly a legal obligation rather than a preference.

> **Key idea:** Functional testing asks whether the feature works. These five ask whether it works *for everyone, everywhere, safely, fast enough, and without leaking anything*.

Each section follows the same four parts: **what breaks**, **the minimum bar**, **how to test it**, and **what blocks a release** - with the evidence that proves it.

Vocabulary note: the industry calls these *non-functional requirements*, or *product quality characteristics* in ISO/IEC 25010. Both names are unhelpful, because to a user a product that cannot be operated with a screen reader is not "non-functional", it is broken.

## 1. Accessibility

Whether people with disabilities can use the product. Permanent (blindness), temporary (a broken arm), or situational (bright sunlight, one hand on a phone).

### What breaks

- Forms reachable with a mouse but not with a keyboard, so nobody using a screen reader can submit.
- Error messages announced only by turning a field border red.
- Buttons labelled by an icon with no accessible name, read aloud as "button".
- Focus that disappears inside a modal, or never returns after it closes.
- Text at 3:1 contrast that the designer approved on a high-end monitor.
- Content that breaks when the user zooms to 200% or enlarges text.

### The minimum bar

**WCAG 2.2 Level AA.** It is the bar named by the European Accessibility Act, by [EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) for public procurement in the EU, and by US Section 508. For a multinational product, AA is not a stretch goal, it is the floor that keeps the product sellable.

Four principles, worth knowing by name because they are how every requirement is grouped - content must be **perceivable, operable, understandable, and robust**.

### How to test it

| Check | How | Catches |
|---|---|---|
| Keyboard only | Unplug the mouse. Tab through the whole flow. | Traps, unreachable controls, invisible focus |
| Automated scan | axe, Lighthouse, WAVE, or the equivalent in your pipeline | ~30-40% of issues: contrast, missing labels, ARIA misuse |
| Screen reader | NVDA or JAWS on Windows, VoiceOver on macOS and iOS | Unlabelled controls, meaningless reading order |
| Zoom and reflow | 200% zoom, 320px viewport width | Content clipped or overlapping |
| Contrast | Any contrast checker, on both light and dark themes | Text that disappears in one theme |
| Forms and errors | Submit an empty and an invalid form | Errors signalled by color alone, unlinked labels |

> **The trap:** an automated scan finds at most 30-40% of accessibility issues and reports a clean pass on a page nobody can actually operate. The keyboard test takes two minutes and finds the blocking problems the scanner never sees. Never report "accessible" on the strength of a green scan.

### What blocks a release

Any critical user journey that cannot be completed by keyboard alone. Any form error that is not announced to assistive technology. Any new text below AA contrast.

**Evidence:** scan report, a short keyboard-only walkthrough recording, screen reader notes for the critical journey, contrast values for new colors.

## 2. Internationalization and localization

**Internationalization (i18n)** is building the product so it *can* adapt to a locale. **Localization (l10n)** is the adaptation itself: translation, formats, content. i18n is an architecture property and QA should challenge it before code exists; l10n is content and QA validates it per market.

For a company operating in several countries, this is the single most under-tested area in this guide, because every developer and every tester is working in one locale and everything looks fine.

### What breaks

| Problem | The real failure |
|---|---|
| Date formats | `03/04/2026` is 3 April in London and 4 March in Chicago. Silent, and wrong in reports, audits, and SLAs. |
| Time zones and DST | A job scheduled "at midnight" runs on the wrong day for half the users. DST transitions create hours that happen twice or never. |
| Number and currency formats | `1,000.50` versus `1.000,50`. A parser that assumes one produces a 1000x error in the other. |
| Text expansion | German runs 30-40% longer than English. Buttons and table headers clip or overlap. |
| Right-to-left | Arabic and Hebrew mirror the entire layout, including icons that imply direction. |
| Character sets | Names with accents, Cyrillic, CJK, emoji. Anything that assumes one byte per character corrupts them. |
| Sorting and search | Alphabetical order is locale-specific. So is case-insensitive matching. |
| Names, addresses, phone formats | Required "first name / last name" and fixed postcode formats exclude real people in real countries. |
| Hardcoded strings | Text concatenated in code cannot be translated, and word order differs between languages. |

### The minimum bar

- All user-facing text comes from resource files, never concatenated in code.
- All timestamps stored in UTC, converted only for display, with the time zone visible where it matters.
- Dates, numbers, and currency formatted by locale, never by string manipulation.
- UTF-8 end to end: database, API, files, logs.
- Layout survives a 40% text expansion and a 200% zoom.

### How to test it

- **Pseudo-localization** before any translation exists: replace strings with a longer, accented version of themselves (`[Ŝűƀɱíţ ƒőŕɱ ~~~]`). Every hardcoded string and every clipped layout appears in one pass, in a build nobody had to translate.
- Set the test environment to a non-default locale and time zone, and keep one there permanently.
- Include one RTL locale if the product ships to any RTL market.
- Include boundary dates: DST transitions, leap day, year end, midnight in a time zone 12 hours away.
- Test names and addresses that are not Anglo-American.

### What blocks a release

Clipped or unreadable text in a supported locale. Any date, time, or currency displayed or stored ambiguously. Data corruption on non-ASCII input.

**Evidence:** screenshots in at least one long-text locale and one RTL locale, a date and time zone test matrix, pseudo-localization pass results.

## 3. Security

QA is not a penetration tester, and should not pretend to be. QA *is* the person who asks whether a user can reach something they should not, and who checks that the answer was tested rather than assumed.

### What breaks

- Authorization checked in the UI but not in the API, so hiding a button hides nothing.
- **IDOR** (Insecure Direct Object Reference): changing `/orders/1041` to `/orders/1042` returns someone else's order.
- Secrets committed to the repository or printed into logs.
- Dependencies with known CVEs, shipped because nobody watched the scan.
- Errors that leak stack traces, queries, or internal hostnames to the user.
- Input validated on the client only.

### The minimum bar

| Layer | What runs | Who owns it |
|---|---|---|
| **SAST** | Static analysis of source for vulnerable patterns | Dev, in CI |
| **SCA** | Dependency and license scan for known CVEs | Dev, in CI |
| **Secrets scanning** | Blocks credentials from entering the repo | Platform, pre-commit and CI |
| **DAST** | Scans the running application | Security, scheduled |
| **Penetration testing** | Human, adversarial, scoped | Specialists, periodic |
| **Authorization testing** | Every role against every protected resource | **QA** |

The last row is the one QA owns outright, and the one most often skipped.

### How to test it

The practical QA version, worth running on every change that touches permissions:

1. Build a small matrix: roles down the side, protected actions across the top.
2. For each cell, call the **API directly**, not the UI. Bypass the interface entirely.
3. Confirm the response is a clean refusal, not the data, and not a stack trace.
4. Repeat with an expired token, no token, and another tenant's token.
5. Change one ID in the URL to a record you do not own.

> **Principle:** if a permission rule is only enforced in the UI, it is not enforced. Test every authorization rule at the layer that actually decides.

### What blocks a release

Any unauthorized access to data. Any secret in the repo, logs, URLs, or error messages. Any unresolved critical or high CVE in a shipped dependency.

**Evidence:** role-versus-resource matrix with results, API responses for the refusal cases, clean SAST/SCA runs on the changed code.

## 4. Performance

Performance testing fails most often not because the tests are wrong, but because nobody agreed what "fast enough" means, so the results cannot be judged.

### What breaks

- A query that is fine against 1,000 test records and unusable against 10 million production rows.
- An endpoint that works one user at a time and collapses at fifty.
- A batch job that grows past its window and starts overlapping the next run.
- A memory leak invisible in a 10-minute test and fatal after four days.
- A downstream timeout no one configured, so a slow dependency becomes a total outage.

### The minimum bar

Agree the numbers **before** testing, in the story, not after the results arrive:

| Question | Example answer |
|---|---|
| How many concurrent users or requests? | 200 concurrent, 50 requests/second peak |
| How fast, at which percentile? | p95 under 800 ms, p99 under 2 s |
| How much data? | 10 million records, 5 years of history |
| How long must it hold? | Stable for 24 hours with no memory growth |
| What happens at the limit? | Queue and degrade, never drop or corrupt |

> **Use percentiles, not averages.** An average response time of 300 ms can hide a p99 of 11 seconds, which is the experience of your most active users, on your busiest day.

### How to test it

Pick the type that matches the question: **load** (does it hold at expected peak), **stress** (where does it break, and does it break safely), **soak** (does it survive days, not minutes), **volume** (does it survive production-sized data), **spike** (does it survive a sudden 10x, and recover). Definitions: [Testing Types Reference](testing-types.md).

Run against production-like data volume. A performance test on an empty database measures nothing.

### What blocks a release

A critical journey missing its agreed target. Unbounded resource growth. Failure at the limit that loses or corrupts data rather than degrading.

**Evidence:** response times by percentile against the agreed target, resource usage over the run, the breaking point and the behavior at it.

## 5. Privacy and test data

Every environment that holds a copy of production data is a copy of the breach. This section is where the playbook's "synthetic data only" rule becomes a method.

### What breaks

- A production dump copied into staging "just for this test", and left there.
- Personal data written into logs, then shipped to a third-party log platform.
- Personal data pasted into an AI assistant prompt.
- Test accounts using real customer email addresses, which receive real test emails.
- Data copied across a border into a region where it is not permitted to sit.
- Test data never deleted, so retention limits are breached in a non-production system nobody audits.

### The minimum bar

| Rule | In practice |
|---|---|
| **Synthetic first** | Generate test data. It is safer, reproducible, and easier to reason about at boundaries. |
| **Masked second** | If realism is genuinely required, irreversibly mask before the data leaves production - referentially consistent, so joins survive. |
| **Never raw** | A production copy in a lower environment is a reportable incident waiting for a date. |
| **No personal data in logs** | Log an identifier, never the person. Correlation IDs exist for this. |
| **No personal data in prompts** | Applies to every AI tool, including the ones in this playbook. |
| **Residency respected** | Data that must stay in a region stays in that region, test environments included. |
| **Retention applies** | Test data expires too. Know who deletes it and when. |

**PII** (personally identifiable information) is broader than most teams assume: names, emails, phone numbers, addresses, IP addresses, device identifiers, precise location, government identifiers, health and biometric data, and any combination that identifies someone indirectly.

### How to test it

- Search logs for personal data after running a full journey. Grep for the test user's name, email, and identifiers.
- Confirm what third parties receive: analytics, error trackers, log platforms, support tools.
- Check that deletion is real. Ask for an account to be deleted, then look for it in backups, caches, search indexes, and downstream systems.
- Check that an export request returns everything the system holds about a person.

### What blocks a release

Personal data in logs or error messages. Production data in a non-production environment. A deletion path that leaves the data recoverable in a downstream system.

**Evidence:** test data source and generation method, log scan results, the list of third parties receiving data, deletion verification.

## 6. Where these land across the three phases

None of these are a phase of their own. They are decisions made early and verified continuously.

| Attribute | [01 - Before](../01-before-development.md) | [02 - During](../02-during-development.md) | [03 - After](../03-after-development.md) |
|---|---|---|---|
| Accessibility | Name the AA bar in the AC; check designs for contrast, focus order, labels | Keyboard pass and automated scan per change | Real assistive-technology use, user feedback |
| i18n / l10n | Confirm locales, time zones, and text direction in scope | Pseudo-localization, non-default locale environment | Locale-specific error rates and support tickets |
| Security | Threat-think the change: who could reach what | Authorization matrix, SAST/SCA in CI, PR review | Dependency alerts, access anomalies, incident review |
| Performance | Agree targets and data volume as acceptance criteria | Profile the changed path; catch N+1 queries in PR review | Real latency percentiles, saturation, trend |
| Privacy | Identify personal data, residency, and retention up front | Log scan, masked or synthetic data only | Deletion and export verification, third-party review |

> **Practical reminder:** you will not get all five onto every story, and pretending otherwise produces a checklist the team quietly stops reading. Pick the ones the change actually touches. A permissions change is a security story. A new screen is an accessibility story. A new market is an i18n story. A report over five years of history is a performance story.

## Related

- [Testing Types Reference](testing-types.md) - the full catalogue of testing types and a context-to-validation map
- [Clean Code Review Guide for QA](clean-code-guide.md) - what to look for in a PR, including security and observability
- [01 - Map risk before defining test depth](../01-before-development.md#4-map-risk-before-defining-test-depth) - the override that keeps safety, money, personal data, and compliance above Low risk
