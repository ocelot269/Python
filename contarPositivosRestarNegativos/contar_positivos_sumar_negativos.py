def count_positives_sum_negatives(arr):
    contador = []
    if arr:
        i = 0
        pos = 0
        sumador = 0
        while i < len(arr):
            if arr[i] > 0:
                pos += 1
            else:
                sumador += arr[i]
            i += 1
        contador.append(pos)
        contador.append(sumador)
    return contador
if __name__ == '__main__':

    assert count_positives_sum_negatives(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
    assert count_positives_sum_negatives(
        [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
    assert count_positives_sum_negatives([1]) == [1, 0]
    assert count_positives_sum_negatives([-1]) == [0, -1]
    assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
    assert count_positives_sum_negatives([]) == []
