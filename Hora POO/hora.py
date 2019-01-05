class Hora():

    def __init__(self, hora, minutos, segundos):
        self.__hora = 00
        self.__minutos = 00
        self.__segundos = 00

    def setHora(self, hora, minutos, segundos):
        if self.__hora > 24 or self.__minutos > 59 or self.__segundos > 59:
            return 0

    def getHora(self):
        return self.__hora + ":" + self.__minutos + ":" + self.__segundos

    def imprimirHora(self):
        print(str(self.__hora) + ":" + str(self.__minutos) +
              ":" + str(self.__segundos))

if __name__ == '__main__':

        # Casos test
    hora1 = Hora(25, 00, 15)
    hora2 = Hora(24, 23, 21)

    print(hora1.imprimirHora())
    assert hora1.imprimirHora() == 0:0:0
