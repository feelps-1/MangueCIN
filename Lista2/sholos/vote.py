candidato1 = input()
candidato2 = input()
votos1 = 0
votos2 = 0
delegados1 = 0
delegados2 = 0

if candidato1 != 'Kanye West' and candidato2 != 'Kanye West':
    print('Sem o Ye, sem eleição!')
else:
    while True:
        estado = input()

        if estado == 'FIM':
            break
        else:
            estado, numDelegados = estado.split(', ')

        voto1 = input()

        if voto1 != 'Taylor Swift roubou as urnas!':
            voto2 = input()

        while voto1 == 'Taylor Swift roubou as urnas!' or voto2 == 'Taylor Swift roubou as urnas!':
            print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')

            voto1 = input()

            if voto1 == 'Taylor Swift roubou as urnas!':
                continue

            voto2 = input()

        voto1 = int(voto1)
        voto2 = int(voto2)

        if voto1 > voto2:
            print(f'{candidato1} obteve maioria no(a) {estado} com {int(voto1 / (voto1 + voto2) * 100)}% dos votos.')
            delegados1 += int(numDelegados)
            votos1 += voto1
        else:
            print(f'{candidato2} obteve maioria no(a) {estado} com {int(voto2 / (voto1 + voto2) * 100)}% dos votos.')
            delegados2 += int(numDelegados)
            votos2 += voto2

    if votos1 > votos2:
        print(f'Temos o resultado final! {candidato1} vence a disputa pela presidência, com o apoio de {delegados1} delegados do colégio eleitoral e {votos1} votos populares.')
        if candidato1 == 'Kanye West':
            print('"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know."')
        else:
            print('"Não tem problema, eu obtive o molho!"')
    else:
        print(f'Temos o resultado final! {candidato2} vence a disputa pela presidência, com o apoio de {delegados2} delegados do colégio eleitoral e {votos2} votos populares.')
        if candidato2 == 'Kanye West':
            print('"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know."')
        else:
            print('"Não tem problema, eu obtive o molho!"')
