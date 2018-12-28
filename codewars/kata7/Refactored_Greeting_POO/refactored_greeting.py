class Person():

    def __init__(self, name):
        self.name = name

    def greet(self, friends_name):
        return "Hello %s, my name is %s" % (friends_name, self.name)


if __name__ == '__main__':

    jack = Person("Jack")
    jill = Person("Jill")

    assert jack.greet("Jill") == "Hello Jill, my name is Jack"
    assert jack.greet("Mary") == "Hello Mary, my name is Jack"
    assert jill.greet("Jack") == "Hello Jack, my name is Jill"
