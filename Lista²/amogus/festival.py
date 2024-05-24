dimensao = input()
linhas, colunas = map(int, dimensao.split(' x '))

matriz = [[0 for c in range(colunas)] for c in range(linhas)]

quantidadeElementos = int(input())

for c in range(quantidadeElementos):
    elemento = input().split()
    nivelAtratividade = int(elemento[0])
    y, x = map(int, elemento[1][1:-1].split(','))
    matriz[y][x] = nivelAtratividade

while True:
    operacao = input()
    if operacao == "Fim":
        break
    elif operacao == "Permutar":
        coords = input().split()
        i1, j1 = map(int, coords[0][1:-1].split(','))
        i2, j2 = map(int, coords[1][1:-1].split(','))
        matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]
    elif operacao == "Transposição":
        matriz = [[matriz[x][y] for x in range(linhas)] for y in range(colunas)]
        linhas, colunas = colunas, linhas
    elif operacao == "Remover":
        minVal = float('inf')
        minPos = (-1, -1)
        for y in range(linhas):
            for x in range(colunas):
                if matriz[y][x] != 0 and matriz[y][x] < minVal:
                    minVal = matriz[y][x]
                    minPos = (y, x)
        if minPos != (-1, -1):
            matriz[minPos[0]][minPos[1]] = 0

print("Atual Arranjo:")
for y in range(linhas):
    print(" ".join(map(str, matriz[y])))
