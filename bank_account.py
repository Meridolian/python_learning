class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        return self.balance
