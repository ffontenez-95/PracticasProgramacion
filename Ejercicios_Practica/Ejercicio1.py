"""1. Clasificación de nota 
Situación: Ingresar una nota del 0 al 10 y mostrar si 
el estudiante está: 
● Desaprobado (0 a 5) 
● Aprobado (6 a 8) 
● Sobresaliente (9 o 10) 
"""


nota=int(input("Ingrese una nota del 0 al 10\n"))

if nota >=0 and nota<=5:
    print (f"El Estudiante esta desaprobado con {nota}")

elif nota>=6 and nota <=8:
    print (f"El estudiante esta aprobado con {nota}")

elif nota>=9 and nota<=10:
    print (f"Sobresaliente con {nota}")

else: 
    print ("Ingrese una nota valida")