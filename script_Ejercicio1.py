# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:15:32 2021

@author: camil
"""

# Aqui se imprime una cadena
print("Empezando a trabajar con Python")

# aqui se imprime mi nombre
print ("Realizado por: Camilo Auz")

# Aqui se imprime una cadena
print ("Consultando los tipos de valores:")

# Aqui se imprime el tipo de dato correspondiente
print("El tipo de dato de 875 es:", type(875))
print("El tipo de dato de 4.89 es:", type(4.89))
print("El tipo de dato del texto: Now is better than never. es:", type('Now is better than never'))
print("El tipo de dato de 1.32 es:", type(1.32))


# Aqui se imprime si la respuesta es verdadera o falsa con respecto al tipo de dato
print("¿El valor 5 + 8i corresponde a un valor entero?", isinstance(5 + 8j, int))
print("¿El valor 8.2 corresponde a un valor entero?", isinstance (8.2, int))
print("¿El texto: Readability counts. corresponde a un string?", isinstance ("Readability counts", str))