# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:46:43 2021

@author: camil
"""

print("Primera Interacción, ingrese un valor cualquiera:")

variable1= input()

try:
    variable_str=int((variable1))
    print("Usted ingreso un tipo de dato entero")
  
except Exception:
    
    try:
    
        variable_str=float(variable1)
        print("Usted ingreso un tipo de dato flotante")
    
    except Exception:
        
        try:
    
            variable_str=complex(variable1)
            print("Usted ingreso un tipo de dato complejo")
    
        except Exception:

            try:
        
                variable_str=str(variable1)
                print("Usted ingreso un tipo de dato string")
        
            except Exception:
                print("ya no hay mas tipos")
                

print("Segunda Interacción, ingrese un valor cualquiera:")

variable1= input()

try:
    variable_str=int((variable1))
    print("Usted ingreso un tipo de dato entero")
  
except Exception:
    
    try:
    
        variable_str=float(variable1)
        print("Usted ingreso un tipo de dato flotante")
    
    except Exception:
        
        try:
    
            variable_str=complex(variable1)
            print("Usted ingreso un tipo de dato complejo")
    
        except Exception:

            try:
        
                variable_str=str(variable1)
                print("Usted ingreso un tipo de dato string")
        
            except Exception:
                print("ya no hay mas tipos")
                
                                
print("Tercera Interacción, ingrese un valor cualquiera:")

variable1= input()

try:
    variable_str=int((variable1))
    print("Usted ingreso un tipo de dato entero")
  
except Exception:
    
    try:
    
        variable_str=float(variable1)
        print("Usted ingreso un tipo de dato flotante")
    
    except Exception:
        
        try:
    
            variable_str=complex(variable1)
            print("Usted ingreso un tipo de dato complejo")
    
        except Exception:

            try:
        
                variable_str=str(variable1)
                print("Usted ingreso un tipo de dato string")
        
            except Exception:
                print("ya no hay mas tipos")
                
                
print("Cuarta Interacción, ingrese un valor cualquiera:")

variable1= input()

try:
    variable_str=int((variable1))
    print("Usted ingreso un tipo de dato entero")
  
except Exception:
    
    try:
    
        variable_str=float(variable1)
        print("Usted ingreso un tipo de dato flotante")
    
    except Exception:
        
        try:
    
            variable_str=complex(variable1)
            print("Usted ingreso un tipo de dato complejo")
    
        except Exception:

            try:
        
                variable_str=str(variable1)
                print("Usted ingreso un tipo de dato string")
        
            except Exception:
                print("ya no hay mas tipos")
                
                
print("Quinta Interacción, ingrese un valor cualquiera:")

variable1= input()

try:
    variable_str=int((variable1))
    print("Usted ingreso un tipo de dato entero")

except Exception:
    
    try:
    
        variable_str=float(variable1)
        print("Usted ingreso un tipo de dato flotante")
    
    except Exception:
        
        try:
    
            variable_str=complex(variable1)
            print("Usted ingreso un tipo de dato complejo")
    
        except Exception:

            try:
        
                variable_str=str(variable1)
                print("Usted ingreso un tipo de dato string")
        
            except Exception:
                print("ya no hay mas tipos")

print("¡YA NO SE HARÁN MÁS INTERACCIONES!")