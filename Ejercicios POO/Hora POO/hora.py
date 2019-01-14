class Hora():

    def __init__(self, horas, minutos, segundos):
        self.hora = 0
        self.minuto = 0
        self.segundos = 0

    def getHoras(self):
        return self.hora

    def getMinuto(self):
        return self.minuto

    def getSegundos(self):
        return self.segundos

    def setSegundos(self, segundos):
        self.segundos += segundos

    def setMinuto(self, minutos):
        self.minuto += minutos

    def setHoras(self, horas):
        self.hora += horas

    def setHora(self, hora, minutos, segundos):  # Muestra toda la hora al completo en string
        if self.setHoras(hora) < 25:
            self.setHoras(hora)
        elif self.setHoras(hora) > 59 :
            self.setHoras(0)
        if self.setMinuto(minutos) < 60:
            self.setMinutos(minutos)
        elif self.setMinuto(minutos) > 59:
            self.setMinutos(0)
            self.setHoras(1)
        if self.setSegundos(segundos) < 60:
            self.setSegundos(segundos)
        elif self.setSegundos(segundos) > 59:
            self.setSegundos(0)
            self.setMinuto(1)

    def getHora(self):
        return str(self.getHoras()) + ":" + str(self.getMinuto()) + ":" + str(self.getSegundos())


if __name__ == '__main__':

    hora1 = Hora(12, 00, 21)
    hora1.getSegundos()
    hora1.getMinuto()
    hora1.getHoras()
    assert hora1.getHora() == "0:0:0"
    #hora1.setHora()