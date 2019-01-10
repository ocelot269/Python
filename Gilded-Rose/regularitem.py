from item import Item
from updatable import Updatable


class RegularItem(Updatable, Item):

    def getName(self):
        return self.name

    def getSell_in(self):
        return int(self.sell_in)

    def getQuality(self):
        return self.quality

	
    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self,valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


if __name__ == '__main__':

    pato = RegularItem("pato", 100, 1)

    pato.update_quality()
    assert pato.quality == 0

    pipes = RegularItem("pipes", -2, 4)

    pipes.update_quality()
    assert pipes.quality == 2

    pato = RegularItem("Pato", 100, 1)

    assert pato.getName() == "Pato"

    assert pato.getSell_in() == 100

    assert pato.getQuality() == 1
