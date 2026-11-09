# UI Design System (Collateral Management)

The visual rules used by the prototype, so the Angular build and later modules (Amendment, Cancellation) look the same.

## Visual style: the bank's new screens (November 2026)

The bank's front-end teams have moved on from the @unionsg/ui look (see below). New screens, e.g. *Cheque Book Requisition*, use the style below, and Collateral Management now follows it. Where this section and the @unionsg/ui section disagree, this section wins.

| Element | New style |
|---|---|
| Title banner | Royal-blue bar (`#1E4E9C`, easing to `#4F7FC6` at the right end), square corners. **Back arrow** in a small square on the left, the screen title in white with a one-line subtitle. It stays under the top bar when you scroll |
| Actions on the banner | On the right of the banner: **Help** and **Comment** as icon buttons (Comment shows its count as a badge), then **New** (white outline) and **Submit** (solid green). Approvals: **Return** (solid amber), **Reject** (solid rose), **Authorize** (solid green) |
| Exit | The back arrow. It does what Exit did on that screen: details → list, list → module home, and it asks before discarding unsaved changes. Ctrl+Q still works |
| Section bars | Blue bar, square corners, uppercase title after a white tick. Step circles and subtitles are not shown (list bars keep their record count) |
| Sections inside a form | Blue uppercase title after a short tick in the collateral type's colour, the description under it, a thin rule |
| Inputs | Underline style: no box, a 1px bottom line that turns blue on focus and red on error; label small and grey above. Lookups, dates, phone and GPS fields follow the same line. Narration keeps a light box |
| Read-only values | Plain text, no grey box (amounts still right-aligned) |
| Side panels | White panel with a blue left edge, title in blue with its icon (as *Account Summary* on Cheque Book Requisition) |
| Tabs | Pills; the active one filled blue |
| Corners | 3–4px on cards and dialogs; banners and bars square |

## Component library: @unionsg/ui (superseded for look, kept for behaviour)

The bank's standard UI library ([unionsg-ui.vercel.app](https://unionsg-ui.vercel.app), v1.6.0) sets the look of the form controls, buttons, lookups, data tables and tabs. The prototype follows it (October 2026). The library ships as React components; its documented class values (Tailwind) and plain CSS are what the Angular build should reproduce.

| Library component | Used for in Collateral Management | Spec followed |
|---|---|---|
| TextInput | Every text, amount, date, phone and number field | 28px high, 4px corners, 1px `#d1d5db` border, 14px text; blue `#2563eb` border and 1px ring on focus; red `#f87171` border and 12px red message on error |
| TextInput (read-only) | Auto-filled and view-only values, and the customer's details | `#eceef2` fill (a shade deeper than the library's `#f9f8fa`, which hardly shows on the off-white cards), no border, semi-bold `#0f172a` text |
| TextInput (disabled) | LOVs waiting for their parent field | `#f3f4f6` fill, `#e5e7eb` border, grey text, not-allowed cursor |
| Label | Every field label | 13.5px, weight 500, `#374151`, **on top of the input**, left-aligned, red asterisk for required (the library puts labels beside inputs; the bank prefers them on top) |
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
- **3-column grid.** Every field starts on one of three column lines, and each input is only as wide as its longest value (see *Form layout*).

## Principles

1. **One task per page, in steps.** Customer, then type, then details. Each step shows a check mark once it is complete.
2. **Show codes and words together.** Bank users know the codes (`C03`, `220`, `010`). Every lookup shows the code and its description.
3. **Read-only looks read-only.** System-filled values sit on a grey fill with no border. Editable fields have a border.
4. **Errors tell you what to do.** "Enter the policy number." appears next to the field and in a summary at the top of the form.
5. **Keyboard first.** Enter fetches the customer. Arrow keys and Enter work in every lookup. Esc closes dialogs. Tab order follows the screen.

## Navigation: module home with cards

The module has **no sidebar**. The bank's main menu (built by another team) opens Collateral Management on its **home** page, and the home page has one card per screen, in four groups:

| Group | Cards |
|---|---|
| Collateral records | Creation · Amendment · Cancellation |
| Approvals | Approvals (red count waiting) · Returned (amber count to correct) |
| Enquiry | All collateral · Running collateral · Used collateral (record counts) |
| Reports | Review due / overdue (red count overdue) |

- Each card has an icon, the screen name, one line on what it is for, and a live count where one helps.
- Every screen shows a breadcrumb that starts with **Collateral Management**, linking home. The **CM** mark in the top bar also links home.
- **Exit** on a list screen returns home; on a details page it returns to its list first, as before.
- Three cards per row on desktop, one per row on phones.

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

## Form layout: 3-column grid, labels on top, fields sized to their values

Every label sits **on top of** its input, left-aligned, with any hint or error under the input. (October 2026: labels were tried beside the inputs, as in Oracle Forms, then moved back on top.)

Every section, and the Customer section, is a **3-column grid** (November 2026). Every field starts on one of the three column lines, so fields line up from section to section and from one collateral type to the next. A wide field (names, the main lookup of a section) takes two columns, so the field after it starts on the third line; Narration takes all three. Inside its column each input is only as wide as its longest value:

| Field | Width |
|---|---|
| Lookup (LOV), auto-filled code values | 280px, or the column width if smaller |
| Wide field: account name, ownership name, valuer name, insurance company, policy type, share code, financial institution, guarantee account | 2 columns, input up to 420px |
| Currency and branch next to a wide lookup | 210px |
| Account number (cash source account) | 220px |
| Amount | 150px (`GHS 99,999,999.99`), right-aligned, currency prefix |
| Date | 140px (`25-OCT-2026`), calendar button |
| Short code or number (insurance code, policy number) | 240px |
| Folio number, start, end | 120px |
| Rate | 110px · Count 100px |
| Phone number | 240px, @unionsg/ui PhoneInput: country selector (GH, LR, NG, SL), dial code, then the number |
| GPS location (property) | 250px: `latitude, longitude` box plus a pin button that opens the location picker |
| Narration | All three columns |

Amounts and dates are narrower than the library presets (180px, 160px) because those widths still hold the longest value and keep every form on the grid.

| Collateral | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| Customer (every screen) | Customer number · Customer name · Customer type | Home branch · Collaterals · Amount held | |
| Cash | Source account · Account name (2) | Product · Currency · Source branch | |
| Insurance | Insurance company (2) · Insurance code | Policy type (2) · Policy number | Sum assured |
| Property | Property type · Sub property type | Ownership name (2) · GPS location | Valuer name (2) · Contact number, then Valuation date · Market value · Forced sale |
| Guarantee | Financial institution (2) · Currency | Account number (2) · Branch | Deposit type · Collateral type, then Guarantee amount · Interest rate · Number of months, then Folio number · Folio start · Folio end |
| Shares | Share / security code (2) · Index | No. of shares · Security amount · Market value | Folio number · Folio start · Folio end |
| All (Collateral details) | Amount considered · Review date · Expiry date | Narration (3) | |

- Hints, limits and errors sit under the field.
- **Lookups (LOVs)** are one box showing the code and description separated by a hyphen, e.g. `001 - MERIDIAN LIFE ASSURANCE`. Clicking it opens a dropdown under the field with live search; ↑ ↓ and Enter pick a row, Esc closes it, and the × in the box clears the value (and any LOV that depends on it). Auto-filled code values use the same style (`010 - SINKOR`).
- Values that have their own meaning get their own field. The cash **Source account** box holds only the account number; **Account name**, **Product**, **Currency** and **Source branch** are separate auto-filled fields.
- Auto-filled fields use the library's read-only style (light fill, no border, semi-bold) with a lock icon.
- Side panels (required fields, balances, documents, decision, record) sit on the **right** of the form, 240px wide.
- Below 900px the grid has two columns; on phones one, and every field takes the full row.

Sections:
- Each form is split into short sections (for example *Property details*, *Valuation*, *Collateral details*). Each section has a position marker (`01 / 03`), a title and a one-line description above its fields.
- After a collateral type is picked, the page scrolls so the whole form card, header included, sits under the top bar.

Dates:
- Every date is shown and typed as **DD-MON-YYYY** (for example `25-OCT-2026`); empty fields show the placeholder `dd-mmm-yyyy`.
- Users can type the date (also accepted: `25/10/2026`) or pick it from the calendar button, which is the browser's own date picker. It opens on the date already typed, and the picked date is written back as `DD-MON-YYYY`. A date that doesn't exist (`31-FEB-2027`) shows "Enter the … as dd-mmm-yyyy, e.g. 25-OCT-2026."

## Colour: header bars, numbered sections, panel title strips

Added November 2026 after feedback that the screens had no colour, then refined. It follows the bank's other new screens (e.g. Cash Deposit): noticeable, not loud. **Rule: colour marks meaning, never decoration.** Navy is structure; strong colours are for actions and status (green Submit, red overdue, amber pending); the collateral type's colour is a small identity mark. No decorative side stripes.

| Element | Treatment | Token (light / dark) |
|---|---|---|
| Card header (Customer, Collateral type, the type form, lists, Request, Closure summary) | Navy bar, about 44px, solid for the first half then easing into a lighter steel blue at the right-hand end; white title, light-blue subtitle; step circles white or green | `--hdr` `#2F4462` → `--hdr-end` `#5B7FAE` / `#1C2A3F` → `#2E4A6E` |
| Section inside a form | A circle numbered 1, 2, 3 in the collateral type's colour (cash green, insurance purple, property orange, guarantee blue, shares teal), the title, the description in grey, and a thin line under it | `--tc` |
| Side panel (Required fields, Account balances, Documents, Decision, Record) | A slim tinted title strip with an icon (list, wallet, paperclip, shield, file) | `--band` `#EEF3FA` / `#18233A` |
| Decision panel | Keeps its amber outline (it is the one panel that needs a decision) | `--act-amber` |
| Dialogs and drawers | Same header bar as cards, with the same fade | `--hdr` → `--hdr-end` |
| Module home | Icon tile tinted in its screen's colour; group titles in navy | |

Inputs, buttons, tables and tabs keep their @unionsg/ui colours; the colour sits in the frame around them, so data stays easy to read. Before/after screenshots: `design/comparison/colour-before-*.png` and `colour-after-*.png`.

## Tokens

Light mode uses a soft blue-grey page with off-white cards.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#E6EBF2` | `#0E1522` | Page background |
| `--surface` | `#F9FAFC` | `#151E2E` | Cards, top bar |
| `--surface-2` | `#F1F4F8` | `#1A2436` | Table headers, profile strip, hover |
| `--field` | `#FFFFFF` | `#151E2E` | Editable inputs (the only pure white in light mode) |
| `--sunken` | `#E7ECF2` | `#111A28` | Read-only fields, code chips |
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

- A module with several screens gets one card per screen on the module home (All collateral, Running collateral, Used collateral) and matching @unionsg/ui **Tabs** at the top of the page: an icon, the label and a record-count badge, with the active tab solid green. Both link to the same routes.

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
- The **Approvals** card on the module home shows a red count of requests waiting.

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
| Amount input | Right-aligned, currency prefix, formatted `1,234.56` on blur. Read-only amounts and counts (e.g. Amount held, Collaterals) are right-aligned too | `matInput` + custom formatter directive |
| Date input | Typed or picked; always shown as `DD-MON-YYYY`, placeholder `dd-mmm-yyyy`, matching Oracle | `mat-datepicker` with a custom `DD-MMM-YYYY` date format |
| Required-fields panel | Count of required fields complete, a progress bar, and the fields still empty (each jumps to its field) | Standalone component |
| Drawer | Help and Comments slide in from the right | `mat-sidenav` (mode `over`) |
| Status pill | *Approved* (green), *Pending approval* (amber) | `mat-chip` |

The look of inputs, buttons, LOVs, tables and tabs is fixed by @unionsg/ui (see the top of this page). The library is React; the Angular build reproduces its classes and CSS, for example as Angular components that share the same Tailwind classes.

### GPS location picker (Property)

- The property's **GPS location** replaces the free-text location. The field holds `latitude, longitude` in decimal degrees to 6 places, e.g. `6.290500, -10.771200` (about 10 cm).
- The pin button opens **Property location**, a map picker:
  - **Click the map** where the property is to drop the pin; **drag the pin** to adjust. The coordinates fill in as you go.
  - **Map / Satellite** switches between the street map (OpenStreetMap) and satellite imagery (Esri), which helps to find a plot or building.
  - **Use my current location** reads the device's GPS (the browser asks permission first), moves the map and pin there, and shows how accurate the fix is.
  - **Latitude** and **Longitude** can also be typed; the pin follows. Pasting `6.29, -10.77` into either box fills both.
  - The map opens on the current value, or on Monrovia when the field is empty.
- **Or paste a map link:** a link copied from Google Maps (`…/@6.2905,-10.7712,17z…`, `…!3d6.29061!4d-10.77135…`, `?q=6.29,-10.77`) or OpenStreetMap (`#map=17/6.2935/-10.775`, `?mlat=…&mlon=…`) fills the coordinates and moves the pin. Pasting a link straight into the GPS field works too. Short share links (`maps.app.goo.gl/…`) carry no coordinates and are flagged. **Find the property in OpenStreetMap** opens OpenStreetMap where the picker's map is looking.
- If live map images are blocked (the Claude viewer blocks them), the picker shows a **saved street map of greater Monrovia** (OpenStreetMap, zoom 15, `design/prototype/maps/monrovia-z15.webp`, 1.4 MB). Clicking places the pin on real streets. Satellite is disabled in that mode. If even the saved map can't load, a latitude/longitude grid with reference points is shown. If the map library can't load at all, the picker says so, and GPS, links and typing still work.
- Under the field, and in every read-only view (approval, cancellation, enquiry), **View on map** opens the point so the approver can check it.
- Checks: required; latitude −90 to 90 and longitude −180 to 180.
- Angular: Leaflet (`@asymmetrik/ngx-leaflet` or plain Leaflet) with `navigator.geolocation.getCurrentPosition` (`enableHighAccuracy`). For production, use a tile provider the bank has agreed terms with (its own tile server, or a licensed Google, Esri or Mapbox account): the public OpenStreetMap and Esri tiles in the prototype are for demonstration only.

### Keyboard shortcuts (all screens)

The Oracle Forms keys the officers already use. The keyboard button in the top bar, or **Ctrl+K**, lists them.

| Key | Does | Forms name |
|---|---|---|
| F10 | The screen's green button: Submit, or Authorize on an approval (opens the checklist) | Commit (Accept) |
| F9 | Opens the lookup for the field the cursor is in; also customer search and the GPS picker | List of Values |
| F11 or F7 | Puts the cursor in the screen's search box | Enter Query |
| Ctrl+F11 or F8 | Runs the search, or fetches the customer | Execute Query |
| Ctrl+Q | The screen's Exit button | Exit |
| F1 | Help for the screen | Help |
| Ctrl+K | The list of keys | Show Keys |
| Esc | Closes a dialog, list or picker | |

- Web Forms keys (F11, Ctrl+F11) and the older client-server keys (F7, F8) both work. To confirm against the bank's own key file (`fmrweb.res`).
- Each shortcut shows a short toast naming the action, e.g. "F10 · Submit".
- Some browsers keep F11 (full screen) or Ctrl+Q (quit) for themselves. The Angular app should keep F7/F8 and the buttons as fallbacks, or ship as an installed web app where the page gets these keys.

### Duplicate warning (Creation)

On Submit, once the form is valid, the security is checked against approved collateral (not cancelled) and creation requests waiting or returned:

| Type | Counts as the same security |
|---|---|
| Cash | Same source account |
| Insurance | Same insurance company and policy number |
| Property | GPS location within 50 m of another property |
| Guarantee | Same guarantee account, or the same institution and folio number with an overlapping folio range |
| Shares | Same security code and folio number with an overlapping folio range |

- A match opens **Possible duplicate**: the matching collateral number, customer, status and why it matches.
- **Go back and check** returns to the form. **Submit anyway** needs a reason, because a second lien can be legitimate.
- The approver sees an amber banner on the request with the match and the reason. The reason is also recorded in the collateral's history.
- It is a warning, not a block. The rules are a proposal for Credit and Risk to confirm.

### History (Enquiry details, Amendment and Cancellation approvals)

A **History** card lists what happened to the collateral, newest first. Each event has a coloured icon, a label, who did it, when, and a note (the reason for a return or rejection, the number of fields changed, the duplicate-warning reason):

Captured · Corrected and resubmitted · Approved · Amendment submitted / approved / rejected · Cancellation submitted / Cancelled / rejected · Returned for correction · Rejected.

The Angular build reads these events from the audit trail (`USER_ACTION_AUDIT`, the approval tables), so nothing new has to be stored.

### Reasons from a list (Cancellation, Reject)

- The **closure reason** at Cancellation uses the standard LOV (`01 - Facility fully repaid` … `99 - Other`). The **rejection reason** at Approvals is a plain list inside the reject dialog.
- Picking **Other** shows a text box for the reason; it is then required. Any other choice needs no typing.
