
class Item():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "El objeto se llama " + str(self.getName) + " tiene que venderse en " + str(self.getSell_in) + " dias, y su calidad es " + str(self.getQuality)
