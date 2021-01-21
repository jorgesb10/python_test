import abc

class Evento(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def gatillarEvento(self):
        pass

    