"""
Menú de opciones (condicional múltiple) 
Situación: El programa debe simular un menú bancario 
simple. 
Mostrar el siguiente menú al usuario: 
1. Ver saldo   
2. Realizar transferencia   
3. Salir 
El usuario debe ingresar un número del 1 al 3 según la opción 
que quiera. El programa mostrará un mensaje correspondiente: 
● Si elige 1 → mostrar "Su saldo es $15.000" 
● Si elige 2 → mostrar "Transferencia realizada con éxito" 
● Si elige 3 → mostrar "Saliendo del sistema..." 
● Si elige otro número → mostrar "Opción inválida" 
"""

print("TU BANCO DE CONFIANZA")


print ("1 = Ver Saldo")
print ("2= Realizar transferencia")
print ("3= Salir")
opc=int(input("Ingrese la opcion que desea realizar\n"))

if opc == 1:
    print ("Su saldo es de $15.000")

elif opc ==2:
    print ("Transferencia realizada con éxito")

elif opc ==3:
    print ("Saliendo del sistema...")

else:
    print ("Opcion Invalida")
