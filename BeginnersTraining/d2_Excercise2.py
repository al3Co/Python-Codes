"""
Calculo del volumen de un cilindro dados su altura y diametro.
"""

import math

diametro = float(raw_input('Introduzca el diametro (m): '))
altura = float(raw_input ('Introduzca la altura (m): '))

print 'El volumen del cilindro es:', math.pi * math.pow(diametro/2,2) * altura
