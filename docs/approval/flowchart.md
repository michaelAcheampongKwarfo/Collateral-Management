# Collateral Approval: Process Flow (draft)

> **Status: draft.** Based on the approval screenshots and the agreed design. It will be rewritten once the approval PL/SQL is reviewed. Nodes marked *(to confirm)* match [`collateral-approval.md` §5](collateral-approval.md#5-to-confirm-against-the-plsql).

```mermaid
flowchart TD
    S1[Creation submitted] --> Q
    S2[Amendment submitted] --> Q
    S3[Cancellation submitted] --> Q
    Q[(Approval queue)] --> A([Approver opens Approvals])
    A --> O[Select › on a request]
    O --> V[Read-only entry screen<br/>amendments: changed fields highlighted<br/>cancellations: closure reason]
    V --> C{Decision}
    C -- Authorize --> VC{"Verification checklist<br/>every item ticked?"}
    VC -- No --> V
    VC -- Yes --> MC{"Approver is not the submitter?<br/>(maker-checker, to confirm)"}
    MC -- No --> MC1[Block: another officer must authorize] --> V
    MC -- Yes --> AU{Request type}
    AU -- Creation --> R1[Collateral becomes Approved]
    AU -- Amendment --> R2[New values replace the old]
    AU -- Cancellation --> R3[Collateral closed]
    C -- Return --> RT[/Return reason/]
    RT --> RQ[(Returned queue)]
    RQ --> RE[Submitter reopens it on its entry screen<br/>reason shown in a banner]
    RE --> RS[Correct and Submit<br/>same collateral number] --> Q
    C -- Dismiss --> DM[/Dismissal reason +<br/>Dismiss permanently tick/]
    DM --> R4[Request ends<br/>creation not created · amendment / cancellation: record unchanged]
    R1 & R2 & R3 & R4 --> N["Submitter notified<br/>(to confirm)"] --> E([Back to the queue])

    classDef term fill:#0F2342,stroke:#0F2342,color:#FFFFFF
    classDef ok fill:#E4F3EB,stroke:#1D7A4C,color:#13223A
    classDef ret fill:#FFF4E0,stroke:#9A5A00,color:#13223A
    classDef bad fill:#FCEBF1,stroke:#B4234F,color:#13223A
    class A,E term
    class R1,R2,R3 ok
    class RT,RQ,RE,RS ret
    class DM,R4,MC1 bad
```
