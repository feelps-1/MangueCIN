from math import floor

candidato1 = input()
candidato2 = input()

acabou, fim = False, False

apoiodel1, apoiodel2 = 0, 0
votos_totais1, votos_totais2 = 0, 0

info = ""

if candidato1 != "Kanye West" and candidato2 != "Kanye West":
    print("Sem o Ye, sem eleição!")

else:
    while not acabou:
        fim = False
        info = input()

        if info != "FIM":
            

            info = info.split(", ")
            estado = info[0]
            delegados = int(info[1])

            while not fim:
                votos_c1 = input()
                
                if votos_c1 != "Taylor Swift roubou as urnas!":
                    votos_c1 = int(votos_c1)
                    votos_c2 = input()
                    
                    if votos_c2 != "Taylor Swift roubou as urnas!":
                        votos_c2 = int(votos_c2)
                
                        totais = votos_c1 + votos_c2

                        if votos_c1 > votos_c2:
                            percentual = floor(100*votos_c1/totais)
                            apoiodel1 += delegados
                            votos_totais1 += votos_c1
                            
                            print(f"{candidato1} obteve maioria no(a) {estado} com {percentual}% dos votos.")
                        else:
                            percentual = floor(100*votos_c2/totais)
                            apoiodel2 += delegados
                            votos_totais2 += votos_c2

                            print(f"{candidato2} obteve maioria no(a) {estado} com {percentual}% dos votos.")
                            
                        fim = True
                    else:
                        votos_c2 = 0
                        votos_c1 = 0
                        print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")
                else:
                    votos_c1 = 0
                    print("A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!")

        else:
            acabou = True
    
    if votos_totais1 > votos_totais2:
        vencedor = candidato1
        print(f"Temos o resultado final! {candidato1} vence a disputa pela presidência, com o apoio de {apoiodel1} delegados do colégio eleitoral e {votos_totais1} votos populares.")
    else:
        print(f"Temos o resultado final! {candidato2} vence a disputa pela presidência, com o apoio de {apoiodel2} delegados do colégio eleitoral e {votos_totais2} votos populares.")
        vencedor = candidato2

    if vencedor == "Kanye West":
        print("\"Everybody wanted to know what I would do if I didn't win... I Guess We'll Never Know.\"")
    else:
        print("\"Não tem problema, eu obtive o molho!\"")
