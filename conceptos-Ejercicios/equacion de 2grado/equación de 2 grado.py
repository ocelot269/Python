import math
#resolver caso test; espero un 0#
a=-1
b=0
c=0


def raices_resultado(a, b, c):
	discriminante = b**2 - 4 * a * c

	if a != 0 and discriminante < 0:
		raizPositiva = (- b + math.sqrt(discriminante)) / (2*a)
		return raizPositiva
	return None

raizPositiva = raices_resultado(a, b, c)

#EL nombre del procedimiento tienes que ponerlo como si fuese para alguien que no tiene ni idea
#raices_resultado(a,b,c)
                  # 1 2 3
#if raizPositiva == 0:
	#print("ok")
#else :
	#print(a,b,c + "FAIL")

#Caso text numero 2
