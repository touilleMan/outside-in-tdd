from unittest.mock import Mock, call

from app.domain.account import Account
from app.infrastructure.clock import Clock
from app.infrastructure.console import Console
from app.infrastructure.statement_console_printer import StatementConsolePrinter
from app.infrastructure.transaction_in_memory_repository import TransactionInMemoryRepository


class TestPrintStatementFeature:
    def setup_method(self):
        self.clock = Mock(Clock)
        transaction_repository = TransactionInMemoryRepository(self.clock)
        self.console = Mock(Console)
        statement_printer = StatementConsolePrinter(self.console)
        self.account = Account(transaction_repository, statement_printer)

    def test_print_statement_containing_all_transactions(self):
        self.clock.today_as_string.side_effect = ['01/04/2014', '02/04/2014', '10/04/2014']

        self.account.deposit(1000)
        self.account.withdraw(100)
        self.account.deposit(500)

        self.account.print_statement()

        calls = [
            call("DATE | AMOUNT | BALANCE"),
            call("10/04/2014 | 500.00 | 1400.00"),
            call("02/04/2014 | -100.00 | 900.00"),
            call("01/04/2014 | 1000.00 | 1000.00"),
        ]
        self.console.print_line.assert_has_calls(calls)
