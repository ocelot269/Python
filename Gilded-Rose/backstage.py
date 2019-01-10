from regularitem import RegularItem


class Backstage(RegularItem):

    def update_quality(self):

        if self.getSell_in() <= 10:
            self.setQuality(2)

        elif self.getSell_in() <= 5:
            self.setQuality(3)

        elif self.getSell_in() < 0:
            self.quality = 0
        else:
            self.setQuality(1)


if __name__ == '__main__':

    # casos test
    objeto = Backstage("Backs trompeta", 9, 8)
    objeto1 = Backstage("Backs TOP", 5, 10)
    objeto2 = Backstage("Backs TWOP", -1, 10)
    objeto3 = Backstage("Backs TOP", 200, 10)
    objeto.update_quality()
    objeto1.update_quality()
    objeto2.update_quality()
    objeto3.update_quality()
    assert objeto.quality == 10
