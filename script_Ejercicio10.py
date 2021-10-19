# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:54:56 2021

@author: camil
"""

num_pst=int(input("Escriba un número positivo: "))

while num_pst<0:
    print("El númer ingresado es negativo, ingrese nuevamente")
    num_pst=int(input("Escriba un número positivo: "))
    
print("El valor ingresado es correcto")