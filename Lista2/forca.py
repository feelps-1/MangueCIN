qtd = int(input())

for i in range(qtd):
    palavra = input()

    parte = ""

    for i in range(len(palavra)):
        parte += "_"

    print(parte)

    while parte != palavra:
        chute = input()
        parte = ""
        for i in range(len(palavra)):
            
            if chute == palavra[i]:
                parte += chute
            else: 
                parte += "_"

        print(parte)


    
