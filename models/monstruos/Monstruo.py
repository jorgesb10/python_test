import abc
import typing

class Monstruo(metaclass=abc.ABCMeta):

    def __init__(self, vidaMaxima:int, arma: 'Arma'):
