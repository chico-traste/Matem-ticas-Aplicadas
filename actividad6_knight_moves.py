# Función de transición para el caballo en un tablero 4x4

def knight_moves(casilla):
    i, j = casilla
    pasos = [(2,1),(1,2),(-1,2),(-2,1),
             (-2,-1),(-1,-2),(1,-2),(2,-1)]
    vecinos = []
    for di, dj in pasos:
        ni, nj = i + di, j + dj
        if 1 <= ni <= 4 and 1 <= nj <= 4:
            vecinos.append((ni, nj))
    return vecinos

# Ejemplo: movimientos posibles desde (2,2)
print("Movimientos desde (2,2):", knight_moves((2,2)))

# Ejemplo: construir lista de adyacencia completa
grafo = {(i,j): knight_moves((i,j)) for i in range(1,5) for j in range(1,5)}
for k,v in grafo.items():
    print(f"{k}: {v}")
