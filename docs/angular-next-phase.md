# Next phase: the Angular build

**Status (11-NOV-2026): on hold, waiting for the green light.** The UI mock-up was presented and approved. Discussions on the pilot test, security and related matters are still going on. Nothing in this phase starts until the project owner gives the go-ahead.

## What happens on the green light

The prototype (`design/prototype/index.html`) is promoted into the real Angular project. The prototype is plain HTML and JavaScript; it fixes the screens and behaviour, and Angular rebuilds them.

The source of truth for the build:

| What | Where |
|---|---|
| Visual style, widths, colours, components, shortcuts, duplicate rules, history | `docs/design-system.md` (the *Visual style: the bank's new screens* section wins over the older @unionsg/ui section) |
| What each Submit / Approve does in the database, and the proposed API calls and payloads | `docs/*/…-flow.html`, `docs/returned/return-flow.html` |
| Module specs | `docs/creation`, `docs/amendment`, `docs/cancellation`, `docs/approval`, `docs/enquiry`, `docs/returned`, `docs/reporting` |
| Open questions for the PL/SQL team (incl. where GPS coordinates are stored, real column sizes) | *Collateral Management: Questions for the PL/SQL Team* (Claude Docs) |
| Agreed design | Collateral type as **tiles** (`index.html`); `index-type-lov.html` is a comparison copy only |

## Planned work (to confirm on the green light)

1. **Shared Angular components** matching the new style: title banner with back arrow and actions, section bars, underline inputs, lookup (LOV) dropdown, `DD-MON-YYYY` date input, phone input, GPS map picker (Leaflet), data table with pager, read-only details panel, 3-column form grid.
2. **Creation screen first**, wired to the API, as the pattern for the other screens.
3. **Developer handover pack:** one page per screen covering fields, widths, validations, lookup sources, API calls and component names.
4. Amendment, Cancellation, Approvals, Returned, Enquiry and the review report, in that order.

## Inputs still needed before or during the build

- **Pilot test and security** outcomes, which may change scope: authentication and roles, maker-checker enforcement on the server, audit logging, data masking.
- **Angular project details:** version, repository, the UI library or shared components it already has, routing, and how the bank's main menu opens the module.
- **API and backend:** contracts from the PL/SQL / service team, and answers to the open questions.
- **Map provider** approved by IT for the GPS picker (the prototype's public OpenStreetMap and Esri tiles are for demonstration only).
- **Exact brand colours** from the front-end team (the prototype's blues were matched by eye from a photo).
- **Key file** (`fmrweb.res`), to confirm the Oracle Forms keyboard shortcuts.
