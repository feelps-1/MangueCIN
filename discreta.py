salas = int(input())
pessoas = int(input())
qnt = 0

for i in range(pessoas + 1):

    nFact = 1
    for n in range(1, pessoas + 1):
        nFact *= n

    kFact = 1
    for k in range(1, qnt + 1):
        kFact *= k

    mFact = 1
    for m in range(1, pessoas - qnt + 1):
        mFact *= m

    if qnt == 0 or qnt == 10:
        comb = 1
    else:
        comb = nFact / (kFact * mFact)

    resto = (salas - 1) ** (pessoas - qnt)

    divisor = salas ** pessoas

    probabilidade = (comb * resto) / divisor

    print(f"O número de maneiras de distribuir na sala é de {divisor} maneiras e a probabilidade de ter {qnt} pessoas na sala é de {comb}/{divisor} = {probabilidade}")
    qnt += 1

