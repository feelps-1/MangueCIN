def calculaCP(qtAtaque, qtDefesa, qtStamina, cpMultiplicador):
    return (qtAtaque * qtDefesa ** 0.5 * qtStamina ** 0.5 * cpMultiplicador ** 2) / 10


def maiorCp(pokemons):
    repetido = False
    maior = -1
    nome = ''

    for c in range(len(pokemons[0])):
        if pokemons[1][c] > maior:
            maior = pokemons[1][c]
            nome = pokemons[0][c]
            repetido = False
        elif pokemons[1][c] == maior:
            if pokemons[0][c] > nome:
                nome = pokemons[0][c]
                maior = pokemons[1][c]
                repetido = True

    if repetido:
        return f'Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {nome}, com CP máximo de {maior:.2f}'

    return f'O Pokémon com o maior CP na região de Kanto é: {nome}, com CP máximo de {maior:.2f}'

pokemons = [[], []]
while True:
    nomePokemon = input()

    if nomePokemon == 'Fim':
        break

    if nomePokemon not in pokemons[0]:
        qtAtaque = int(input())
        qtDefesa = int(input())
        qtStamina = int(input())
        cpMultiplicador = float(input())
        cp = calculaCP(qtAtaque, qtDefesa, qtStamina, cpMultiplicador)
        pokemons[0].append(nomePokemon)
        pokemons[1].append(cp)
        print('Pokémon computado com sucesso.')
    else:
        print('Opa, esse Pokémon já foi analisado.')
        

print(maiorCp(pokemons))
