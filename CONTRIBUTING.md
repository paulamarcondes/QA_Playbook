# Contributing

Open an issue for anything structural. Send a pull request for corrections and small additions.

**In scope:** practices a team can apply on Monday. Every addition should survive one question: **what does a team do differently after reading this?** Not tool tutorials, vendor comparisons, certification material, or theory with no practical use.

## House rules

- Plain language. Tables, bullets, and checklists over paragraphs.
- Hyphen `-`, never an em dash.
- Real-world over textbook. If a practice rarely survives delivery pressure, say so.
- Every number carries a citable source.
- Synthetic or anonymized data only, templates included.
- Say a thing once, then link to it. Exception: `ai-tools/`, where safety rules stay duplicated because those files are often loaded alone.
- Refer to a section by **name**, never by number: `[Map risk](01-before-development.md#4-map-risk-before-defining-test-depth)` breaks loudly when a section is renumbered and the checker reports it, while "see 01 §4" rots silently. When you do renumber, update every cross-reference and note it in [CHANGELOG.md](CHANGELOG.md).
- New references go in `resources/`, new fill-in artifacts in `templates/`, plus a row in the matching README table.
- No hardcoded counts, versions, or dates in prose. The version lives in the changelog, the file lists in the README tables, and "last updated" is a badge GitHub fills in.

## Diagrams

Mermaid only, so the source is reviewable in a pull request.

- WCAG 2.2 AA, verified on light and dark GitHub themes.
- Never colour alone. Pair it with a label or shape, and add a text equivalent nearby.
- Every node carries explicit `fill`, `stroke`, and `color`, or it inherits the viewer's theme and disappears in one of the two.

### Palette

GitHub renders each diagram in isolation, so these values repeat in every file. **Copy them from here, not from a nearby diagram**, or the palette drifts.

| Role | classDef |
|---|---|
| Before phase, neutral step | `fill:#d6deea,stroke:#3f4f68,color:#222a38` |
| During phase, medium risk, caution | `fill:#ecdcb8,stroke:#6e5418,color:#3d3115` |
| After phase, low risk, go | `fill:#d4e4d8,stroke:#2f5a43,color:#1f3329` |
| Check, decision, AI step | `fill:#d4dcf0,stroke:#38507e,color:#20284a` |
| High risk | `fill:#ecc9b0,stroke:#8a4423,color:#3f2614` |
| Critical, no-go, defect | `fill:#e6c2c4,stroke:#7a3338,color:#38191b` |

**Red is reserved for risk and severity.** For a gradient that is not risk, such as the cost ramp in the test pyramid, use a single-hue blue ramp: `#e3eaf4` to `#c9d6e8` to `#aec2dc`, strokes `#4a5f80`, `#3f4f68`, `#2f3d56`.

## Before opening a pull request

```bash
python .github/tools/check-links.py
```

It checks every internal link and anchor, and runs again automatically on the pull request. The rest is by eye:

- [ ] No em dashes.
- [ ] Section numbering still runs 1, 2, 3.
- [ ] Diagrams render correctly on light **and** dark themes.
- [ ] [CHANGELOG.md](CHANGELOG.md) updated.

Contributions are released under the [MIT Licence](LICENSE). The *Bugs Have Feelings Too* cartoon is excluded: Copyright 2010 Andy Glover, used with permission, not sub-licensable.
