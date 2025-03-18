from abc import ABC, abstractmethod


class BaseSwitch(ABC):
    @abstractmethod
    def set_input_port(self, port: int):
        pass
