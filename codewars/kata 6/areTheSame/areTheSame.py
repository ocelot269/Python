def areTheSame(array1, array2):
    # precondicion
    assert len(array1) == len(array2)

    if len(array1) == len(array2):
        return True

    for numero in array1:
        if numero ** 2 in array2:
        	array2.remove(numero ** 2)
            continue
        else:
            return False
    return True


if __name__ == '__main__':

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161,
          19 * 19, 144 * 144, 19 * 19]

    assert areTheSame([], [])
    assert areTheSame()