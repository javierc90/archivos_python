# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv

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

def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    with open('alturas.csv') as csvfile:
        # Leer todos los datos y almacenarlos en una 
        # lista de diccionarios
        personas = list(csv.DictReader(csvfile))
    
    cantidad = 0
    altura_acumulada = 0
    for persona in personas:
        if persona['genero'] == genero:
            cantidad += 1
            altura_acumulada += float(persona['altura'])
    promedio = altura_acumulada / cantidad
    print(f"Hay {cantidad} personas de genero {genero} con promedio: {promedio}")


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
