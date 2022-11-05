class Persona:
    def __init__(self, nombre, edad, altura, sexo, **kwargs):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo
        super().__init__(**kwargs)

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad
    
    def setAltura(self, altura):
        self.altura = altura
    
    def setSexo(self, sexo):
        self.sexo = sexo

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getAltura(self):
        return self.altura
    
    def getSexo(self):
        return self.sexo

class Deportista:
    def __init__(self, deporte = "Futbol", añosPracticando, **kwargs):
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

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre=nombre, edad=edad, altura=altura, sexo=sexo, deporte=deporte, añosPracticando=añosPracticando)
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