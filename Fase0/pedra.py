N = int(input())

palpites = [int(x) for x in input().split()]
erros = [int(x) for x in input().split()].sort()

possiveis = []

extremoMenor = erros[0]
extremoMaior = erros[len(erros) - 1]

for i in range(N):

    testePos = palpites[i] + erros[i]
    testeNeg = palpites[i] - erros[i]

    if i + 1 > N-1:
        proxPos = palpites[i-1] + erros[i-1]
        proxNeg = palpites[i-1] - erros[i-1]
    else:
        proxPos = palpites[i + 1] + erros[i + 1]
        proxNeg = palpites[i + 1] - erros[i + 1]

    if proxPos == testePos and proxPos not in possiveis:
        possiveis.append(testePos)
    if proxNeg == testeNeg and proxNeg not in possiveis:
        possiveis.append(testeNeg)

possiveis.sort()

print(possiveis[0])
if len(possiveis) > 1:
    print(possiveis[1])