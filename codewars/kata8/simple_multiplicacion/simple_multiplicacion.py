def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    elif number % 2 != 0:
        return number * 9

if __name__ == '__main__':

    assert simple_multiplication(2) == 16
    assert simple_multiplication(1) == 9
    assert simple_multiplication(8) == 64
    assert simple_multiplication(4) == 32
    assert simple_multiplication(5) == 45
