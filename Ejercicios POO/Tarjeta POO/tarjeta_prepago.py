class Tarjeta_prepago():

    def __init__(self, n_telefono, nif, saldo):
        self.n_telefono = n_telefono
        self.nif = nif
        self.saldo = float(saldo)  # En euros
        self.consumo = float(0)

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.getN_telefono(), self.getNif(), self.getSaldo(), self.getConsumo())

    def getN_telefono(self):
        return self.n_telefono

    def getNif(self):
        return self.nif

    def getSaldo(self):
        return self.saldo

    def getConsumo(self):
        return self.consumo

    def setSaldo(self, dinero):
        self.saldo += dinero

    def setConsumo(self, gastos):
        self.consumo += gastos

    def ingresarSaldo(self, dinero):
        self.setSaldo(dinero)

    def enviarMensaje(self, n_mensajes):
        # Este metodo resta al saldo el consumo de los mensajes
        # al principio para que el total se convierta en negativo
        self.setSaldo(-(n_mensajes * 9) / 100)

    def realizarLlamada(self, segundos):
        self.setSaldo(-(segundos + 15) / 100)
        self.setConsumo((segundos + 15) / 100)

    def consultarTarjeta(self):
        print("Tu saldo es %s€ y el consumo al numero de telefono %s es %s€ con dni %s" % (
            self.getSaldo(), self.getN_telefono(), self.getConsumo(), self.getNif()))

if __name__ == '__main__':

        # casos test
    tarjeta = Tarjeta_prepago("653333333", "42224953-L", 1000)
    tarjeta.ingresarSaldo(10000)
    tarjeta.realizarLlamada(65)
    tarjeta.consultarTarjeta()
    assert tarjeta.getSaldo() == 10999.2

    tarjeta1 = Tarjeta_prepago("653333333", "42224953-L", 1000)
    tarjeta1.ingresarSaldo(1)
    assert tarjeta1.getSaldo() == 1001

    tarjeta2 = Tarjeta_prepago("653333333", "42224953-L", 1001)
    tarjeta2.enviarMensaje(9)
    assert tarjeta2.getSaldo() == 1000.19

    tarjeta3 = Tarjeta_prepago("653333333", "42224953-L", 1001)
    tarjeta3.enviarMensaje(10)
    assert tarjeta3.getSaldo() == 1000.10

    tarjeta4 = Tarjeta_prepago("653333333", "42224953-L", 1001)
    tarjeta4.realizarLlamada(10)
    assert tarjeta4.getSaldo() == 1000.75
    assert tarjeta4.getConsumo() == 0.25
