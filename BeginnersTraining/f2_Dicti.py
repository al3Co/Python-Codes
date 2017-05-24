# dictionary (No matter the position)

def dictionary():
    # declarar diccionario
    print
    mi_diccionario = {'clave_1': 10, 'clave_2': 'Texto', 'clave_7': 5.1}
    print mi_diccionario
    print
    
    # consultar y eliminar clave del diccionario
    print mi_diccionario['clave_2']     # Salida: valor_2
    del(mi_diccionario['clave_2'])      # Elimina Clave del diccionario
    print mi_diccionario
    print

    # asignar nuevo valor a clave de diccionario
    mi_diccionario['clave_1'] = 'Nuevo Valor'   # Modificar valor de la clave
    print mi_diccionario
    print
    
    # agregar claves a diccionario
    mi_diccionario['Clave_nueva'] = 22
    mi_diccionario['Clave_nueva 2'] = 'Texto Nuevo'
    print mi_diccionario
    print

    # consultar por elemento
    if 'clave_1' in mi_diccionario: print mi_diccionario['clave_1']
    print
    
    # eliminar diccionario
    del mi_diccionario


if __name__ == "__main__":
    dictionary()
