class CuentaCorriente(object):

    def __init__(self, nombre, apellidos, direccion, telefono, nif):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.saldo = float(1000)
        self.nif = nif

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono

    def getSaldo(self):
        return self.saldo

    def getNif(self):
        return self.nif

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setNif(self, nif):
        self.nif = nif

    def setSaldo(self, saldo):
        self.saldo += saldo

    def retirarDinero(self, cantidad_retirada):
        self.setSaldo(-cantidad_retirada)

    def ingresarDinero(self, cantidad_ingresada):
        self.setSaldo(cantidad_ingresada)

    def consultarCuenta(self):
        print("Nombre: " + str(self.getNombre()) + " " + str(self.getApellidos()) + ", Tu saldo es: " + str(self.getSaldo()) + "€")

    def saldoNegativo(self):
        if self.getSaldo() < 0:
            return True
        return False


if __name__ == '__main__':

    cuenta = CuentaCorriente(
        "Jose Antonio", "Zamora Andres", "Calle Falsa nª63", "654564561", "43224953-H")
    assert cuenta.getSaldo() == 1000
    assert cuenta.getNif() == "43224953-H"
    assert cuenta.getTelefono() == "654564561"
    assert cuenta.getDireccion() == "Calle Falsa nª63"
    assert cuenta.getNombre() == "Jose Antonio"
    assert cuenta.getApellidos() == "Zamora Andres"

    cuenta.retirarDinero(1000)
    assert cuenta.getSaldo() == 0
    cuenta.retirarDinero(1500) == -1500
    assert cuenta.getSaldo() == -1500
    cuenta.ingresarDinero(1500)
    assert cuenta.getSaldo() == 0
    cuenta.ingresarDinero(3000)
    assert cuenta.getSaldo() == 3000

    cuenta.consultarCuenta()
    assert cuenta.saldoNegativo() == False
    cuenta.retirarDinero(5000)
    assert cuenta.getSaldo()== -2000
    assert cuenta.saldoNegativo()==True