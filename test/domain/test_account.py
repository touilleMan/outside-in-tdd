from unittest.mock import Mock

from pytest import mark

from app.domain.account import Account
from app.domain.statement_printer import StatementPrinter
from app.domain.transaction import Transaction
from app.domain.transaction_repository import TransactionRepository


@mark.unit
class TestAccountShould:
    def setup_method(self):
        self.transaction_repository = Mock(TransactionRepository)
        self.statement_printer = Mock(StatementPrinter)
        self.account = Account(self.transaction_repository, self.statement_printer)

    def test_store_a_deposit_transaction(self):
        self.account.deposit(100)
        self.transaction_repository.add_deposit.assert_called_with(100)

    def test_store_a_withdrawal_transaction(self):
        self.account.withdraw(100)
        self.transaction_repository.add_withdrawal.assert_called_with(100)

    def test_print_a_statement(self):
        transactions = [Transaction("12/05/2015", 100)]
        self.transaction_repository.all_transactions.return_value = transactions

        self.account.print_statement()

        self.statement_printer.print.assert_called_with(transactions)
