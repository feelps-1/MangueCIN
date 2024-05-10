quantidadeExercicios = int(input())
tipoTreino = input()

while tipoTreino != 'Fim do Treino':
    aprovadas = quantidadeExercicios
    print(tipoTreino)

    for c in range (1, quantidadeExercicios + 1):
        nomeMusica = input()
        nota = int(input())
        print(f'{c}° música {nomeMusica} tocando agora')

        if nota < 7:
            print('O padre Marcelo está desanimado, não conseguiu finalizar suas séries')
            aprovadas -= 1
        else:
            print('O padre Marcelo está inspirado, conseguiu finalizar suas séries!')

    if aprovadas >= quantidadeExercicios / 2:
        print('ME DEI BEM COM ESSA PLAYLIST, APROVADO')
    else:
        print('NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL')

    tipoTreino = input()
