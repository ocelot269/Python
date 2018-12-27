def twice_as_old(da, ha):
    indice = 0
    padre = da
    hijo = ha
    if padre > 2 * hijo:
        while (padre + indice) > (hijo + indice) * 2:
            indice += 1
        return indice
    else:
        while (padre + indice) < (hijo + indice) * 2:
            indice -= 1
        return (indice * -1)
if __name__ == '__main__':

    assert twice_as_old(36, 7) == 22
    assert twice_as_old(55, 30) == 5
    assert twice_as_old(42, 21) == 0
    assert twice_as_old(22, 1) == 20
    assert twice_as_old(29, 0) == 29
