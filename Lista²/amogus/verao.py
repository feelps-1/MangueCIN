numGalinheiros = int(input())
coelhos = 0
galinhas = 0
patos = 0

for c in range(numGalinheiros):
    animais = input().split(', ')
    coelhos += animais.count('Coelho')
    galinhas += animais.count('Galinha')
    patos += animais.count('Pato')

if coelhos > 0:
    print(f"A fazenda tem {coelhos} coelhos!")
else:
    print("Poxa que pena, não temos coelhos.")

if galinhas > 0:
    print(f"A fazenda tem {galinhas} galinhas!")
else:
    print("Poxa que pena, não temos galinhas.")

if patos > 0:
    print(f"A fazenda tem {patos} patos!")
else:
    print("Poxa que pena, não temos patos.")

listaComprasRicardo = input().split(', ')
sementesPierre = input().split(', ')

if 'Melão' in listaComprasRicardo:
    print("Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...")

comprasPossiveis = []
for fruta in listaComprasRicardo:
    if fruta in sementesPierre:
        comprasPossiveis.append(fruta)

if len(comprasPossiveis) == len(listaComprasRicardo):
    print("Consegui comprar todas as frutas que queria!")
elif len(comprasPossiveis) == 0:
    print("Poxa, acho que ficaremos sem plantações.")
else:
    print("Consegui comprar as seguintes sementes:")
    comprasPossiveis.sort()
    print(", ".join(comprasPossiveis))

itensStefan = input().split(', ')
quantidadesStefan = list(map(int, input().split(', ')))

barraFerro = quantidadesStefan[itensStefan.index('Barra de ferro')]
quartzoRefinado = quantidadesStefan[itensStefan.index('Quartzo refinado')]
asaMorcego = quantidadesStefan[itensStefan.index('Asa de morcego')] // 5

numPararaios = min(barraFerro, quartzoRefinado, asaMorcego)

print(f"Com os itens que tenho, consigo fazer {numPararaios} para-raios!")
