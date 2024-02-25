# Programa 2: Ordenación de Arreglo Multidimensional

# Definir la matriz bidimensional
matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matrix, fila):
    matrix[fila] = sorted(matrix[fila])

# Mostrar la matriz original
print("Matriz original:")
for row in matrix:
    print(row)

# Ordenar una fila específica (por ejemplo, la primera fila)
ordenar_fila(matrix, 0)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la primera fila ordenada:")
for row in matrix:
    print(row)
