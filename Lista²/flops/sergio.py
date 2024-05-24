salas = ["artesanato", "copa"]
concluidas = ["caldeira", "aquário", "mural"]
todas = ["artesanato", "copa", "caldeira", "aquário", "mural"]

repetiu = False

conjuntosDisponiveis = [["copa", "artesanato"]
    , ["recursos da primavera", "recursos do verao", "recursos do outono", "recursos do inverno"]
    , ["plantacoes da primavera", "plantacoes do verao", "plantacoes do outono", "artesao"]
    , ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
    , ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
    , ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
    , ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]
    , ["chirivia", "vagem", "couve-flor", "batata"]
    , ["tomate", "mirtilo", "melao", "pimenta-quente"]
    , ["milho", "beringela", "abobora", "inhame"]
    , ["mel", "geleia", "queijo", "tecido"]]

sala = input()

conjuntos = input()

itens = input()

if conjuntos == " ":
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
elif itens == " ":
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
elif sala in concluidas:
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
elif sala not in todas:
    print("Essa sala não está no centro comunitário")
else:
    conjuntos = [conjunto for conjunto in conjuntos.split(", ")]
    itens = [item for item in itens.split(", ")]

    pertenceSala = []
    itensPertence = []

    for conjunto in conjuntos:
        if conjunto in conjuntosDisponiveis[conjuntosDisponiveis[0].index(sala) + 1]:
            pertenceSala.append(conjunto)

    for conjunto in pertenceSala:
        if sala == "copa":
            itensPertence += conjuntosDisponiveis[conjuntosDisponiveis[conjuntosDisponiveis[0].index(sala) + 1].index(conjunto) + 3]
        elif sala == "artesanato":
            itensPertence += conjuntosDisponiveis[conjuntosDisponiveis[conjuntosDisponiveis[0].index(sala) + 1].index(conjunto) + 7]

    analisado = []
    repetiu = False
    print(itensPertence)

    for item in itens:
        if item in analisado:
            repetiu = True
        elif item in itensPertence:
            print(f"{item} vai ser entregue ao centro logo!")
            itensPertence.remove(item)
            analisado.append(item)
        else:
            print(f"{item} pode ser analisado depois")
            analisado.append(item)

    print(pertenceSala)
    print(itensPertence)






