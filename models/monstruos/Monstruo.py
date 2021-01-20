import abc
import typing

if typing.TYPE_CHECKING:
    from models.armas.Arma import Arma



class Monstruo(metaclass=abc.ABCMeta):

    def __init__(self, vidaMaxima:int, arma: 'Arma'):
        pass
