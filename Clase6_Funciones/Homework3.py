"""
Ejercicio N°3 - Procedimiento
Crear una función que realice la suma, resta, división y multiplicación de dos números y lo imprima con el nombre de cada operación. 
a) Si el usuario introduce 1, que sume dos números. 
b) Si el usuario introduce 2, reste dos números. 
c) Si el usuario introduce 3, multiplique dos números 
d) Si el usuario introduce 4, divida dos números.
"""

def Calculadora(num1,num2):
    """
    Funcion que solicita a un usuario que seleccione una opcion y dependiendo de la misma
    se realiza una operacion
    """
    opcion= int(input("Seleccione 1, para sumar dos numeros. 2 para restar dos numeros, 3 para multiplicarlos y 4 para dividirlos\n"))

    if opcion ==1:
        print(f"SUMA: es igual a {num1 + num2}")
    
    elif opcion ==2:
        print(f"RESTA: es igual a {num1 - num2}")

    elif opcion ==3:
        print(f"MULTIPLICACION: es igual a {num1 * num2}")

    elif opcion ==4:
        print(f"DIVISION: es igual a {num1 / num2}")
    
    else:
        print("La opcion ingresada no es correcta")


Calculadora(25,5)
