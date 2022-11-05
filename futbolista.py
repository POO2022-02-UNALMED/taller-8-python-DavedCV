from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre=nombre, edad=edad, altura=altura, sexo=sexo, deporte="Futbol", añosPracticando=añosPracticando)
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self.golesMarcados
    
    def getTarjetasRojas(self):
        return self.tarjetasRojas

    def getPiernaHabil(self):
        return self.piernaHabil

    def setGolesMarcados(self, goles_marca):
        self.golesMarcados = goles_marca
    
    def setTarjetasRojas(self, tarjetas_roja):
        self.tarjetasRojas = tarjetas_roja

    def setPiernaHabil(self, pierna_habil):
        self.piernaHabil = pierna_habil

    def __str__(self):
        return f'Mi nombre es {self.nombre} soy profesional en el deporte {self.deporte} Tengo {self.edad} años de edad y llevo {self.añosPracticando} Participando años en el deporte'