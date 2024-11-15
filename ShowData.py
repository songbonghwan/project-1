from abc import ABC, abstractmethod

class ShowData(ABC):
    @abstractmethod
    def showData(self):
        pass