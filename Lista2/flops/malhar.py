qtd = int(input())
treino = input()
passou = 0

while treino != "Fim do Treino":
    counter = 1

    print(treino)
    while counter != qtd + 1:
        musica = input()
        nota = int(input())
        print(f"{counter}° música {musica} tocando agora")
        if nota < 7:
            print("O padre Marcelo está desanimado, não conseguiu finalizar suas séries")
        else:
            print("O padre Marcelo está inspirado, conseguiu finalizar suas séries!")
            passou += 1

        counter += 1

    if passou >= qtd / 2:
        print("ME DEI BEM COM ESSA PLAYLIST, APROVADO")
    else:
        print("NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL")

    counter = 1
    passou = 0
    treino = input()