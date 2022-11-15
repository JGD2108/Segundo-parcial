import abc
class Jugador(abc.ABC):
    def __init__(self, points:int) -> None:
        self._defense=0
        self._attack=0
        self._points = points
        self._name = ""
    @abc.abstractmethod
    def points():
        pass

    @abc.abstractmethod
    def name():
        pass
    @abc.abstractmethod
    def highPunch():
        pass
    @abc.abstractmethod
    def midPunch():
        pass
    @abc.abstractmethod
    def LowPunch():
        pass
    @abc.abstractmethod
    def highDefense():
        pass
    @abc.abstractmethod
    def midDefense():
        pass
    @abc.abstractmethod
    def lowDefense():
        pass
    def __repr__(self):
        return self.attack,self.defense