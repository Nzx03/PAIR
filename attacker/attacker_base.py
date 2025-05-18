
from abc import ABC, abstractmethod

class BaseAttacker(ABC):
    @abstractmethod
    def run(self):
        pass
