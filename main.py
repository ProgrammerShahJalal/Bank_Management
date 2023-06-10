class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.loan_amount = 0
        self.transactions = []

    
