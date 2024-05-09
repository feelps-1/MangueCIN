numRodadas = int(input())
desordemKanye = 0
desordemTaylor = 0
vitoriasKanye = 0
vitoriasTaylor = 0
desordem = False

c = 1
while c <= numRodadas:
    print(f'{c}° RODADA:')
    mimimi = ''
    musicaKanye = input()
    rodadaKanye = 0
    rodadaTaylor = 0
    
    for d in range(3):
        avaliacaoKanye = input()
        
        if avaliacaoKanye == 'boa':
            rodadaKanye += 2
        if avaliacaoKanye == 'média':
            rodadaKanye += 1
        if avaliacaoKanye == 'ruim':
            rodadaKanye -= 3
        if avaliacaoKanye == 'péssima':
            while mimimi != 'ORDEM':
                mimimi = input()
                if mimimi != 'ORDEM': desordemKanye += 1

    if desordemKanye < 5:
        musicaTaylor = input()
        for f in range(3):
            avaliacaoTaylor = input()
            
            if avaliacaoTaylor == 'boa':
                rodadaTaylor += 2
            if avaliacaoTaylor == 'média':
                rodadaTaylor += 1
            if avaliacaoTaylor == 'ruim':
                rodadaTaylor -= 3
            if avaliacaoTaylor == 'péssima':
                while mimimi != 'ORDEM':
                    mimimi = input()
                    if mimimi != 'ORDEM': desordemTaylor += 1

    if desordemTaylor >= 5:
        c = numRodadas
        print(f'Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!')
        vitoriasTaylor = 0
        desordem = True
    elif desordemKanye >= 5:
        c = numRodadas
        print(f'Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!')
        vitoriasKanye = 0
        desordem = True
    elif rodadaKanye > rodadaTaylor:
        vitoriasKanye += 1
        print(f'O(a) vencedor(a) da {c}° rodada foi Kanye West')
    elif rodadaKanye < rodadaTaylor:
        print(f'O(a) vencedor(a) da {c}° rodada foi Taylor Swift')
        vitoriasTaylor += 1
    else:
        print(f'Não houve vencedor na {c}° rodada')

    if vitoriasKanye >= 3:
        c = numRodadas
    elif vitoriasTaylor >= 3:
        c = numRodadas

    if c == numRodadas and desordem == False:
        if vitoriasKanye > vitoriasTaylor:
            print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitoriasKanye} vitórias, é Kanye West, parabéns!')
        elif vitoriasTaylor > vitoriasKanye:
            print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitoriasTaylor} vitórias, é Taylor Swift, parabéns!')
        else:
            print('Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!')
    else:
        if desordemKanye >= 5:
            print('O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!')
        elif desordemTaylor >= 5:
            print('O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!')

    c += 1
