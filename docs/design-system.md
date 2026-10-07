# UI Design System (Collateral Management)

The visual rules used by the prototype, so the Angular build and later modules (Amendment, Cancellation) look the same.

## Principles

1. **One task per page, in steps.** Customer, then type, then details. Each step shows a check mark once it is complete.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`). Every lookup shows the code and its description.
3. **Read-only looks read-only.** System-filled values sit on a grey fill with no border. Editable fields have a border.
4. **Errors tell you what to do.** "Enter the policy number." appears next to the field and in a summary at the top of the form.
5. **Keyboard first.** Enter fetches the customer. Arrow keys and Enter work in every lookup. Esc closes dialogs. Tab order follows the screen.

## Standard action bar

Every module screen (Creation, Amendment, Cancellation, …) uses the same action bar, top right of the page header, in this order and colour:

| Order | Button | Colour | Style | Action |
|---|---|---|---|---|
| 1 | Help | Blue | Tinted (blue border and text) | Opens the help panel for the screen |
| 2 | Comment | Blue | Tinted | Opens the comments panel. Shows a count when comments exist |
| — | *divider* | | | Separates the information actions from the record actions |
| 3 | New | Blue | Tinted | Clears the screen for a new record |
| 4 | Submit | Green | Solid (the only solid button) | Validates and saves the record |
| 5 | Exit | Red | Tinted (red border and text) | Leaves the screen |

Rules:
- The order, colours and icons do not change between screens. A screen that does not need an action disables it rather than removing it, so buttons never shift position.
- Buttons share a minimum width (104px) so the bar looks the same whatever the label.
- Submit is the only solid button on the page, which makes it the primary action.
- On narrow screens the buttons wrap and stretch to fill the row, keeping the same order.

| Token | Light | Dark |
|---|---|---|
| `--act-blue` | `#0B5CAD` | `#6AAEF2` |
| `--act-green` | `#1D7A4C` | `#3FB57A` |
| `--act-red` | `#B42318` | `#F2867B` |

## Form layout: 12-column grid

Every form section is a 12-column grid. Each field spans a number of columns that matches the length of its value, and **every row adds up to exactly 12**. Fields stay proportional to their content, and the left and right edges of every row line up.

| Columns | Used for |
|---|---|
| 4 (one third) | Amounts, dates, codes, folio numbers, rates, counts, short lookups (policy type, currency), branch |
| 5–7 | Paired descriptive values: ownership name / location, property type / sub-type, deposit type / collateral type |
| 8 (two thirds) | Long-name lookups (source account, financial institution, insurance company), product, valuer name. Always paired with a 4-column field |
| 12 (full row) | Comment |

Standard row patterns:

| Pattern | Example |
|---|---|
| 8 + 4 | Source account + Source branch · Financial institution + Branch · Insurance company + Insurance code |
| 4 + 4 + 4 | Amount considered + Review date + Expiry date (the closing row of every collateral type) · Folio number + Start + End |
| 6 + 6 | Property type + Sub property type · Share code + Index |
| 12 | Comment |

Sections:
- Each form is split into short sections (for example *Property details*, *Valuation*, *Collateral details*). Each section has a position marker (`01 / 03`), a title and a one-line description.
- When the form is wide (880px or more), section titles move into a left column and the fields sit to the right.
- Auto-filled fields have a grey fill, a lock icon and an "Auto-filled" tag next to the label.
- On phones every field takes the full row.

## Tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--primary` | `#0B5CAD` | `#5AA2EE` | Focus ring, active nav, links |
| `--bg` | `#F2F5F9` | `#0E1522` | Page background |
| `--surface` | `#FFFFFF` | `#151E2E` | Cards, inputs |
| `--sunken` | `#EEF2F7` | `#111A28` | Read-only fields, code chips |
| `--fg` / `--muted` | `#13223A` / `#5A6A80` | `#E5ECF5` / `#9AA9BE` | Text |
| `--danger` | `#B42318` | `#F2867B` | Required asterisk, errors |
| `--success` | `#1D7A4C` | `#5CC892` | Completed steps, *Approved* |
| `--warn` | `#9A5A00` | `#E9B15C` | *Pending approval*, corporate badge |

Each collateral type has an identifying colour, used only on its tile and form heading: Cash `#1D7A4C`, Insurance `#6A4BC2`, Property `#B05E0C`, Guarantee `#0B5CAD`, Shares `#0D7A84`.

**Type:** Public Sans for the interface, IBM Plex Mono for codes, account numbers and amounts (tabular figures so columns line up). Sizes: 24 page title, 15.5 card title, 14 body, 12.5 labels, 11.5 uppercase section labels.

**Shape:** 6px radius on controls, 10px on cards. 38px control height. 16–20px grid gap.

## Components

| Component | Behaviour | Angular Material equivalent |
|---|---|---|
| Lookup field (LOV) | Button showing `code · description`. Opens a searchable dialog. Disabled until its parent field is set. | `mat-dialog` + `mat-table`, or `mat-autocomplete` for short lists |
| Amount input | Right-aligned, currency prefix, formatted `1,234.56` on blur | `matInput` + custom formatter directive |
| Date input | Native date picker. Displayed as `DD-MON-YYYY` in tables, matching Oracle | `mat-datepicker` with a custom date format |
| Type tiles | Radio group of cards | `mat-radio-group` with custom card template |
| Summary panel | Live summary + required-field progress | Standalone component |
| Drawer | Help and Comments slide in from the right | `mat-sidenav` (mode `over`) |
| Status pill | *Approved* (green), *Pending approval* (amber) | `mat-chip` |

PrimeNG offers equivalents for every row if the team prefers it. The choice of library is open.
