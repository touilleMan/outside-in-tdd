from abc import ABC, abstractmethod


class TransactionRepository(ABC):
    @abstractmethod
    def add_deposit(self, amount):
        raise NotImplementedError()

    @abstractmethod
    def add_withdrawal(self, amount):
        raise NotImplementedError()

    @abstractmethod
    def all_transactions(self):
        raise NotImplementedError()
