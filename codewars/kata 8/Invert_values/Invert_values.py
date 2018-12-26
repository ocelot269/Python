def invertValor(lista):
    invert = []
    for numero in lista:
        invert.append(-numero)
    return(invert)


if __name__ == '__main__':

    assert invertValor([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
    assert invertValor([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
    assert invertValor([]) == []
