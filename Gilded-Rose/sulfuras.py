class Sulfuras():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        assert self.quality == 80, "Quality de %s no es 80" % self.__class__.__name__#Esto es una invariante,tanto como entra como sale debe ser 80
        pass

    def __repr__(self):  # Esto devuelve la calidad del objeto en string
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)#Aqui hacedemos al objeto a la propiedad


if __name__ == '__main__':

    # Casos text
    item = Sulfuras("Sulfuras, mano de Maradona", 3, 80)
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    # test update_quality incorret input
    item = Sulfuras("Sulfuras, mano de Dios", 3, 10000)
    for dia in range(1, 10):
        item.update_quality()
        print(item)
