
class TarjetaCredito:
    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f" Credito:{self.limite_credito} Saldo a pagar: {self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

# Crear 3 tarjetas

tarjeta1 = TarjetaCredito(100, 20000, 0.05)
tarjeta2 = TarjetaCredito(500, 10000, 0.1)
tarjeta3 = TarjetaCredito(200, 30000, 0.15)

#haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta;
#todo esto en una sola línea a través de la encadenación.
tarjeta1.compra(500).compra(300).pago(200).cobrar_interes().mostrar_info_tarjeta()

#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; 
#todo esto en una sola línea a través de la encadenación.
tarjeta2.compra(500).compra(300).compra(100).pago(200).pago(100).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. 
#Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tarjeta3.compra(500).compra(300).compra(100).compra(500).compra(500).mostrar_info_tarjeta()
