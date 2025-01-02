from Tamagotchi import Tamagotchi

class Personaje(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
        self.nombre = nombre
        self.color = color
    def jugar(self):
        self.energia -= 1
        self.felicidad += 1
        self.salud += 1
        print(f"El tamagotchi de {self.nombre} ha jugado.")
    def comer(self):
        self.energia += 1
        self.felicidad += 1
        self.salud += 1
    def curar(self):
        self.energia += 1
        self.felicidad += 1
        self.salud += 1

personaje1 = Personaje("Mimitchi", "Azul")
personaje1.jugar()