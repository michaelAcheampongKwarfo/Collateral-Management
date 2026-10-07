# Collateral Amendment: Process Flow (draft)

> **Status: draft.** Based on the screenshots only. It will be rewritten once the PL/SQL behind the Oracle Forms screens is reviewed. Nodes marked *(to confirm)* match the open questions in [`collateral-amendment.md` §6.2](collateral-amendment.md#62-to-confirm-against-the-plsql).

```mermaid
flowchart TD
    A([Open Collateral Amendment]) --> B[List approved collaterals]
    B --> C[Optional: enter customer number and/or collateral number, Fetch]
    C --> D{Records found?}
    D -- No --> D1[Show 'No collaterals match'] --> C
    D -- Yes --> E[Filter by type / sort / page]
    E --> F[Select › on a record]
    F --> G{"Amendment already pending?<br/>(to confirm)"}
    G -- Yes --> G1[Record locked until approved or rejected] --> E
    G -- No --> H[Open details page for the collateral type<br/>pre-filled with current values]
    H --> I[Edit fields<br/>each change highlighted with original value]
    I --> J{Any field changed?}
    J -- No --> J1[Submit stays disabled] --> I
    J -- Yes --> K[Submit]
    K --> L{Required fields and formats valid?}
    L -- No --> L1[Show field errors and summary] --> I
    L -- Yes --> M{"Business rules pass?<br/>(to confirm)"}
    M -- No --> M1[Show rule message] --> I
    M -- Yes --> N[Save amendment: changed fields, old and new values]
    N --> O[Collateral status: Amendment pending<br/>current values stay in force]
    O --> P([Confirmation with before / after table])
    P --> B
    H -. Exit with unsaved changes .-> X[Confirm discard] --> B
```
