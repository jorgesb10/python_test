
from models.eventos.Evento import Evento

class MonstruoMuere(Evento):

    def visitarJuego(self, juego: 'Juego'):
        juego.pasarASiguienteMonstruo()
        
