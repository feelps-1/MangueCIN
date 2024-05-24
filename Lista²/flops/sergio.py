salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]

recursosPrimavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursosVerao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursosOutono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursosInverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]

plantacoesPrimavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoesVerao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoesOutono = ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]

sala = input()

conjuntos = input()

itens = input()

if sala in salas:
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
elif conjuntos == " ":
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
elif itens == " ":
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
else:
    conjuntos = [conjunto for conjunto in conjuntos.split(", ")]
    itens = [item for item in itens.split(", ")]






