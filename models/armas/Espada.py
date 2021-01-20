import sys
sys.path.append("/Users/jorgesuarez/Desktop/test/python_test/")

from models.armas.Arma import Arma

class Espada(Arma):

    def __init__(self):
        pass
    
    def getAttack(self) -> int:
        return 3
    
    def __str__(self) -> str:
        return "Espada"
