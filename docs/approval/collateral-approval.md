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
| Search | One box, about 360px wide (as in Enquiry): customer name, customer number or collateral number, filtering as you type |
| Request filter | Chips: All, Creation, Amendment, Cancellation, each with a count and its own colour (blue, amber, red) |
| Table | Request (coloured badge) · Collateral no. · Customer · Collateral type · Considered · **What's asked** (*New collateral*, *3 fields changed*, *Close: reason…*) · Submitted (date, *by* user, "(you)" if it's yours) · **›** |
| Sidebar | **Approvals** shows a red badge with the number of requests waiting |

### 3.2 Request page

The request opens on the **same layout as its entry screen**, with every field read-only.

| Area | Design |
|---|---|
| Header | **Back to approvals**, title "*Creation / Amendment / Cancellation* approval" + collateral number |
| Action bar | **Help**, **Comment**, divider, **Return** (amber), **Dismiss** (rose), **Authorize** (green, solid), divider, **Exit** |
| Request strip | Request type · Submitted by · Submitted on · Collateral type · Amount considered · plus *Collateral no.* (creation), *Fields changed* (amendment) or *Coverage released* (cancellation) |
| Customer | The shared customer profile strip |
| Closure reason | Cancellation only: the reason as entered, in a red-edged card |
| Form | The type's form, read-only: the **Creation** form for creation requests, the **Amendment** form for amendments and cancellations |
| Amendment highlighting | Each changed field has an amber outline, a **Changed** tag and its current (pre-amendment) value underneath |
| Rail: Decision | What each action does: Return, Dismiss, Authorize, and how many checklist items Authorize needs |
| Rail: Requested changes | Amendment only: count and *old → new* list |
| Rail: Account balances | Cash only |
| Rail: Documents | Documents attached to the request, with **View documents** (read-only documents modal) |

### 3.3 Decisions

| Action | What happens |
|---|---|
| **Authorize** | Opens the **verification checklist** (below). Once every item is ticked: creation → the collateral becomes *Approved* and appears in Amendment and Cancellation; amendment → the new values replace the old; cancellation → the collateral is closed and leaves the lists. |
| **Return** | Opens a dialog with a required **Return reason** ("say exactly what needs correcting"). The request leaves the approval queue and goes to the submitter's **Returned** queue (§3.5). The collateral shows *Amendment returned* / *Cancellation returned* and stays locked. |
| **Dismiss** | Opens a dialog with a required **Dismissal reason** and a **Dismiss permanently** tick. The request leaves the queue for good: a creation is not created; an amendment or cancellation leaves the collateral unchanged and available again. Replaces *Reject*. |

**Verification checklist** (training note 5, modelled on the Forms *VER* window). A blue "Verification · Confirm" header, then one row per item with a tick box, an "*n* of *m* confirmed" counter and **Tick all**. Authorize stays disabled until every item is ticked. Items depend on the request and collateral type:

| Part | Items |
|---|---|
| First | Creation: *Customer and collateral type confirmed?* · Amendment: *Every changed field confirmed?* · Cancellation: *Closure reason confirmed?* and *No running loan still depends on this collateral?* |
| By type | Cash: source account and balances; amount within available balance · Insurance: company and policy; amount within sum assured · Property: property, ownership, location; market and forced sale value · Guarantee: institution and account; amount, rate and tenor · Shares: security code and units; market value and folio range |
| Last | *Review and expiry dates confirmed?* · *Supporting documents confirmed?* |

### 3.5 Returned queue (training note 4)

- A **Returned** module in the sidebar, with an amber count. Its list is laid out like the approval queue: action bar **Help**, **New** (clears the search), **Exit**; the same search box; request-type chips with counts; columns request type, collateral no., customer, type, amount considered, **return reason**, returned by and when, and **›**.
- **›** reopens the request **on its own entry screen**, filled with what was submitted:
  - Creation → the Creation screen, customer and type selected, every field filled.
  - Amendment → the Amendment details page, with the proposed changes highlighted against the approved values.
  - Cancellation → the Cancellation details page, with the closure reason filled in.
- An amber **Returned for correction** banner at the top shows who returned it, when, and the reason.
- **Submit** sends it back to the approval queue with the **same collateral number** and removes it from Returned.

### 3.4 Connected prototype

Requests created in the prototype's Creation, Amendment and Cancellation modules go straight into this queue. Deciding them updates every module, so the full lifecycle can be demonstrated live: submit → approve → amend → approve → cancel → approve, plus return → correct → resubmit and dismiss.

## 4. Maker-checker (confirmed)

**Rule:** a user can't approve a request they submitted. In Forms this is checked in the `WHEN-NEW-FORM-INSTANCE` trigger (`username != posted_by`). The Angular build must enforce it on the server as well as in the screen.

In the prototype:

- The queue still lists the user's own requests, with *by K.ASARE (you)* and a grey **Yours** tag, so they can see what is waiting.
- Opening one shows a blue banner: *"You submitted this request, so you can't decide on it. Another officer must return, dismiss or authorize it."* The action bar drops to **Help**, **Comment**, **Exit**, and the Decision card is hidden.
- For the demo, the user menu at the top right switches between **K. Asare** (collateral officer) and **A. Mensah** (credit supervisor), so both sides can be shown.

## 5. To confirm against the PL/SQL

| # | Question |
|---|---|
| Q1 | ~~Is maker-checker enforced?~~ Confirmed: yes (§4). Still open: is there an approval limit by amount or role? |
| Q2 | How does an approver reach requests today: an approval inbox, or by entering the collateral number? (The design assumes a queue.) |
| Q3 | Where are return and dismissal reasons stored, and how is the submitter notified (in-app, email)? |
| Q4 | Can the submitter withdraw a returned request instead of correcting it? Is there a time limit before it is dismissed automatically? |
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
