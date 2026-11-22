## 4: Interaction, State & Activity Diagrams — MediQuick

## 1. Interaction Diagrams
- **Sequence Diagram (Place Order & Approval)**:
  - `Customer` -> `PharmacySystem`: `searchMedicines(...)` / `placeOrder(...)`
  - `PharmacySystem` -> `Medicine`: check expiry (`isExpired()`), check stock, `reserveStock(qty)`
  - `PharmacySystem` -> `Order`: create order; if `hasPrescriptionMedicine()` is false -> `approve()`, else wait for `Pharmacist` -> `approveOrder(order)` or `rejectOrder(order)`
  - `Order` -> `Customer`: `onOrderStatusChanged(order, newStatus)` (screen text message)
- **Communication Diagram (Record Mobile Money Payment)**:
  - `Cashier` -> `PharmacySystem`: `recordPayment(order, mobileMoneyPayment)`
  - `MobileMoneyPayment` -> `MobileMoneyProvider`: confirm payment (1% fee on amount to be paid)
  - `Order` -> `Customer`: `onOrderStatusChanged(order, PAID)`

## 2. State Diagram (Order Lifecycle)
- States: `PendingApproval`, `Approved`, `Paid`, `Dispatched`, `Delivered`, `Rejected`, `Cancelled`.
- Key transitions:
  - Order placed with prescription -> `PendingApproval` -> `Approved` (by `Pharmacist`) or `Rejected` (releases reserved stock).
  - Order placed without prescription -> `Approved` automatically.
  - `Approved` -> `Paid` (by `Cashier`).
  - `Paid` -> `Dispatched` -> `Delivered` (by `DeliveryAgent`).
  - Any state before `Dispatched` -> `Cancelled` (releases reserved stock). Never `Cancelled` after `Dispatched`.
  - Every status change notifies `Customer` on screen.

## 3. Activity Diagram (Fulfilling an Order: Payment to Delivery)
- Start -> Payment recorded by `Cashier` (cash on delivery 0%, mobile money 1% via simulated provider, or bank card 2.5%).
- Decision: Is payment valid / confirmed?
  - If No -> Payment failed / order remains awaiting payment.
  - If Yes -> Order marked `Paid` -> `DeliveryAgent` dispatches order (`Dispatched`) -> `DeliveryAgent` delivers order (`Delivered`, counts toward customer's 5 received orders for future 5% medicine discount) -> End.