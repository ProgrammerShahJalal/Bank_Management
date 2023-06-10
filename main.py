class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.loan_amount = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
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
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, account_number, balance=0):
        new_user = User(name, account_number, balance)
        self.users.append(new_user)
        self.total_balance += balance

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

    def perform_loan(self, user):
        if self.loan_feature_enabled:
            loan_amount = user.balance * 2
            user.balance += loan_amount
            user.loan_amount += loan_amount
            self.total_balance += loan_amount
            self.total_loan_amount += loan_amount
            user.transactions.append(f"Loan: +{loan_amount}")
            return loan_amount
        else:
            return 0

