print('Bem vindo ao jogo da forca do ye!')

n = int(input())
pontos = 0

for c in range(1, n + 1):
    chutes = ''
    musica = input()

    if c == n:
        print('Última música!')
    else:
        print(f'Esta é a música {c} de {n}.')

    d = 1
    while d <= ((len(musica) - musica.count(' ')) * 2):
        chute = input()

        if chute in chutes:
            print('Já tinha colocado essa letra antes, preciso de mais atenção.')
        elif chute in musica:
            print('Uhuuuuu! Consegui adivinhar uma letra!')
            chutes += chute
        else:
            print(f'Eita! Parece que a letra {chute} não está na música secreta!')        

        segredo = ''
        for f in musica:
            if f in chutes:
                segredo += f
            elif f == ' ':
                segredo += ' '
            else:
                segredo += '_'

        print(f'Resposta atual: {segredo}')

        if segredo == musica:
            print('Isso! Consegui acertar uma música!')
            pontos += 1
            d = (len(musica) - musica.count(' ')) * 2

        d += 1
    
    if segredo != musica:
        print(f'Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!')

print(f'Consegui acertar {pontos} músicas de {n}!')

taxaAcertos = pontos / n * 100

if taxaAcertos <= 50:
    print('Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!')
elif taxaAcertos <= 75:
    print('Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.')
elif taxaAcertos < 100:
    print('Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.')
else:
    print('Eu sou o próprio Kanye West.')
