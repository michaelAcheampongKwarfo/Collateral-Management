# Collateral Management: Oracle Forms → Angular

Design and documentation for moving the Collateral Management screens from Oracle Forms to Angular. Work goes module by module.

| Module | Status |
|---|---|
| Creation | Spec, UI prototype and flowchart from the PL/SQL ready ([flowchart](docs/creation/flowchart.md)). |
| Amendment | Spec, UI prototype and draft flow ready. Open questions listed in the spec. |
| Cancellation | Spec, UI prototype and draft flow ready. Uses the Amendment list with a read-only form and closure reason. |

## Contents

```
screenshots/creation/          Current Oracle Forms screens (reference)
screenshots/amendment/
screenshots/cancellation/
design/prototype/index.html    Interactive UI prototype for all modules (open in any browser)
design/creation/screens/       Prototype screenshots for slides
design/amendment/screens/
design/cancellation/screens/
docs/creation/                 Functional spec and process flow per module
docs/amendment/
docs/cancellation/
docs/design-system.md          Colours, layout grid, action bar and components shared by all modules
```

## Before and after

| Oracle Forms | Angular design |
|---|---|
| ![Current creation screen](screenshots/creation/cash.PNG) | ![New creation screen](design/creation/screens/01-cash.png) |
| ![Current amendment list](screenshots/amendment/amendment%20grid.PNG) | ![New amendment list](design/amendment/screens/01-search-list.png) |
| ![Current amendment details](screenshots/amendment/amendment%20property-entry.PNG) | ![New amendment details](design/amendment/screens/09-edited.png) |
| ![Current cancellation screen](screenshots/cancellation/cancellation.PNG) | ![New cancellation details](design/cancellation/screens/07-reason.png) |

**Creation screens:** [insurance](design/creation/screens/02-insurance.png) · [property](design/creation/screens/03-property.png) · [guarantee](design/creation/screens/04-guarantee.png) · [shares](design/creation/screens/05-shares.png) · [validation](design/creation/screens/06-validation.png) · [lookup](design/creation/screens/07-lookup.png) · [submitted](design/creation/screens/08-submitted.png) · [blank](design/creation/screens/00-blank.png) · [mobile, dark](design/creation/screens/09-mobile-dark.png)

**Amendment screens:** [filtered and sorted](design/amendment/screens/02-filtered-sorted.png) · [search by customer](design/amendment/screens/03-search-customer.png) · [cash](design/amendment/screens/04-cash.png) · [insurance](design/amendment/screens/05-insurance.png) · [property](design/amendment/screens/06-property.png) · [guarantee](design/amendment/screens/07-guarantee.png) · [shares](design/amendment/screens/08-shares.png) · [validation](design/amendment/screens/10-validation.png) · [submitted](design/amendment/screens/11-submitted.png) · [pending in list](design/amendment/screens/12-list-pending.png) · [mobile, dark](design/amendment/screens/13-mobile-dark.png) · [desktop, dark](design/amendment/screens/14-desktop-dark.png)

**Cancellation screens:** [search list](design/cancellation/screens/01-search-list.png) · [cash](design/cancellation/screens/02-cash.png) · [insurance](design/cancellation/screens/03-insurance.png) · [property](design/cancellation/screens/04-property.png) · [guarantee](design/cancellation/screens/05-guarantee.png) · [shares](design/cancellation/screens/06-shares.png) · [confirm](design/cancellation/screens/08-confirm.png) · [submitted](design/cancellation/screens/09-submitted.png) · [pending in list](design/cancellation/screens/10-list-pending.png) · [mobile, dark](design/cancellation/screens/11-mobile-dark.png)

## Using the prototype

Open `design/prototype/index.html` in a browser and switch modules from the sidebar (`#amendment` or `#cancellation` in the address opens that module directly).

**Creation** starts with sample customer `056719` and a cash collateral. Try other customer numbers (`048213`, `061104`, `072530`) or the search button, each collateral type tile, **Submit** with empty fields, then a complete submit.

**Amendment** lists 14 approved collaterals. Try searching for customer `004997`, the type chips, sorting a column, then **›** on a row. Change a few fields to see change tracking and **Undo**, then **Submit**.

**Cancellation** uses the same list. Open a record to see its read-only form, pick or type a closure reason, then **Submit** and confirm. The record is then locked in both Amendment and Cancellation.

All names, accounts and amounts are sample data.
