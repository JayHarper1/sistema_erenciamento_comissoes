class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

class Seller:
    def __init__(self, name, unique_id, contact_info):
        self.name = name
        self.unique_id = unique_id
        self.contact_info = contact_info

class Sale:
    def __init__(self, customer, seller, contract, date, amount, payment_status):
        self.customer = customer
        self.seller = seller
        self.contract = contract
        self.date = date
        self.amount = amount
        self.payment_status = payment_status

    def calculate_commission(self):
        if self.seller.unique_id.startswith('1'):
            return 0.04 * self.amount
        elif self.seller.unique_id.startswith('2'):
            return 0.07 * self.amount
        else:
            return 0

class Contract:
    def __init__(self, terms_and_conditions):
        self.terms_and_conditions = terms_and_conditions

class CommissionManagementSystem:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.sales = []
        self.contracts = []

    def show_customer(self):
        x = 0
        for customer in self.customers:
            print("Customer Name: ", customer.name, "Number", x)
            x += 1

    def show_vender(self):
        x = 0
        for seller in self.sellers:
            print("Vendor Name: ", seller.name, "Number", x)
            x += 1 

    def show_contract(self):
        x = 0
        for contract in self.contracts:
            print("Contract Details: ", contract.terms_and_conditions, "Number", x)
            x += 1

    def register_customer(self, name, address, contact_info):
        customer = Customer(name, address, contact_info)
        self.customers.append(customer)

    def register_seller(self, name, unique_id, contact_info):
        seller = Seller(name, unique_id, contact_info)
        self.sellers.append(seller)

    def register_sale(self, customer, seller, contract, date, amount, payment_status):
        sale = Sale(customer, seller, contract, date, amount, payment_status)
        self.sales.append(sale)

    def register_contract(self, terms_and_conditions):
        contract = Contract(terms_and_conditions)
        self.contracts.append(contract)

    def generate_sales_report(self):
        for sale in self.sales:
            print(f"Date: {sale.date}, Customer: {sale.customer.name}, Seller: {sale.seller.name}, Amount: ${sale.amount}, Payment Status: {sale.payment_status}")

    def generate_commission_report(self):
        for sale in self.sales:
            commission = sale.calculate_commission()
            print(f"Date: {sale.date}, Seller: {sale.seller.name}, Commission: ${commission:.2f}")

if True:
    cms = CommissionManagementSystem()

    while True:
        print("\nCommission Management System Menu:")
        print("1. Register Customer")
        print("2. Register Seller")
        print("3. Register Contract")
        print("4. Register Sale")
        print("5. Generate Sales Report")
        print("6. Generate Commission Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            contact_info = input("Enter customer contact info: ")
            cms.register_customer(name, address, contact_info)

        elif choice == "2":
            name = input("Enter seller name: ")
            unique_id = input("Enter seller unique ID: ")
            contact_info = input("Enter seller contact info: ")
            cms.register_seller(name, unique_id, contact_info)

        elif choice == "3":
            terms_and_conditions = input("Enter contract terms and conditions: ")
            cms.register_contract(terms_and_conditions)

        elif choice == "4":
            cms.show_customer()
            customer_idx = int(input("Enter customer: "))
            cms.show_vender()
            seller_idx = int(input("Enter seller: "))
            cms.show_contract()
            contract_idx = int(input("Enter contract: "))
            date = input("Enter sale date: ")
            amount = float(input("Enter sale amount: "))
            payment_status = input("Enter payment status: ")
            cms.register_sale(cms.customers[customer_idx], cms.sellers[seller_idx], cms.contracts[contract_idx], date, amount, payment_status)
            
        elif choice == "5":
            cms.generate_sales_report()

        elif choice == "6":
            cms.generate_commission_report()

        elif choice == "7":
            print("Exiting Commission Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

