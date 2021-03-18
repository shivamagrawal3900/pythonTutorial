from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def show(self):
        pass
