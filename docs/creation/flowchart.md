# Collateral Creation: Process Flow (draft)

> **Status: draft.** This flow is based only on the screenshots. It will be rewritten once the PL/SQL behind the Oracle Forms screen is reviewed. Nodes marked *(to confirm)* match the open questions in [`collateral-creation.md` §5.2](collateral-creation.md#52-to-confirm-against-the-plsql).

```mermaid
flowchart TD
    A([Open Collateral Creation]) --> B[Enter or search customer number]
    B --> C{Customer found?}
    C -- No --> C1[Show 'No customer found'] --> B
    C -- Yes --> D[Show customer name and type<br/>Load customer's other collaterals]
    D --> E[Choose collateral type]
    E --> F{Type}
    F -- C01 Cash --> G1[Select source account<br/>Fill branch, product, currency, balances]
    F -- C02 Insurance --> G2[Insurance company, code,<br/>policy type, policy number]
    F -- C03 Property --> G3[Property type, ownership, location,<br/>valuer, valuation, market and forced sale values]
    F -- C04 Guarantee --> G4[Institution, account, currency, deposit type,<br/>rate, amount, months, folio range]
    F -- C05 Shares --> G5[Security code, index, units,<br/>amount, market value, folio range]
    G1 & G2 & G3 & G4 & G5 --> H[Collateral details:<br/>amount, review date, expiry date, comment]
    H --> I[Attach documents - optional]
    I --> J[Submit]
    J --> K{All required fields valid?}
    K -- No --> K1[Show field errors and summary] --> H
    K -- Yes --> L{"Business rules pass?<br/>(to confirm)"}
    L -- No --> L1[Show rule message] --> H
    L -- Yes --> M[Save collateral<br/>Generate collateral number]
    M --> N[Status: Pending approval]
    N --> O([Confirmation: capture another or return])
```
