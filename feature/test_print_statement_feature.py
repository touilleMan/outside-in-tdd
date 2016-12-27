from unittest.mock import Mock
from src.console import Console

def test_print_statement_containing_all_transactions():
    # Given
    console = Mock(Console)
    account = Mock(["print_statement"])

    # When
    account.print_statement()

    # Then
    console.print_line.assert_called_with("DATE | AMOUNT | BALANCE")
    console.print_line.assert_called_with("10/04/2014 | 500.00 | 1400.00")
    console.print_line.assert_called_with("02/04/2014 | -100.00 | 900.00")
    console.print_line.assert_called_with("01/04/2014 | 1000.00 | 1000.00")

