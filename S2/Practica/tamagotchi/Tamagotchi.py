class Tamagotchi:
    def __init__(self, nombre,color):
        self.nombre = nombre
        self.color = color
        self.energia = 100
        self.felicidad = 100
        self.salud = 100

    def jugar(self):
        self.energia -= 50
        self.salud -= 10
        if self.felicidad >= 100:
            self.felicidad += 0
        else:
            self.felicidad += 10
            
    def comer(self):
        self.energia += 10
        self.felicidad += 10
        self.salud += 10
    def curar(self):
        self.energia += 10
        self.felicidad += 10
        self.salud += 10


    
        