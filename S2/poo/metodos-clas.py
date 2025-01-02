class TarjetaCredito:

    # Atributos de clase

    banco = "Banco Internacional de Programadores"

    # Agregamos un atributo de clase que guarda todas las tarjetas de crédito

    todas_las_tarjetas = []

    def __init__(self, limite_credito, saldo_pagar):

        # Esteblecemos los atributos de instancia

        self.limite_credito = limite_credito

        self.saldo_pagar = saldo_pagar

        # Cada que se cree una nueva instancia de la clase, se agrega a todas_las_tarjetas

        TarjetaCredito.todas_las_tarjetas.append(self)

    # Método de clase que cambia el banco

    @classmethod
    def cambiar_banco(cls, nombre):

        cls.banco = nombre

    # Método de clase que imprime el total de saldos a pagar de todas las tarjetas

    def todos_saldos(cls):

        total_saldos = 0

        for tarjeta in cls.todas_las_tarjetas:  # Usamos cls para hacer referencia a la clase

            total_saldos += tarjeta.saldo_pagar

        return total_saldos

    def hacer_compra(self, monto):  # recibe como argumento el monto de la compra

        # Evaluamos si puede realizar la compra con un método estático

        if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):

            # el saldo a pagar del usuario aumenta en la cantidad del valor recibido
            self.saldo_pagar += monto

        else:

            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")

        return self

    # Solamente tienen acceso a los argumentos que reciben

    @staticmethod
    def puede_comprar(limite, saldo_utilizado, monto):

        # Revisamos si con la compra, el saldo sobrepasa el límite de crédito

        if (saldo_utilizado + monto) > limite:

            return False

        else:

            return True
