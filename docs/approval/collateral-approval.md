# Collateral Approval: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Approvals (Oracle Forms `Collateral Registration` opened for authorization) |
| **Target** | Angular front end (migration from Oracle Forms) |
| **Status** | Draft for presentation. Business rules will be confirmed against the PL/SQL. |
| **Prototype** | [`design/prototype/index.html#approvals`](../../design/prototype/index.html) (open in a browser, then choose **Approvals** in the sidebar) |
| **Reference screens** | [`screenshots/approval/`](../../screenshots/approval/): creation and amendment approval samples. There is no cancellation approval screen; it is designed to match. |

---

## 1. Purpose

Every creation, amendment and cancellation is a request until an authorized officer approves it. The Approvals module is where that officer reviews each request and **authorizes** or **rejects** it.

## 2. What the Forms screens do

Both samples are the normal entry screen opened read-only, with:

- **Toolbar:** Help, Comment, (New), Reject, Authorize, Exit.
- **"Tick to Confirm All Details"** checkbox. Reject and Authorize are greyed out until it is ticked.
- **View Documents**.

The Angular design keeps all three ideas.

## 3. Design

### 3.1 Queue (list)

| Area | Design |
|---|---|
| Action bar | **Help**, **New** (clears the search), **Exit**. The same as the other search lists |
| Search | One box: customer name, customer number or collateral number, filtering as you type |
| Request filter | Chips: All, Creation, Amendment, Cancellation, each with a count and its own colour (blue, amber, red) |
| Table | Request (coloured badge) · Collateral no. · Customer · Collateral type · Considered · **What's asked** (*New collateral*, *3 fields changed*, *Close: reason…*) · Submitted (date, *by* user, "(you)" if it's yours) · **›** |
| Sidebar | **Approvals** shows a red badge with the number of requests waiting |

### 3.2 Request page

The request opens on the **same layout as its entry screen**, with every field read-only.

| Area | Design |
|---|---|
| Header | **Back to approvals**, title "*Creation / Amendment / Cancellation* approval" + collateral number |
| Action bar | **Help**, **Comment**, divider, **Reject** (amber), **Authorize** (green, solid), **Exit**. Reject and Authorize are disabled until the confirmation is ticked |
| Request strip | Request type · Submitted by · Submitted on · Collateral type · Amount considered · plus *Collateral no.* (creation), *Fields changed* (amendment) or *Coverage released* (cancellation) |
| Customer | The shared customer profile strip |
| Closure reason | Cancellation only: the reason as entered, in a red-edged card |
| Form | The type's form, read-only: the **Creation** form for creation requests, the **Amendment** form for amendments and cancellations |
| Amendment highlighting | Each changed field has an amber outline, a **Changed** tag and its current (pre-amendment) value underneath |
| Rail: Decision | **I have checked all the details** checkbox (the Forms "Tick to Confirm All Details"). The card turns green when ticked |
| Rail: Requested changes | Amendment only: count and *old → new* list |
| Rail: Account balances | Cash only |
| Rail: Documents | Documents attached to the request, with **View documents** (read-only documents modal) |

### 3.3 Decisions

| Action | What happens |
|---|---|
| **Authorize** | Creation: the collateral becomes *Approved* and appears in Amendment and Cancellation. Amendment: the new values replace the old. Cancellation: the collateral is closed and leaves the lists. A confirmation names the result. |
| **Reject** | Opens a dialog with a required **Rejection reason** (300 characters). Creation: the collateral is not created. Amendment or cancellation: the collateral keeps its values and becomes available again. The submitter sees the reason. |

### 3.4 Connected prototype

Requests created in the prototype's Creation, Amendment and Cancellation modules go straight into this queue. Deciding them updates every module, so the full lifecycle can be demonstrated live: submit → approve → amend → approve → cancel → approve.

## 4. Maker-checker

The prototype marks requests submitted by the signed-in user with "(you)" and shows a note on the request page: *"You submitted this request. In production a different officer must authorize it."* It still allows the approval so the demo works with one user. See Q1.

## 5. To confirm against the PL/SQL

| # | Question |
|---|---|
| Q1 | Is maker-checker enforced (the submitter cannot authorize their own request)? Is there an approval limit by amount or role? |
| Q2 | How does an approver reach requests today: an approval inbox, or by entering the collateral number? (The design assumes a queue.) |
| Q3 | Is a rejection reason captured today? Where is it stored, and is the submitter notified? |
| Q4 | Does a rejected request go back to the submitter for correction and resubmission, or is it closed? |
| Q5 | The creation sample shows **New** on the approval toolbar. What does it do there? (Left out of the design.) |
| Q6 | Is there a separate cancellation approval screen, or does the closing screen get re-opened for approval? |
| Q7 | Is one level of approval enough, or do some requests need two approvers? |

## 6. Angular notes

- Reuse the dynamic form with `readonly` (from Cancellation) and the change comparison (from Amendment).
- Candidate endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/approvals?type=&q=` | Queue |
| `GET` | `/approvals/{id}` | Request with the proposed values and, for amendments, the current values |
| `POST` | `/approvals/{id}/authorize` | Authorize |
| `POST` | `/approvals/{id}/reject` | Reject (body: reason) |
