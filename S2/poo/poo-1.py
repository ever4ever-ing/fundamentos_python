class Perro:
    def __init__(self, nombre, edad, raza):
        self.name = nombre
        self.age = edad
        self.race = raza

# instanciar un objeto
#perro1 = Perro("Firulais", 5, "Pastor Aleman")
#print(perro1.name)
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  # Método
        self.saldo_pagar += monto


miyagi = Usuario( "Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
print(miyagi.nombre)  

miyagi.hacer_compra(1000)
miyagi.hacer_compra(3000)

daniel.hacer_compra(4500)
print("Saldo a pagar:")
print(f"Miyagi: {miyagi.saldo_pagar}") 
print(f"Daniel: {daniel.saldo_pagar}") 