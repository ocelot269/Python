class Tarjeta_prepago():

    def __init__(self, n_telefono, nif, saldo):
        self.n_telefono = n_telefono
        self.nif = nif
        self.saldo = float(saldo)  # En euros
        #self.consumo = consumo

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.n_telefono, self.nif, self.saldo)

    def getN_telefono(self):
        return self.n_telefono

    def getNif(self):
        return self.nif

    def getSaldo(self):
        return self.saldo

    def getConsumo(self):
        return self.consumo

    def ingresarSaldo(self, dinero):
        self.saldo += dinero

    def enviarMensaje(self, n_mensajes):
        self.saldo -= n_mensajes * 9 / 100


if __name__ == '__main__':

        # casos test
    tarjeta = Tarjeta_prepago("653333333", "42224953-L", 1000)
    tarjeta.ingresarSaldo(10000)
    assert tarjeta.getSaldo() == 11000

    tarjeta1 = Tarjeta_prepago("653333333", "42224953-L", 1000)
    tarjeta1.ingresarSaldo(1)
    assert tarjeta1.getSaldo() == 1001

    tarjeta2 = Tarjeta_prepago("653333333", "42224953-L", 1001)
    tarjeta2.enviarMensaje(9)
    assert tarjeta2.getSaldo() == 1000.19

    tarjeta3 = Tarjeta_prepago("653333333", "42224953-L", 1001)
    tarjeta3.enviarMensaje(10)
    assert tarjeta3.getSaldo() == 1000.10


