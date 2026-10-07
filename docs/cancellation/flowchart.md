# Collateral Cancellation: Process Flow (draft)

> **Status: draft.** Based on the screenshot and the agreed design only. It will be rewritten once the PL/SQL behind the Oracle Forms closing screen is reviewed. Nodes marked *(to confirm)* match the open questions in [`collateral-cancellation.md` §6.2](collateral-cancellation.md#62-to-confirm-against-the-plsql).

```mermaid
flowchart TD
    A([Open Collateral Cancellation]) --> B[List approved collaterals]
    B --> C[Optional: customer number and/or collateral number, Fetch]
    C --> E[Filter by type / sort / page]
    E --> F[Select › on a record]
    F --> G{Amendment or cancellation<br/>already pending?}
    G -- Yes --> G1[Record locked until approved or rejected] --> E
    G -- No --> H[Open details: customer, closure summary,<br/>read-only type form]
    H --> I[Enter closure reason<br/>quick-pick or free text]
    I --> J{Reason entered?}
    J -- No --> J1[Submit stays disabled] --> I
    J -- Yes --> K[Submit]
    K --> L{Confirm cancellation?}
    L -- Keep collateral --> I
    L -- Submit cancellation --> M{"Business rules pass?<br/>e.g. no active facility (to confirm)"}
    M -- No --> M1[Show rule message] --> I
    M -- Yes --> N[Save cancellation request with reason]
    N --> O[Status: Cancellation pending<br/>locked in Amendment and Cancellation]
    O --> P([Confirmation]) --> B
    O -. on approval .-> Q["Collateral closed<br/>cash: hold on account released (to confirm)"]
    H -. Exit with a typed reason .-> X[Confirm discard] --> B

    classDef term fill:#0F2342,stroke:#0F2342,color:#FFFFFF
    classDef warn fill:#FDEDEB,stroke:#B42318,color:#13223A
    class A,P term
    class L,Q warn
```
