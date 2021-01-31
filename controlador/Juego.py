
import typing
from rx.subject import Subject



if typing.TYPE_CHECKING:
    from models.monstruos.Goblin import Goblin
    from models.eventos.Evento import Evento
    from models.monstruos.Monstruo import Monstruo

class Juego:

    def __init__(self, jugador: 'Jugador'):
        self.jugador = jugador
        self.monstruoActual = Goblin()
        self.monstruoLista = [
            Goblin(),
            Goblin()
        ]

        self.jugadorDisposable = self.eventoObservable.subcribe(self.aceptarEvento)
        self.monstruoActualDisposable = \
            self.monstruoActual.eventoObservable.subscribe(self.aceptarEvento)

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

    def pasarASiguienteMonstruo(self)-> None:
        self.monstruoActualDisposable.dispose()
        if len(self.monstruoLista)==0:
            self.ganar()
        else:   
            self.monstruoActual = self.monstruoLista.pop()
            self.monstruoActualDisposable=\
                self.monstruoActual.eventoObservable.subscribe(self.aceptarEvento)
            self.nombreSiguienteMonstruo.on_next(self.monstruoActual.__str__())

    def interaccion(self,
                    monstruoAtacante: 'Monstruo',
                    monstruoAtacado: 'Monstruo')->str:
        monstruoAtacante.atacar(monstruoAtacado)
        return "{} recibió daño".format(monstruoAtacado.__str__())

    def jugadorAtaca(self)->str:
        return self.interaccion(self.jugador, self.monstruoActual)

    def monstruoAtaca(self)->str:
        return self.interaccion(self.monstruoActual,self.jugador)
    
    def comenzar(self)->None:
        self.nombreSiguienteMonstruo.on_next(self.monstruoActual.__str__())