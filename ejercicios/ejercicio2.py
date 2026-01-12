'''
Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula
'''
import math

def distancia(p1,p2):
   # p1 = (x1, y1), p2 = (x2, y2)
    dx = p2[0] - p1[0]  # diferencia en x
    dy = p2[1] - p1[1]  # diferencia en y

    return math.sqrt(dx**2 + dy**2)  # fórmula de distancia



tuplax = (1,2)
tuplay = (3,4)

print("La distancia es:", distancia(tuplax, tuplay))