
from models.eventos.Evento import Evento
import typing
if typing.TYPE_CHECKING:
    from controlador.Juego import Juego


class MonstruoMuere(Evento):

    def visitarJuego(self, juego: 'Juego'):
        juego.pasarASiguienteMonstruo()
        