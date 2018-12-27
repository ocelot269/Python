def positive_sum(arr):
    suma = 0
    for i in arr:
        if i > 0:
            suma += i
    return suma

if __name__ == '__main__':

    assert positive_sum([1, 2, 3, 4, 5]) == 15
    assert positive_sum([1, -2, 3, 4, 5]) == 13
    assert positive_sum([-1, 2, 3, 4, -5]) == 9
    assert positive_sum([]) == 0
    assert positive_sum([-1, -2, -3, -4, -5]) == 0
