amigos = int(input())
chutes = list(map(int, input().split()))
erro = list(map(int, input().split()))

chutes = sorted(chutes)
erro = sorted(erro)

menorChute = chutes[0]
maiorCHute = chutes[-1]
menorErro = erro[0]
maiorErro = erro[-1]
possibilidades = [
    menorChute - menorErro,
    menorChute + menorErro,
    menorChute - maiorErro,
    menorChute + maiorErro,
    maiorCHute - menorErro,
    maiorCHute + menorErro,
    maiorCHute - maiorErro,
    maiorCHute + maiorErro,
]


resultado = []


class BreakIt(Exception):
    pass


try:
    for i in range(len(possibilidades)):
        totalErro = []
        for j in range(len(chutes)):
            momento = abs(possibilidades[i] - chutes[j])
            if momento in erro:
                totalErro.append(momento)
                if sorted(totalErro) == erro and possibilidades[i] not in resultado:
                    resultado.append(possibilidades[i])
                    break
            else:
                break


except BreakIt:
    pass


resultado = sorted(resultado)

resultado = [x for x in resultado if x > 0 and x < 10**9]

print(resultado[0]) if resultado[0] > 0 else None

if len(resultado) > 1:
    resultado = sorted(resultado)
    print(resultado[1])