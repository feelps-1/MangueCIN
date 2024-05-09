acabou = False
votos = 0
totais = 0
sturno = False

while not acabou:

    n = input()
    if n != "FIM":
        n = int(n)
        if n % 2 == 0:
            votos += 10 ** 7
            totais += 10 ** 7
        elif n % 7 == 0:
            votos += 20 * 10 ** 6
            totais += 20 * 10 ** 6
        else:
            totais += 14 * 10 ** 6

    if totais >= 3 * 10 ** 8 or n == "FIM":
        acabou = True

if votos <= 13 * 10 ** 7:
    print("Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")
elif votos > 13 * 10 ** 7 and votos <= 17 * 10 ** 7:
    print("A eleição está disputada, vamos ter um segundo turno!")
    sturno = True
    acabou = False
elif votos >= 17 * 10 ** 7:
    print(
        "O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")

print(f"Kanye conseguiu ao final da campanha um total de {votos} votos.")

if sturno:
    votos = 0
    totais = 0
    while not acabou:

        n = input()
        if n != "FIM":
            n = int(n)
            if n % 2 == 0:
                votos += 10 ** 7
                totais += 10 ** 7
            elif n % 7 == 0:
                votos += 20 * 10 ** 6
                totais += 20 * 10 ** 6
            else:
                totais += 14 * 10 ** 6

        if totais >= 3 * 10 ** 8 or n == "FIM":
            acabou = True

    if votos > 13 * 10 ** 7:
        print(
            "Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.")
    else:
        print(
            "Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.")

    print(f"Kanye conseguiu ao final da campanha um total de {votos} votos.")
