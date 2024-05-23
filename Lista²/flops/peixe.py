for i in range(3):
    pescador = input()
    nomePescador = pescador.split(":")[0]

    conquistas = []
    conquistas = [x for x in pescador.split(": ")[1].split(", ")]

    acabou = False
    peixes = []
    peixesUnicos = []
    conquistasReais = []

    while not acabou:
        peixe = input()

        if peixe != "FIM":
            peixes.append(peixe)
            if peixe not in peixesUnicos:
                peixesUnicos.append(peixe)
        else:
            acabou = True

    if "Pescador" in conquistas:
        if len(peixesUnicos) >= 5:
            conquistasReais.append("Pescador")

    if "Velho Marinheiro" in conquistas:
        if len(peixesUnicos) >= 10:
            conquistasReais.append("Velho Marinheiro")

    if "Velho Pescador" in conquistas:
        if len(peixesUnicos) == 15:
            conquistasReais.append("Velho Pescador")

    if "Deus Pescador" in conquistas:
        if len(peixes) >= 25:
            conquistasReais.append("Deus Pescador")

    if sorted(conquistasReais) == sorted(conquistas):
        print(f"{nomePescador} realmente estava falando a verdade!!!")
    else:
        print(f"{nomePescador} é um mentiroso, ele não tem todas essas conquistas!")



