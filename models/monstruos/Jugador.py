
from models.monstruos.Monstruo import Monstruo
from models.armas.Espada import Espada
from models.eventos.JugadorMuere import JugadorMuere

class Jugador(Monstruo):
    def __init__(self, nombre:str):
        super().__init__(10, Espada(),nombre)

    def recuperarse(self) -> None:
        self.vidaMaxima += 3
        if self.vidaActual > self.vidaMaxima:
            self.vidaActual = self.vidaMaxima
            self.morir()

    def morir(self) -> None:
        self.eventoObservable.on_next(JugadorMuere())
        self.eventoObservable.on_completed()
