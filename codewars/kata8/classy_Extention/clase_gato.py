class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " meows."


cat = Cat('Mr Whiskers')
cat1 = Cat('Lamp')
cat2 = Cat('$$Money Bags$$')

if __name__ == '__main__':

        # CASOS TEST
    assert cat.speak() == 'Mr Whiskers meows.'
    assert cat1.speak() == 'Lamp meows.'
    assert cat2.speak() == '$$Money Bags$$ meows.'
