galinheiros = int(input())
animaisTodos = [[0, "coelhos"], [0, "galinhas"], [0, "patos"]]

for i in range(galinheiros):
    animais = [x for x in input().split(", ")]
    animaisTodos[1][0] += animais.count("Galinha")
    animaisTodos[2][0] += animais.count("Pato")
    animaisTodos[0][0] += animais.count("Coelho")

for i in range(len(animaisTodos)):
    if animaisTodos[i][0] > 0:
        print(f"A fazenda tem {animaisTodos[i][0]} {animaisTodos[i][1]}!")
    else:
        print(f"Poxa que pena, não temos {animaisTodos[i][1]}.")


listaCompras = [x for x in input().split(", ")]
tem = []

pierreCorno = [x for x in input().split(", ")]

if "Melão" in listaCompras:
    print("Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...")

for i in pierreCorno:
    if i in listaCompras:
        tem.append(i)

if len(tem) == len(listaCompras):
    print("Consegui comprar todas as frutas que queria!")
elif len(tem) == 0:
    print("Poxa, acho que ficaremos sem plantações.")
else:
    print("Consegui comprar as seguintes sementes:")
    ordenado = sorted(tem)
    saida = ""

    for i in range(len(ordenado)):
        saida += ordenado[i]
        if i+1 != len(ordenado):
            saida += ", "

    print(saida)

mochila = [x for x in input().split(", ")]
quantidade = [int(x) for x in input().split(", ")]

materiais = sorted([quantidade[mochila.index("Barra de ferro")], quantidade[mochila.index("Quartzo refinado")], quantidade[mochila.index("Asa de morcego")] // 5])

paraRaios = materiais[0]

print(f"Com os itens que tenho, consigo fazer {paraRaios} para-raios!")



