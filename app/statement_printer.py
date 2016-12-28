STATEMENT_HEADER = 'DATE | AMOUNT | BALANCE'


class StatementPrinter:
    def __init__(self, console):
        self.console = console

    def print(self, transactions):
        self.console.print_line(STATEMENT_HEADER)
