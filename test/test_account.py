from unittest.mock import Mock
from app.account import Account
from app.transaction_repository import TransactionRepository


class TestAccountShould:
    def setup_method(self):
        self.transaction_repository = Mock(TransactionRepository)
        self.account = Account(self.transaction_repository)

    def test_store_a_deposit_transaction(self):
        self.account.deposit(100)
        self.transaction_repository.add_deposit.assert_called_with(100)

    def test_store_a_withdrawal_transaction(self):
        self.account.withdraw(100)
        self.transaction_repository.add_withdrawal.assert_called_with(100)
