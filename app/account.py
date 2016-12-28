class Account:
    def __init__(self, transaction_repository, statement_printer):
        self.transaction_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount):
        self.transaction_repository.add_deposit(amount)

    def withdraw(self, amount):
        self.transaction_repository.add_withdrawal(amount)

    def print_statement(self):
        transactions = self.transaction_repository.all_transactions()
        self.statement_printer.print(transactions)
