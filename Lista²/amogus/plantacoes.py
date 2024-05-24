info = [
    ['m', 'r', 'c', 'l', 'p', 't'],
    [250, 90, 750, 25, 40, 25],
    [12, 6, 13, 11, 5, 4]
]

colher = ['M', 'R', 'C', 'L', 'P', 'T']

n = int(input())

matriz = []
for c in range(n):
    matriz.append(input().split())


sementes = []
while True:
    semente = input()

    if semente == "FIM":
        break
    
    sementes.append(semente[0].lower())

if sementes == []:
    print("Putz parece que não nos preparamos para o Verão. Não vai ser possível tirar um dinheirinho com colheita, mas ainda temos os animais e a pesca!")
else:
    dia = 1
    contagem = [[0 for c in range(n)] for c in range(n)]
    molhaveis = []
    dinheiros = 0
    dinheiro = 0
    molhados = 0

    for c in range(n):
        for d in range(n):
            if matriz[c][d] == '1':
                maxMolhados = 4
                molhaveis.append([c - 1, d])
                molhaveis.append([c, d - 1])
                molhaveis.append([c, d + 1])
                molhaveis.append([c + 1, d])
            elif matriz[c][d] == '2':
                maxMolhados = 8
                molhaveis.append([c - 1, d - 1])
                molhaveis.append([c - 1, d])
                molhaveis.append([c - 1, d + 1])
                molhaveis.append([c, d - 1])
                molhaveis.append([c, d + 1])
                molhaveis.append([c + 1, d - 1])
                molhaveis.append([c + 1, d])
                molhaveis.append([c + 1, d + 1])


    while dia <= 28:
        dinheiros += dinheiro
        dinheiro = 0

        for c in range(len(molhaveis)):
            if matriz[molhaveis[c][0]][molhaveis[c][1]] == '#':
                molhados += 1
        
        if molhados >= maxMolhados:
            print(f'Eita, parece que não sobrou mais sementes, vamos encerrar a plantação do verão por aqui com {dinheiros} ouros.')
            break

        molhados = 0

        print(f'Dia {dia}:')

        if dia == 1:
            for c in range(n):
                for d in range(n):
                    if ([c, d] in molhaveis):
                        matriz[c][d] = '#'

                    if d == n - 1:
                        print(matriz[c][d], end='')
                    else:
                        print(matriz[c][d], end=' ')
                            
                    if d == n - 1:
                        print('')
            print('')

        for c in range(n):
            for d in range(n):
                if ([c, d] in molhaveis):
                    if (matriz[c][d] in info[0]):
                        if contagem[c][d] == info[2][info[0].index(matriz[c][d])]:
                            matriz[c][d] = matriz[c][d].upper()
                            dinheiro += info[1][colher.index(matriz[c][d])]
                            if sementes == []:
                                molhados += 1

                        contagem[c][d] += 1
                    elif matriz[c][d] in colher:
                        if sementes != []:
                            matriz[c][d] = sementes.pop(0)
                            contagem[c][d] = 2
                        else:
                            matriz[c][d] = '#'
                    elif matriz[c][d] == '#':
                        if sementes != []:
                            matriz[c][d] = sementes.pop(0)
                        contagem[c][d] = 1

                if d == n - 1:
                    print(matriz[c][d], end='')
                else:
                    print(matriz[c][d], end=' ')

                if d == n - 1:
                    print('')

        if dia != 1: print(f'Caixa: {dinheiros} ouros')

        if dinheiro != 0:
            print(f'Dia de colheita! Conseguimos {dinheiro} ouros hoje!')
        
        dia += 1

    if molhados < maxMolhados:
        print('Chegamos ao fim de mais um Verão!! Vamos ver quanto ouro conseguimos')
        print(f'{dinheiros} Ouros')
