dimensao = input()
linhas, colunas = dimensao.split(' x ')

matriz = [[0 for c in range(int(colunas))] for c in range(int(linhas))]

quantidadeElementos = int(input())

for c in range(quantidadeElementos):
    elemento = input().split()
    nivelAtratividade = int(elemento[0])
    y, x = elemento[1][1:-1].split(',')
    matriz[int(y)][int(x)] = nivelAtratividade

while True:
    operacao = input()
    if operacao == "Fim":
        break
    elif operacao == "Permutar":
        coords = input().split()
        i1, j1 = coords[0][1:-1].split(',')
        i2, j2 = coords[1][1:-1].split(',')
        matriz[int(i1)][int(j1)], matriz[int(i2)][int(j2)] = matriz[int(i2)][int(j2)], matriz[int(i1)][int(j1)]
    elif operacao == "Transposição":
        matriz = [[matriz[x][y] for x in range(int(linhas))] for y in range(int(colunas))]
        linhas, colunas = colunas, linhas
    elif operacao == "Remover":
        minVal = float('inf')
        minPos = (-1, -1)
        for y in range(int(linhas)):
            for x in range(int(colunas)):
                if matriz[y][x] != 0 and matriz[y][x] < minVal:
                    minVal = matriz[y][x]
                    minPos = (y, x)
        if minPos != (-1, -1):
            matriz[minPos[0]][minPos[1]] = 0

print("Atual Arranjo:")
for y in range(int(linhas)):
    for c in range(len(matriz[y])):
        matriz[y][c] = str(matriz[y][c])
    print(" ".join(matriz[y]))
