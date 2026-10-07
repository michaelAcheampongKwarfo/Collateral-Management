# Collateral Amendment: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Amendment (Oracle Forms screens `Collateral Amendment/Evaluat. - LRRU` and `Collateral Registration`) |
| **Target** | Angular front end (migration from Oracle Forms) |
| **Status** | Draft for presentation. Business rules will be confirmed against the PL/SQL behind the current screens. |
| **Prototype** | [`design/prototype/index.html#amendment`](../../design/prototype/index.html) (open in a browser, then choose **Amendment** in the sidebar) |
| **Reference screens** | [`screenshots/amendment/`](../../screenshots/amendment/) |

---

## 1. Purpose

Amendment lets a user change the details of a collateral that has already been approved: for example a revaluation, a new review date or a corrected policy number. The change is submitted for approval, and the current values stay in force until it is approved.

The module has two screens:

1. **Search list.** Find an approved collateral by customer number, collateral number or both.
2. **Details page.** One page per collateral type, pre-filled with the current values, where the user makes and submits the changes.

## 2. User flow

1. Open **Amendment**. The list shows approved collaterals.
2. Optionally enter a **customer number** (name fills in) and/or a **collateral number**, then select **Fetch**. **Clear** (or **New**) resets the search.
3. Optionally narrow the list by collateral type, or sort any column.
4. Select **›** on a row (or the row itself) to open the details page for that collateral's type.
5. Change the fields that need updating. Each edited field is highlighted and shows its original value with an **Undo** link. The right-hand panel counts and lists every change.
6. Select **Submit**. The system validates the record, saves the amendment and marks the collateral **Amendment pending**.
7. A confirmation shows a before-and-after table of the changes. The user returns to the search list.

A draft flowchart is in [`flowchart.md`](flowchart.md).

## 3. Screen 1: Search list

### 3.1 Oracle Forms (current)

Window `Collateral Amendment/Evaluat. - LRRU`.

| Area | Content |
|---|---|
| Toolbar | Fetch, Refresh, Exit |
| Search criteria | Customer number* (LOV, shows name), Collateral number* (shows description) |
| Grid "Collateral Amendment Details" | Collateral No, Customer Number, Customer Name, Collateral type, Amount, Amount Considered, Review Date, Exp Date, Approved By, `>` button |
| Footer | First / Last paging |

### 3.2 Angular design

| Area | Design |
|---|---|
| Action bar | **Help**, **New**, **Exit**. New clears the search (the old *Refresh*). |
| Search criteria card | Customer number (search + LOV) · Customer name (auto-filled) · Collateral number, on the 12-column grid (3 + 5 + 4). **Fetch** (the old toolbar Fetch) and **Clear** sit under the fields. Both criteria are optional; blank lists everything. |
| Type filter | Chips: All, Cash, Insurance, Property, Guarantee, Shares, each with a count |
| Results table | Collateral no. · Customer (name, number below) · Collateral type (colour dot, name, code) · Amount · Considered · Review / expiry (stacked) · Status (pill, *by* approver below) · **›** |
| Sorting | Every column except **›** sorts by click or Enter |
| Paging | 8 rows per page. "Showing 1–8 of 14", First, previous, page number, next, Last |
| Pending records | Rows already awaiting an amendment approval show **Amendment pending**, appear muted, and their **›** is disabled |

The **›** column stays pinned to the right edge, so the open action is always visible even when the table scrolls sideways.

**Amount** shows the main value of each type: the source balance for cash, sum assured for insurance, collateral amount for property, guarantee amount for guarantees, and market value for shares. *(To confirm, see Q2.)*

## 4. Screen 2: Details page

### 4.1 Oracle Forms (current)

Window `Collateral Registration`. Toolbar: Help, Comment, Reject (disabled), Submit, Exit. Header: customer number + name, collateral type code + description, collateral number. Below is a type-specific form with a **View Documents** button.

### 4.2 Angular design

| Area | Design |
|---|---|
| Header | **Back to search results** link, title "Amend collateral" + collateral number, standard action bar |
| Customer card | The same **customer profile strip** as Creation: name and number, type, home branch, collaterals held, amount held. Read-only. |
| Form card | Type heading (colour and icon), collateral number chip, then the type's sections on the 12-column grid |
| Change tracking | An edited field gets an amber outline, an **Edited** tag and a line under it: "Was *old value* · Undo" |
| Amendment panel | Number of fields changed, a list of *old → new* for each, and **Undo all changes** |
| Record panel | Collateral no., type, status, approved by, approval date |
| Account balances (cash) | Available amount, source balance, used amount, amount considered |
| Documents panel | The first documents plus **Manage documents (n)**, opening the documents modal to view, add, scan or delete (the old *View Documents*) |
| Action bar | **Help**, **Comment**, **New**, **Submit**, **Exit**. **New resets every field to its original value** in case of a mistake. New and Submit switch on once at least one field has changed. Exit returns to the list and asks before discarding unsaved changes. The Forms **Reject** button is not carried over (see Q5). |

## 5. Fields per type

The fields follow the Oracle Forms amendment screens. Layout uses the same 12-column rows as Creation. **Ed.** = editable in the Forms screenshots.

### 5.1 Cash (`C01`)

| Section | Field | Kind | Ed. | Columns |
|---|---|---|---|---|
| Account details | Source account | LOV | Yes | 8 |
| | Source branch | Auto-filled | | 4 |
| | Product | Auto-filled | | 8 |
| | Currency | Auto-filled | | 4 |
| Collateral details | Amount considered | Amount | Yes | 4 |
| | Review date | Date | Yes | 4 |
| | Expiry date | Date | Yes | 4 |
| | Comments | Text area | Yes | 12 |

The Forms "Balance Info" block (source balance, available amount, used amount) moves to the **Account balances** panel. *Product* is not on the Forms amendment screen. It is shown for consistency with Creation and comes from the same account.

### 5.2 Insurance (`C02`)

| Section | Field | Kind | Columns |
|---|---|---|---|
| Insurance details | Insurance company | LOV | 8 |
| | Insurance code | Text | 4 |
| | Policy type | LOV | 4 |
| | Policy number | Text | 4 |
| | Sum assured | Amount | 4 |
| Collateral details | Amount considered · Review date · Expiry date | | 4 · 4 · 4 |
| | Comments | Text area | 12 |

### 5.3 Property (`C03`)

| Section | Field | Kind | Columns |
|---|---|---|---|
| Property details | Property type · Sub property type | LOV · LOV | 6 · 6 |
| | Ownership name · Location | Text · Text | 5 · 7 |
| Valuation | Valuer name · Valuer contact number | Text · Phone | 8 · 4 |
| | Valuation date · Collateral amount · Forced sale value | Date · Amount · Amount | 4 · 4 · 4 |
| Collateral details | Amount considered · Review date · Expiry date | | 4 · 4 · 4 |
| | Comments | Text area | 12 |

The Forms property screen shows **Collateral Amount** where Creation shows **Market value**. See Q3.

### 5.4 Guarantee (`C04`)

| Section | Field | Kind | Columns |
|---|---|---|---|
| Guarantee details | Financial institution · Branch | LOV · Text | 8 · 4 |
| | Currency · Deposit type | LOV · LOV | 4 · 8 |
| Terms and folio | Guarantee amount · Interest rate · Number of months | Amount · Percent · Integer | 4 · 4 · 4 |
| | Folio number · Folio start number · Folio end number | Text | 4 · 4 · 4 |
| Collateral details | Amount considered · Review date · Expiry date | | 4 · 4 · 4 |
| | Comments | Text area | 12 |

Creation also has *Account number* and *Collateral type* for guarantees. They are not on the Forms amendment screen, so they are not editable here. See Q4.

### 5.5 Shares / stock / security (`C05`)

| Section | Field | Kind | Columns |
|---|---|---|---|
| Security details | Share / security code · Index | LOV · LOV | 6 · 6 |
| | Number of shares · Stock amount · Market value | Integer · Amount · Amount | 4 · 4 · 4 |
| Folio | Folio number · Folio start number · Folio end number | Text | 4 · 4 · 4 |
| Collateral details | Amount considered · Review date · Expiry date | | 4 · 4 · 4 |
| | Comments | Text area | 12 |

Forms calls it *Stock Amount* here and *Security Amount* on Creation. See Q3.

## 6. Behaviour and validation

### 6.1 In the prototype

- Required fields and number formats are validated as on Creation, with the same messages and error summary.
- A change is detected by comparing each field with its value when the page opened. Amounts and numbers are compared as numbers (`4,000,000` = `4,000,000.00`).
- Changing a lookup that others depend on (property type → sub-type) clears the dependent field. Undo on the parent restores both.
- Submit sends only when at least one field differs from the original.
- After submit the record shows **Amendment pending** and cannot be opened again from the list.

### 6.2 To confirm against the PL/SQL

| # | Question |
|---|---|
| Q1 | Which records does the list return: only approved collaterals, or all statuses? Is either search field mandatory (both carry an asterisk in Forms)? |
| Q2 | What does the **Amount** column hold for each type? |
| Q3 | Field naming: is property *Collateral amount* the same as *Market value* on Creation? Is shares *Stock amount* the same as *Security amount*? |
| Q4 | Can the guarantee *Account number* and *Collateral type* be amended? Can the cash *Source account* be changed, or only the amount and dates? |
| Q5 | The Forms screen has a **Reject** button, left out of the new design. If approvers evaluate amendments on this screen (the title says "Amendment/**Evaluation**"), that belongs on a separate approval screen. Confirm. |
| Q6 | Does an amendment need its own approval, and does the old value stay in force until then? (The design assumes yes.) |
| Q7 | Is a reason for the amendment required (for audit), or is *Comments* enough? |
| Q8 | Can a record with a pending amendment be amended again, or must the first one be approved or rejected? (The design blocks it.) |
| Q9 | Are any fields locked after approval (for example the customer or the collateral type)? |
| Q10 | Is an audit history of past amendments needed on the details page? |

## 7. Angular notes

- The details page reuses the Creation **dynamic form** and field definitions. Each type's amendment layout is a `CollateralTypeDef` that reuses Creation sections where the fields match.
- Change tracking is a small wrapper around the form: keep the loaded values, compare on every change (`form.valueChanges`), and expose `changes[]` for the Amendment panel and the Submit state.
- Candidate endpoints:

| Method | Endpoint | Replaces (Forms) |
|---|---|---|
| `GET` | `/collaterals?customerNo=&collateralNo=&type=&sort=&page=` | Fetch / grid query |
| `GET` | `/collaterals/{no}` | `>` button, details page load |
| `POST` | `/collaterals/{no}/amendments` | Submit (body: changed fields only, with old and new values) |
| `POST` | `/collaterals/{no}/amendments/{id}/reject` | Reject (future approval screen, not this module) |
| `GET` | `/collaterals/{no}/documents` | View Documents |
