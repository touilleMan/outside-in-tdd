from .domain.account import Account
from .infrastructure.clock import Clock
from .infrastructure.console import Console
from .infrastructure.statement_console_printer import StatementConsolePrinter
from .infrastructure.transaction_in_memory_repository import TransactionInMemoryRepository


def main():
    clock = Clock()
    transaction_repository = TransactionInMemoryRepository(clock)
    console = Console()
    statement_printer = StatementConsolePrinter(console)
    account = Account(transaction_repository, statement_printer)

    account.deposit(1000)
    account.withdraw(400)
    account.deposit(100)

    account.print_statement()


if __name__ == '__main__':
    main()
