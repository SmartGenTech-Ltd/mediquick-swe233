# MediQuick — Test Cases

| ID | Rule Tested | Expected Result | Observed Result |
| --- | --- | --- | --- |
| TC-01 | Unique phone number | Duplicate phone rejected | |
| TC-02 | Expired medicine | Expired medicine blocked | |
| TC-03 | Stock limit & reservation | Exceeding stock blocked; valid order reserves stock | |
| TC-04 | Stock release on cancel/reject | Reserved stock returned; status message shown | |
| TC-05 | Prescription & approval | Doctor & Rx required; waits approval if Rx medicine | |
| TC-06 | Auto-approval | Non-prescription order is approved automatically | |
| TC-07 | Delivery fee | 1,000 XAF; free if medicines >= 20,000 XAF | |
| TC-08 | 5% loyalty discount | 5% off medicines after 5 delivered orders | |
| TC-09 | Payment fees | Cash 0%, mobile money 1%, card 2.5% | |
| TC-10 | No cancel after dispatch | Cancellation refused once dispatched | |
| TC-11 | Messages & low-stock alert | Status message shown; low-stock alert triggered | |
| TC-12 | Manager report | Daily sales summary and low-stock list shown | |
## Observed Test Results (`mediquick.py`)

- **Search medicine (`paracetamol`)**: Displayed `M1 Paracetamol 2000 Stock: 10` and returned to main menu.
- **Create free-sale order (`ORD1`, customer `670000001`, item `M1`, qty `2`)**: Displayed `[Message to Ali]: Order ORD1 is now APPROVED.` and `Order created. ORD1`.
- **Pay order (`ORD1`, `mobile_money`)**: Displayed `[Message to Ali]: Order ORD1 is now PAID.` and `Paid 5050 XAF.`
- **Dispatch order (`ORD1`, agent `Moussa`)**: Displayed `[Message to Ali]: Order ORD1 is now DISPATCHED.` and `Dispatched`.
- **Deliver order (`ORD1`)**: Displayed `Delivered`.
- **Daily sales report (`8.Report`)**: Displayed `Date 2026-11-22: 1 paid orders, Total = 5050 XAF`.