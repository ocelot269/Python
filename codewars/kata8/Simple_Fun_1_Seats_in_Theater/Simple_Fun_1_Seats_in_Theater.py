def seats_in_theater(total_colum, total_filas, colum, filas):
    return (total_colum - (colum - 1)) * (total_filas - filas)


if __name__ == '__main__':
    assert seats_in_theater(16, 11, 5, 3) == 96
    assert seats_in_theater(1, 1, 1, 1) == 0
    assert seats_in_theater(13, 6, 8, 3) == 18
    assert seats_in_theater(60, 100, 60, 1) == 99
    assert seats_in_theater(1000, 1000, 1000, 1000) == 0
