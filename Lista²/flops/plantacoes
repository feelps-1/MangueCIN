tamanho = int(input())

matrizInicial = []
caixa = 0

stashSementes = [["Melao", "Rabanete", "Carambola", "Lupulo", "Pimenta", "Trigo"],
                 [250, 90, 750, 25, 40, 25],
                 [12, 6, 13, 11, 5, 4],
                 [0, 0, 0, 0, 0, 0]]

for i in range(tamanho):
    matrizInicial.append(input().split())

acabou = False

while not acabou:
    semente = input()
    if semente == "FIM":
        acabou = True
    else:
        stashSementes[3][stashSementes[0].index(semente)] += 1

preparado = True
campo = matrizInicial

if stashSementes == [0, 0, 0, 0, 0, 0]:
    preparado = False

if preparado:
    for linha in range(len(campo)):
        for coluna in range(len(campo[linha])):
            if campo[linha][coluna] == "1":
                coordAspersor = [linha, coluna]
                for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    coordTerra = [i[k] + coordAspersor[k] for k in range(len(coordAspersor))]
                    if campo[coordTerra[0]][coordTerra[1]] == "*":
                        campo[coordTerra[0]][coordTerra[1]] = "#"
            elif campo[linha][coluna] == "2":
                coordAspersor = [linha, coluna]
                for i in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    coordTerra = [i[k] + coordAspersor[k] for k in range(len(coordAspersor))]
                    if campo[coordTerra[0]][coordTerra[1]] == "*":
                        campo[coordTerra[0]][coordTerra[1]] = "#"
                


else:
    print("Putz parece que não nos preparamos para o Verão. Não vai ser possível tirar um dinheirinho com colheita, mas ainda temos os animais e a pesca!")



for i in campo:
    print(" ".join(i))

print(stashSementes[3])


