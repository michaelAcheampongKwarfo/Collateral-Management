# Collateral Cancellation: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Cancellation (Oracle Forms screen `Collateral Closing`, block *Collateral Closure*) |
| **Target** | Angular front end (migration from Oracle Forms) |
| **Status** | Draft for presentation. Business rules will be confirmed against the PL/SQL behind the current screen. |
| **Prototype** | [`design/prototype/index.html#cancellation`](../../design/prototype/index.html) (open in a browser, then choose **Cancellation** in the sidebar) |
| **Reference screen** | [`screenshots/cancellation/cancellation.PNG`](../../screenshots/cancellation/cancellation.PNG) |

---

## 1. Purpose

Cancellation closes an approved collateral that the bank no longer holds, for example because the facility it secured was repaid. The user records a **closure reason** and submits the cancellation for approval. Nothing else about the collateral can be changed here.

## 2. Design decision: same pattern as Amendment

The Oracle Forms screen is a single generic form for every collateral type: pick the customer and collateral number, see a fixed set of summary fields, enter the closure reason. It has no list and no per-type forms.

The Angular design deliberately follows the **Amendment** pattern instead, so the three modules work the same way:

| | Oracle Forms | Angular |
|---|---|---|
| Finding the record | Customer ID LOV, then Collateral No LOV | The same **search list** as Amendment: optional customer and collateral number, type chips, sorting, paging, **›** to open |
| Showing the record | One generic block of fields for all types | The collateral's **own type form**, the same layout as Amendment, shown **read-only** |
| Summary values | Estimated market, coverage, available and realizability values in the form | Kept, as a **Closure summary** strip above the form |
| Closure reason | Text field | A **Cancellation** card: quick-pick reasons that fill an editable text box, required, 300 characters |
| Submit | Submits directly | Asks for **confirmation** first, then sends for approval |

Why:
- **One way of working.** A user who knows Amendment already knows Cancellation. The list, type forms and record panels are shared code in Angular.
- **The user sees what they are closing.** The full type form shows exactly which policy, property or account is being released, instead of a generic summary.
- **Read-only is obvious.** Values sit in plain grey boxes with no input borders, and the form header says "Read only". The only editable control on the page is the reason, in a card with a red edge.

## 3. User flow

1. Open **Cancellation**. The list shows approved collaterals.
2. Optionally search by customer number and/or collateral number, filter by type, or sort.
3. Select **›** to open a collateral.
4. Review the customer, the **Closure summary** and the read-only type form.
5. Enter the **closure reason**. A quick-pick reason fills the box and can be edited.
6. Select **Submit**. A confirmation dialog states what happens on approval and shows the reason.
7. Confirm with **Submit cancellation**. The collateral shows **Cancellation pending** and is locked in both Amendment and Cancellation until the request is approved or rejected.

A draft flowchart is in [`flowchart.md`](flowchart.md).

## 4. Screen 1: Search list

The same component as Amendment ([amendment spec §3.2](../amendment/collateral-amendment.md#32-angular-design)), with Cancellation wording ("Cancel a collateral", "Select › to open one to cancel it").

Rows whose status is not *Approved* (either *Amendment pending* or *Cancellation pending*) are muted and cannot be opened, in either module.

## 5. Screen 2: Details page

| Area | Design |
|---|---|
| Header | **Back to search results**, title "Cancel collateral" + collateral number, standard action bar |
| Customer | The shared customer profile strip |
| Closure summary | Collateral type · Currency · Estimated market · Coverage value · Available value · Realizability value |
| Type form | The Amendment form for the collateral's type, read-only (values in grey boxes, lookups as code chip + description, amounts right-aligned) |
| Cancellation card | Closure reason* with quick-pick chips and a character count · Cancellation date (today, auto-filled) · Requested by (current user, auto-filled) · Status after submit (*Cancellation pending*) |
| Rail: What happens on submit | Sent for approval → locked → closed on approval (for cash: hold on the account released) |
| Rail: Record, Account balances (cash), Documents | As Amendment. Documents are **view only** |
| Action bar | Help, Comment enabled. New disabled. Reject disabled (see Q6). **Submit enabled only once a reason is entered.** Exit returns to the list and asks before discarding a typed reason. |

### 5.1 Quick-pick reasons (proposal)

Facility fully repaid · Collateral replaced by another collateral · Collateral released to the customer · Captured in error.

These only fill the text box; the stored value is the free text, as in Forms. If the bank wants reasons reported on, they should become a coded list (see Q3).

### 5.2 Closure summary mapping (to confirm)

The labels come from the Forms closing screen. How the prototype fills them with sample data:

| Forms label | Prototype value | Question |
|---|---|---|
| Estimated Market | The type's main value (account balance, sum assured, collateral amount, guarantee amount, market value) | Q4 |
| Coverage Value | Amount considered | Q4 |
| Available Value | Amount considered (`AMT_AVAIL` in Creation) | Q4 |
| Realizability Value | Forced sale value for property, otherwise amount considered | Q4 |

### 5.3 Forms fields not shown separately

*Collateral Description*, *No. of Shares*, *Pledged A/C*, *Company* and *Collateral Location* are generic Forms fields that the type forms already show under their real names (for example *Number of shares*, *Source account*, *Insurance company*, *Location*).

## 6. Behaviour and validation

### 6.1 In the prototype

- Closure reason is required (trimmed) and limited to 300 characters.
- Submit opens a confirmation (`alertdialog`) with the type, the coverage value released and the reason. **Keep collateral** cancels; **Submit cancellation** submits.
- After submit the record shows **Cancellation pending** in both modules' lists and cannot be opened.

### 6.2 To confirm against the PL/SQL

| # | Question |
|---|---|
| Q1 | Does cancellation need approval, or does Submit close the collateral immediately? (The design assumes approval, like Creation and Amendment.) |
| Q2 | Can a collateral be closed while it still secures an active facility? Should the system block it or warn? |
| Q3 | Is the closure reason free text only, or should it be a coded list for reporting? |
| Q4 | Where do Estimated Market, Coverage, Available and Realizability values come from? |
| Q5 | In Forms, *Estimated Market* and *Review Date* look editable at closure. Should they be? (The design shows them read-only.) |
| Q6 | Is **Reject** used on this screen by an approver? |
| Q7 | For cash collateral, is the lien or hold on the pledged account released automatically on approval? |
| Q8 | Is a closed collateral kept (status *Closed*) or deleted from `TB_COLLATERAL`? |

## 7. Angular notes

- Reuse the Amendment list, details layout and type definitions. Add a `readonly` input to the dynamic form so it renders values instead of controls.
- Candidate endpoints:

| Method | Endpoint | Replaces (Forms) |
|---|---|---|
| `GET` | `/collaterals?customerNo=&collateralNo=&type=&status=APPROVED` | Customer ID / Collateral No LOVs |
| `GET` | `/collaterals/{no}` | Loading the closing form |
| `POST` | `/collaterals/{no}/cancellations` | Submit (body: reason) |
| `GET` | `/collaterals/{no}/documents` | View Documents |
