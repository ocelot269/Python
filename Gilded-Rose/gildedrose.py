from age_brie1 import AgedBrie
from sulfuras1 import Sulfuras
from backstage import Backstage


class GildedRose():

    def __init__(self, stock):
        self.stock = stock

    def getStock(self):
        return self.stock

    def actualizarStock(self):
        for item in stock:
            item.update_quality()

    def getQualityItem(self, nombre):

        array = self.getStock()

        for item in array:
            if item.getName() == nombre:
                return item.getQuality()

if __name__ == '__main__':

    stock = [AgedBrie("nombre", 100, 0), Sulfuras(
        "sulfuras1", 20, 14), Backstage("Backstage", 10, 15)]

    tienda = GildedRose(stock)

    tienda.actualizarStock()

    assert 1 == tienda.getQualityItem("nombre")
    assert 80 == tienda.getQualityItem("sulfuras1")
    assert 17 == tienda.getQualityItem("Backstage")
