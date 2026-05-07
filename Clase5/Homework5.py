"""
Ciclo Do-While
Simula un ciclo do while para pedir al usuario que ingrese una contraseña y verifica si es correcta. Debe continuar hasta que se ingrese
la contraseña correcta
"""

print ("  --- CONTRASEÑA ---")

contraseña= "HolaContraseña"

verificacion= input("Ingrese su contraseña\n")
while verificacion != contraseña:
    verificacion= input("Contraseña invalida. Intente nuevamente\n")

print ("Su contraseña es Valida")