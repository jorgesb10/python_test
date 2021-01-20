import abc

class Arma(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def getAttack(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
