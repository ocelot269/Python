def es_bubble_sort(array):
    intercambio = True
    while intercambio:
        intercambio = False
        pos = 0
        while pos < len(array) -1:
            if array[pos] > array[pos + 1]:
                aux = array[pos]
                array[pos] = array[pos + 1]
                array[pos + 1] = aux
                intercambio = True
            pos = pos + 1
    return array

if __name__ == '__main__':

    array = [5, 3, 8, 17, 2, 300, 145, 270]
    print(es_bubble_sort(array))
