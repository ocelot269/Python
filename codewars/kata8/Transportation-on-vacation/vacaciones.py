def rental_car_cost(dias):
    if dias < 3:
        return dias * 40
    elif dias < 7:
        return dias * 40 - 20
    else:
        return dias * 40 - 50

if __name__ == '__main__':

    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270
