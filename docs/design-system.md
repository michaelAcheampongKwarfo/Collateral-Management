# UI Design System (Collateral Management)

The visual and behaviour rules the prototype (`design/prototype/index.html`) follows, for the Angular build. Screenshots are in `design/screens/`.

## Principles

1. **One task per page, in steps.** Customer, then collateral type, then details.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`), so every lookup shows `code - description`.
3. **Fields are sized to their values.** An input is as wide as its longest value, never stretched to fill space.
4. **Colour means something.** Blue is structure; strong colours mark actions and status (green Submit, red overdue, amber pending); the collateral type's colour is a small identity mark.
5. **Errors say what to do.** "Enter the policy number." shows under the field and in a summary at the top of the form.
6. **Keyboard first.** The Oracle Forms keys work (see *Keyboard shortcuts*), Enter fetches, arrow keys and Enter work in every lookup, Esc closes dialogs.

## Visual style

Collateral Management follows the bank's newer screens (e.g. *Cheque Book Requisition*). This replaces the @unionsg/ui look the October 2026 prototype used; the library's behaviour (lookup dropdown, data-table pager, phone input) is kept.

| Element | Style |
|---|---|
| Title banner | Royal-blue bar (`#1E4E9C`, easing to `#4F7FC6` at the right end), square corners, stays under the top bar when scrolling. **Back arrow** on the left, the title in white with a one-line subtitle |
| Actions on the banner | On the right: **Help** and **Comment** (soft white buttons, icon and label; Comment shows a count badge), then **New** (white outline) and **Submit** (solid green). Approvals: **Return** (amber), **Reject** (rose), **Authorize** (green), all solid |
| Exit | The back arrow: details → list, list → module home, asking before discarding unsaved changes. Ctrl+Q does the same |
| Section bars | Blue bar, square corners, uppercase title after a white tick; list bars also show the record count |
| Sections inside a form | Blue uppercase title after a short tick in the collateral type's colour (cash green, insurance purple, property orange, guarantee blue, shares teal), a one-line description, a thin rule |
| Inputs | Underline style: no box, a 1px bottom line that turns blue on focus and red on error; label small and grey above. Lookups, dates, phone and GPS fields use the same line. Narration keeps a light box |
| Read-only values | Plain text with a lock icon for auto-filled values; amounts right-aligned |
| Details panel | **Customer** section only: number and name on top; Customer type · Home branch · Collaterals · Amount held in a light panel with dividers |
| Side panels | White panel with a blue left edge, title in blue with an icon (Required fields, Account balances, Documents, Decision, Record). The Decision panel has an amber outline |
| Tables | Light-blue header row, sortable columns, a **›** open button in the last column, pager footer ("Showing 1 to 10 of 14 records", page numbers, Per page 5/10/25) |
| Tabs | Pills; the active one filled blue, each with an icon and a count |
| Dialogs | Same blue header bar; 4px corners |
| Corners | 3–4px on cards and dialogs; banners and bars square |

| Token | Light | Dark | Use |
|---|---|---|---|
| `--hdr` → `--hdr-end` | `#1E4E9C` → `#4F7FC6` | `#173B73` → `#2D5A98` | Banner, section bars, dialog headers |
| `--sec-ink` | `#1E4E9C` | `#9CC0F5` | Section and panel titles |
| `--ul` | `#C3CCD8` | `#3B4A63` | Input underline |
| `--panel` | `#F1F4F9` | `#18233A` | Details panel |
| `--bg` / `--surface` | `#E6EBF2` / `#F9FAFC` | `#0E1522` / `#151E2E` | Page / cards |
| `--fg` / `--muted` | `#13223A` / `#5A6A80` | `#E5ECF5` / `#9AA9BE` | Text |
| `--danger` / `--success` / `--warn` | `#B42318` / `#1D7A4C` / `#9A5A00` | `#F2867B` / `#5CC892` / `#E9B15C` | Errors and overdue / Approved / Pending |
| `--chg` | `#A35F00` | `#E9B15C` | Edited fields in Amendment |

The blues were matched by eye from a photo of *Cheque Book Requisition*; take the exact values from the front-end team.

## Navigation

- No sidebar: the bank's main menu (another team) opens the module **home**, which has one card per screen: *Collateral records* (Creation, Amendment, Cancellation), *Approvals* (Approvals with a red waiting count, Returned with an amber count), *Enquiry* (All, Running, Used) and *Reports* (Review due / overdue, with the overdue count).
- Every screen has a breadcrumb starting with **Collateral Management** (links home); the **CM** mark also links home.
- Routes: `#home`, `#creation`, `#amendment`, `#cancellation`, `#approvals`, `#returned`, `#enquiry-all`, `#enquiry-running`, `#enquiry-used`, `#report-review`.

## Actions per screen

| Screen | Banner actions | New does |
|---|---|---|
| Creation | Help, Comment, New, Submit | Clears the screen |
| Amendment / Cancellation list | Help, New | Clears the search |
| Amendment details | Help, Comment, New, Submit | Resets every field; New and Submit stay disabled until something changed |
| Cancellation details | Help, Comment, New, Submit | Clears the closure reason |
| Approvals queue, Returned queue | Help, New | Clears the search |
| Approval request | Help, Comment, Return, Reject, Authorize | — (your own request: Help and Comment only, maker-checker) |
| Enquiry grids | Help, New | Clears the search and filters |
| Enquiry details | Help | — |
| Reports | Help, New | Resets the parameters |

Every screen also has the back arrow. A button a screen doesn't use is left out, not shown disabled.

## Form layout

Labels sit **on top** of their inputs. Every section, the Customer section and the enquiry filters use a **3-column grid**: every field starts on one of three column lines, so fields line up from section to section and across collateral types. A wide field takes two columns; Narration takes all three. Below 900px the grid has two columns, on phones one.

| Field | Width |
|---|---|
| Lookup (LOV), auto-filled code value | 280px (or the column width) |
| Wide field: account name, ownership name, valuer name, insurance company, policy type, share code, financial institution, guarantee account | 2 columns, input up to 420px |
| Currency and branch beside a wide lookup | 210px |
| Cash source account | 220px |
| Customer number | 150px, with search |
| Amount | 150px (`GHS 99,999,999.99`), right-aligned, currency prefix |
| Date | 140px (`25-OCT-2026`), calendar button |
| Insurance code, policy number | 240px |
| Folio number, start, end | 120px |
| Rate 110px · Count 100px | |
| Phone | 240px: country (GH, LR, NG, SL), dial code, number |
| GPS location | 250px: `latitude, longitude` and a pin button |

| Section | Rows |
|---|---|
| Customer | Customer number · Customer name (2), then the details panel |
| Collateral type | One lookup (`C01 - CASH COLLATERALS`) with the type's description under it |
| Cash | Source account · Account name (2), then Product · Currency · Source branch |
| Insurance | Insurance company (2) · Insurance code; Policy type (2) · Policy number; Sum assured |
| Property | Property type · Sub property type; Ownership name (2) · GPS location; Valuer name (2) · Contact number; Valuation date · Market value · Forced sale |
| Guarantee | Financial institution (2) · Currency; Account number (2) · Branch; Deposit type · Collateral type; Guarantee amount · Interest rate · Number of months; Folio number · Folio start · Folio end |
| Shares | Share / security code (2) · Index; No. of shares · Security amount · Market value; Folio number · Folio start · Folio end |
| Collateral details (all types) | Amount considered · Review date · Expiry date; Narration (3) |

- Hints and limits sit under the field before the user hits them ("Up to the available balance 1,220.78", "Before the expiry date"); a broken rule on Submit shows as an error there and in the summary.
- After a collateral type is picked, the page scrolls to the form.
- **Dates** are shown and typed as `DD-MON-YYYY` (placeholder `dd-mmm-yyyy`; `25/10/2026` is also accepted). The calendar button is the browser's own picker, opens on the typed date, and writes back `DD-MON-YYYY`. An impossible date (`31-FEB-2027`) is rejected with an example.

## Components

| Component | Behaviour | Angular build |
|---|---|---|
| Lookup (LOV) | One box `code - description`; a dropdown under the field with live search, ↑ ↓ Enter, Esc; × clears it and any lookup that depends on it; disabled until its parent is set. Used for Collateral type, every code field and the closure reason (`01 - Facility fully repaid` … `99 - Other`; Other opens a text box) | CDK overlay component |
| Customer search | Dialog with a searchable customer list | Dialog component |
| Amount | Right-aligned, currency prefix, `1,234.56` on blur | Input + formatter directive |
| Date | As under *Form layout* | Datepicker with a `DD-MMM-YYYY` format |
| Required fields panel | Count complete, progress bar, the fields still empty (each jumps to its field) | Standalone component |
| Account balances (cash) | Available balance, then cleared, uncleared, OD and block amounts; a small arrow button opens the uncleared items and blocked amounts | Standalone component |
| Supporting documents | The panel shows the count; the dialog adds (file, drop or scan; ref. no.; description; expiry), views and deletes (with confirm). View only in Cancellation and Approvals | Dialog component |
| Help, Comments | Slide-in drawers from the right | Side drawer |
| Status pill | *Approved* green, *Pending* amber, *Returned* amber, *Closed* grey | Chip |

### GPS location picker (Property)

- The field holds `latitude, longitude` to 6 decimals (about 10 cm). The pin opens **Property location**: click the map to drop the pin, drag to adjust; **Map / Satellite**; **Use my current location** (the browser asks first; shows the accuracy); latitude and longitude can be typed; **Or paste a map link** takes a Google Maps or OpenStreetMap link (a link pasted straight into the field works too; short `maps.app.goo.gl` links have no coordinates and are flagged).
- Where live map images are blocked, a saved street map of greater Monrovia (`design/prototype/maps/monrovia-z15.webp`) is shown instead.
- Read-only views show the coordinates with **View on map**. Checks: required; latitude −90 to 90, longitude −180 to 180.
- Angular: Leaflet and `navigator.geolocation`. Production needs a map provider the bank has agreed terms with; the public OpenStreetMap and Esri tiles are for the prototype only.

### Keyboard shortcuts (all screens)

| Key | Does | Forms name |
|---|---|---|
| F10 | Submit, or Authorize on an approval | Commit (Accept) |
| F9 | Opens the lookup for the field the cursor is in (also customer search and the GPS picker) | List of Values |
| F11 or F7 | Cursor to the screen's search box | Enter Query |
| Ctrl+F11 or F8 | Runs the search, or fetches the customer | Execute Query |
| Ctrl+Q | Exit (the back arrow) | Exit |
| F1 | Help | Help |
| Ctrl+K | Lists the keys (also the keyboard button in the top bar) | Show Keys |
| Esc | Closes a dialog, list or picker | |

Each key shows a short toast naming the action. Some browsers keep F11 and Ctrl+Q, so F7/F8 and the buttons stay as fallbacks. To confirm against the bank's key file (`fmrweb.res`).

### Duplicate warning (Creation)

On a valid Submit, the security is checked against approved collateral (not cancelled) and creation requests waiting or returned:

| Type | Same security when |
|---|---|
| Cash | Same source account |
| Insurance | Same insurer and policy number |
| Property | GPS location within 50 m |
| Guarantee | Same guarantee account, or same institution and folio number with an overlapping range |
| Shares | Same security code and folio number with an overlapping range |

A match opens **Possible duplicate** (collateral no., customer, status, why it matches). **Submit anyway** needs a reason; the approver sees it in an amber banner and it goes into the history. A warning, not a block; the rules are for Credit and Risk to confirm.

### History

A **History** card (enquiry details, amendment and cancellation approvals) lists the collateral's events newest first, each with who, when and a note: captured, corrected and resubmitted, approved, amendment submitted / approved / rejected, cancellation submitted / cancelled / rejected, returned, rejected. In Angular it reads the audit trail (`USER_ACTION_AUDIT`, the approval tables); nothing new is stored.

## Patterns

- **Search list (Amendment, Cancellation):** search criteria (collateral number, customer number with search, customer name), **Fetch** and **Clear**; results with type chips and counts, sortable columns, two-line cells (name over number, review over expiry, status over approver). Rows with a pending request are muted and can't be opened; a pending request locks the record in both modules.
- **Quick search with funnel (Enquiry):** one search box filtering as you type; the funnel opens **Advanced filters** (on the 3-column grid, value-sized: Customer ID 150px, Collateral no. 180px, Branch 220px, Collateral type 180px, Status 150px, amount and date ranges as two boxes with *to*); applied filters show as removable chips with **Clear all**. **Overdue** and **Due in 30 days** chips filter by review date; grids tag those dates.
- **Grid toolbar (Enquiry):** title, record count and **Refresh**; **PDF** and **Excel** export the rows shown.
- **Change tracking (Amendment):** an edited field gets an amber line, an **Edited** tag and "Was *old value* · Undo"; a panel lists old → new with **Undo all changes**; leaving asks before discarding; the confirmation shows Field / Before / After.
- **Cancellation:** the record read-only, the closure reason in its own card; Submit asks "Cancel collateral *number*?" with **Keep collateral** first.
- **Approval request:** opens on the entry screen's layout, read-only; amendment changes highlighted with the current value under them. **Authorize** opens a verification checklist (every item ticked); **Return** asks for a reason; **Reject** asks for a reason from a list and a "Reject permanently" tick.
- **Maker-checker:** your own requests are marked *Yours*; opening one shows a lock banner and no decision buttons.
- **Returned:** a returned request reopens on its entry screen with an amber banner (who, when, the reason) and is resubmitted under the same collateral number.
- **Request type colours:** Creation blue, Amendment amber, Cancellation red (badges, chips, dots).
- **Report (Review due / overdue):** parameters (As at, Due within, Branch, Collateral type), a summary strip, results grouped by state, **PDF** and **Excel**.
