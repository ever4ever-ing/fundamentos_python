class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra
        self.saldo_pagar += monto
        return self
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
        return self
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}, Saldo a pagar: ${self.saldo_pagar}")
        return self
    def transferir_deuda(self, otro_usuario, monto): #BONUS
        if otro_usuario.saldo_pagar + monto <= otro_usuario.limite_credito:
            #Acumular saldo a pagar en el otro usuario
            otro_usuario.saldo_pagar += monto
            #Restar el monto a pagar del usuario actual
            self.saldo_pagar -= monto
            return self
        else:
            print("El monto excede el limite de credito del usuario receptor")
            return self


usuario1 = Usuario("1","b","c")
usuario1.hacer_compra(1000).mostrar_saldo_usuario().hacer_compra(2000).mostrar_saldo_usuario()
usuario1.pagar_tarjeta(1000).pagar_tarjeta(1000)
usuario1.mostrar_saldo_usuario()
usuario2 = Usuario("2","e","f")
usuario2.mostrar_saldo_usuario()
usuario1.transferir_deuda(usuario2, 1000)
usuario2.mostrar_saldo_usuario()

