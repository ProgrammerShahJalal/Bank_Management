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
            self.transactions.append(f"Transfer: -{amount} to {recipient.account_number}")
            recipient.transactions.append(f"Transfer: +{amount} from {self.account_number}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transactions



