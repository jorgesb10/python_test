import abc
import typing

if typing.TYPE_CHECKING:
    from controlador.Juego import Juego

class Evento(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def visitarJuego(self, juego: 'Juego'):
        pass

