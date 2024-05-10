qtd = int(input())
counter = 1
taylor = 0
beyonce = 0
empate = False
acabou = False

# votação 1
while not acabou:
    voto = input()

    if voto == "beyonce":
        beyonce += 1
        print(f"Aluno {counter} votou na Beyoncé.")
    elif voto == "taylor swift":
        taylor += 1
        print(f"Aluno {counter} votou na Taylor Swift.")

    counter += 1
    if counter == qtd + 1:
        counter = 1
        acabou = True

print(f"Contagem de votos:")
print(f"Taylor Swift: {taylor} votos")
print(f"Beyoncé: {beyonce} votos")

if beyonce == taylor:
    empate = True

if empate:
    print("Empate! Iniciando rodada de debate.")
    print("Alunos, agora é a sua chance de convencer os outros a mudar de voto!")

    acabou = False

    while not acabou:
        check = input()
        if check == "sim":
            voto = input()
        elif check == "nao":
            print(f"Aluno {counter} não mudou seu voto.")
            voto = ""

        if voto == "beyonce":
            beyonce += 1
            print(f"Aluno {counter} mudou seu voto para Beyoncé.")
        elif voto == "taylor swift":
            taylor += 1
            print(f"Aluno {counter} mudou seu voto para Taylor Swift.")

        counter += 1
        if counter == qtd + 1:
            acabou = True

    if beyonce == taylor:
        empate = True
    else:
        empate = False

    print("Nova contagem de votos após o debate:")
    print(f"Taylor Swift: {taylor} votos")
    print(f"Beyoncé: {beyonce} votos")

if empate:
    print("Aldo, como presidente do evento, tem o voto decisivo.")
    check = input()

    if check == "beyonce":
        print("Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?")
    elif check == "taylor swift":
        print("Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.")
else:
    if beyonce > taylor:
        print(f"Beyoncé venceu com {beyonce} votos! Será que Kanye West estava certo?")
    else:
        print(f"Taylor Swift venceu com {taylor} votos! Kanye West tá irritado com isso.")







