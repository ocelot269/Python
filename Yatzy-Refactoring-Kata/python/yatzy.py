class Yatzy:

    @staticmethod
    def chance(* args):
                            #La suma de todos los dados
        assert type(args) == tuple

        acumulador = 0

        for dado in args:
            acumulador += dado

        assert type(acumulador) == int

        return acumulador

    @staticmethod
    def yatzy(*dice):
                    #Devuelve 50 puntos si un numero se repite 5 veces sino devuelve 0
        return 50 if dice.count(dice[0]) == 5 else 0

    @staticmethod
    def ones(* dice):
                        #Contamos los 1 los multiplicamos por 1
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(* dice):

        TWO = 2         ##Contamos los 2 los multiplicamos por 2
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(*dice):
                        #Contamos los 3 los multiplicamos por 3
        THREE = 3

        return dice.count(THREE) * THREE

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def fours(*dice):
        FOUR = 4 #Contamos los 4 los multiplicamos por 4
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = 5 #Contamos los 5 los multiplicamos por 5
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = 6 #Contamos los 6 los multiplicamos por 6
        return dice.count(SIX) * SIX

    @staticmethod
    def pairs(*dice):

        acumulador = 0
        maximum = 0

        for die in dice:
            if dice.count(die) == 2:
                if die > maximum:
                    maximum = die

        return maximum * 2

    @staticmethod
    def two_pair(*dice):
        numeroParejas = 0
        acumulador = 0
        for die in dice:
            if dice.count(die) == 2:
                numeroParejas += 1
                acumulador += die

        if numeroParejas == 4:
            return acumulador

        else:
            return 0

    @staticmethod
    def four_of_a_kind(*args):
        for dado in range(1, 7):# Si 4 numeros se repiten o mas,ese mismo numero * 4
            if args.count(dado) >= 4:
                return dado * 4
        return 0

    @staticmethod
    def three_of_a_kind(*args):
        for dado in range(1, 7): # Si 3 numeros se repiten o mas,ese mismo numero * 3
            if args.count(dado) >= 3:
                return dado * 3
        return 0

    @staticmethod
    def smallStraight(*args):
        for dado in range(1, 7): #una escalera del 1 al 5
            if len(set(args)) == 5 and dado < 6:
                return 15
        return 0

    @staticmethod
    def largeStraight(*args):
        for dado in range(1, 7): #una escalera del 2 al 6
            if dado > 1 and len(set(args)) == 5:
                return 20
        return 0

    @staticmethod
    def fullHouse(*args):
        full = [] #Un trio + una pareja
        for dado in args:
            if len(set(args)) == 2:
                return 18
        return 0


if __name__ == '__main__':

    # cada dado

    d1 = 1
    d2 = 2
    d3 = 3
    d4 = 4
    d5 = 5
    d6 = 6

    # casos test de chance

    assert Yatzy.chance(d1, d2, d3, d4, d5) == 15
    assert Yatzy.chance(d2, d2, d2, d2, d2) == 10
    assert Yatzy.chance(d2, d3, d5, d2) == 12

    # casos test de ones

    assert Yatzy.ones(d1, d5, d2) == 1
    assert Yatzy.ones(d2, d1, d3, d3, d2) == 1
    assert Yatzy.ones(d2, d4, d4, d2) == 0
    assert Yatzy.ones(d1, d1, d1, d1) == 4

    # casos test twos

    assert Yatzy.twos(d1, d5, d2) == 2
    assert Yatzy.twos(d2, d1, d3, d3, d2) == 4
    assert Yatzy.twos(d5, d4, d4, d1) == 0
    assert Yatzy.twos(d2, d2, d2, d2) == 8

    # casos test de three

    assert Yatzy.threes(d1, d5, d2, d3, d5) == 3
    assert Yatzy.threes(d2, d1, d3, d3, d2) == 6
    assert Yatzy.threes(d3, d3, d4, d3) == 9
    assert Yatzy.threes(d3, d3, d3, d3) == 12

    # casos test de fours

    assert Yatzy.fours(d1, d5, d2, d3, d5) == 0
    assert Yatzy.fours(d2, d1, d4, d3, d4) == 8
    assert Yatzy.fours(d3, d3, d4, d3) == 4
    assert Yatzy.fours(d4, d4, d4, d4) == 16

    # casos test de fives

    assert Yatzy.fives(d1, d5, d2, d3, d5) == 10
    assert Yatzy.fives(d2, d1, d4, d3, d4) == 0
    assert Yatzy.fives(d3, d5, d5, d5) == 15
    assert Yatzy.fives(d5, d5, d5, d5) == 20

    # casos test de six

    assert Yatzy.sixes(d1, d5, d2, d3, d5) == 0
    assert Yatzy.sixes(d2, d1, d6, d3, d6) == 12
    assert Yatzy.sixes(d3, d3, d6, d3) == 6
    assert Yatzy.sixes(d6, d6, d6, d6) == 24

    # yatzy

    assert Yatzy.yatzy(d1, d1, d1, d1, d1) == 50
    assert Yatzy.yatzy(d1, d2, d3, d4, d5) == 0

    # pairs

    assert Yatzy.pairs(d1, d1, d4, d4, d5) == 8
    assert Yatzy.pairs(d1, d2, d3, d4, d6) == 0
    assert Yatzy.pairs(d3, d2, d5, d3, d4) == 6
    assert Yatzy.pairs(d5, d5, d3, d6, d6) == 12

    # two_pairs

    assert Yatzy.two_pair(d1, d1, d4, d4, d5) == 10
    assert Yatzy.two_pair(d1, d2, d3, d4, d6) == 0
    assert Yatzy.two_pair(d3, d2, d5, d3, d4) == 0
    assert Yatzy.two_pair(d5, d5, d3, d6, d6) == 22

    # def test_four_of_a_knd():
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yatzy.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yatzy.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yatzy.four_of_a_kind(3, 3, 3, 2, 1)
    assert 16 == Yatzy.four_of_a_kind(4, 4, 4, 4, 1)

    # def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yatzy.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 5)

    # def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)

    # def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)

    # def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
