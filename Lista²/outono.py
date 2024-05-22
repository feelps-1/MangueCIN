tamanhos = [int(x) for x in input().split(" x ")]
linhas = tamanhos[0]
colunas = tamanhos[1]

quantidade = int(input())

matriz = []

for i in range(linhas):
    linha = []
    for x in range(colunas):
        linha.append(0)

    matriz.append(linha)

for i in range(quantidade):
    coord = [i for i in input().split()]
    item = coord[0]
    coordenadas = coord[1].strip("()").split(",")

    matriz[int(coordenadas[0])][int(coordenadas[1])] = item

acabou = False

while not acabou:
    operacao = input()

    if operacao == "Permutar":
        coordP = [j for j in input().strip("()").split()]
        coord1 = coordP[0].strip("()").split(",")
        coord2 = coordP[1].strip("()").split(",")

        obj1 = matriz[int(coord1[0])][int(coord1[1])]
        obj2 = matriz[int(coord2[0])][int(coord2[1])]

        matriz[int(coord2[0])][int(coord2[1])] = obj1
        matriz[int(coord1[0])][int(coord1[1])] = obj2
    elif operacao == "Transposição":
        #pipo
    elif operacao == "Remover":
        #pipo
    elif operacao == "Fim":
        acabou = True

print(matriz)


