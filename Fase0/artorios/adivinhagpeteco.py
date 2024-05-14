amigos = int(input())
chutes = list(map(int, input().split()))
erro = list(map(int, input().split()))

chutes.sort()
erro.sort()

resultado = []

for chute in chutes:
    for e in erro:
        for possibilidade in [chute + e, chute - e]:
            totalErro = [abs(possibilidade - c) for c in chutes if abs(possibilidade - c) in erro]
            if len(totalErro) == len(chutes) and possibilidade not in resultado:
                resultado.append(possibilidade)

resultado = sorted(x for x in resultado if 0 < x < 10**9)

if resultado:
    print(resultado[0])

if len(resultado) > 1:
    print(resultado[1])