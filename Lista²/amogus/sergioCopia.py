salas = [["artesanato", "copa"], ["caldeira", "aquario", "mural"]]
salasFeitas = salas[1]

analsala = [ #dados da questão
    [
        "recursos da primavera",
        "recursos do verao",
        "recursos do outono",
        "recursos do inverno",
        "plantacoes da primavera",
        "plantacoes do verao",
        "plantacoes do outono",
        "artesao",
    ],
    ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"],
    ["uva", "cafe-de-jardim", "ervilha-de-cheiro"],
    ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"],
    ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"],
    ["chirivia", "vagem", "couve-flor", "batata"],
    ["tomate", "mirtilo", "melao", "pimenta-quente"],
    ["milho", "beringela", "abobora", "inhame"],
    ["mel", "geleia", "queijo", "tecido"],
]


sala = input()
acabou = False
conjuntos = input().split(", ")


itens = input().split(", ") #caso ele esqueça alguma info
if itens[0] == " " or conjuntos[0] == " ":
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
    acabou = True


if sala in salasFeitas: 
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
elif sala not in salas[0]:
    print("Essa sala não está no centro comunitário")
elif not acabou:
    analconjuntos = []

    for i in conjuntos:

        indice = analsala[0].index(i) + 1
        if indice <= 4 and sala == "copa":
            analconjuntos.append(analsala[indice])
        elif indice > 4 and sala == "artesanato":
            analconjuntos.append(analsala[indice])
    totalItens = []
    analisados = []
    for j in itens:
        for i in analconjuntos: #capta so os conjuntos da sala
            if j in i:
                totalItens.append(j)

        if j in totalItens and j not in analisados: #printa se é item importante ou não
            print(f"{j} vai ser entregue ao centro logo!")
            analisados.append(j)
        elif j not in analisados and j not in totalItens:
            print(f"{j} pode ser analisado depois")

    rep = [0 for i in totalItens if totalItens.count(i) > 1] #caos sergio mande 2 coisas iguais
    if len(rep) > 0:
        print(
            "Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…"
        )
