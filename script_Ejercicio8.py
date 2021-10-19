# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:20:56 2021

@author: camil
"""

ing_edad=int(input("Ingrese su edad en número:"))

if ing_edad<=17:
    print(" Su edad corresponde a un menor")
    calc=ing_edad*10
elif ing_edad>18 and ing_edad<=40:
    print("Su edad corresponde a un adulto joven ")
    calc=ing_edad*20
elif ing_edad>40 and ing_edad<=60:
    print("Su edad corresponde a un adulto ")
    calc=ing_edad*30

else:
    print("Su edad corresponde a un adulto mayor")
    calc=ing_edad*40
    
print(f"La edad ingresada fue: {ing_edad}\nEl valor del cálculo es: {calc}")