qtd = int(input())



for i in range(qtd):
    palavra = input()

    parte = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            parte += palavra[i]
        else:
            parte += "_"

    print(parte)
    ultima = parte
    while parte != palavra:
        chute = input()
        parte = ""
        for i in range(len(palavra)):
            
            if chute == palavra[i]:
                parte += chute
            elif chute != ultima[i]:
                parte += ultima[i]
            elif " " == palavra[i]:
                parte += " "
            else: 
                parte += "_"

        ultima = parte

        print(parte)


    
