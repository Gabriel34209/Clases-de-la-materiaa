# Crea una matriz tridimencional 3x3

matriz = [
    [5, 2, 9],
    [3, 7, 1],
    [8, 4, 6]
]

# Funciona para ordenar una fila de manera ascendente utilizando Bubble sort

def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Funcion para mostrar la matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
