def russian_peasant_multiplication(x, y):
    i = 0
    contador = 0
    while i < y:
        contador += x
        i += 1
    return contador


if __name__ == '__main__':

    assert russian_peasant_multiplication(10, 5) == 50
    assert russian_peasant_multiplication(1.001, 2) == 2.002
