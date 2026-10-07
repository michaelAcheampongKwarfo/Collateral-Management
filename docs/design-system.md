# UI Design System (Collateral Management)

The visual rules used by the prototype, so the Angular build and later modules (Amendment, Cancellation) look the same.

## Principles

1. **One task per page, in steps.** Customer, then type, then details. Each step shows a check mark once it is complete.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`). Every lookup shows the code and its description.
3. **Read-only looks read-only.** System-filled values sit on a grey fill with no border. Editable fields have a border.
4. **Errors tell you what to do.** "Enter the policy number." appears next to the field and in a summary at the top of the form.
5. **Keyboard first.** Enter fetches the customer. Arrow keys and Enter work in every lookup. Esc closes dialogs. Tab order follows the screen.

## Tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--primary` | `#0B5CAD` | `#5AA2EE` | Primary button, focus, active nav |
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
