# UI Design System (Collateral Management)

The visual rules used by the prototype, so the Angular build and later modules (Amendment, Cancellation) look the same.

## Component library: @unionsg/ui

The bank's standard UI library ([unionsg-ui.vercel.app](https://unionsg-ui.vercel.app), v1.6.0) sets the look of the form controls, buttons, lookups, data tables and tabs. The prototype follows it (October 2026). The library ships as React components; its documented class values (Tailwind) and plain CSS are what the Angular build should reproduce.

| Library component | Used for in Collateral Management | Spec followed |
|---|---|---|
| TextInput | Every text, amount, date, phone and number field | 28px high, 4px corners, 1px `#d1d5db` border, 14px text; blue `#2563eb` border and 1px ring on focus; red `#f87171` border and 12px red message on error |
| TextInput (read-only) | Auto-filled and view-only values, and the customer's details | `#eceef2` fill (a shade deeper than the library's `#f9f8fa`, which hardly shows on the off-white cards), no border, semi-bold `#0f172a` text |
| TextInput (disabled) | LOVs waiting for their parent field | `#f3f4f6` fill, `#e5e7eb` border, grey text, not-allowed cursor |
| Label | Every field label | 14px, weight 500, `#374151`, right-aligned beside the input, red asterisk for required |
| Width presets | Field widths (see Form layout) | Name 420, LOV 280, phone 240, short 240, amount 180, date 160 |
| LOV | Every lookup field | One box `001 - DESCRIPTION`, search-icon segment on the right with a divider, a × to clear the value, and a dropdown under the field with live search and arrow-key selection |
| Button | Action bar, Fetch, Clear, exports | `rounded-lg`, `px-4 py-2 text-sm font-medium`, white with coloured text and border, light tint on hover |
| DataTable | Amendment, Cancellation, Approvals, Returned and Enquiry lists, and Creation's *Customer's other collaterals* (with the record-count footer) | `#E9EFFB` sticky header (12px, semi-bold, not upper case), triangle sort icons, 12px `#334155` rows on `#f7f4f0`, light blue hover, small row-action buttons, footer pager |
| Tabs | Enquiry: All / Running / Used collateral | Grey tab strip; active tab solid green-600 with white text; icon and count badge on each tab |

Where the library has no rule, the prototype keeps the module's agreed choices:
- **Submit and Authorize** are solid green (green-600). The library's generic primary button is indigo; green was agreed for Submit.
- **Return** (amber) and **Reject** (rose) use the library's outlined button shape in their own colours.
- **Dates** stay `DD-MON-YYYY`, as agreed, at the library's 160px date width, centred. The library's own example uses `DD/MM/YYYY`.
- The customer search and the documents list stay as dialogs; the library LOV dropdown is for code lists.
- **Collateral type** at Creation is picked from five tiles (icon, name, code, one-line description), not a LOV: with only five types, every option stays visible and is one click away.
- **Customer details** at Creation (and the customer card on every other screen) are read-only inputs on the form grid, each sized to its value: Customer number 150px (input plus search; no helper line under it, only errors), Customer name 420px, Customer type 160px, Home branch 220px, Collaterals 80px, Amount held 180px.
- **Shared lines.** Fields that belong together sit on one line, with short labels, and each is only as wide as its longest value (see *Lines of compact fields* under Form layout).

## Principles

1. **One task per page, in steps.** Customer, then type, then details. Each step shows a check mark once it is complete.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`). Every lookup shows the code and its description.
3. **Read-only looks read-only.** System-filled values sit on a grey fill with no border. Editable fields have a border.
4. **Errors tell you what to do.** "Enter the policy number." appears next to the field and in a summary at the top of the form.
5. **Keyboard first.** Enter fetches the customer. Arrow keys and Enter work in every lookup. Esc closes dialogs. Tab order follows the screen.

## Standard action bar

Every screen uses the same buttons, in the same order and colours. Each screen shows only the buttons it uses, so nothing on the bar is a dead control.

The bar always sits **on the right of the page header**, on every screen (entry, list, details, approval, enquiry). When a long title pushes it onto its own row it stays right-aligned, so the buttons always end at the same edge.

| Order | Button | Colour | @unionsg/ui style |
|---|---|---|---|
| 1 | Help | Blue | `search` variant: white, blue-700 text, blue-300 border |
| 2 | Comment | Blue | `search` variant |
| — | *divider* | | Separates the information actions from the record actions |
| 3 | New | Blue | `search` variant |
| 4 | Submit | Green | Solid green-600 (the only solid button) |
| 5 | Exit | Red | `exit` variant: white, red-600 text, red-300 border |
| — | Return *(Approvals only)* | Amber | Outlined, amber-700 text, amber-300 border, before Reject |
| — | Reject *(Approvals only)* | Rose | Outlined, rose-700 text, rose-300 border (distinct from the red Exit), before the green Authorize |

Other buttons: **Fetch** uses the library's `fetch` variant (sky-700 text, sky-300 border); **Back**, **Cancel** and dialog buttons use the `return` variant (grey).

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
| `--u-blue` / `--u-blue-b` | `#1d4ed8` / `#93c5fd` | `#93c5fd` / `#2c4f86` |
| `--u-sky` / `--u-sky-b` | `#0369a1` / `#7dd3fc` | `#7dd3fc` / `#1f5671` |
| `--u-green` | `#16a34a` | `#22a85a` |
| `--u-red` / `--u-red-b` | `#dc2626` / `#fca5a5` | `#fca5a5` / `#7f2a2a` |
| `--u-amber` / `--u-amber-b` | `#b45309` / `#fcd34d` | `#fcd34d` / `#6b4a12` |
| `--u-rose` / `--u-rose-b` | `#be123c` / `#fda4af` | `#fda4af` / `#7a2a3d` |

## Form layout: inline labels, fields sized to their values

Every label sits **on the same line** as its field, on the left, as in Oracle Forms. Since adopting @unionsg/ui, each section is a **two-column grid**: each column is a right-aligned label (144px) beside its input. Inputs keep the library's preset width for the value they hold.

| Field | Width (@unionsg/ui preset) |
|---|---|
| Lookup (LOV), including the account number | 280px |
| Auto-filled code values (product, currency, branch) | 280px |
| Account name | 420px (name) |
| Amount | 180px, right-aligned, currency prefix |
| Date | 160px, centred, calendar button |
| Short code or number (insurance code, policy number) | 240px (short) |
| Phone number | 240px, @unionsg/ui PhoneInput: country selector (GH, LR, NG, SL), dial code, then the number |
| Percentage, count | 120px |
| Names and free text (ownership, location, valuer) | Full row, up to 420px |
| Narration | Full row |

- Fields fill the grid left to right, two per row: *Insurance company · Insurance code*; *Policy type · Policy number*.
- **Lines of compact fields.** Fields that belong together share one full-width line. Inside a line each field is only as wide as its longest value: amount 150px (`GHS 99,999,999.99`), date 140px (`25-OCT-2026`), count 100px, rate 110px, folio 120px. The fields are spread across the line (space-between), so the last one ends at the right edge; the gap between them is never less than 8px. Every line fits beside the side panel at 1440px.

| Collateral | Line |
|---|---|
| All | Amount considered (Collateral amount for cash) · Review date · Expiry date |
| Guarantee | Financial institution (fills the line) · Currency 210px |
| Guarantee | Account number (fills the line) · Branch 210px |
| Guarantee | Guarantee amount · Interest rate · Number of months |
| Guarantee, Shares | Folio number · Folio start · Folio end |
| Shares | No. of shares · Security amount (Stock amount at Amendment) · Market value |
| Property | Ownership name · Location (both fill the line) |
| Property | Valuer name (fills the line) · Contact number (phone, 240px) |
| Property | Valuation date · Market value (Collateral amount at Amendment) · Forced sale |
- Long labels wrap onto a second line inside their column.
- Hints, limits and errors sit under the field.
- **Lookups (LOVs)** are one box showing the code and description separated by a hyphen, e.g. `001 - MERIDIAN LIFE ASSURANCE`. Clicking it opens a dropdown under the field with live search; ↑ ↓ and Enter pick a row, Esc closes it, and the × in the box clears the value (and any LOV that depends on it). Auto-filled code values use the same style (`010 - SINKOR`).
- Values that have their own meaning get their own field. The cash **Source account** box holds only the account number; **Account name**, **Product**, **Currency** and **Source branch** are separate auto-filled fields.
- Auto-filled fields use the library's read-only style (light fill, no border, semi-bold) with a lock icon.
- Side panels (required fields, balances, documents, decision, record) sit on the **right** of the form, 240px wide.
- Below 900px the grid becomes one column; on phones the label moves above the field and every field takes the full row.

Sections:
- Each form is split into short sections (for example *Property details*, *Valuation*, *Collateral details*). Each section has a position marker (`01 / 03`), a title and a one-line description above its fields.
- After a collateral type is picked, the page scrolls so the whole form card, header included, sits under the top bar.

Dates:
- Every date is shown and typed as **DD-MON-YYYY** (for example `25-OCT-2026`); empty fields show the placeholder `dd-mmm-yyyy`.
- Users can type the date (also accepted: `25/10/2026`) or pick it from the calendar button, which is the browser's own date picker. It opens on the date already typed, and the picked date is written back as `DD-MON-YYYY`. A date that doesn't exist (`31-FEB-2027`) shows "Enter the … as dd-mmm-yyyy, e.g. 25-OCT-2026."

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
- A results card with type filter chips (with counts), sortable columns and the @unionsg/ui DataTable footer: "Showing 1 to 10 of 14 records", ‹, page numbers (current page solid blue), › and **Per page** (5, 10 or 25; 10 by default).
- Two-line cells keep the table narrow: customer name over number, review over expiry date, status over approver.
- The last column holds a simple **›** open button (28px, bordered, blue arrow), the same in every list (Amendment, Cancellation, Approvals, Returned, Enquiry). It stays pinned to the right edge. Clicking the row does the same.
- Rows that can't be opened (*Amendment pending* or *Cancellation pending*) are muted and their action button is disabled with a tooltip explaining why. A pending request in either module locks the record in **both**.

### Quick search with funnel (Enquiry)

- One search box, about 360px wide (customer name or number, collateral number, description, status), that filters as you type, with a solid blue **funnel** button beside it. Approvals and Returned use the same 360px box without the funnel.
- The funnel opens an **Advanced filters** panel inside the same card, laid out two fields per row with inline labels (ranges as *from – to*). **Fetch** applies and closes it; **Clear filters** empties it.
- Applied filters appear as chips under the search box, each with its own ×, plus **Clear all**. The funnel shows a red count of active filters.

### Data grid toolbar (Enquiry)

- Title, a record-count pill and **Refresh** on the left; **PDF** and **Excel** on the right. Exports use the rows currently shown.
- Long tables keep to the screen width: column headers may wrap to two lines, and secondary facts (type, currency) sit under the description.

### Module sub-navigation (Enquiry)

- A module with several screens gets an indented sub-list in the sidebar (All collateral, Running collateral, Used collateral) and matching @unionsg/ui **Tabs** at the top of the page: an icon, the label and a record-count badge, with the active tab solid green. Both link to the same routes.

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

| Component | Behaviour | Angular build |
|---|---|---|
| Lookup field (LOV) | @unionsg/ui LOV: one box showing `code - description` (e.g. `001 - MERIDIAN LIFE ASSURANCE`), a dropdown with live search, and a × to clear. Disabled until its parent field is set. (Collateral type at Creation uses tiles instead.) | Angular port of the @unionsg/ui LOV (CDK overlay) |
| Amount input | Right-aligned, currency prefix, formatted `1,234.56` on blur | `matInput` + custom formatter directive |
| Date input | Typed or picked; always shown as `DD-MON-YYYY`, placeholder `dd-mmm-yyyy`, matching Oracle | `mat-datepicker` with a custom `DD-MMM-YYYY` date format |
| Required-fields panel | Count of required fields complete, a progress bar, and the fields still empty (each jumps to its field) | Standalone component |
| Drawer | Help and Comments slide in from the right | `mat-sidenav` (mode `over`) |
| Status pill | *Approved* (green), *Pending approval* (amber) | `mat-chip` |

The look of inputs, buttons, LOVs, tables and tabs is fixed by @unionsg/ui (see the top of this page). The library is React; the Angular build reproduces its classes and CSS, for example as Angular components that share the same Tailwind classes.

### Reasons from a list (Cancellation, Reject)

- The **closure reason** at Cancellation uses the standard LOV (`01 - Facility fully repaid` … `99 - Other`). The **rejection reason** at Approvals is a plain list inside the reject dialog.
- Picking **Other** shows a text box for the reason; it is then required. Any other choice needs no typing.
