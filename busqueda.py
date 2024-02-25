# Programa 1: Búsqueda en Arreglo Multidimensional

# Definir la matriz bidimensional
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matrix, valor):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == valor:
                return True, (i, j)
    return False, None

# Solicitar al usuario que ingrese el valor a buscar
valor_buscar = int(input("Ingresa el valor que deseas buscar: "))

# Realizar la búsqueda
encontrado, posicion = buscar_valor(matrix, valor_buscar)

# Mostrar resultados
if encontrado:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
