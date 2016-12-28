from unittest.mock import Mock

from app.console import Console
from app.statement_printer import StatementPrinter

NO_TRANSACTIONS = []


class TestStatementPrinter:
    def setup_method(self):
        self.console = Mock(Console)
        self.statement_printer = StatementPrinter(self.console)

    def test_statement_printer_should_always_print_the_header(self):
        self.statement_printer.print(NO_TRANSACTIONS)
        self.console.print_line.assert_called_with('DATE | AMOUNT | BALANCE')
