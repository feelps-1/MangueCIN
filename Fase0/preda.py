N = int(input())

palpites = [int(x) for x in input().split()]
erros = [int(x) for x in input().split()]

erros.sort()

possiveis = []

extremoMenor = erros[0]
extremoMaior = erros[len(erros) - 1]

pos1 = [item + extremoMaior for item in palpites]
pos2 = [item - extremoMaior for item in palpites]
pos3 = [item + extremoMenor for item in palpites]
pos4 = [item - extremoMenor for item in palpites]

print(pos1)
print(pos2)
print(pos3)
print(pos4)

tudao = pos1 + pos2 + pos3 + pos4

print(tudao)

tudao.sort()
for i in range(1, len(tudao)):
    if tudao[i] == tudao[i-1]:
        print(tudao[i])


