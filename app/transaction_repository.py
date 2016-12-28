from app.transaction import Transaction


class TransactionRepository:
    def __init__(self, clock):
        self.clock = clock
        self.transactions = []

    def add_deposit(self, amount):
        deposit_transaction = Transaction(self.clock.today_as_string(), amount)
        self.transactions.append(deposit_transaction)

    def add_withdrawal(self, amount):
        raise NotImplementedError()

    def all_transactions(self):
        return tuple(self.transactions)
