from regularitem import RegularItem


class Sulfuras(RegularItem):

    def update_quality(self):
        if self.quality != 80:
            self.quality = 80

if __name__ == '__main__':

    # casos text
    sulfuras = Sulfuras("Sulfuras mano de la paz", 20, 80)
    sulfuras.update_quality()
    assert sulfuras.quality == 80

    sulfuras = Sulfuras("Sulfuras mano de la paz", 20, 40)
    sulfuras.update_quality()
    assert sulfuras.quality == 80

    sulfuras = Sulfuras("Sulfuras mano de la paz", 20, 10)
    sulfuras.update_quality()
    assert sulfuras.quality == 80