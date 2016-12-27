class Account:
    def __init__(self, transaction_repository):
        self.transaction_repository = transaction_repository

    def deposit(self, amount):
        self.transaction_repository.add_deposit(amount)

    def withdraw(self, amount):
        self.transaction_repository.add_withdrawal(amount)

    def print_statement(self):
        pass
