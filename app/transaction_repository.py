class TransactionRepository:
    def add_deposit(self, amount):
        raise NotImplementedError()

    def add_withdrawal(self, amount):
        raise NotImplementedError()

    def all_transactions(self):
        raise NotImplementedError()
