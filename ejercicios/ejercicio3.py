''' Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.
'''

def analizar_texto(texto):



    numeroCaracteres = len(texto)


    palabras = texto.split()
    numeroPalabras = len(palabras)

    primeraPalabra = palabras[0]

    
    
    tupla = (numeroCaracteres , numeroPalabras , primeraPalabra)
    
    return tupla



texto = "Anoche vi una estrella fugaz"
resultado = analizar_texto(texto)
print(resultado)