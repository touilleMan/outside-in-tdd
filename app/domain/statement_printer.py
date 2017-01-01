from abc import ABC, abstractmethod


class StatementPrinter(ABC):
    @abstractmethod
    def print(self, transactions):
        raise NotImplementedError()
