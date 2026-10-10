# Review Due / Overdue Report: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Reports (new; no Oracle Forms equivalent) |
| **Target** | Angular front end |
| **Status** | Draft for presentation. Answers training note 6 (enforce the next review date). |
| **Prototype** | [`design/prototype/index.html#report-review`](../../design/prototype/index.html) |
| **Screenshots** | [`design/reporting/screens/`](../../design/reporting/screens/) |

---

## 1. Purpose

Lists open collateral whose **next review date** has passed, or falls within a chosen period, so branches can chase reviews before the collateral loses value or lapses. It is the on-screen side of the review reminders. The daily job that sends the same list by notification or email is backend work.

**Open** means approved and not cancelled. Pending requests are left out because their values aren't approved yet.

## 2. Screen

| Area | Content |
|---|---|
| Header | "Review due / overdue", action bar **Help**, **New** (resets the parameters), **Exit** |
| Parameters | **As at** (date, defaults to today) · **Due within** (30, 60 or 90 days) · **Branch** (all or one) · **Collateral type** (all or one). The report updates as they change. |
| Summary | Overdue (count) · Amount overdue · Due within *N* days (count) · Amount due · Longest overdue (days) · Reviewed on time (% of open collateral not overdue) |
| Results | Grouped table: **Overdue** first, then **Due by *date***, each with a count. Chips **All / Overdue / Due**, **PDF**, **Excel**. Footer shows the parameters and who ran it. |

Columns: Collateral no. · Customer (name, number) · Description (type and currency underneath) · Branch · Amount considered · Review date · Days (*"13 days overdue"* in red, *"in 14 days"* in amber) · Expiry date. Rows are in review-date order, oldest first.

## 3. Rules

| Rule | Detail |
|---|---|
| Overdue | Review date before the *As at* date |
| Due | Review date on or after *As at*, and within *Due within* days |
| Amounts | Sum of the amount considered |
| Reviewed on time | (open collateral − overdue) ÷ open collateral |
| Exports | PDF (landscape A4, with parameters, date and user) and Excel, using the rows shown |

## 4. To confirm

| # | Question |
|---|---|
| Q1 | Which date counts as "reviewed": a new review date entered through Amendment, or a separate review record? |
| Q2 | Who receives the daily reminder (submitter, branch manager, credit risk), and how (in-app, email)? |
| Q3 | Should users only see their own branch's collateral? |
| Q4 | Is a default window other than 30 days preferred? |

## 5. Angular notes

- One `ReportPage` layout (parameters, summary, grouped table, exports) reused by the chosen next reports, **Expiring collateral** and **Audit trail**.
- Candidate endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/reports/review-due?asAt=&within=&branch=&type=` | Summary and rows |
| `GET` | `/reports/review-due/export?format=pdf\|xlsx&...` | PDF / Excel |
