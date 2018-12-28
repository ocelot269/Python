def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == '__main__':
    assert even_or_odd(2) == "Even"
    assert even_or_odd(0) == "Even"
    assert even_or_odd(7) == "Odd"
    assert even_or_odd(1) == "Odd"
