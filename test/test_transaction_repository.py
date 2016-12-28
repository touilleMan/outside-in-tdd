from unittest.mock import Mock

from app.clock import Clock
from app.transaction import Transaction
from app.transaction_repository import TransactionRepository

today = "12/05/2015"


class TestTransactionRepositoryShould:
    def setup_method(self):
        self.clock = Mock(Clock)
        self.clock.today_as_string.return_value = today
        self.transaction_repository = TransactionRepository(self.clock)

    def test_create_and_store_a_deposit_transaction(self):
        self.transaction_repository.add_deposit(100)

        transactions = self.transaction_repository.all_transactions()
        assert len(transactions) == 1
        assert transactions[0] == Transaction(today, 100)

    def test_create_and_store_a_withdrawal_transaction(self):
        self.transaction_repository.add_withdrawal(100)

        transactions = self.transaction_repository.all_transactions()
        assert len(transactions) == 1
        assert transactions[0] == Transaction(today, -100)
