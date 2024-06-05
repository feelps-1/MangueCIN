'''
[{   (((2 * nivel) + 10) / 250)    *    ((poder /defesa_inimigo) * poder_ataque))    } + 2 ] * efetividade

tipo| fraco contra | forte contra | neutro contra

fogo | agua | grama| fogo e normal

agua | grama| fogo | agua e normal

grama | fogo | agua | grama e normal

normal| nenhum | nenhum | todos
'''
def calcularDano(nivel, poder, defesaInimigo, poderAtaque, efetividade):
    return int((((((2 * nivel) + 10) / 250) * ((poder / defesaInimigo) * poderAtaque)) + 2) * efetividade)


def calculoEfetividade(tipo, tipoInimigo):
    if tipo == 'fogo':
        if tipoInimigo == 'agua':
            return 0.5
        elif tipoInimigo == 'grama':
            return 2
        else:
            return 1
    elif tipo == 'agua':
        if tipoInimigo == 'grama':
            return 0.5
        elif tipoInimigo == 'fogo':
            return 2
        else:
            return 1
    elif tipo == 'grama':
        if tipoInimigo == 'fogo':
            return 0.5
        elif tipoInimigo == 'agua':
            return 2
        else:
            return 1
    else:
        return 1


nome, tipo, nivel, vida, poder, defesa, velocidade, ataque, poderAtaque = input().split(', ')
nivel = int(nivel)
vida = int(vida)
poder = int(poder)
defesa = int(defesa)
velocidade = int(velocidade)
poderAtaque = int(poderAtaque)
copiaVida = vida
print(f'escolho você {nome}')
while True:
    estado = input()
    nomeInimigo, tipoInimigo, nivelInimigo, vidaInimigo, poderInimigo, defesaInimigo, velocidadeInimigo, ataqueInimigo, poderAtaqueInimigo = input().split(', ')
    nivelInimigo = int(nivelInimigo)
    vidaInimigo = int(vidaInimigo)
    poderInimigo = int(poderInimigo)
    defesaInimigo = int(defesaInimigo)
    velocidadeInimigo = int(velocidadeInimigo)
    poderAtaqueInimigo = int(poderAtaqueInimigo)
    copiaVidaInimigo = vidaInimigo

    if estado == 'um pokemon selvagem aparece!':
        print('vamo botar pra quebrar!')

    elif estado == 'Equipe Rocket':
        print(f'{nome}, bora acabar com a raça desses bandidos e salvar o professor!')
    
    print()
    efetividade = calculoEfetividade(tipo, tipoInimigo)
    efetividadeInimigo = calculoEfetividade(tipoInimigo, tipo)
    dano = calcularDano(nivel, poder, defesaInimigo, poderAtaque, efetividade)
    danoInimigo = calcularDano(nivelInimigo, poderInimigo, defesa, poderAtaqueInimigo, efetividadeInimigo)

    while copiaVida > 0 and copiaVidaInimigo > 0:
        acao = input()

        if acao == 'atacar':
            if velocidade < velocidadeInimigo:
                copiaVida -= danoInimigo
                print(f'{nomeInimigo} usou {ataqueInimigo}')

                if efetividadeInimigo == 2:
                    print('foi super efetivo!')
                elif efetividadeInimigo == 0.5:
                    print('não foi muito efetivo')

                if copiaVida <= 0:
                    copiaVida = 0
                    break

                copiaVidaInimigo -= dano
                print(f'{nome} usou {ataque}')

                if efetividade == 2:
                    print('foi super efetivo!')
                elif efetividade == 0.5:
                    print('não foi muito efetivo')

                if copiaVidaInimigo <= 0:
                    copiaVidaInimigo = 0
                    break
            else:
                copiaVidaInimigo -= dano
                print(f'{nome} usou {ataque}')

                if efetividade == 2:
                    print('foi super efetivo!')
                elif efetividade == 0.5:
                    print('não foi muito efetivo')

                if copiaVidaInimigo <= 0:
                    copiaVidaInimigo = 0
                    break

                copiaVida -= danoInimigo
                print(f'{nomeInimigo} usou {ataqueInimigo}')

                if efetividadeInimigo == 2:
                    print('foi super efetivo!')
                elif efetividadeInimigo == 0.5:
                    print('não foi muito efetivo')

                if copiaVida <= 0:
                    copiaVida = 0
                    break

            print(f'HP: {copiaVida}/{vida} | HP inimigo: {copiaVidaInimigo}/{vidaInimigo}')
        elif acao == 'correr':
            if estado == 'um pokemon selvagem aparece!':
                print('ufa, consegui meter o pé!')
                break
            else:
                print('lascou, eles não largam do meu pé!')

    if acao == 'atacar':
        print(f'HP: {copiaVida}/{vida} | HP inimigo: {copiaVidaInimigo}/{vidaInimigo}')

    if copiaVidaInimigo == 0:
        print(f'{nomeInimigo} derrotado!\n')
    elif copiaVida == 0:
        print(f'{nome} derrotado!\n')
        print(f'Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
        break

    if estado == 'Equipe Rocket':
        print(f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome}?')
        break

'''
Charmander, fogo, 5, 39, 52, 43, 65, brasa, 40
um pokemon selvagem aparece!
Tangela, grama, 2, 20, 52, 43, 25, absorver, 40
correr
Equipe Rocket
Bulbasaur, grama, 3, 30, 49, 49, 45, absorver, 40
atacar
atacar
atacar
'''
