from datetime import date


class Medicine:
    def __init__(self, code, name, category, price, stock, reorder_level, expiry_date, needs_prescription):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.reorder_level = reorder_level
        self.expiry_date = expiry_date
        self.needs_prescription = needs_prescription

    def is_expired(self):
        return date.today() > self.expiry_date

    def is_low_stock(self):
        return self.stock <= self.reorder_level

    def reserve(self, qty):
        if self.is_expired():
            return False, "Expired medicine cannot be sold."
        if qty <= 0 or qty > self.stock:
            return False, "Invalid or insufficient stock."
        self.stock -= qty
        return True, "Stock reserved."

    def release(self, qty):
        self.stock += qty


class Customer:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.delivered_count = 0

    def notify(self, message):
        print(f"[Message to {self.name}]: {message}")


class Order:
    def __init__(self, order_id, customer, items, doctor_name="", prescription_no=""):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of (Medicine, qty)
        self.doctor_name = doctor_name
        self.prescription_no = prescription_no
        self.date = date.today()
        self.paid_amount = 0.0

        if self.has_prescription():
            self.set_status("PENDING_APPROVAL")
        else:
            self.set_status("APPROVED")

    def set_status(self, new_status):
        self.status = new_status
        self.customer.notify(f"Order {self.order_id} is now {self.status}.")

    def has_prescription(self):
        return any(med.needs_prescription for med, _ in self.items)

    def medicines_cost(self):
        total = sum(med.price * qty for med, qty in self.items)
        if self.customer.delivered_count >= 5:
            total = total * 0.95  # 5% off after 5 received orders
        return total

    def total_before_payment_fee(self):
        meds = self.medicines_cost()
        delivery_fee = 0.0 if meds >= 20000 else 1000.0
        return meds + delivery_fee

    def approve(self):
        self.set_status("APPROVED")

    def reject(self):
        for med, qty in self.items:
            med.release(qty)
        self.set_status("REJECTED")

    def pay(self, method):
        if self.status != "APPROVED":
            return False, "Order must be approved first."
        amount = self.total_before_payment_fee()
        if method == "cash":
            fee_rate = 0.0
        elif method == "mobile_money":
            fee_rate = 0.01
            print("[Mobile Money Provider]: Payment confirmed.")
        elif method == "card":
            fee_rate = 0.025
        else:
            return False, "Unknown payment method."

        self.paid_amount = amount * (1 + fee_rate)
        self.set_status("PAID")
        return True, f"Paid {self.paid_amount:.0f} XAF."

    def dispatch(self):
        if self.status == "PAID":
            self.set_status("DISPATCHED")
            return True
        return False

    def deliver(self):
        if self.status == "DISPATCHED":
            self.set_status("DELIVERED")
            self.customer.delivered_count += 1
            return True
        return False

    def cancel(self):
        if self.status in ("DISPATCHED", "DELIVERED"):
            return False, "Cannot cancel after dispatch."
        for med, qty in self.items:
            med.release(qty)
        self.set_status("CANCELLED")
        return True, "Order cancelled and stock released."


class Staff:
    def __init__(self, staff_no, name, phone, role):
        self.staff_no = staff_no
        self.name = name
        self.phone = phone
        self.role = role


class PharmacySystem:
    def __init__(self):
        self.customers = {}   # phone -> Customer
        self.medicines = {}   # code -> Medicine
        self.orders = []
        self.next_id = 1

    def register_customer(self, name, phone, email, address):
        if phone in self.customers:
            return False, "Phone number already used."
        self.customers[phone] = Customer(name, phone, email, address)
        return True, "Customer registered."

    def search_medicine(self, query):
        q = query.lower()
        return [m for m in self.medicines.values() if q in m.name.lower() or q in m.category.lower()]

    def place_order(self, phone, chosen_items, doctor_name="", prescription_no=""):
        if phone not in self.customers:
            return None, "Customer not found."
        customer = self.customers[phone]
        reserved = []

        for code, qty in chosen_items:
            med = self.medicines.get(code)
            if not med:
                for m, q in reserved:
                    m.release(q)
                return None, f"Medicine {code} not found."
            if med.needs_prescription and (not doctor_name or not prescription_no):
                for m, q in reserved:
                    m.release(q)
                return None, "Doctor name and prescription number required."
            ok, msg = med.reserve(qty)
            if not ok:
                for m, q in reserved:
                    m.release(q)
                return None, msg
            reserved.append((med, qty))

        order = Order(f"ORD{self.next_id}", customer, reserved, doctor_name, prescription_no)
        self.next_id += 1
        self.orders.append(order)

        for med, _ in reserved:
            if med.is_low_stock():
                print(f"[Pharmacist Alert]: {med.name} stock is low ({med.stock}).")

        return order, "Order created."

    def daily_sales_summary(self, target_date):
        paid_orders = [o for o in self.orders if o.date == target_date and o.paid_amount > 0]
        total = sum(o.paid_amount for o in paid_orders)
        return f"Date {target_date}: {len(paid_orders)} paid orders, Total = {total:.0f} XAF"

    def low_stock_list(self):
        return [m for m in self.medicines.values() if m.is_low_stock()]


def demo():
    app = PharmacySystem()
    app.register_customer("Ali", "670000001", "ali@mail.com", "Simbock")
    app.medicines["M1"] = Medicine("M1", "Paracetamol", "Pain", 2000, 10, 3, date(2028, 1, 1), False)
    app.medicines["M2"] = Medicine("M2", "Amoxicillin", "Antibiotic", 5000, 8, 2, date(2028, 1, 1), True)

    while True:
        print("\n1.Search  2.Order  3.Approve  4.Pay  5.Dispatch  6.Deliver  7.Cancel  8.Report  0.Exit")
        c = input("Choice: ").strip()
        if c == "0":
            break
        elif c == "1":
            for m in app.search_medicine(input("Name/Category: ")):
                print(m.code, m.name, m.price, "Stock:", m.stock)
        elif c == "2":
            phone = input("Phone: ")
            code = input("Medicine code: ")
            qty = int(input("Qty: "))
            doc = input("Doctor (if prescription): ")
            rx = input("Prescription no: ")
            order, msg = app.place_order(phone, [(code, qty)], doc, rx)
            print(msg, order.order_id if order else "")
        elif c == "3":
            oid = input("Order ID: ")
            for o in app.orders:
                if o.order_id == oid:
                    o.approve() if input("A=Approve / R=Reject: ").upper() == "A" else o.reject()
        elif c == "4":
            oid = input("Order ID: ")
            method = input("cash / mobile_money / card: ")
            for o in app.orders:
                if o.order_id == oid:
                    _, msg = o.pay(method)
                    print(msg)
        elif c == "5":
            oid = input("Order ID: ")
            for o in app.orders:
                if o.order_id == oid:
                    print("Dispatched" if o.dispatch() else "Cannot dispatch")
        elif c == "6":
            oid = input("Order ID: ")
            for o in app.orders:
                if o.order_id == oid:
                    print("Delivered" if o.deliver() else "Cannot deliver")
        elif c == "7":
            oid = input("Order ID: ")
            for o in app.orders:
                if o.order_id == oid:
                    _, msg = o.cancel()
                    print(msg)
        elif c == "8":
            print(app.daily_sales_summary(date.today()))
            for m in app.low_stock_list():
                print("Low stock:", m.name, m.stock)


if __name__ == "__main__":
    demo()