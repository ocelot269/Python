from regularitem import RegularItem


class AgedBrie(RegularItem):

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(1)
        else:
            self.setQuality(2)


if __name__ == '__main__':

    # casos test
    pestoso = AgedBrie("pestoso", 0, 3)
    pestoso.update_quality()
    assert pestoso.quality == 4
    quesito = AgedBrie("pestoso", -1, 3)
    pestoso.update_quality()
    assert pestoso.quality == 5
