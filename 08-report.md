# MediQuick — Short Report
**Group members**: Yve Walter Nde Takougang, Cheigang Tyra-Sandy Wadjeh, Same Alucious, Fombe Christabel

## 1. Assumptions
- Only `DELIVERED` orders count toward the 5 received orders for the 5% medicine discount.
- The 5% loyalty discount applies to medicines cost, delivery fee (1,000 XAF, or 0 XAF if medicines >= 20,000 XAF) is added, and payment fee (0% cash, 1% mobile money, 2.5% card) applies to the amount to pay.
- Mobile money confirmation is simulated in the code, and users choose actions from the text menu.

## 2. How Diagrams Match the Code
- **Use case diagram**: Maps to methods on `PharmacySystem`, `Customer`, and `Order` (search, place order, approve/reject, pay, dispatch/deliver, cancel, daily report).
- **Class diagram**: Matches `Medicine`, `Customer`, `Order`, `Staff`, and `PharmacySystem` attributes and methods (`reserve`, `release`, `is_expired`, `is_low_stock`, `approve`, `reject`, `pay`, `dispatch`, `deliver`, `cancel`).
- **Interaction, state & activity diagrams**: Match order status transitions (`PENDING_APPROVAL`, `APPROVED`, `PAID`, `DISPATCHED`, `DELIVERED`, `REJECTED`, `CANCELLED`), screen status messages (`Customer.notify`), and payment/delivery flow.

## 3. Deliverables & Test Summary
- **Files included**: `01-rules-assumptions.md`, `02-use-cases.md`, `03-class-diagramm.md`, `04-interaction-state-activity.md`, `07-tests.md`, `08-report.md`, `mediquick.py`, `use-case-diagram.png`, `class-diagram.png`, `sequence-diagram.png`, `state-diagram.png`, `activity-diagram.png`.
- **Execution check**: Verified end-to-end flow in `mediquick.py` (search, order placement, approval, `mobile_money` payment totaling `5050 XAF`, dispatch, delivery, and daily report showing `1 paid orders, Total = 5050 XAF`).