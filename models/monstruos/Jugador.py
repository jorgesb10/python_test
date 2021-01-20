import sys
sys.path.append("/Users/jorgesuarez/Desktop/test/python_test/")

from models.monstruos.Monstruo import Monstruo
from models.armas.Espada import Espada

class Jugador(Monstruo):
    def __init__(self, nombre:str):
        super().__init__(10, Espada(),nombre)

    def recuperarse(self) -> None:
        self.vidaMaxima += 3
        if self.vidaActual > self.vidaMaxima:
            self.vidaActual = self.vidaMaxima

