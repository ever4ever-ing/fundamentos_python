from tamagotchi.Tamagotchi import Tamagotchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = Tamagotchi(tamagotchi.nombre, tamagotchi.color)

    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()
        print(f"El tamagotchi de {self.nombre} ha jugado.")
        print(f"Energía: {self.tamagotchi.energia} felicidad: {self.tamagotchi.felicidad} salud: {self.tamagotchi.salud}")
    def darle_comida(self):
        self.tamagotchi.comer()
        print(f"El tamagotchi de {self.nombre} ha comido")
        print(f"Energía: {self.tamagotchi.energia} felicidad: {self.tamagotchi.felicidad} salud: {self.tamagotchi.salud}")

    def curarlo(self):
        self.tamagotchi.curar()
        print(f"El tamagotchi de {self.nombre} ha sido curado")
        print(f"Energía: {self.tamagotchi.energia} felicidad: {self.tamagotchi.felicidad} salud: {self.tamagotchi.salud}")

persona1 = Persona("Pepe", "Perez", Tamagotchi("Pepito", "Azul"))
persona1.darle_comida()
persona1.jugar_con_tamagotchi()
persona1.curarlo()