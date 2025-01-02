class TarjetaCredito:
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self  # Devolver self para encadenamiento

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self  # Devolver self para encadenamiento

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self  # Devolver self para encadenamiento


class Usuario:
    def __init__(self, nombre, tarjetas=[]):
        self.nombre = nombre
        self.tarjeta = TarjetaCredito(limite_credito=10000, intereses=0.015, saldo_pagar=10)
        self.tarjetas = tarjetas
    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra
        self.tarjeta.saldo_pagar += monto
        print(f"Compra realizada de {monto} pesos")
        return self
    def pagar_tarjeta(self, monto):
        self.tarjeta.saldo_pagar -= monto
        return self
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}, Saldo a pagar: ${self.tarjeta.saldo_pagar}")
        return self
    def transferir_deuda(self, otro_usuario, monto): #BONUS
        if otro_usuario.tarjeta.saldo_pagar + monto <= otro_usuario.tarjeta.limite_credito:
            #Acumular saldo a pagar en el otro usuario
            otro_usuario.tarjeta.saldo_pagar += monto
            #Restar el monto a pagar del usuario actual
            self.tarjeta.saldo_pagar -= monto
            return self
        else:
            print("El monto excede el limite de credito del usuario receptor")
            return self

    #BONUS
    def hacer_compra_tarjeta(self, monto, numero_tarjeta=0):
        if numero_tarjeta < len(self.tarjetas):
            self.tarjetas[numero_tarjeta].compra(monto)
        else:
            print("Número de tarjeta inválido.")
        return self
    def pagar_tarjeta_numero(self, monto, numero_tarjeta=0):
        if numero_tarjeta < len(self.tarjetas):
            self.tarjetas[numero_tarjeta].pago(monto)
        else:
            print("Número de tarjeta inválido.")
        return self
    def mostrar_saldo_usuario_tarjetas(self):
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"Tarjeta {i+1}:")
            tarjeta.mostrar_info_tarjeta()
    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)
        return self  # Devolver self para encadenamiento


# Crear usuario con una sola tarjeta
usuario = Usuario("Carlos")
usuario.hacer_compra(1000)
usuario.mostrar_saldo_usuario()
usuario.tarjeta.cobrar_interes()
usuario.mostrar_saldo_usuario()

print("----------------------------------------------")







# Crear instancias de usuario y tarjetas
usuario1 = Usuario("Juan")
tarjeta1 = TarjetaCredito(limite_credito=5000, intereses=0.02)
usuario1.agregar_tarjeta(tarjeta1)

usuario2 = Usuario("María")
tarjeta2 = TarjetaCredito(limite_credito=10000, intereses=0.03, saldo_pagar=1000)
tarjeta3 = TarjetaCredito(limite_credito=2000, intereses=0.05)
usuario2.agregar_tarjeta(tarjeta2).agregar_tarjeta(tarjeta3)  # Encadenamiento

# Realizar operaciones
usuario1.hacer_compra(1000).mostrar_saldo_usuario()
usuario2.hacer_compra(500, 0).pagar_tarjeta(200, 1).mostrar_saldo_usuario()

