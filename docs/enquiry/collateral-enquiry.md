# Collateral Enquiry: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Enquiry (Oracle Forms `Collateral Enquiry`, module code LRCE) |
| **Target** | Angular front end (migration from Oracle Forms) |
| **Status** | Draft for presentation. Business rules will be confirmed against the PL/SQL. |
| **Prototype** | [`design/prototype/index.html#enquiry-all`](../../design/prototype/index.html) (`#enquiry-running`, `#enquiry-used` open the other two) |
| **Reference screens** | [`screenshots/enquiry/`](../../screenshots/enquiry/): grid and details for each of the three enquiries |

---

## 1. Purpose

Enquiry is read-only. It lets staff find any collateral and see its value, coverage and how much of it loans are using. There are three enquiries:

| Enquiry | Shows | Forms grid columns |
|---|---|---|
| **All collateral** | Every collateral, whatever its status | Customer No, Collateral No, Coll Type, Coll Description, Market Val, Value Used, Amount Considered, Account Number, Review Date |
| **Running collateral** (summary) | Active collateral and the coverage still available | Customer No, Collateral No, Coll Description, Market Value, Coverage Val, Realiz. Rate, Value Used, Avail. Value, Review Date |
| **Used collateral** (loan collateral) | Collateral drawn on by loan accounts, one row per loan | Customer No, Collateral No, Amount Considered, Coverage Val, Value Used, Coll Type, Account Number, Description, Used, Posted Date |

## 2. What changes from Forms

| | Oracle Forms | Angular |
|---|---|---|
| Choosing an enquiry | Separate screens | One **Enquiry** module: a sidebar group with three links, and tabs on the page |
| Search | A Filter Criteria block always open, filled before **Fetch** | **One search box** (customer name or number, collateral number, description, status) that filters as you type, with a **funnel** button for advanced filters |
| Advanced filters | Always visible | Opened from the funnel. Applied filters show as removable chips; the funnel shows how many are active |
| Grid | Fixed columns, `>` button per row | Sortable columns, paging, record count, **Refresh**, **PDF** and **Excel**, pinned **›** |
| Details | One generic form for every collateral type | Valuation and coverage figures, a **usage** panel, and the collateral's **own type form**, read-only |

## 3. Search and filters

**Quick search** matches customer name, customer number, collateral number, description and status as the user types.

**Advanced filters** (funnel), per enquiry, taken from the Forms Filter Criteria:

| Filter | All | Running | Used |
|---|---|---|---|
| Customer ID (with customer search) | ✓ | ✓ | ✓ |
| Branch | ✓ | ✓ | ✓ |
| Collateral no. | ✓ | ✓ | ✓ |
| Collateral type | ✓ | ✓ | ✓ |
| Status (Active, Pending, Closed) | ✓ | | |
| Coverage amount between | ✓ | ✓ | ✓ |
| Review date between | ✓ | ✓ | |
| Expiry date between | ✓ | ✓ | |
| Posted date between | | | ✓ |

**Fetch** applies the filters and closes the panel. Each applied filter becomes a chip (for example *Type: C03 · Property*) with its own remove button, plus **Clear all**. **New** on the action bar clears the search and every filter.

## 4. Grids

| Enquiry | Columns |
|---|---|
| All | Collateral no. · Customer (name, number) · Description (type, currency underneath) · Market value · Value used · Amount considered · Review date · Status · › |
| Running | Collateral no. · Customer · Description · Market value · Coverage value · Realiz. rate % · Value used · Avail. value · Review date · › |
| Used | Collateral no. · Customer · Description · Amt considered · Coverage value · Value used · Loan account · Posted date · › |

- Collateral type and currency sit under the description, so each grid fits a normal laptop screen without scrolling sideways.
- Every column sorts. 8 rows per page.
- **Excel** exports the rows currently shown (search and filters applied). In the prototype this is a CSV file; the Angular app should produce `.xlsx`.
- **PDF** exports the same rows as a landscape A4 report: title, record count, the active filters, date and user, then the table. The prototype builds it in the browser with jsPDF; the Angular app can do the same or generate it server-side.
- *Pending* creations appear in **All** with status *Pending*. **Running** shows only *Active* collateral. Closed collateral appears only in **All**.

## 5. Details page

| Area | Content |
|---|---|
| Header | Back link, "Collateral *number*" with its status, action bar **Help**, **Exit** (as in Forms) |
| Customer | The shared customer profile strip |
| Valuation and coverage | Collateral currency · Estimated market · Current value · Coverage value · Coverage rate % · Forced sale value · FSV rate % · Risk associated · Status of collateral · Registered stamp cost · Review date · Expiry date (the Forms details fields) |
| Usage | A bar of value used against coverage, with used and available amounts, and the loan accounts drawing on the collateral (account, value used, posted date) |
| Type form | The collateral's own form (cash, insurance, property, guarantee or shares), read-only |
| Rail | Record (number, type, status, branch, approved by, approval date) and Documents (view-only documents modal) |

The Forms details screen shows generic fields (*Policy No.*, *Pledge Account*, *Company*, *Collateral Location*, *Address*, *Shares Quantity*). These are covered by the type form under their real names, so they are not repeated.

## 6. To confirm against the PL/SQL

| # | Question |
|---|---|
| Q1 | How are **Value used**, **Avail. value** and **Realiz. rate** calculated? (The prototype uses value used = sum of loan usage, available = coverage − used, realization rate = coverage ÷ market value.) |
| Q2 | How are **Current value**, **Forced sale value**, **FSV rate %**, **Risk associated** and **Registered stamp cost** derived or stored? |
| Q3 | Which statuses does each enquiry include? Does **Running** exclude collateral with nothing available? |
| Q4 | In **Used**, what does the *Used* flag (`Y`) mean, and can one loan draw on several collateral items? |
| Q5 | Should the enquiry respect branch access (users only see their branch's collateral)? |
| Q6 | Are there limits on export size, and should exports be audited? |

## 7. Angular notes

- One `EnquiryPage` component with a route parameter (`/enquiry/all`, `/enquiry/running`, `/enquiry/used`) and a per-enquiry column and filter definition.
- Quick search and advanced filters map to one query object; chips are rendered from the applied filters.
- Candidate endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/collaterals/enquiry/{all\|running\|used}?q=&customerNo=&branch=&collateralNo=&type=&status=&coverageFrom=&coverageTo=&reviewFrom=&reviewTo=&expiryFrom=&expiryTo=&postedFrom=&postedTo=&sort=&page=` | Grid |
| `GET` | `/collaterals/enquiry/{...}/export?format=pdf\|xlsx&...` | PDF / Excel |
| `GET` | `/collaterals/{no}/enquiry` | Details: valuation, usage, type form values |
