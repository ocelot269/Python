def multimatrices(a, b):
	filasA = 0
	AB = []
	while filasA < len(a):
		columna = 0
		AB.append([])
		while columna < len(b[0]):
			pos = 0
			resultado = 0
			while pos < len(b):
				resultado = a[filasA][pos] * b[pos][columna]
				pos = pos + 1
			AB[filasA].append(resultado)
			columna = columna + 1
		filasA = filasA + 1
	return AB
if __name__ == '__main__':

    ### CASOS TEST ###

    a = [[1, 6, 7],
         [5, 8, 9],
         [6, 7, 9]]

    #   multiplicar por   #

    b = [[1, 6, 7, 5, 3],
         [6, 3, 7, 2, 1],
         [7, 3, 1, 6, 7]]

    print(multimatrices(a, b))
