from abc import ABC, abstractmethod


class IApresentador(ABC):

    @abstractmethod
    def apresentar_show(self) -> None:
        pass
