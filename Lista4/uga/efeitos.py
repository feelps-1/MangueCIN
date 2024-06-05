def adicao(statusPokemon, valorItem):
    return statusPokemon + valorItem


def subtracao(statusPokemon, valorItem):
    return statusPokemon - valorItem


def multiplicacao(statusPokemon, valorItem):
    return statusPokemon * valorItem


def divisao(statusPokemon, valorItem):
    return int(statusPokemon / valorItem)


def potenciacao(statusPokemon, valorItem):
    return statusPokemon ** valorItem


def radiciacao(statusPokemon, valorItem):
    return int(statusPokemon ** (1 / valorItem))


quantidadeOperacoes = int(input())
if quantidadeOperacoes == -1:
    print('Acho que vou desistir, confio no meu Pokemon sem nenhum item!')
else:
    for c in range(quantidadeOperacoes):
        acao = input()
        statusPokemon = int(input())
        valorItem = int(input())

        if acao == 'Quero deixar meu Pokemon mais forte!':
            acao = 'Adição'
            novoStatusPokemon = adicao(statusPokemon, valorItem)
        elif acao == 'Deixa eu testar esse cogumelo estranho…':
            acao = 'Subtração'
            novoStatusPokemon = subtracao(statusPokemon, valorItem)
        elif acao == 'Vou evoluir meu Pokemon!':
            acao = 'Multiplicação'
            novoStatusPokemon = multiplicacao(statusPokemon, valorItem)
        elif acao == 'Não! Essa comida diminui o ataque…':
            acao = 'Divisão'
            novoStatusPokemon = divisao(statusPokemon, valorItem)
        elif acao == 'E se eu colocar essa Mega Stone…':
            acao = 'Potenciação'
            novoStatusPokemon = potenciacao(statusPokemon, valorItem)
        elif acao == 'Essa Mega Stone está estranha…':
            acao = 'Radiciação'
            novoStatusPokemon = radiciacao(statusPokemon, valorItem)

        print(f'Ao dar esse item eu esperava uma operação de {acao.title()} e com isso o status do meu Pokemon de {statusPokemon} foi para {novoStatusPokemon}')

    print('Agora tenho confiança que vou vencer!')
