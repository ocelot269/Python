class Tarjeta_prepago():

    def __init__(self, n_telefono, nif, saldo):
        self.n_telefono = n_telefono
        self.nif = nif
        self.saldo = saldo  # En euros
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

    def IngresarSaldo(self, valor):
        self.saldo += valor


if __name__ == '__main__':

        # casos test
    tarjeta = Tarjeta_prepago("653333333", "42224953-L", 1000)
    tarjeta.IngresarSaldo(1000)
    assert tarjeta.getSaldo()== 2000