class CuentaCorriente(object):

    def __init__(self, nombre, apellidos, direccion, telefono):
        self.nombre = str(nombre)
        self.apellidos = str(apellidos)
        self.__direccion = str(direccion)
        self.telefono = str(telefono)
        self.__saldo = float(1000)
        self.__nif = True

    def setRetirarDinero(self, cantidad_retirada):
        self.__saldo -= cantidad_retirada
        return self.__saldo

    def setIngresarDinero(self, cantidad_ingresada):
        self.__saldo += cantidad_ingresada
        assert type(self.__saldo == str)
        return self.__saldo

    def getConsultarCuenta(self):
        return "Nombre: " + self.nombre + self.apellidos + " Tu saldo es: " + str(self.__saldo) + "€"

    def getSaldoNegativo(self):
        if self.__saldo < 0:
            return True
        return False


if __name__ == '__main__':

    cuenta = CuentaCorriente(
        "Jose Antonio ", "Zamora Andres", "Calle Falsa nª63", "654564561",)
    assert cuenta.getConsultarCuenta(
    ) == "Nombre: Jose Antonio Zamora Andres Tu saldo es: 1000.0€"
    assert cuenta.getSaldoNegativo() == False
    assert cuenta.setIngresarDinero(1000) == 2000
    assert cuenta.setRetirarDinero(2100) == -100
    assert cuenta.getSaldoNegativo() == True
