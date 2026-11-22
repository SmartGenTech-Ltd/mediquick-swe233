## 3: Class Diagram Specification — MediQuick

## 1. Classes, Attributes & Operations

### Abstract Class: `Staff`
- **Attributes**:
  - `- staffNumber: String`
  - `- name: String`
  - `- phoneNumber: String`
- **Operations**:
  - `+ getStaffNumber(): String`
  - `+ getName(): String`
  - `+ getPhoneNumber(): String`
  - `+ getRole(): String` *(abstract)*

### Subclasses of `Staff` (Inheritance)
- **`Pharmacist`** extends `Staff`
  - `+ addOrUpdateMedicine(catalog: PharmacySystem, medicine: Medicine): void`
  - `+ approveOrder(order: Order): void`
  - `+ rejectOrder(order: Order): void`
  - `+ onLowStockAlert(medicine: Medicine): void`
- **`Cashier`** extends `Staff`
  - `+ recordPayment(order: Order, payment: Payment): boolean`
- **`DeliveryAgent`** extends `Staff`
  - `+ dispatchOrder(order: Order): void`
  - `+ deliverOrder(order: Order): void`
- **`PharmacyManager`** extends `Staff`
  - `+ viewDailySalesSummary(system: PharmacySystem, date: LocalDate): String`
  - `+ viewLowStockMedicines(system: PharmacySystem): List<Medicine>`

### Class: `Customer` (implements `OrderObserver`)
- **Attributes**:
  - `- name: String`
  - `- phoneNumber: String` *(unique)*
  - `- email: String`
  - `- address: String`
  - `- deliveredOrdersCount: int`
- **Operations**:
  - `+ isEligibleForLoyaltyDiscount(): boolean`
  - `+ incrementDeliveredOrders(): void`
  - `+ onOrderStatusChanged(order: Order, newStatus: OrderStatus): void`

### Class: `Medicine`
- **Attributes**:
  - `- code: String`
  - `- name: String`
  - `- category: String`
  - `- unitPrice: double`
  - `- quantityInStock: int`
  - `- reorderLevel: int`
  - `- expiryDate: LocalDate`
  - `- requiresPrescription: boolean`
- **Operations**:
  - `+ isExpired(): boolean`
  - `+ isLowStock(): boolean`
  - `+ reserveStock(qty: int): void`
  - `+ releaseStock(qty: int): void`

### Class: `Order`
- **Attributes**:
  - `- orderId: String`
  - `- orderDate: LocalDate`
  - `- status: OrderStatus`
  - `- doctorName: String`
  - `- prescriptionNumber: String`
  - `- items: List<OrderItem>`
- **Operations**:
  - `+ addItem(medicine: Medicine, quantity: int): void`
  - `+ hasPrescriptionMedicine(): boolean`
  - `+ calculateMedicinesTotal(): double`
  - `+ calculateDiscount(): double`
  - `+ calculateDeliveryFee(): double`
  - `+ calculateAmountBeforePaymentFee(): double`
  - `+ approve(): void`
  - `+ reject(): void`
  - `+ markPaid(): void`
  - `+ dispatch(): void`
  - `+ deliver(): void`
  - `+ cancel(): void`

### Class: `OrderItem`
- **Attributes**:
  - `- medicine: Medicine`
  - `- quantity: int`
  - `- unitPriceAtOrder: double`
- **Operations**:
  - `+ getSubtotal(): double`

### Interface & Implementations: `Payment` (Polymorphism)
- **Interface `Payment`**:
  - `+ getMethodName(): String`
  - `+ calculateFee(baseAmount: double): double`
  - `+ calculateTotalPaid(baseAmount: double): double`
  - `+ processPayment(baseAmount: double): boolean`
- **Implementations**:
  - `CashOnDeliveryPayment` (0% fee)
  - `MobileMoneyPayment` (1% fee, uses `MobileMoneyProvider`)
  - `BankCardPayment` (2.5% fee)

### Interface: `OrderObserver` & Class: `PharmacySystem` (Singleton)
- **Interface `OrderObserver`**:
  - `+ onOrderStatusChanged(order: Order, newStatus: OrderStatus): void`
- **Class `PharmacySystem` (Singleton)**:
  - `- instance: PharmacySystem`
  - `- customers: Map<String, Customer>`
  - `- medicines: Map<String, Medicine>`
  - `- orders: List<Order>`
  - `+ getInstance(): PharmacySystem`
  - `+ registerCustomer(customer: Customer): void`
  - `+ searchMedicines(keyword: String): List<Medicine>`
  - `+ placeOrder(order: Order): void`

## 2. Relationships & Multiplicities
- `Pharmacist`, `Cashier`, `DeliveryAgent`, `PharmacyManager` **inherit from** (`--|>`) `Staff` (abstract class).
- `CashOnDeliveryPayment`, `MobileMoneyPayment`, `BankCardPayment` **implement** (`..|>`) `Payment` (interface).
- `Customer` **implements** (`..|>`) `OrderObserver` (interface).
- `Customer` `1` —— `0..*` `Order` (places).
- `Order` `1` *—— `1..*` `OrderItem` (**Composition**: an order owns its order items).
- `OrderItem` `0..*` ——> `1` `Medicine` (references).
- `Order` `1` o—— `0..1` `Payment` (**Aggregation**: payment attached once paid).
- `PharmacySystem` `1` o—— `0..*` `Medicine` (**Aggregation**).