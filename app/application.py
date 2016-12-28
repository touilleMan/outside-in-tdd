from .domain.account import Account
from .infra.clock import Clock
from .infra.console import Console
from .infra.console_statement_printer import ConsoleStatementPrinter
from .infra.in_memory_transaction_repository import InMemoryTransactionRepository


def main():
    clock = Clock()
    transaction_repository = InMemoryTransactionRepository(clock)
    console = Console()
    statement_printer = ConsoleStatementPrinter(console)
    account = Account(transaction_repository, statement_printer)

    account.deposit(1000)
    account.withdraw(400)
    account.deposit(100)

    account.print_statement()


if __name__ == '__main__':
    main()
