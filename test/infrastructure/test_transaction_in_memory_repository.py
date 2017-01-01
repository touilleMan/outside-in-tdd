from unittest.mock import Mock

from pytest import mark

from app.domain.transaction import Transaction
from app.infrastructure.clock import Clock
from app.infrastructure.transaction_in_memory_repository import TransactionInMemoryRepository

TODAY = "12/05/2015"


@mark.unit
class TestTransactionInMemoryRepositoryShould:
    def setup_method(self):
        self.clock = Mock(Clock)
        self.clock.today_as_string.return_value = TODAY
        self.transaction_repository = TransactionInMemoryRepository(self.clock)

    def test_create_and_store_a_deposit_transaction(self):
        self.transaction_repository.add_deposit(100)

        transactions = self.transaction_repository.all_transactions()
        assert len(transactions) == 1
        assert transactions[0] == Transaction(TODAY, 100)

    def test_create_and_store_a_withdrawal_transaction(self):
        self.transaction_repository.add_withdrawal(100)

        transactions = self.transaction_repository.all_transactions()
        assert len(transactions) == 1
        assert transactions[0] == Transaction(TODAY, -100)
