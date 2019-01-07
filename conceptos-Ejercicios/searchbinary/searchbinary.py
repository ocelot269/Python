def SearchBinary(array):
    izq = 0
    derecha = len(array)-1
    central = (izq + derecha) // 2
    n = 255
    while array[central] != n and izq <= derecha:
        if n > array[central]:
            izq = central + 1
        else:
            derecha = central - 1
        central = (izq + derecha) // 2
    if array[central] == n:
        return("Encontrado")
    else:
        return("no se encuentra dentro de la array")

if __name__ == '__main__':
    
    array = [2, 3, 4, 6, 32, 255, 2445, 65474, 8568585]
    print(SearchBinary(array))
    
