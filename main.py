class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.loan_amount = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        admin.total_bank_balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            admin.total_bank_balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient balance.")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transfer: -{amount} to {recipient.account_number} and recipient name: {recipient.name}")
            recipient.transactions.append(f"Transfer: +{amount} from {self.account_number} and Sender name: {self.name}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transactions


class Admin:
    def __init__(self):
        self.users = []
        self.total_bank_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, account_number, balance=0):
        new_user = User(name, account_number, balance)
        self.users.append(new_user)
        self.total_bank_balance += balance

    def check_total_bank_balance(self):
        return self.total_bank_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

    def perform_loan(self, user):
        if self.loan_feature_enabled:
            loan_amount = user.balance*2
            user.balance += loan_amount
            user.loan_amount += loan_amount
            self.total_bank_balance += loan_amount
            self.total_loan_amount += loan_amount
            user.transactions.append(f"Loan: +{loan_amount}")
            return loan_amount
        else:
            return 0


admin = Admin()
admin.create_account("Shah Jalal", "IIBL-35346", 1200)
admin.create_account("Farabi", "IIBL-67890", 500)
admin.create_account("Shaimum", "IIBL-23469", 1500)
admin.create_account("Mamun", "IIBL-64381", 22000)

user1, user2, user3, user4 = admin.users

print('=============> Before transactions <===================')
print()

print(f"The balance of {user1.name}: {user1.check_balance()}") 
print(f"The balance of {user2.name}: {user2.check_balance()}")
print(f"The balance of {user3.name}: {user3.check_balance()}")
print(f"The balance of {user4.name}: {user4.check_balance()}")
print("The total available balance of the bank:", admin.check_total_bank_balance())

print()
user1.deposit(1000)
user1.withdraw(100)
user1.transfer(200, user2)
user2.deposit(400)
user3.withdraw(500)
user4.transfer(18000, user1)

print()

print(f"The transaction history of {user1.name}: {user1.check_transaction_history()}")
print(f"The transaction history of {user2.name}: {user2.check_transaction_history()}")
print(f"The transaction history of {user3.name}: {user3.check_transaction_history()}")
print(f"The transaction history of {user4.name}: {user4.check_transaction_history()}")

print()

print('==============> After transactions <=================')
print()
print(f"The balance of {user1.name}: {user1.check_balance()}") 
print(f"The balance of {user2.name}: {user2.check_balance()}")
print(f"The balance of {user3.name}: {user3.check_balance()}")
print(f"The balance of {user4.name}: {user4.check_balance()}")
print("The total available balance of the bank:", admin.check_total_bank_balance())

print()

admin.enable_loan_feature()
loan_amount = admin.perform_loan(user4)
print('============> After loan performance <================')
print()
print(f"The loan amount of {user4.name}: {loan_amount}")
print(f"{user1.name} balance: {user1.check_balance()}")
print(f"{user2.name} balance: {user2.check_balance()}")
print(f"{user3.name} balance: {user3.check_balance()}")
print(f"{user4.name} balance: {user4.check_balance()}")
print("The Total loan amount:", admin.check_total_loan_amount())
print("The total available balance of the bank:", admin.check_total_bank_balance())
