from .account import Account
from .clock import Clock
from .console import Console
from .statement_printer import StatementPrinter
from .transaction_repository import TransactionRepository


def main():
    clock = Clock()
    transaction_repository = TransactionRepository(clock)
    console = Console()
    statement_printer = StatementPrinter(console)
    account = Account(transaction_repository, statement_printer)

    account.deposit(1000)
    account.withdraw(400)
    account.deposit(100)

    account.print_statement()

if __name__ == '__main__':
    main()
