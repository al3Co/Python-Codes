"""
Calculo del volumen de un cilindro dados su altura y diametro.
"""

import math

diametro = input('Introduzca el diametro (m): ')
altura = input ('Introduzca la altura (m): ')

print 'El volumen del cilindro es:', math.pi * math.pow(diametro/2,2) * altura
