from Paquete.Jugador import Jugador
import random
class Cpu(Jugador):
    @property
    def points(self):
        return self._points
    @points.setter
    def points(self,a):
        self._points =a
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,a):
        self._name=a
    def highPunch(self):
        self.attack = 3
        self.defense = None
    def midPunch(self):
        self.attack=2
        self.defense= None
    def LowPunch(self):
        self.attack = 1
        self.defense= None
    def highDefense(self):
        self.defense = 3
        self.attack= None
    def midDefense(self):
        self.defense = 2
        self.attack= None
    def lowDefense(self):
        self.defense = 1
        self.attack= None
    
    def Escoger(Cpu):
        opc1 = random.choice((1,2))
        opc2 = random.choice((1,2,3))
        if opc1==1:
            if opc2==1:
                Cpu.lowDefense()
            elif opc2==2:
                Cpu.midDefense()
            elif opc2==3:
                Cpu.highDefense()
        else: 
             if opc2==1:
                Cpu.LowPunch()
             elif opc2==2:
                Cpu.midPunch()
             elif opc2==3:
                Cpu.highPunch()