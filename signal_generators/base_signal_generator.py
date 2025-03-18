from abc import ABC, abstractmethod


class BaseSignalGenerator(ABC):
    @abstractmethod
    def start(self, freq: int, power: int):
        pass

    @abstractmethod
    def stop(self):
        pass
