# Training Session Notes: Traceability

Notes taken after the Collateral Management training session, with where each one is handled. **Status** is one of:

- **Prototype**: shown in the UI prototype (`design/prototype/index.html`).
- **Backend**: a server-side rule or job for the Angular build; the prototype may show the UI side.
- **To research / decide**: needs an answer from the business or the PL/SQL team.

Modules in scope: **Creation, Amendment, Cancellation, Enquiry, Approval, Returned, Reporting**.

## Creation

| # | Note | Status | Where / how |
|---|---|---|---|
| 1 | All customers allowed to make collateral | Prototype + Backend | Any customer can be searched. The current Forms list filters on account type ≠ 9 and status N (see [creation flowchart](creation/flowchart.md)); confirm whether that filter stays. |
| 2 | Collateral number is system generated | Prototype + Backend | Shown as "Assigned on submit"; generated on submit. Backend: one sequence for all types (Forms uses `GET_BATCHNO` for cash only). |
| 3 | Source accounts linked to the customer number | Prototype | The account lookup lists only the selected customer's accounts. |
| 4 | Selecting a source account auto-fills account details and balances | Prototype | Branch, product, currency (auto-filled) and the Account balances panel. |
| 5 | Cash: validate collateral amount against available balance | **Prototype (new)** | "Can't exceed the available balance of …". Hint under the field states the limit. Also enforced in Amendment. |
| 6 | Enforce the next review date (alert, notification, report) | **Prototype (new)** + Backend | Enquiry gets **Overdue** and **Due in 30 days** quick filters and an Overdue / Due soon tag on the review date. The **Review due / overdue** report is built (see Reporting below). Backend: a daily job for reminders. |
| 7 | Next review date must be before the expiry date | **Prototype (new)** | "The review date must be before the expiry date." on every collateral type, in Creation and Amendment. |
| 8 | Document reference button opens a modal to register documents | Prototype | Supporting documents modal (replaces Forms *Document Registration*). |
| 9 | Show other collateral registered for the customer | Prototype | "Customer's other collaterals" table and the Collaterals / Amount held figures on the customer strip. Now read from the same records as every other module. |
| 10 | Insurance: sum assured = policy total; amount considered = amount secured | Prototype | Field labels and the limit hint under Amount considered. |
| 11 | Insurance: validate amount considered against sum assured | **Prototype (new)** | "Can't exceed the sum assured of …". |
| 12 | Property: validate market value against forced sale value | **Prototype (new)** | Forced sale value can't exceed market value (collateral amount in Amendment). |
| 13 | Property: validate amount considered against forced sale value | **Prototype (new)** | "Can't exceed the forced sale value of …". |
| 14 | Guarantee: branch populates from the customer account | **Prototype (new)** | Account number now lists the customer's own accounts (as the Forms PL/SQL does: `G_LEDGER` types 1–3) and Branch is auto-filled from the chosen account. |
| 15 | Guarantee: research deposit type, collateral type, interest rate, months, folio | To research | See [Guarantee fields: working notes](#guarantee-fields-working-notes). |

## Approval and Enquiry

| # | Note | Status | Where / how |
|---|---|---|---|
| 1 | Show the exact details captured; approval has actions, enquiry has none | Prototype | Both open the captured type form read-only. Approval has Return, Dismiss, Authorize. Enquiry details only has Help and Exit (navigation, no actions on the record). |
| 2 | Approver can approve or reject | **Prototype (updated)** | Actions are **Authorize**, **Return** and **Dismiss** (dismiss replaces reject). |
| 3 | Approval and enquiry fields read-only | Prototype | No inputs on either screen. |
| 4 | Return with a reason → queue for correction → resubmit; and a button to dismiss for good with a reason and confirmation | **Prototype (new)** | **Return** needs a reason and sends the request to the new **Returned** queue. The submitter reopens it on its own entry screen (Creation, Amendment or Cancellation) with the reason in a banner, corrects it and submits again with the same collateral number. **Dismiss** needs a reason and a "Dismiss permanently" tick; the request leaves the queue. |
| 5 | Confirmation modal the approver must tick before approving / dismissing | **Prototype (new)** | **Authorize** opens a verification checklist modelled on the Forms *VER* window: 5–6 items specific to the request and collateral type; Authorize stays disabled until all are ticked. **Dismiss** needs the reason plus the final confirmation tick. |

## Guarantee fields: working notes

These are **working assumptions from common banking practice**, to be confirmed against the PL/SQL and with the credit team (note 15). The Forms screen and the creation PL/SQL give these clues: the institution list is the same as insurance companies (`CODE_DESC` type `ICC`), the account list is the customer's own accounts, deposit types come from `CODE_DESC` type `ACT`, and the guarantee's own collateral type is chosen from C01, C02, C03, C05 (never C04) and stored in `PROPERTY_TYPE`.

| Field | Likely meaning | Likely linked to |
|---|---|---|
| Financial institution | The bank or insurer that issued the guarantee or holds the deposit | The institution, not the customer |
| Account number | The customer's account the guarantee relates to (in Forms: the customer's own accounts) | The customer |
| Deposit type | The kind of deposit backing the guarantee: fixed deposit, call deposit, treasury bill… | The deposit at the institution |
| Collateral type (inside guarantee) | What the guarantee is ultimately backed by: cash, insurance, property or shares | The underlying asset |
| Interest rate | The rate earned on the backing deposit | The deposit (agreed with the institution) |
| Number of months | The deposit's tenor; the guarantee should not outlive it | The deposit |
| Folio no., start, end | The register / certificate reference and the range of certificates or leaves pledged | The institution's register |

**Questions for the team:** Should currency, rate and months be read from the deposit record rather than typed? Should the review/expiry dates be capped by the deposit's maturity (start date + months)? Should institutions have their own list instead of reusing insurance companies?

## Reporting

The training listed **Reporting** as a module. Chosen for the roadmap: **Review due / overdue**, **Expiring collateral** and **Audit trail**. The presentation is about the UI, so one is prototyped: **Review due / overdue** ([spec](reporting/review-due-overdue.md)). The others reuse the same layout (parameters, summary, grouped table, PDF / Excel).

All proposed reports, filterable by branch, type and date and exportable to PDF / Excel like the enquiry grids:

| Report | Purpose |
|---|---|
| Review due / overdue | Collateral whose next review date is overdue or within N days (answers creation note 6). **Prototyped** |
| Expiring collateral | Collateral expiring within N days. **Chosen, next** |
| Coverage and utilisation | Coverage, value used and available, by customer, branch and type |
| Pending, returned and dismissed requests | Ageing of the approval queue and the Returned queue, with reasons |
| Collateral register | Everything held, as at a date |
| Audit trail | Who created, amended, returned, dismissed or authorized what, and when. **Chosen, next** |

## Other decisions from the follow-up

| Point | Outcome |
|---|---|
| Maker-checker | Confirmed: a user can't approve their own entry (Forms `WHEN-NEW-FORM-INSTANCE`, `username != posted_by`). Enforced in the prototype; see [Approval §4](approval/collateral-approval.md#4-maker-checker-confirmed). |
| Approvals search | Narrowed to about half (360px), the same box as Enquiry. |
| Returned queue | Laid out like the approval queue: search, request-type chips, the same columns plus the return reason. |
| Entry screen wording | Shortened: Amendment *"Edit what needs changing. Changes are highlighted."*; Cancellation *"Enter the reason for cancelling. Everything else is read only."* |
