def basic_operator(operator, a, b):
    if operator == "+":
        return a + b

    if operator == "-":
        return a - b

    if operator == "*":
        return a * b

    if operator == "/":
        return a / b
    else:
        print("Introduce un operador válido")

if __name__ == '__main__':

    assert basic_operator('+', 4, 7) == 11
    assert basic_operator('-', 15, 18) == -3
    assert basic_operator('*', 5, 5) == 25
    assert basic_operator('/', 49, 7) == 7
