
import abc
import typing

from rx.subject import Subject
from models.eventos.MonstruoMuere import MonstruoMuere

if typing.TYPE_CHECKING:
    from models.armas.Arma import Arma
    from models.eventos.Evento import Evento

class Monstruo(metaclass=abc.ABCMeta):

    def __init__(self, vidaMaxima:int, arma: 'Arma', nombre: str):
        self.vidaMaxima = vidaMaxima
        self.arma = arma
        self.nombre = nombre
        self.vidaActual = vidaMaxima
        self.eventoObservable: Subject['Evento'] = Subject()

    def getAttackPoints(self) -> int:
        return self.arma.getAttack()

    def recibirdano(self, monstruo: 'Monstruo') -> None:
        self.vidaActual -= monstruo.getAttackPoints()
        if self.vidaActual <= 0:
            self.vidaActual = 0
            self.morir()
    
    def atacar(self, monstruoQueRecibe : 'Monstruo')-> None:
        monstruoQueRecibe.recibirdano(self)

    def morir(self) -> None:
        self.eventoObservable.on_next(MonstruoMuere())
        self.eventoObservable.on_completed()