rodadas = int(input())

pontosKanye, pontosTaylor = 0, 0
rodadasKanye, rodadasTaylor = 0, 0

desordemKanye, desordemTaylor = 0, 0
desordem, maxVitorias, terminou = False, False, False

while not maxVitorias and not terminou:
    for i in range(rodadas):

        if not maxVitorias and not terminou:
            print(f"{i + 1}° RODADA:")

            if desordemKanye < 5 or desordemTaylor < 5:
                musicaKanye = input()
                for j in range(3):
                    avaliaKanye = input()
                    if avaliaKanye == "boa":
                        pontosKanye += 2
                    elif avaliaKanye == "média":
                        pontosKanye += 1
                    elif avaliaKanye == "ruim":
                        pontosKanye -= 3
                    else:
                        desordem = True
                        while desordem:
                            mimimi = input()
                            if mimimi == "ORDEM":
                                desordem = not desordem
                            else:
                                desordemKanye += 1

                if desordemKanye < 5:
                    musicaTaylor = input()
                    for j in range(3):
                        avaliaTaylor = input()
                        if avaliaTaylor == "boa":
                            pontosTaylor += 2
                        elif avaliaTaylor == "média":
                            pontosTaylor += 1
                        elif avaliaTaylor == "ruim":
                            pontosTaylor -= 3
                        else:
                            desordem = True
                            while desordem:
                                mimimi = input()
                                if mimimi == "ORDEM":
                                    desordem = not desordem
                                else:
                                    desordemTaylor += 1

            if desordemKanye < 5 and desordemTaylor < 5:
                if pontosTaylor > pontosKanye:
                    rodadasTaylor += 1
                    print(f"O(a) vencedor(a) da {i + 1}° rodada foi Taylor Swift")
                elif pontosKanye > pontosTaylor:
                    rodadasKanye += 1
                    print(f"O(a) vencedor(a) da {i + 1}° rodada foi Kanye West")
                else:
                    print(f"Não houve vencedor na {i + 1}° rodada")

        if rodadasTaylor >= 3 or rodadasKanye >= 3:
            maxVitorias = True
        elif i == rodadas - 1 or desordemTaylor >= 5 or desordemKanye >= 5:
            terminou = True

        pontosKanye, pontosTaylor = 0, 0

if desordemKanye >= 5:
    print("Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!")
    print("O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!")
elif desordemTaylor >= 5:
    print("Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!")
    print("O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!")
elif rodadasKanye == rodadasTaylor:
    print("Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!")
else:
    if rodadasTaylor > rodadasKanye:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {rodadasTaylor} vitórias, é Taylor Swift, parabéns!")
    else:
        print(f"O(a) vencedor(a) do Cin Awards, com um total de {rodadasKanye} vitórias, é Kanye West, parabéns!")