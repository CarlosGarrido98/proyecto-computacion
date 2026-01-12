'''
Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.

'''


#Funcion 
def calcular_estadisticas(numeros):

    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros)/len(numeros)

    tupla = (minimo,maximo,media)

    return tupla


numeros = [ 1 , 10 , 20  , 2]

resultados = calcular_estadisticas(numeros)
print(resultados)