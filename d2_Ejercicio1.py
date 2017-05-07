"""
	Una empresa que trabaja con vehiculos desea calcular las necesidades de combustible (cantidad de combustible necesario para llenar los depositos de todos sus vehiculos) para lo cual nos han facilitado este esquema de calculo. Se desea crear un programa para que puedan realizar el calculo de forma automatizada.
"""

carrosTurismo = input('Escribe la cantidad de carros Turismo: ')
carrosTodoTerreno = input('Escribe la cantidad de carros Todoterreno: ')

capTurismos = 40
capTodoTerreno = 65

necesidadesComb = (carrosTurismo * capTurismos) + (carrosTodoTerreno * capTodoTerreno)

print 'La necesidad de combistible es: ', necesidadesComb