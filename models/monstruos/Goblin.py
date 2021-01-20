
from models.monstruos.Monstruo import Monstruo
from models.armas.Espada import Espada

class Goblin(Monstruo):
    def __init__(self):
        super().__init__(5, Espada(), 'Goblin')

