# aritmetics
# tuplas - listas / array - vectors

def aritmetics():
    a = 10 + 5  # suma
    a = 12 - 7  # resta
    a = -5      # negacion
    a = 7 * 5   # multiplic
    a = 2 ** 3  # exponente
    a = 12.5 / 2    # Div. (flotantes)
    a = 27 % 4  # modulo

def tuplasListas():
    print   # Generar un espacio en la consola
    mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
    print mi_lista
    print len(mi_lista)
    print   # Generar un espacio en la consola
    
    print mi_lista[1]       # Salida: 15
    print mi_lista[1:4]     # Devuelve: [15, 2.8, 'otro dato']
    print mi_lista[-2]      # Salida: otro dato
    print
    
    mi_lista.append('Nuevo Dato1')   # Agregar un dato a la lista
    print mi_lista
    mi_lista.append('Nuevo Dato2')   # Agregar un dato a la lista
    print mi_lista
    print
    
    mi_lista.remove('Nuevo Dato2')  # Eliminar un dato de la lista
    print mi_lista

    if 'hola' in mi_lista: mi_lista.remove('hola')  #Si el dato esta en la lista: Eliminar dato
    if 'Nuevo Dato1' in mi_lista: mi_lista.remove('Nuevo Dato1')
    print mi_lista
    
    numero = 15
    if numero in mi_lista: mi_lista.remove(numero)
    print mi_lista
    print

    numero = 2.8
    if numero in mi_lista: mi_lista.append('Si existe')
    print mi_lista

    mi_lista[:] = []
    print (mi_lista)
    print len(mi_lista)


if __name__ == "__main__":
    tuplasListas()
