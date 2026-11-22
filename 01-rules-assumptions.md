## 1. Rules Extracted Strictly from the Scenario

### Customers & Registration
- Customers register with their **name**, **phone number**, **email**, and **address**.
- A phone number can belong to **only one customer**.

### Catalog & Medicines
- The catalog is managed by the **pharmacist**.
- A customer can search the catalog by **medicine name** or **category**.
- Every medicine has:
  - **code**
  - **name**
  - **category**
  - **unit price in XAF**
  - **quantity in stock**
  - **reorder level**
  - **expiry date**
  - **dispensing type**: sold freely OR only with a doctor's prescription
- **Expired medicines cannot be sold.**

### Ordering & Stock Rules
- A customer can place an order for **one or more medicines**, choosing a **quantity** for each.
- An order **cannot ask for more than the stock available**.
- When an order is placed, the **stock is reserved**.
- The reserved stock is **released again** if the order is **cancelled** or **rejected**.
- An order can be **cancelled at any point until it has been dispatched**, but **never after**.

### Prescriptions & Order Approval
- If an order contains a **prescription-only medicine**, the customer must give the **doctor's name** and the **prescription number**.
- For orders with a prescription-only medicine, a **pharmacist must approve or reject** the order before it can be paid.
- **All other orders are approved automatically.**

### Payments, Fees & Discounts
- After approval, the order is **paid**.
- **Only a cashier records payments.**
- Accepted payment methods and fees on the amount to be paid:
  - **Cash on delivery**: **0%** fee (no fee)
  - **Mobile money**: **1%** fee (confirmed by an outside mobile money provider, whose service may be simulated)
  - **Bank cards**: **2.5%** fee
- **Delivery fee**: **1,000 XAF**, and **free** when the medicines cost **20,000 XAF or more**.
- **Loyalty discount**: A customer who has already received **five orders** gets **5% off the medicines** in the next one.

### Delivery, Notifications & Management Reports
- Paid orders are **dispatched and delivered by a delivery agent**.
- At **every change in the status of an order**, the customer is sent a message (**simulated by text on the screen**).
- When the **stock of a medicine falls to its reorder level**, the **pharmacist is warned**.
- The **pharmacy manager** wants:
  - a **daily summary of sales**
  - a **list of the medicines that are running low**

### Staff Roles
- The **pharmacist**, the **cashier**, and the **delivery agent** are all **members of staff**.
- Each staff member has a **staff number**, a **name**, and a **phone number**.
- Each staff role is allowed to do **different things** in the system.

---

## 2. Assumptions (Decisions Left Open by the Scenario)
*(The scenario states: "decide for yourselves what the system must do and how it should be organised... State clearly any assumptions you make.")*

- **Counting "five orders already received":** Only orders that have reached the `Delivered` status count toward the five received orders required for the 5% medicine discount.
- **Order of discount and fee calculation:** The 5% loyalty discount applies to the medicines cost; the delivery fee (0 XAF if medicines cost is 20,000 XAF or more, otherwise 1,000 XAF) is added to get the amount to be paid, and the payment method fee (0%, 1%, or 2.5%) is calculated on that amount to be paid.
- **User access in the text-menu interface:** Users select their role and identify themselves (by customer phone number or staff number) in the console menu so the system enforces role-specific permissions.
- **External mobile money provider simulation:** The outside mobile money provider is simulated by a service class that returns a confirmation or failure response during payment recording.