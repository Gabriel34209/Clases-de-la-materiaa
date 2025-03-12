# Crea una matriz tridimencional 3x3

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 8

for fila in range (len(matriz)):
    for columna in range (len(matriz[fila])):
        if matriz[fila][columna] == valor_a_buscar:
            print(f"Encuentra la posición ({fila}, {columna})")
            break
    else:
        continue # continua al siguinte
    break
else:
    print("valor no encontrado")