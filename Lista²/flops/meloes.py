info = [["Torre do Mago", "Rancho da Marnie", "Saloon",
          "Armazém do Pierre", "Casa do Prefeito", "Peixaria",
          "Museu", "Ferreiro", "Mercado Joja",
          "Carpintaria", "Minas", "Centro Comunitário"],
          [700, 260, 1200,
           1100, 1500, 1900,
           1870, 1700, 1800,
           1500, 1850, 1300],
          ["06:00", "09:00", "12:00",
           "09:00", "08:30", "09:00",
           "08:00", "09:00", "09:00",
           "09:00", "Todo o dia", "Todo o dia"],
          ["23:00", "16:00", "24:00",
           "17:00", "22:00", "17:00",
           "18:00", "16:00", "23:00",
           "17:00", "Todo o dia", "Todo o dia"]
          ]

alibis = []
ladrao = []
mentiraLocal = []

acabou = False

for i in range(6):
    alibis.append([x for x in input().split(" - ")])

while not acabou:
    for j in alibis:
        if j[2] not in info[0]:
            ladrao.append(j[0])
            mentiraLocal.append(j[2])

    if ladrao != []:
        ladrao = sorted(ladrao)
        mentiraLocal = sorted((mentiraLocal))

        todosLadroes = ", ".join(ladrao)
        todosLocais = ", ".join(mentiraLocal)
        
        if len(ladrao) == 1:
          print(f"Esse lugar {todosLocais} nem existe! {todosLadroes} foi quem roubou os melões!")
        else:
          print(f"{todosLocais} nem existem! {todosLadroes} roubaram os melões!")
          
        acabou = True
    else: #horarios
        for j in alibis:
            if info[2][info[0].index(j[2])] != "Todo o dia":
                horarioAlibi = [int(z) for z in j[1].split(":")]
                horaAlibi = horarioAlibi[0]
                minutoAlibi = horarioAlibi[1]

                horarioAbertura = [int(k) for k in info[2][info[0].index(j[2])].split(":")]
                horaAbertura = horarioAbertura[0]
                minutoAbertura = horarioAbertura[1]

                horarioFechamento = [int(w) for w in info[3][info[0].index(j[2])].split(":")]
                horaFechamento = horarioFechamento[0]
                minutoFechamento = horarioFechamento[1]

                if horaAlibi > horaFechamento or horaAlibi < horaAbertura:
                    ladrao.append(j[0])
                    mentiraLocal.append(j[2])
                elif horaAlibi == horaFechamento or horaAlibi == horaAbertura:
                    if minutoAlibi > minutoFechamento or minutoAlibi < minutoAbertura:
                        ladrao.append(j[0])
                        mentiraLocal.append(j[2])

        if ladrao != []:
            
            if len(ladrao) == 1:
                fechamento = info[3][info[0].index(mentiraLocal[0])]
                if fechamento == "24:00":
                    fechamento = "00:00"
                    
                todosLadroes = ", ".join(ladrao)
                todosLocais = ", ".join(mentiraLocal)

                print(f"{todosLocais} nem estava aberto nessa hora, esse lugar foi fechado às {fechamento}! {todosLadroes} roubou os melões!")
            else:
                ladrao = sorted(ladrao)
                mentiraLocal = sorted((mentiraLocal))

                todosLadroes = ", ".join(ladrao)
                todosLocais = ", ".join(mentiraLocal)

                print(f"{todosLocais} nem estavam abertos nessa hora, esses lugares foram fechados beeem antes! {todosLadroes} se uniram e roubaram os melões!")

            acabou = True
        else:
            distancias = []
            for j in alibis:
                distancias.append(info[1][info[0].index(j[2])])
                distancias = sorted(distancias)

            for j in alibis:
                if info[1][info[0].index(j[2])] == distancias[0]:
                    ladrao.append(j[0])

            ladrao = sorted(ladrao)

            todosLadroes = ", ".join(ladrao)

            acabou = True

            if len(ladrao) == 1:
                print(f"{todosLadroes} estava a {distancias[0]} metros da plantação! Agora é nosso suspeito número um. Fiquem de olho!")
            else:
                print(f"{todosLadroes} estavam a {distancias[0]} metros da plantação! Eles podiam estar cometendo o roubo juntos... Fiquem de olho!")




