from unittest.mock import Mock, call

from pytest import mark

from app.domain.transaction import Transaction
from app.infra.console import Console
from app.infra.console_statement_printer import ConsoleStatementPrinter

NO_TRANSACTIONS = []


@mark.unit
class TestConsoleStatementPrinter:
    def setup_method(self):
        self.console = Mock(Console)
        self.statement_printer = ConsoleStatementPrinter(self.console)

    def test_statement_printer_should_always_print_the_header(self):
        self.statement_printer.print(NO_TRANSACTIONS)
        self.console.print_line.assert_called_with('DATE | AMOUNT | BALANCE')

    def test_statement_printer_should_print_transactions_in_reverse_chronological_order(self):
        transactions = (
            Transaction('01/04/2014', 1000),
            Transaction('02/04/2014', -100),
            Transaction('10/04/2014', 500),
        )
        self.statement_printer.print(transactions)

        calls = [
            call("DATE | AMOUNT | BALANCE"),
            call("10/04/2014 | 500.00 | 1400.00"),
            call("02/04/2014 | -100.00 | 900.00"),
            call("01/04/2014 | 1000.00 | 1000.00"),
        ]
        self.console.print_line.assert_has_calls(calls)