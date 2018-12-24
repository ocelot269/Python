class CuentaCorriente(object):

    def __init__(self, nombre, apellidos, direccion, telefono):
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)
        self.__direccion = str(direccion)
        self.__telefono = str(telefono)
        self.__saldo = float(1000)
        self.__nif = True

    def retirarDinero(self, cantidad_retirada):
        self.__saldo -= self.cantidad_retirada  
        return self.__saldo

    def ingresarDinero(self, cantidad_ingresada):
        self.__saldo += self.cantidad_ingresada
        return self.__saldo

    def consultarCuenta(self,):
        print(self.__saldo)

    def saldoNegativo(self,__saldo):
        if self.saldo >= 0:
            return True
        return False


if __name__ == '__main__':


    cuenta = CuentaCorriente("Jose Antonio ", "Zamora Andres", "Calle Falsa nª63", "654564561",)
    cuenta.consultarCuenta()
