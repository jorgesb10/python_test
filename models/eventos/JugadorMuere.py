
from models.eventos.Evento import Event

import typing
if typing.TYPE_CHECKING:
    from controlador.Juego import Juego

class JugadorMuere(Evento):

    def visitarJuego(self, juego: 'Juego'):
        juego.perder()
