def isShiny(nome, pokemon, passos, tempo):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    novoNome = ''

    for x in nome:
        index = (alfabeto.index(x.upper()) + 4) % 26 - 1
        novoNome += alfabeto[index]

    idNome = str(sum([ord(x.lower()) for x in novoNome]))

    novoPokemon = ''

    for x in pokemon:
        index = (alfabeto.index(x.upper()) + passos + 1) % 26 - 1
        novoPokemon += alfabeto[index]

    idPokemon = str(sum([ord(x.lower()) for x in novoPokemon]) * tempo)
    if idNome[-1] == idPokemon[-1]:
        return True
    
    return False

nParticipantes = int(input())
dados = [[], [], []]

for c in range(nParticipantes):
    apresentacao = input()
    dados[0].append(apresentacao.split('Olá, meu nome é ')[1].split(', meu pokémon preferido é')[0])
    dados[1].append(apresentacao.split(', meu pokémon preferido é ')[1].split(' e tenho ')[0])
    dados[2].append(int(apresentacao.split(' e tenho ')[1].split(' pokébolas')[0]))

shinies = [[] for x in range(nParticipantes)]
shiny = False
while not shiny:
    encontro = input()
    pokemon = encontro.split('Um ')[1].split(' selvagem apareceu! Foram ')[0]
    tempo = int(encontro.split(' selvagem apareceu! Foram ')[1].split(' segundos e ')[0])
    passos = int(encontro.split(' segundos e ')[1].split(' passos desde o último encontro de ')[0])
    nome = encontro.split(' passos desde o último encontro de ')[1]

    if isShiny(nome, pokemon, passos, tempo):
        if dados[2][dados[0].index(nome)] == 1 and pokemon == dados[1][dados[0].index(nome)]:
            shinies[dados[0].index(nome)].append(pokemon)
            dados[2][dados[0].index(nome)] -= 1
            print(f'{nome}: Que sorte! Não apenas achei meu shiny favorito, como também o capturei em minha última pokébola!!!\n')
            print('---Vamos verificar o que todos encontraram!---')
            for c in range(len(dados[0])):
                if len(shinies[c]) == 0:
                    print(f'Coitado, {dados[0][c]} não conseguiu capturar um único shiny hoje')
                else:
                    print(f'{dados[0][c]} capturou os seguintes shinies: {", ".join(shinies[c])}')
            shiny = True
        elif pokemon == dados[1][dados[0].index(nome)] and dados[2][dados[0].index(nome)] > 0:
            shinies[dados[0].index(nome)].append(pokemon)
            dados[2][dados[0].index(nome)] -= 1
            print(f'{nome}: Consegui capturar um {pokemon} shiny!\n')
            print('---Vamos verificar o que todos encontraram!---')
            for c in range(len(dados[0])):
                if len(shinies[c]) == 0:
                    print(f'Coitado, {dados[0][c]} não conseguiu capturar um único shiny hoje')
                else:
                    print(f'{dados[0][c]} capturou os seguintes shinies: {", ".join(shinies[c])}')
            shiny = True
        elif pokemon not in shinies[dados[0].index(nome)] and pokemon != dados[1][dados[0].index(nome)] and dados[2][dados[0].index(nome)] > 0:
            shinies[dados[0].index(nome)].append(pokemon)
            dados[2][dados[0].index(nome)] -= 1
            print(f'{nome}: Mais um shiny para a coleção, mas ainda não é um {dados[1][dados[0].index(nome)]}')
        elif pokemon in shinies[dados[0].index(nome)]:
            print(f'{nome}: Achei um {pokemon} shiny, mas não posso desperdiçar pokébolas em um shiny que já tenho...')
        elif dados[2][dados[0].index(nome)] == 0 and pokemon == dados[1][dados[0].index(nome)]:
            print(f'{nome}: Só pode ser brincadeira, um {pokemon} shiny logo agora?!')
        elif dados[2][dados[0].index(nome)] == 0 and pokemon != dados[1][dados[0].index(nome)]:
            print(f'{nome}: Péssimo momento, encontrei um {pokemon} shiny, mas não tenho mais pokébolas!')
    elif pokemon == dados[1][dados[0].index(nome)]:
        if dados[2][dados[0].index(nome)] == 0:
            print(f'{nome}: Desculpa, meu querido {pokemon}, mas não poderei lhe capturar hoje')
        else:
            print(f'{nome}: Uau, um {pokemon}! Pena que não é um shiny...')
            dados[2][dados[0].index(nome)] -= 1
    elif dados[2][dados[0].index(nome)] == 0:
        print(f'{nome}: Só um {pokemon} normal?Bom, não é como se eu tivesse pokébolas para capturar algo raro mesmo...')
    elif dados[2][dados[0].index(nome)] > 0:
        print(f'{nome}: Ainda não é um {dados[1][dados[0].index(nome)]} shiny, tenho que continuar procurando...')


'''
3
Olá, meu nome é Thomaz, meu pokémon preferido é Grumpig e tenho 0 pokébolas
Olá, meu nome é Cesar, meu pokémon preferido é Zoroark e tenho 1 pokébolas
Olá, meu nome é Josias, meu pokémon preferido é Chandelure e tenho 5 pokébolas
Um Pikachu selvagem apareceu! Foram 51 segundos e 33 passos desde o último encontro de Thomaz
Um Pikachu selvagem apareceu! Foram 51 segundos e 34 passos desde o último encontro de Thomaz
Um Grumpig selvagem apareceu! Foram 11 segundos e 3 passos desde o último encontro de Thomaz
Um Chandelure selvagem apareceu! Foram 16 segundos e 9 passos desde o último encontro de Josias
Um Rattata selvagem apareceu! Foram 55 segundos e 36 passos desde o último encontro de Cesar
Um Eevee selvagem apareceu! Foram 43 segundos e 25 passos desde o último encontro de Cesar
Um Grumpig selvagem apareceu! Foram 11 segundos e 3 passos desde o último encontro de Thomaz
Um Grumpig selvagem apareceu! Foram 11 segundos e 4 passos desde o último encontro de Thomaz
'''