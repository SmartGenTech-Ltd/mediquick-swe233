## 2.Written Description of the 3 Most Important Use Cases — MediQuick

## Use Case 1: Place Order
- **Actor**: Customer
- **Main Flow**:
  1. Customer searches the catalog by medicine name or category.
  2. Customer selects one or more medicines and chooses a quantity for each (not exceeding available stock and not expired).
  3. If the order contains a prescription-only medicine, the customer provides the doctor's name and the prescription number.
  4. The system reserves the stock for the ordered items.
  5. If the order has no prescription-only medicine, it is approved automatically; otherwise it waits for a pharmacist's approval before payment.
  6. The system sends a status message on screen to the customer.
- **Alternative Flows**:
  - **Medicine expired or insufficient stock**: The system blocks adding the medicine to the order.
  - **Stock falls to reorder level**: The pharmacist is warned.

## Use Case 2: Approve or Reject Prescription Order
- **Actor**: Pharmacist
- **Main Flow**:
  1. Pharmacist checks the pending prescription order (doctor's name and prescription number).
  2. Pharmacist approves the order so it can proceed to payment.
  3. The system updates the status and displays a status message on screen to the customer.
- **Alternative Flow**:
  - **Pharmacist rejects the order**: The system marks the order as rejected, releases the reserved stock, and displays a status message on screen to the customer.

## Use Case 3: Cancel Order
- **Actor**: Customer
- **Main Flow**:
  1. Customer requests to cancel the order before it is dispatched.
  2. The system cancels the order, releases the reserved stock, and displays a status message on screen to the customer.
- **Alternative Flow**:
  - **Order already dispatched**: Cancellation is refused because an order can never be cancelled after it has been dispatched.