def capturar(boxes, quantidadePokemons):
    while quantidadePokemons > 0:
        for d in range(len(boxes)):
            for e in range(len(boxes[d])):
                for f in range(len(boxes[d][e])):
                    if quantidadePokemons == 0: break
                    if boxes[d][e][f] == 0:
                        boxes[d][e][f] = 1
                        quantidadePokemons -= 1
        if quantidadePokemons > 0: boxes.append([[0 for x in range(6)] for y in range(5)])


def transferir(boxes, quantidadePokemons):
    for c in range(len(boxes) -1, -1, -1):
            for d in range(len(boxes[c]) - 1, -1, -1):
                for e in range(len(boxes[c][d]) - 1, -1, -1):
                    if quantidadePokemons == 0: break
                    if boxes[c][d][e] == 1:
                        boxes[c][d][e] = 0
                        quantidadePokemons -= 1
            if len(boxes) > 1: boxes.pop()
            if quantidadePokemons == 0: break


def printarPc(boxes):
    for c in range(len(boxes)):
        print(f'BOX {c + 1}:')
        for d in range(len(boxes[c])):
            for e in range(len(boxes[c][d])):
                if e == len(boxes[c][d]) - 1:
                    print(f'{boxes[c][d][e]}', end='')
                else:
                    print(f'{boxes[c][d][e]}', end=' ')
            print()
        print()


pokemonsArmazenados = int(input())
boxes = [[[0 for x in range(6)] for y in range(5)]]
capturar(boxes, pokemonsArmazenados)

while True:
    comando = input()

    if comando == 'Finalizar':
        break

    if comando == 'Capturar':
        quantidadePokemons = int(input())
        pokemonsArmazenados += quantidadePokemons
        capturar(boxes, quantidadePokemons)

    if comando == 'Transferir':
        quantidadePokemons = int(input())

        if quantidadePokemons > pokemonsArmazenados:
            quantidadePokemons = pokemonsArmazenados

        pokemonsArmazenados -= quantidadePokemons
        transferir(boxes, quantidadePokemons)
    
    printarPc(boxes)

print('RELATÓRIO FINAL:\n')
print(f'BOXES: {len(boxes)}')
print(f'POKEMONS: {pokemonsArmazenados}')
