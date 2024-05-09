n = int(input())
div = n
nota = 0

if n == 0:
    media = 0
else:
    while n != 0:
        pratica = input()

        if pratica == "Códigos limpos e organizados" or pratica == "Assistir às aulas do REDU" or pratica == "Tirar dúvidas com os monitores e professores":
            nota += 10
        elif pratica == "Evitar repetições desnecessárias de códigos" or pratica == "Comentários significativos":
            nota += 5
        elif pratica == "Nomenclatura objetiva e de fácil identificação de variáveis":
            nota += 7
        elif pratica == "Programar utilizando uma boa IDE":
            nota += 3
        elif pratica == "Programar sem utilizar IDE" or pratica == "Nomenclatura confusa e difícil de identificar variáveis":
            nota -= 5
        elif pratica == "Não tirar dúvidas com professores e monitores":
            nota -= 10
        elif pratica == "Código bagunçado e mal estruturado":
            nota -= 6

        n -= 1

if div == 0:
    media = 0
else:
    media = nota / div

if media < 0:
    media = 0
elif media > 10:
    media = 10

if media < 3:
    print("É melhor voltar a cantar mesmo!")
elif media < 7:
    print("Vai precisar se esforçar um pouco mais, meu cantor!")
elif media == 7:
    print("Na conta certa!")
elif media < 9:
    print("Nasceu para programar!")
else:
    print("Já pode ser chamado de Kanye, the dev, West!")

