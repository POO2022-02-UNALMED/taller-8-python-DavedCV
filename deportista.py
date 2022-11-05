class Deportista:
    def __init__(self,  añosPracticando, deporte = "Futbol", **kwargs):
        self.deporte = deporte
        self.añosPracticando = añosPracticando
        super().__init__(**kwargs)

    def setDesporte(self, desporte):
        self.deporte = desporte

    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando
    
    def getDesporte(self):
        return self.deporte
    
    def getAñosPracticando(self):
        return self.añosPracticando