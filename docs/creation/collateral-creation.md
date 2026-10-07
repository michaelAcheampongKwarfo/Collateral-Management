# Collateral Creation: Functional Specification

| | |
|---|---|
| **Module** | Collateral Management › Creation (Oracle Forms screen `Collateral Creation - LRSK`) |
| **Target** | Angular front end (migration from Oracle Forms) |
| **Status** | Draft for presentation. Business rules will be confirmed against the PL/SQL behind the current screen. |
| **Prototype** | [`design/prototype/index.html`](../../design/prototype/index.html) (open in a browser; Creation is the default view) |
| **Reference screens** | [`screenshots/creation/`](../../screenshots/creation/) |

---

## 1. Purpose

The Collateral Creation screen lets a user record a new collateral item against a customer. The user identifies the customer, chooses a collateral type, and fills in the details that type requires. On submit, the system assigns a collateral number and the record waits for approval.

Five collateral types exist today. Each type has its own form:

| Code | Type | What is pledged |
|---|---|---|
| `C01` | Cash collaterals | A lien on one of the customer's own deposit accounts |
| `C02` | Insurance collaterals | An assigned insurance policy |
| `C03` | Property collateral | Land or buildings |
| `C04` | Guarantee collaterals | A guarantee or deposit held at a financial institution |
| `C05` | Shares / stocks / securities collateral | Listed shares, stocks or securities |

> The type list comes from a lookup (LOV) in Oracle Forms. The Angular version must load it from the same reference table so that new types can be added without a front-end release. Each type then needs a form definition (see §6).

## 2. User flow

1. **Find the customer.** The user types the customer number and presses Enter, or searches the customer list. The system fetches and shows the **customer name** and **customer type** (e.g. `INDIVIDUAL`, `CORPORATE`). The customer's existing collaterals load into the table at the bottom of the screen.
2. **Choose the collateral type.** The user picks one of the five types. The details area shows the form for that type.
3. **Complete the details.** The user fills in the type-specific fields and the common *Collateral details* section (amount, review date, expiry date, comment).
4. **Attach documents** (optional): valuation report, title deed, policy, share certificate, and so on.
5. **Submit.** The system validates every required field. If all pass, it saves the record, assigns the **collateral number** and sends the record for approval.

Toolbar actions available throughout: **Help**, **Comment**, **New** (clear the screen), **Submit**, **Exit**.

The flowchart, built from the PL/SQL, is in [`flowchart.md`](flowchart.md).

## 3. Screen layout

### 3.1 Oracle Forms (current)

```
┌ Collateral Creation - LRSK ─────────────────────────────────────────┐
│ [Help] [Comment]                          [New] [Submit] [Exit]      │
│ ─────────────── CAPTURE CUSTOMER COLLATERAL ───────────────────────  │
│ Customer Number* [______][🔍]      Customer Type [__________]        │
│ Customer Name    [___________________________________]               │
│ Collateral Type* [___][🔍] [________________________]                │
│ ┌──────────── dynamic area: form for the chosen type ─────────────┐  │
│ │                                                                  │  │
│ └──────────────────────────────────────────────────────────────────┘ │
│ Customer other collaterals (grid)                                    │
│ Mandatory fields are indicated by a red asterisk (*).                │
└──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Angular (proposed)

| Area | Oracle Forms | Angular design |
|---|---|---|
| Navigation | One window per screen | App shell with a module sidebar: **Creation** now, **Amendment** and **Cancellation** next |
| Toolbar | Help, Comment, New, Submit, Exit buttons | The **standard action bar** used on every module screen, in the same order as Forms: Help, Comment, New (blue), Reject (amber, disabled on Creation), Submit (green), Exit (red). Help and Comment open side panels. See [design system](../design-system.md#standard-action-bar). |
| Customer | Number + LOV button, read-only name and type | **Step 1** card: number field with search (Enter to fetch), next to a **customer profile strip** across the row: name and number, customer type, home branch (`010 · SINKOR`), number of collaterals held and total amount held |
| Collateral type | Code + LOV button + description | **Step 2** card: five selectable tiles that show code, name and a one-line description. Arrow keys move between tiles. |
| Dynamic area | Stacked canvas for the selected type | **Step 3** card built from the type's form definition, grouped into sections |
| Collateral No | Read-only green field | Shown in the **Summary** panel as "Assigned on submit", then in the confirmation dialog |
| Balances (cash) | Panel on the right of the cash form | **Account balances** card in the right-hand panel |
| Attach Document | Green button | **Supporting documents** drop zone with a file list |
| Other collaterals | Grid at the bottom | Table at the bottom with an added **Status** column. New submissions appear at the top as *Pending approval*. |
| Mandatory hint | Footer bar | Red asterisk on labels, an inline message under each field and an error summary at the top of the form |

## 4. Fields

Legend: **Req** = mandatory (red asterisk in Forms). **LOV** = picked from a lookup list (shows code + description). **RO** = read-only, filled by the system.

### 4.1 Header (all types)

| Field | Kind | Req | Notes |
|---|---|---|---|
| Customer number | Text + LOV | Yes | Enter or LOV pick fetches the customer |
| Customer name | RO | | From customer master |
| Customer type | RO | | e.g. `INDIVIDUAL`, `CORPORATE` |
| Collateral type | LOV | Yes | `C01` to `C05`. Code and description |

### 4.2 Cash collateral (`C01`)

**Account details**

| Field | Kind | Req | Notes |
|---|---|---|---|
| Source account | LOV | Yes | The customer's accounts. Shows the account name |
| Source branch | RO | | Code + name from the account, e.g. `010 SINKOR` |
| Product | RO | | Code + description, e.g. `220 SAVINGS PERSONAL` |
| Currency | RO | | Code + description, e.g. `010 GHANA CEDIS` |

**Balances** (RO, from the account): Available balance, Cleared balance, Uncleared balance (with drill-down), OD amount, Block amount (with drill-down).

**Collateral details**

| Field | Kind | Req |
|---|---|---|
| Collateral amount | Amount | Yes |
| Next review date | Date | Yes |
| Expiry review date | Date | Yes |
| Comment | Text area | |

### 4.3 Insurance collateral (`C02`)

| Section | Field | Kind | Req |
|---|---|---|---|
| Insurance details | Insurance company | LOV | Yes |
| | Insurance code | Text | Yes |
| | Policy type | LOV | Yes |
| | Policy number | Text | Yes |
| Collateral details | Amount considered | Amount | Yes |
| | Sum assured | Amount | Yes |
| | Review date | Date | Yes |
| | Expiry date | Date | Yes |
| | Comment | Text area | |

### 4.4 Property collateral (`C03`)

| Section | Field | Kind | Req | Notes |
|---|---|---|---|---|
| Property details | Property type | LOV | Yes | |
| | Sub property type | LOV | | Filtered by property type (assumed) |
| | Ownership name | Text | Yes | |
| | Location | Text | Yes | |
| | Valuer name | Text | Yes | |
| | Valuer contact number | Phone | Yes | Format hint: `0302678178` |
| | Valuation date | Date | Yes | |
| | Market value | Amount | Yes | |
| | Forced sale value | Amount | Yes | |
| Collateral details | Amount considered | Amount | Yes | |
| | Review date | Date | Yes | |
| | Expiry date | Date | Yes | |
| | Comment | Text area | | |

### 4.5 Guarantee collateral (`C04`)

| Section | Field | Kind | Req | Notes |
|---|---|---|---|---|
| Guarantee details | Financial institution | LOV | Yes | |
| | Account number | LOV | Yes | Filtered by institution (assumed) |
| | Currency | LOV | Yes | |
| | Branch | Text | | |
| | Deposit type | LOV | Yes | |
| | Collateral type | LOV | Yes | Sub-type of guarantee |
| | Interest rate | Percent | Yes | |
| | Guarantee amount | Amount | Yes | |
| | Number of months | Integer | Yes | |
| | Folio number | Text | Yes | |
| | Folio start number | Text | Yes | |
| | Folio end number | Text | Yes | |
| Collateral details | Amount considered | Amount | Yes | |
| | Review date | Date | Yes | |
| | Expiry date | Date | Yes | |
| | Comment | Text area | | |

### 4.6 Shares / stock / security collateral (`C05`)

| Section | Field | Kind | Req |
|---|---|---|---|
| Shares / stock / security details | Share / security code | LOV | Yes |
| | Index | LOV | Yes |
| | Number of shares / securities | Integer | Yes |
| | Security amount | Amount | Yes |
| | Market value | Amount | Yes |
| | Folio number | Text | Yes |
| | Folio start number | Text | Yes |
| | Folio end number | Text | Yes |
| Collateral details | Amount considered | Amount | Yes |
| | Review date | Date | Yes |
| | Expiry date | Date | Yes |
| | Comment | Text area | |

### 4.7 Customer's other collaterals (grid)

Columns: Collateral no., Customer no., Collateral type, Description, Amount considered, Amount available, Approval date. The Angular design adds **Status** (e.g. *Approved*, *Pending approval*).

## 5. Behaviour and validation

### 5.1 Confirmed from the screenshots

- Customer name and type are filled from the customer number and cannot be edited.
- The collateral type decides which form is shown.
- For cash, choosing the source account fills branch, product, currency and the balance panel.
- Fields marked with a red asterisk are mandatory.
- The collateral number is system-generated. Example: `202509273039629`, which looks like `YYYYMMDD` + a 7-digit sequence.

### 5.2 To confirm against the PL/SQL

> **Update:** the Creation PL/SQL answers Q1 (cash only), Q5, Q8 and Q9, and shows no business-rule checks for Q2–Q4. See [flowchart.md §5–6](flowchart.md#5-findings-to-check-before-migrating) for the answers and the findings it raised.

These rules are likely but not visible in the screenshots. The prototype does **not** enforce them yet.

| # | Question |
|---|---|
| Q1 | When is the collateral number generated: when the type is chosen (the cash screenshot shows one) or on commit (other types show it blank)? |
| Q2 | Can the cash *collateral amount* exceed the account's available balance? Does submit place a block/lien on the account? |
| Q3 | Must the review date be before the expiry date? Must either be in the future? |
| Q4 | Is *amount considered* limited by market value, forced sale value, sum assured or guarantee amount (e.g. a haircut percentage)? |
| Q5 | Does *Sub property type* depend on *Property type*? Does the guarantee *Account number* depend on the *Financial institution*? |
| Q6 | Folio start/end: is end ≥ start required, and must the count match the number of shares? |
| Q7 | Which customer statuses or types are blocked from creating collateral? |
| Q8 | What does **Comment** on the toolbar store, compared with the *Comment* field inside the form? |
| Q9 | What happens after submit: which approval queue, and who is notified? |
| Q10 | Allowed file types and size for attached documents, and where they are stored. |
| Q11 | Is there a check for duplicates (same policy number, same account, same folio range)? |

### 5.3 Validation messages (Angular)

| Situation | Message |
|---|---|
| Required text/amount empty | "Enter the {field}." |
| Required LOV empty | "Select the {field}." |
| Required date empty | "Choose the {field}." |
| Non-numeric amount | "{Field} must be a number." |
| Customer not found | "No customer found with number {n}. Check the number or search by name." |
| Submit with errors | Error summary at the top of the form: "{n} fields need attention before you can submit.", with each item linking to its field |

## 6. Proposed Angular approach

### 6.1 Dynamic forms from configuration

In Oracle Forms each type has its own canvas. In Angular, one **dynamic form** component renders any type from a definition:

```ts
interface CollateralTypeDef {
  code: 'C01' | 'C02' | 'C03' | 'C04' | 'C05' | string;
  title: string;
  sections: { title: string; desc: string; fields: FieldDef[] }[];
  sidePanel?: 'balances';
}

interface FieldDef {
  id: string;                 // maps to the API / DB column
  label: string;
  type: 'text' | 'amount' | 'percent' | 'int' | 'date' | 'tel' | 'textarea' | 'lookup' | 'derived';
  required?: boolean;
  lookup?: string;            // reference-data endpoint, e.g. 'insurance-companies'
  dependsOn?: string;         // parent field for cascading lookups
  col: 4 | 5 | 6 | 7 | 8 | 12;  // columns out of 12; each row totals 12
}
```

The prototype already works this way (`TYPES` and `LOVS` in `design/prototype/index.html`). The same definitions can move into a TypeScript constant or come from the server.

### 6.2 Suggested component structure

```
collateral/
├── shell/                         app layout, module sidebar
├── creation/
│   ├── creation-page.component    page header, toolbar, step orchestration
│   ├── customer-lookup.component  step 1
│   ├── collateral-type-picker     step 2 (tiles)
│   ├── dynamic-collateral-form    step 3 (renders CollateralTypeDef)
│   ├── summary-panel              summary, progress
│   ├── balances-panel             cash only
│   ├── attachments-panel
│   └── other-collaterals-table
├── shared/
│   ├── lookup-field (LOV)         searchable dialog, keyboard friendly
│   ├── amount-input, date-input
│   └── help-drawer, comment-drawer
└── services/
    ├── customer.service           GET customer, GET customer collaterals
    ├── reference-data.service     all LOVs
    └── collateral.service         POST collateral, upload documents
```

### 6.3 Candidate API endpoints

To be aligned with the existing PL/SQL packages (each likely becomes a REST wrapper around a procedure):

| Method | Endpoint | Replaces (Forms) |
|---|---|---|
| `GET` | `/customers/{customerNo}` | Customer number `WHEN-VALIDATE-ITEM` |
| `GET` | `/customers?query=` | Customer LOV |
| `GET` | `/customers/{customerNo}/collaterals` | "Customer other collaterals" block query |
| `GET` | `/customers/{customerNo}/accounts` | Source account LOV (cash) |
| `GET` | `/accounts/{accountNo}/balances` | Balances panel |
| `GET` | `/reference/collateral-types` | Collateral type LOV |
| `GET` | `/reference/{lookup}?parent=` | Other LOVs (insurance companies, policy types, property types, …) |
| `POST` | `/collaterals` | Submit / commit |
| `POST` | `/collaterals/{no}/documents` | Attach Document |

## 7. Out of scope (later phases)

- **Amendment** and **Cancellation** modules, plus any others to be added.
- Approval workflow screens.
- Role-based permissions (assumed to follow the current Forms responsibilities).
