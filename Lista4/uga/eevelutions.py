'''
0 → Vaporeon (Água);
1 → Jolteon (Elétrico);
2 → Flareon (Fogo);
3 → Espeon (Psíquico);
4 → Umbreon (Sombrio);
5 → Glaceon (Gelo);
6 → Leafeon (Planta);
7 → Sylveon (Fada).

Para o cálculo responsável por definir qual será a evolução do Eevee, passaremos por algumas etapas:

Atribuiremos valores numéricos inteiros (1 - 26) a cada letra do alfabeto (a - z), começando de 1 para 'a', 2 para 'b', 3 para 'c', e assim por diante até 26 para 'z';
Após transformar todas as letras em números, de acordo com a etapa anterior, você deverá obter o somatório de cada número, multiplicando o resultado pela idade do treinador;
Por fim, utilizaremos o resto da divisão do resultado da última etapa por 8, chegando ao index que determina a forma de evolução do Eevee.
Porém, se o nome do treinador for uma referência a um personagem famoso de Pokémon, o programa deverá determinar a forma de evolução do Eevee correspondente à lista abaixo,
independentemente do cálculo anterior:

Água: Misty, Gary, Ivy, Blanche
Elétrico: Ash, Ritchie, Surge, Spark
Fogo: May, Blaine, Candela
Psíquico: Agatha, Sabrina, Fantina
Sombrio: Jessie, James, Giovanni
Gelo: Lorelei, Dawn
Planta: Max, Erika, Tracey, Mallow
Fada: Whitney
OBS.1: Funções de ordenamento nativas não são permitidas.

OBS.2: É obrigatória a criação de pelo menos duas funções: para registrar as informações dos treinadores solicitados no input, e para determinar o tipo de evolução do Eevee.

DICA: O Professor Carvalho recomendou dar uma pesquisada nas funções "capitalize()" e “index()” 😉

De acordo com o respectivo tipo de evolução, imprima a frase que a segue:

Para Vaporeon:
A evolução do Eevee de {nome} é para Vaporeon, o mestre das águas!

Para Jolteon:
O Eevee de {nome} evoluiu para Jolteon, cheio de energia elétrica!

Para Flareon:
O Eevee de {nome} se transformou em Flareon, dominando o calor do fogo!

Para Espeon:
Espeon é a evolução do Eevee de {nome}, mostrando sua mente brilhante!

Para Umbreon:
A evolução sombria do Eevee de {nome} é Umbreon, deslizando pelas sombras!

Para Glaceon:
Glaceon é o novo estágio do Eevee de {nome}, tão frio quanto o gelo!

Para Leafeon:
O Eevee de {nome} se transformou em Leafeon, um espírito da floresta!

Para Sylveon:
Sylveon é a evolução mágica do Eevee de {nome}, irradiando bondade e misticismo!
'''
def registro(n):
    treinadores = []

    for c in range(n):
        nome, idade = input().split(' - ')
        int(idade)    
        treinadores.append([nome, idade])

    return treinadores


def escolha(treinadores):
    escolhas = []
    eevelutions = ['Vaporeon', 'Jolteon', 'Flareon', 'Espeon', 'Umbreon', 'Glaceon', 'Leafeon', 'Sylveon']

    for treinador in treinadores:
        nome = treinador[0]
        idade = treinador[1]
        if nome.capitalize() in ['Misty', 'Gary', 'Ivy', 'Blanche']:
            pokemon = 'Vaporeon'
        elif nome.capitalize() in ['Ash', 'Ritchie', 'Surge', 'Spark']:
            pokemon = 'Jolteon'
        elif nome.capitalize() in ['May', 'Blaine', 'Candela']:
            pokemon = 'Flareon'
        elif nome.capitalize() in ['Agatha', 'Sabrina', 'Fantina']:
            pokemon = 'Espeon'
        elif nome.capitalize() in ['Jessie', 'James', 'Giovanni']:
            pokemon = 'Umbreon'
        elif nome.capitalize() in ['Lorelei', 'Dawn']:
            pokemon = 'Glaceon'
        elif nome.capitalize() in ['Max', 'Erika', 'Tracey', 'Mallow']:
            pokemon = 'Leafeon'
        elif nome.capitalize() in ['Whitney']:
            pokemon = 'Sylveon'
        else:
            letras = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            soma = 0
            for letra in nome:
                soma += letras.index(letra.lower())
            soma *= int(idade)
            index = soma % 8
            pokemon = eevelutions[index]

        if pokemon == 'Vaporeon':
            escolhas.append(f'A evolução do Eevee de {treinador[0].title()} é para Vaporeon, o mestre das águas!')
        elif pokemon == 'Jolteon':
            escolhas.append(f'O Eevee de {treinador[0].title()} evoluiu para Jolteon, cheio de energia elétrica!')
        elif pokemon == 'Flareon':
            escolhas.append(f'O Eevee de {treinador[0].title()} se transformou em Flareon, dominando o calor do fogo!')
        elif pokemon == 'Espeon':
            escolhas.append(f'Espeon é a evolução do Eevee de {treinador[0].title()}, mostrando sua mente brilhante!')
        elif pokemon == 'Umbreon':
            escolhas.append(f'A evolução sombria do Eevee de {treinador[0].title()} é Umbreon, deslizando pelas sombras!')
        elif pokemon == 'Glaceon':
            escolhas.append(f'Glaceon é o novo estágio do Eevee de {treinador[0].title()}, tão frio quanto o gelo!')
        elif pokemon == 'Leafeon':
            escolhas.append(f'O Eevee de {treinador[0].title()} se transformou em Leafeon, um espírito da floresta!')
        elif pokemon == 'Sylveon':
            escolhas.append(f'Sylveon é a evolução mágica do Eevee de {treinador[0].title()}, irradiando bondade e misticismo!')

    return escolhas


n = int(input())

treinadores = registro(n)

escolhas = escolha(treinadores)

for x in escolhas:
    print(x)
