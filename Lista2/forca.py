print("Bem vindo ao jogo da forca do ye!")

qtd = int(input())

for i in range(qtd):


    if i + 1 != qtd:
        print(f"Esta é a música {i+1} de {qtd}.")
    else:
        print("Última música!")
    palavra = input()



    parte = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            parte += palavra[i]
        else:
            parte += "_"

    print(parte)
    ultima = parte
    while parte != palavra or tentativas > 0:
        chute = input()
        parte = ""

        if len(palavra.split()) > 1:
            tentativas = (len(palavra) - len(palavra.split())) * 2
        else:
            tentativas = len(palavra) * 2

        acertou, repetiu = False, False

        for i in range(len(palavra)):
            
            if chute == palavra[i]:
                parte += chute
                print("Uhuuuuu! Consegui adivinhar uma letra!")
                acertou = True
            elif chute != ultima[i]:
                parte += ultima[i]
                print("Já tinha colocado essa letra antes, preciso de mais atenção.")
                repetiu = True
            elif " " == palavra[i]:
                parte += " "
            else: 
                parte += "_"
                print("Eita! Parece que a letra {chute} não está na música secreta!")

        ultima = parte

        if repetiu:
            print("Já tinha colocado essa letra antes, preciso de mais atenção.")
            repetiu = False
        elif acertou:
            print("Uhuuuuu! Consegui adivinhar uma letra!")
            acertou = False
        else:
            print(f"Eita! Parece que a letra {chute} não está na música secreta!")

        print(f"Resposta atual: {parte}")

        tentativas -= 1


    
