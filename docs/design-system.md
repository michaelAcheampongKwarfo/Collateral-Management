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

## Field widths

Controls are sized to the length of the value they hold, not stretched to fill the column. Labels and fields stay left-aligned on a two-column grid, so the edges still line up.

| Size | Width | Used for |
|---|---|---|
| `xs` | 120px | Percent, number of months, number of shares |
| `sm` | 180px | Customer number, dates, phone numbers, insurance code, folio numbers |
| `md` | 220px | Amounts, branch (`010 · SINKOR`), currency (`010 · GHANA CEDIS`), short text |
| `lg` | 300px | Product (`220 · SAVINGS PERSONAL`), shorter code lookups (policy type, deposit type, property type), valuer name |
| `xl` | 420px | Long-name lookups: source account, financial institution, insurance company, share code |
| `2xl` | 560px | Ownership name, location, comment |

Each field type has a default size, and a field definition can override it (`w: 'sm'`). On phones the grid becomes one column; fields keep their size but never grow wider than the screen.

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
