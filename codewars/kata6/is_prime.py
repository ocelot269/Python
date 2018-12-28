def is_prime(num):
    contador = 2
    while contador < num:
        if num % contador == 0:
            return False
        contador += 1
    if num == contador:
        return True
    return False

if __name__ == '__main__':

    assert is_prime(0) == False, '0 is not prime'
    assert is_prime(1) == False, '1 is not prime'
    assert is_prime(2) == True, '2 is prime'
