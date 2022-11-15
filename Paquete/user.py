from Paquete.Jugador import Jugador
class User(Jugador):
    @property
    def points(self):
        return self._points
    @points.setter
    def points(self,a):
        self._points = a
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,a):
        self._name=a
    @property
    def highPunch(self):
        return self._attack
    @property
    def highPunch(self):
        return self._defense
    @highPunch.setter
    def highPunch(self,a,s):
        self._attack = a
        self._defense = s
    @property
    def midPunch(self):
        return self._defense
    @property
    def midPunch(self):
        return self._attack
    @midPunch.setter
    def midPunch(self,a,s):
        self.attack=a
        self.defense= s
    @property
    def LowPunch(self):
        return self._attack
    @property
    def LowPunch(self):
        return self._attack
    @LowPunch.setter
    def LowPunch(self,a,s):
        self.attack = a
        self.defense= s
    @property
    def highDefense(self):
        return self._defense
    @property
    def highDefense(self):
        return self._attack
    @highDefense.setter
    def highDefense(self,a,s):
        self.defense = a
        self.attack= s
    @property
    def midDefense(self):
        return self._defense
    @property
    def midDefense(self):
        return self._attack
    @midDefense.setter
    def midDefense(self,a,s):
        self.defense = a
        self.attack= s
    @property
    def lowDefense(self):
        return self._defense
    @property
    def lowDefense(self):
        return self._attack
    @lowDefense.setter
    def lowDefense(self,a,s):
        self.defense = a
        self.attack= s