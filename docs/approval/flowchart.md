# Collateral Approval: Process Flow (draft)

> **Status: draft.** Based on the approval screenshots and the agreed design. It will be rewritten once the approval PL/SQL is reviewed. Nodes marked *(to confirm)* match [`collateral-approval.md` §5](collateral-approval.md#5-to-confirm-against-the-plsql).

```mermaid
flowchart TD
    S1[Creation submitted] --> Q
    S2[Amendment submitted] --> Q
    S3[Cancellation submitted] --> Q
    Q[(Approval queue)] --> A([Approver opens Approvals])
    A --> F[Filter by request type / search]
    F --> O[Select › on a request]
    O --> V[Read-only entry screen<br/>amendments: changed fields highlighted<br/>cancellations: closure reason]
    V --> D[View documents]
    D --> T{Ticked 'I have checked<br/>all the details'?}
    T -- No --> T1[Reject and Authorize disabled] --> V
    T -- Yes --> C{Decision}
    C -- Authorize --> MC{"Approver is not the submitter?<br/>(maker-checker, to confirm)"}
    MC -- No --> MC1[Block: another officer must authorize] --> F
    MC -- Yes --> AU{Request type}
    AU -- Creation --> R1[Collateral becomes Approved]
    AU -- Amendment --> R2[New values replace the old]
    AU -- Cancellation --> R3[Collateral closed]
    C -- Reject --> RJ[/Enter rejection reason/]
    RJ --> RJ2{Reason entered?}
    RJ2 -- No --> RJ
    RJ2 -- Yes --> R4[Creation: not created<br/>Amendment / cancellation: record released unchanged]
    R1 & R2 & R3 & R4 --> N["Submitter notified<br/>(to confirm)"] --> E([Back to the queue])

    classDef term fill:#0F2342,stroke:#0F2342,color:#FFFFFF
    classDef ok fill:#E4F3EB,stroke:#1D7A4C,color:#13223A
    classDef bad fill:#FFF4E0,stroke:#9A5A00,color:#13223A
    class A,E term
    class R1,R2,R3 ok
    class RJ,R4,MC1 bad
```
