info = {
    "João Gomes": {
        1: 0,
        2: "",
        3: 0 
    },
    "Zé Vaqueiro": {
        1: 0,
        2: "",
        3: 0  
    },
    "Raphaela Santos": {
        1: 0,
        2: "",
        3: 0  
    },
    "Alceu Valença": {
        1: 0,
        2: "",
        3: 0  
    },
    "Priscila Senna":{
        1: 0,
        2: "",
        3: 0  
    }
}

def pontos(idade, views, ordem):

    return idade//ordem + views*10**6

n = int(input())

for i in range(n):
    cidade = input()

    if cidade == "Recife":
        print("A veneza brasileira foi consultada nesta pesquisa!")
    
    if cidade == "Olinda":
        print("Uma honra ver que a primeira capital pernambucana foi consultada!")

    if cidade == "Petrolina":
        print("Ansioso para descobrir a opinião dos petrolinenses!")

    idade = int(input())

    for j in range(3):
        art, m, v = input().split(" - ")
        v = int(v)

        info[art][1] += pontos(idade, v, j+1)

        if v > info[art][3]:
            info[art][2] = m
            info[art][3] = v

pont = []
for p in info:
    pont.append(info[p][1])

pontFinal = max(pont)
vencedor = ""

for k in info:
    if info[k][1] == pontFinal:
        vencedor = k

if vencedor == "João Gomes":
    print("Parabéns, João Gomes, o novo fenômeno da música pernambucana!")
elif vencedor == "Zé Vaqueiro":
    print("Zé Vaqueiro, o astro do forró, agora brilha como o rei da música pernambucana!")
elif vencedor == "Raphaela Santos":
    print("Raphaela Santos, a voz marcante, agora é a rainha da música pernambucana!")
elif vencedor == "Alceu Valença":
    print("Alceu Valença, o ícone da MPB, agora é o gigante da música pernambucana!")
else:
    print("Priscila Senna, a rainha da sofrência, é a mais nova estrela da música pernambucana!")

print(f"O fenômeno é {vencedor}, que canta a música {info[vencedor][2]}, já contando com mais de {info[vencedor][3]} milhões de visualizações na internet.")