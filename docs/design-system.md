# UI Design System (Collateral Management)

The visual rules used by the prototype, so the Angular build and later modules (Amendment, Cancellation) look the same.

## Principles

1. **One task per page, in steps.** Customer, then type, then details. Each step shows a check mark once it is complete.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`). Every lookup shows the code and its description.
3. **Read-only looks read-only.** System-filled values sit on a grey fill with no border. Editable fields have a border.
4. **Errors tell you what to do.** "Enter the policy number." appears next to the field and in a summary at the top of the form.
5. **Keyboard first.** Enter fetches the customer. Arrow keys and Enter work in every lookup. Esc closes dialogs. Tab order follows the screen.

## Standard action bar

Every screen uses the same buttons, in the same order and colours. Each screen shows only the buttons it uses, so nothing on the bar is a dead control.

The bar always sits **on the right of the page header**, on every screen (entry, list, details, approval, enquiry). When a long title pushes it onto its own row it stays right-aligned, so the buttons always end at the same edge.

| Order | Button | Colour | Style |
|---|---|---|---|
| 1 | Help | Blue | Tinted (blue border and text) |
| 2 | Comment | Blue | Tinted |
| — | *divider* | | Separates the information actions from the record actions |
| 3 | New | Blue | Tinted |
| 4 | Submit | Green | Solid (the only solid button) |
| 5 | Exit | Red | Tinted (red border and text) |
| — | Return *(Approvals only)* | Amber | Tinted, before Reject |
| — | Reject *(Approvals only)* | Rose | Tinted (rose border and text, distinct from the red Exit), before the green Authorize |

Which buttons each screen shows, and what New does there:

| Screen | Buttons | New |
|---|---|---|
| Creation | Help, Comment, New, Submit, Exit | Clears the whole screen for a new collateral |
| Amendment / Cancellation search list | Help, New, Exit | Clears the search and shows all collaterals |
| Amendment details | Help, Comment, New, Submit, Exit | Resets every field to its original value. Disabled until something has changed |
| Cancellation details | Help, Comment, New, Submit, Exit | Clears the closure reason. Disabled until a reason is entered |
| Approvals queue | Help, New, Exit | Clears the search |
| Enquiry grids | Help, New, Exit | Clears the search and every filter |
| Enquiry details | Help, Exit | Not shown (read only, as in Forms) |
| Approval request | Help, Comment, Return, Reject, Authorize, Exit | Not shown. Authorize opens the verification checklist; Return and Reject ask for a reason |
| Returned queue | Help, New, Exit | Clears the search |
| Reports | Help, New, Exit | Resets the report parameters |
| Approval request you submitted | Help, Comment, Exit | Not shown (maker-checker: someone else decides) |

Rules:
- The order and colours never change. A button a screen doesn't use is left out, not shown disabled.
- On details pages, **New** and **Submit** switch on together: as soon as there is something to reset, there is also something to submit.
- Buttons share a minimum width (104px) so the bar looks the same whatever the label.
- Submit is the only solid button on the page, which makes it the primary action.
- On narrow screens the buttons wrap and stretch to fill the row, keeping the same order.

| Token | Light | Dark |
|---|---|---|
| `--act-blue` | `#0B5CAD` | `#6AAEF2` |
| `--act-green` | `#1D7A4C` | `#3FB57A` |
| `--act-red` | `#B42318` | `#F2867B` |
| `--act-amber` | `#9A5A00` | `#E9B15C` |
| `--act-rose` | `#B4234F` | `#F08AAB` |

## Form layout: inline labels, fields sized to their values

Changed after the presentation (October 2026): every label sits **on the same line** as its field, on the left, as in Oracle Forms, and each field is only as wide as the values it holds.

| Field | Width |
|---|---|
| Amount | 150px (`GHS` + `4,000,000.00`) |
| Date | 140px (`25-OCT-2026` + calendar button) |
| Short code or number (insurance code, policy number, folio numbers, branch code) | 130px |
| Phone number | 160px |
| Percentage | 110px |
| Count (months, number of shares) | 100px |
| Account number LOV (code only) | 210px |
| Currency, source branch | 196px |
| Lookups, names, locations, product | Fill what is left of the row |
| Narration | Full row |

- Each section lists its fields in **rows**. Compact fields share a row; lookups and long text stretch to fill it. Standard rows: *Collateral amount · Next review date · Expiry review date*; *Insurance company · Insurance code*; *Policy type · Policy number · Sum assured*; *Valuation date · Market value · Forced sale value*; *Folio number · Folio start · Folio end*.
- The first label in each row has a fixed 120px column so rows line up on the left; the labels after it take their own width, up to about 104px, and wrap onto a second line if longer.
- Hints, limits and errors sit under the field.
- **Lookups (LOVs)** are one box showing the code and description separated by a hyphen, e.g. `001 - MERIDIAN LIFE ASSURANCE`. Clicking it opens the searchable list. Auto-filled code values use the same style (`010 - SINKOR`).
- Values that have their own meaning get their own field. The cash **Source account** box holds only the account number; **Account name**, **Product**, **Currency** and **Source branch** are separate auto-filled fields.
- Auto-filled fields have a grey fill and a lock icon.
- Side panels (required fields, balances, documents, decision, record) sit on the **right** of the form, 260px wide. At 1440px and wider every standard row fits on one line; on narrower screens the last field of a row moves to the next line.
- On phones the label moves above the field and every field takes the full row.

Sections:
- Each form is split into short sections (for example *Property details*, *Valuation*, *Collateral details*). Each section has a position marker (`01 / 03`), a title and a one-line description above its fields.
- After a collateral type is picked, the page scrolls so the whole form card, header included, sits under the top bar.

Dates:
- Every date is shown and typed as **DD-MON-YYYY** (for example `25-OCT-2026`); empty fields show the placeholder `dd-mmm-yyyy`.
- Users can type the date (also accepted: `25/10/2026`) or pick it from the calendar button. A date that doesn't exist (`31-FEB-2027`) shows "Enter the … as dd-mmm-yyyy, e.g. 25-OCT-2026."

## Tokens

Light mode uses a soft blue-grey page with off-white cards, and a smoke-white sidebar that matches the cards. Dark mode keeps its dark sidebar.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#E6EBF2` | `#0E1522` | Page background |
| `--surface` | `#F9FAFC` | `#151E2E` | Cards, top bar |
| `--surface-2` | `#F1F4F8` | `#1A2436` | Table headers, profile strip, hover |
| `--field` | `#FFFFFF` | `#151E2E` | Editable inputs (the only pure white in light mode) |
| `--sunken` | `#E7ECF2` | `#111A28` | Read-only fields, code chips |
| `--side-bg` | `#F5F7FA` | `#0A111D` | Module sidebar: smoke white in light mode, matching the cards |
| `--side-active` / `--side-active-fg` | `#E3ECF8` / `#0B5CAD` | `#16304F` / `#E5ECF5` | Active module, with a blue left marker |
| `--primary` | `#0B5CAD` | `#5AA2EE` | Focus ring, links, selected chips |
| `--fg` / `--muted` | `#13223A` / `#5A6A80` | `#E5ECF5` / `#9AA9BE` | Text |
| `--danger` | `#B42318` | `#F2867B` | Required asterisk, errors |
| `--success` | `#1D7A4C` | `#5CC892` | Completed steps, *Approved* |
| `--warn` | `#9A5A00` | `#E9B15C` | *Pending*, corporate badge |
| `--chg` / `--chg-soft` | `#A35F00` / `#FFF1D6` | `#E9B15C` / `#352812` | Edited fields in Amendment |

## Patterns

### Search list (Amendment and Cancellation)

- A **Search criteria** card with three fields: **Collateral number**, **Customer number** (with customer search) and **Customer name** (part of the name is enough). **Fetch** and **Clear** sit under the fields. Criteria are optional; blank lists everything.
- A results card with type filter chips (with counts), sortable columns, 8 rows per page and a pager ("Showing 1–8 of 14", First, ‹, page, ›, Last).
- Two-line cells keep the table narrow: customer name over number, review over expiry date, status over approver.
- The **›** open button is the last column and stays pinned to the right edge. Clicking the row does the same.
- Rows that can't be opened (*Amendment pending* or *Cancellation pending*) are muted and their **›** is disabled with a tooltip explaining why. A pending request in either module locks the record in **both**.

### Quick search with funnel (Enquiry)

- One search box, about 360px wide (customer name or number, collateral number, description, status), that filters as you type, with a solid blue **funnel** button beside it. Approvals and Returned use the same 360px box without the funnel.
- The funnel opens an **Advanced filters** panel inside the same card, laid out two fields per row with inline labels (ranges as *from – to*). **Fetch** applies and closes it; **Clear filters** empties it.
- Applied filters appear as chips under the search box, each with its own ×, plus **Clear all**. The funnel shows a red count of active filters.

### Data grid toolbar (Enquiry)

- Title, a record-count pill and **Refresh** on the left; **PDF** and **Excel** on the right. Exports use the rows currently shown.
- Long tables keep to the screen width: column headers may wrap to two lines, and secondary facts (type, currency) sit under the description.

### Module sub-navigation (Enquiry)

- A module with several screens gets an indented sub-list in the sidebar (All collateral, Running collateral, Used collateral) and a matching tab switcher at the top of the page. Both link to the same routes.

### Business-rule messages

- Limits are stated **before** the user hits them, as a hint under the field: "Up to the available balance 1,220.78", "Up to the sum assured", "Up to the forced sale value", "Must be before the expiry date".
- On Submit, a broken rule shows on the field like any other error and in the summary: "Can't exceed the available balance of 1,220.78."

### Review-date status (Enquiry)

- Quick-filter chips under the search box: **Overdue** (red) and **Due in 30 days** (amber), with counts.
- In the grids, review dates that are overdue or due soon carry a small red *Overdue* or amber *Due soon* tag.

### Change tracking (Amendment)

- An edited field gets an amber outline, an **Edited** tag on its label and "Was *old value* · Undo" underneath.
- A rail panel counts the changes and lists *old → new*, with **Undo all changes**.
- **New** and **Submit** are disabled until at least one field differs from the original. New then resets every field.
- Leaving with unsaved changes asks "Discard your changes?" first.
- The confirmation shows a Field / Before / After table.

### Read-only record view (Cancellation)

- The type form is rendered with the same layout, but values sit in grey boxes with no input border. Lookups show `code - description` in one box; amounts are right-aligned in mono.
- The form header says "Read only" and shows a lock instead of an edit icon.
- The single editable input lives in its own card with a red left edge, so the eye goes straight to it.

### Destructive confirmation (Cancellation)

- Submit opens an `alertdialog`: a warning icon, "Cancel collateral *number*?", one sentence on what happens on approval, then the key values and the reason.
- Buttons: **Keep collateral** (safe, neutral) and **Submit cancellation** (red, tinted). The safe choice is first.

### Supporting documents modal (all modules)

Replaces the Forms *Document Registration (Attach Scanned Document)* window. One modal, two modes:

- **Editable** (Creation, Amendment): a form with **Choose a file** / drop zone and **Scan document**, *Scanned document ref. no.* (pre-filled with the next number, editable), *Document description** (pre-filled from the file name), *Document expiry date*, then **Save document** and **Clear**. Saved documents are stored straight away, as in Forms.
- **View only** (Cancellation, Approvals): the table only.
- The table lists Ref., Document (description over file name), Expiry, Posted by, Posting date, and per-row **View** and **Delete**. Delete needs a second click ("Confirm delete") instead of the Forms radio button plus Delete button. **Return** closes the modal.
- The rail card shows only **how many** documents there are, and a **Manage documents (n)** / **View documents (n)** button that opens this modal with the list.

### Approval request (Approvals)

- The request opens on its entry screen's layout, read-only. Amendment requests highlight changed fields (**Changed** tag, amber outline, current value underneath).
- A **Decision** card at the top of the rail explains Return, Reject and Authorize.
- **Verification checklist** modal before Authorize: blue header row, one tick per item, counter and *Tick all*; the action stays disabled until all are ticked. Reject asks for a reason from a list plus a "Reject permanently" tick.

### Returned for correction (all entry screens)

- An amber banner under the page header: "Returned for correction by *user* on *date*", the reason as a quote, and what to do next.
- The entry screen is otherwise unchanged, so correcting a request works exactly like entering it.
- Request types have their own colours, used for badges, chips and dots: Creation blue, Amendment amber, Cancellation red.
- The **Approvals** sidebar link shows a red count of requests waiting.

### Maker-checker (Approvals)

- Your own requests stay in the queue with *(you)* and a grey **Yours** tag.
- Opening one shows a blue banner with a lock: you submitted it, so another officer must decide. Return, Reject and Authorize are left off the action bar.

### Report page (Reports)

- **Parameters** card with four inline fields on one row (As at, Due within, Branch, Collateral type). The report updates as they change; **New** resets them.
- **Summary** strip using the figures grid: counts and amounts coloured by state (red overdue, amber due, green good).
- Results table grouped by state, with a group header row and count, state chips (All / Overdue / Due), **PDF** and **Excel**, and a footer with the parameters and who ran it.

## Components

| Component | Behaviour | Angular Material equivalent |
|---|---|---|
| Lookup field (LOV) | One box showing `code - description` (e.g. `001 - MERIDIAN LIFE ASSURANCE`); clicking it opens a searchable dialog. Disabled until its parent field is set. Collateral type at Creation is a LOV too. | `mat-dialog` + `mat-table`, or `mat-autocomplete` for short lists |
| Amount input | Right-aligned, currency prefix, formatted `1,234.56` on blur | `matInput` + custom formatter directive |
| Date input | Typed or picked; always shown as `DD-MON-YYYY`, placeholder `dd-mmm-yyyy`, matching Oracle | `mat-datepicker` with a custom `DD-MMM-YYYY` date format |
| Required-fields panel | Count of required fields complete, a progress bar, and the fields still empty (each jumps to its field) | Standalone component |
| Drawer | Help and Comments slide in from the right | `mat-sidenav` (mode `over`) |
| Status pill | *Approved* (green), *Pending approval* (amber) | `mat-chip` |

PrimeNG offers equivalents for every row if the team prefers it. The choice of library is open.

### Reasons from a list (Cancellation, Reject)

- The **closure reason** at Cancellation and the **rejection reason** at Approvals are picked from a list of common reasons.
- Picking **Other** shows a text box for the reason; it is then required. Any other choice needs no typing.
