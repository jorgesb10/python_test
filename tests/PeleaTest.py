import typing

from models.monstruos.Goblin import Goblin

if typing.TYPE_CHECKING:
    from models.monstruos.Monstruo import Monstruo

def recibirDanoTest(monstruoAtacante : 'Monstruo'):
    goblin = Goblin()
    vidaInicial = goblin.vidaActual
    goblin.eventoObservable.subscribe(
        lambda evento: print(evento)
    )

    for _ in range(3):
        monstruoAtacante.atacar(goblin)

    assert goblin.vidaActual<vidaInicial
    assert goblin.vidaActual==0

def tests():
    recibirDanoTest(Goblin())