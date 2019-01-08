from updatable import Updatable


class Item(Updatable):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "El objeto se llama " + str(self.getName) + " tiene que venderse en " + str(self.getSell_in) + " dias, y su calidad es " + str(self.getQuality)

    def getName(self):
        return self.name

    def getSell_in(self):
        return self.sell_in

    def getQuality(self):
        return self.quality


if __name__ == '__main__':

        # Casos test

    Pato = Item("Pato", "100", "1")
    assert Pato.getName() == "Pato"
    assert Pato.getSell_in() == "100"
    assert Pato.getQuality() == "1"
    #assert Pato.__repr__() == "El objeto se llama Pato tiene que venderse en 100 dias, y su calidad es"
