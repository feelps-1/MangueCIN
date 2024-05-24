locaisFazenda = [
    ["Torre do Mago", "Rancho da Marnie", "Saloon", "Armazém do Pierre", "Casa do Prefeito", "Peixaria", "Museu", "Ferreiro", "Mercado Joja", "Carpintaria", "Minas", "Centro Comunitário"],
    [700, 260, 1200, 1100, 1500, 1900, 1870, 1700, 1800, 1500, 1850, 1300],
    [[600, 2300], [900, 1600], [1200, 2400], [900, 1700], [830, 2200], [900, 1700], [800, 1800], [900, 1600], [900, 2300], [900, 1700], [-1, 9999], [-1, 9999]]
]

alibis = []

for c in range(6):
    alibi = input().split(' - ')
    alibi[1] = int(''.join(alibi[1].split(':')))
    alibis.append(alibi)

nomes = []
horarios = []
lugares = []
for x in alibis:
    nomes.append(x[0])
    horarios.append(x[1])
    lugares.append(x[2])

alibis = [nomes, horarios, lugares]

culpados = [[], []]
nomes = []
lugares = []
for x in alibis[2]:
    if x not in locaisFazenda[0]:
        nomes.append(alibis[0][alibis[2].index(x)])
        lugares.append(x)

culpados[0] = [nomes, lugares]

if culpados[0] == [[], []]:

    nomes = []
    horarios = []
    lugares = []
    for x in alibis[1]:
        if x < locaisFazenda[2][locaisFazenda[0].index(alibis[2][alibis[1].index(x)])][0] or x > locaisFazenda[2][locaisFazenda[0].index(alibis[2][alibis[1].index(x)])][1]:
            nomes.append(alibis[0][alibis[1].index(x)])
            horarios.append(x)
            lugares.append(alibis[2][alibis[1].index(x)])

    culpados[1] = [nomes, horarios, lugares]

if len(culpados[0][1]) == 1:
    print(f'Esse lugar {culpados[0][1][0]} nem existe! {culpados[0][0][0]} foi quem roubou os melões!')
elif len(culpados[0][1]) > 1:
    print(', '.join(sorted(culpados[0][1])) + ' nem existem! ' + ', '.join(sorted(culpados[0][0])) + ' roubaram os melões!')

elif len(culpados[1][1]) == 1:
    horaFechamento = locaisFazenda[2][locaisFazenda[0].index(culpados[1][2][0])][1]

    if horaFechamento == 2400:
        horaFechamento = '00:00'
    else:
        if horaFechamento / 100 < 10:
            horaFechamento = f'0{int(horaFechamento / 100)}:{horaFechamento - int(horaFechamento / 100) * 100}0'
        else:
            horaFechamento = f'{int(horaFechamento / 100)}:{horaFechamento - int(horaFechamento / 100) * 100}0'

    print(f'{culpados[1][2][0]} nem estava aberto nessa hora, esse lugar foi fechado às {horaFechamento}! {culpados[1][0][0]} roubou os melões!')
elif len(culpados[1][1]) > 1:
    print(', '.join(sorted(culpados[1][2])) + ' nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! ' + ', '.join(sorted(culpados[1][0])) + ' se uniram e roubaram os melões!')

else:
    distancias = []
    for x in alibis[2]:
        distancias.append(locaisFazenda[1][locaisFazenda[0].index(x)])

    nomes = []
    maisProximo = []
    for x in distancias:
        if x == min(distancias):
            nomes.append(alibis[0][distancias.index(x)])
            maisProximo.append(x)

    culpado = [nomes, maisProximo]
    if len(culpado[0]) == 1:
        print(f'{culpado[0][0]} estava a {culpado[1][0]} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!')
    else:
        print(', '.join(culpado[0]) + ' estavam a ' + str(culpado[1][0]) + ' metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!')
