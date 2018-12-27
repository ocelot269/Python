def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / ((blue_start + red_start) - (red_pulled + blue_pulled))


if __name__ == '__main__':
    assert guess_blue(5, 5, 2, 3) == 0.6
    assert guess_blue(5, 7, 4, 3) == 0.2
    assert guess_blue(12, 18, 4, 6) == 0.4
