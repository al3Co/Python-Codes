
numero = input('Escribe un numero: ')

print numero


if numero  == 10:
	print 'El numero es igual a 10'
elif numero > 10:
	print 'El numero es mayor a 10'
elif numero < 10:
	print 'El numero es menor a 10'

for vez in range (1,5):
	print 'Suma: ', numero + vez
