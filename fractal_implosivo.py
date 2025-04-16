data = "ZENITH-ALGORITMO"
capas = [data[:i+1] for i in range(len(data))][::-1]
matriz = [['' for _ in range(len(capas))] for _ in capas]
for i, capa in enumerate(capas):
    for j, char in enumerate(capa):
        matriz[i][j] = char

# Aplicar permutación reversible U y luego U^{-1}
import random
claves = [random.sample(range(len(fila)), len(fila)) for fila in matriz]
permutada = [['' for _ in fila] for fila in matriz]
revertida = [['' for _ in fila] for fila in matriz]
for i, (fila, clave) in enumerate(zip(matriz, claves)):
    for j, idx in enumerate(clave):
        if idx < len(fila):
            permutada[i][j] = fila[idx]
for i, (fila, clave) in enumerate(zip(permutada, claves)):
    for j, idx in enumerate(clave):
        if idx < len(fila):
            revertida[i][idx] = fila[j]

assert revertida == matriz