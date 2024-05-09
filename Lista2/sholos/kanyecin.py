n = int(input())
nota = 0

if n == 0:
    media = 0
else:
    for c in range(n):
        pratica = input()

        if pratica == "Programar utilizando uma boa IDE":
            nota += 3
        elif pratica == "Códigos limpos e organizados" or pratica == "Assistir às aulas do REDU" or pratica == "Tirar dúvidas com os monitores e professores":
            nota += 10
        elif pratica == "Nomenclatura objetiva e de fácil identificação de variáveis":
            nota += 7
        elif pratica == "Evitar repetições desnecessárias de códigos" or pratica == "Comentários significativos":
            nota += 5
        elif pratica == "Programar sem utilizar IDE" or pratica == "Nomenclatura confusa e difícil de identificar variáveis":
            nota -= 5
        elif pratica == "Código bagunçado e mal estruturado":
            nota -= 6
        elif pratica == "Não tirar dúvidas com professores e monitores":
            nota -= 10

    media = nota / n

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
