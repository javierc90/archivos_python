# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---

    with open('alturas.csv') as csvfile:
        # Leer todos los datos y almacenarlos en una 
        # lista de diccionarios
        personas = list(csv.DictReader(csvfile))

    altura_total = 0
    cantidad_genero = 0

    for i in range(len(personas)):
        if personas[i]['genero'] == genero:
            cantidad_genero += 1
            altura_total += float(personas[i]['altura'])
    
    promedio_altura = 0

    if cantidad_genero > 0:
        promedio_altura = altura_total / cantidad_genero

    print(f"Altura promedio del genero {genero}: {promedio_altura}")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("masculino")
