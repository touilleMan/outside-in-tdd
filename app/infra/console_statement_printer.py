from ..domain.statement_printer import StatementPrinter

STATEMENT_HEADER = 'DATE | AMOUNT | BALANCE'


class ConsoleStatementPrinter(StatementPrinter):
    def __init__(self, console):
        self.console = console

    def print(self, transactions):
        self.console.print_line(STATEMENT_HEADER)
        self.__print_statement_lines(transactions)

    def __print_statement_lines(self, transactions):
        balance = 0
        statement_lines = []
        for transaction in transactions:
            balance = balance + transaction.amount
            statement_lines.append(self.__statement_line(transaction, balance))

        for line in reversed(statement_lines):
            self.console.print_line(line)

    @staticmethod
    def __statement_line(transaction, balance):
        return "{0} | {1:.2f} | {2:.2f}".format(transaction.date, transaction.amount, balance)
