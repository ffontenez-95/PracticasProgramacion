"""
1. Operadores Relacionales
Consigna: Crea un programa que compare dos números ingresados por el usuario y determine si el primero es mayor que el segundo.
"""
#Pedimos los datos
num_a=int(input("Ingrese el valor del numero A: "))
num_b=int(input("Ingrese el valor del numero B: "))

if num_a > num_b: 
    print("El numero A es mayor que el B")
elif num_b> num_a:
    print("El numero B es mayor que el numero A")
    
else: print("Los numeros son iguales")