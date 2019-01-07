
def prime(num):
    contador = 0
    while contador < num:
        divisor = 2
        while divisor < num and num % divisor != 0:
            divisor = divisor + 1
        contador = contador + 1
    if num == divisor:
        return True
    else:
        return False


if __name__ == '__main__':
    
    # TEST CASES #

    print(prime(11))