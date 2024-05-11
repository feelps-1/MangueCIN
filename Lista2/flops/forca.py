print("Bem vindo ao jogo da forca do ye!")

qtd = int(input())
pontos = 0

acertou, errou, repetiu = False, False, False

for i in range(qtd):

    if i + 1 != qtd:
        print(f"Esta é a música {i + 1} de {qtd}.")
    else:
        print("Última música!")
    palavra = input()

    parte = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            parte += palavra[i]
        else:
            parte += "_"

    ultima = parte

    tentativas = (len(palavra) - palavra.count(" ")) * 2 

    while parte != palavra and tentativas > 0:
        chute = input()
        parte = ""

        for i in range(len(palavra)):

            if chute == palavra[i]:
                parte += chute
            elif chute != ultima[i]:
                parte += ultima[i]
            elif " " == palavra[i]:
                parte += " "
            

        if parte != ultima:
            acertou = True
        else:
            if chute not in palavra:
                errou = True
            else: 
                repetiu = True
        
        ultima = parte
        
        if acertou:
            print("Uhuuuuu! Consegui adivinhar uma letra!")
            acertou = False
        elif repetiu:
            print("Já tinha colocado essa letra antes, preciso de mais atenção.")
            repetiu = False
        elif errou:
            print(f"Eita! Parece que a letra {chute} não está na música secreta!")
            errou = False
        

        print(f"Resposta atual: {parte}")

        tentativas -= 1

        if tentativas == 0 and parte != palavra:
            print(f"Vish, essa tava difícil, a música era {palavra}. Espero acertar a próxima!")

        if parte == palavra:
            print("Isso! Consegui acertar uma música!")
            pontos += 1
        

print(f"Consegui acertar {pontos} músicas de {qtd}!")
taxaAcertos = (pontos*100) / qtd

if taxaAcertos <= 50:
    print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")
elif taxaAcertos <= 75:
    print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
elif taxaAcertos < 100:
    print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
else:
    print("Eu sou o próprio Kanye West.")

