"""
Crear una función que pida el ingreso de edades de personas, al finalizar mostrar el promedio de edades de las personas mayores
y el promedio de edades de los menores de edad. 
El corte del ciclo será la edad 0 (cero).
"""

def promedio_edades():
    """
    Funcion que calcula los promedio de edades dependiendo de si son mayores o menores de edad
    Para cerrar el ciclo el usuario debe apretar 0
    """
    personas_mayores=0
    personas_menores=0
    contador_mayores=0
    contador_menores=0
    while True:
        edad=int(input("Inserte una edad\n"))
        if edad ==0:
            break
        if edad<18:
            personas_menores+=edad
            contador_menores= contador_menores+1

        elif edad>=18:
            personas_mayores+=edad
            contador_mayores = contador_mayores+ 1

    promedio_mayores= personas_mayores/contador_mayores
    promedio_menores= personas_menores/contador_menores
    print(f"El promedio de las edades que son mayores de edad es de {promedio_mayores} y el promedio de las personas menores es de {promedio_menores}")


promedio_edades()