
import abc
import typing

if typing.TYPE_CHECKING:
    from models.armas.Arma import Arma


class Monstruo(metaclass=abc.ABCMeta):

    def __init__(self, vidaMaxima:int, arma: 'Arma', nombre: str):
        self.vidaMaxima = vidaMaxima
        self.arma = arma
        self.nombre = nombre
        self.vidaActual = vidaMaxima

    def getAttackPoints(self) -> int:
        return self.arma.getAttack()

    def recibirdano(self, monstruo: 'Monstruo') -> None:
        self.vidaActual -= monstruo.getAttackPoints()
        if self.vidaActual <= 0:
            self.vidaActual = 0
    
    def atacar(self, monstruoQueRecibe : 'Monstruo')-> None:
        monstruoQueRecibe.recibirdano(self)
    