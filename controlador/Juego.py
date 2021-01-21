
import typing
from rx.subject import Subject
from models.monstruos.Monstruo import Monstruo


if typing.TYPE_CHECKING:
    from models.monstruos.Goblin import Goblin
    from models.eventos.Evento import Evento

class Juego:

    def __init__(self, jugador: 'Jugador'):
        self.jugador = jugador
        self.monstruoActual = Goblin()
        self.monstruoLista = [
            Goblin(),
            Goblin()
        ]
        self.jugadorDisposable = self.eventoObservable.subcribe()
        self.monstruoActualDisposable = \
            self.monstruoActual.eventoObservable.subscribe()

        self.resultado: Subject[bool] = Subject()
        self.nombreSiguienteMonstruo: Subject[str] = Subject() 
    
    def liberar(self) -> None:
        self.jugadorDisposable.dispose()
        self.monstruoActualDisposable.dispose()

    def ganar(self) -> None:
        self.liberar()
        self.resultado.on_next(True)
        self.resultado.on_completed()

    def perder(self) -> None:
        self.liberar()
        self.resultado.on_next(False)
        self.resultado.on_completed()

    def aceptarEvento(self,evento: 'Evento') -> None:
        evento.visitarJuego(self)


