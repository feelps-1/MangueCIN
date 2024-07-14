fortunas = {
    1: {
        "Priscila Senna": [40, 10000, 0],
        "Eduarda": [60, 9990, 0],
        "Academia da Berlinda": [30, 9995, 0],
        "Martins": [25, 9970, 0],
        "Igor de Carvalho": [25, 9965, 0]
    },
    2: {

    }
}

def venda(fortunas, artista, discos):
    lucro = 0
    
    if discos > 5:
        imposto = 0.93
    elif discos > 3:
        imposto = 0.95
    elif discos > 1:
        imposto = 0.98
    else:
        imposto = 1

    lucro = 20 * discos * imposto

    if artista in fortunas[1]:
        fortunas[1][artista][2] += ((100*lucro)/fortunas[1][artista][1])
        fortunas[1][artista][1] += lucro
    else:
        fortunas[2][artista] = [discos, lucro]

    return fortunas

n = int(input())
lucrou, vendeu = [], []

for i in range(n):
    art, d = input().split(" - ")
    d = int(d)

    fortunas = venda(fortunas, art, d)
    
    if art not in fortunas[1]:
        vendeu.append(art)
    else:
        if fortunas[1][art][2] > 0:
            lucrou.append(art)


if lucrou:
    print("Estes artistas obtiveram aumento do lucro em relação à primeira semana:")
    for k in lucrou:
        print(f"{k} - Lucro em relação à primeira semana: {fortunas[1][k][2]:.2f}%")
else:
    print("Os artistas da primeira semana não tiveram aumento do lucro na segunda semana!")

print("\nEsta é a fortuna atual dos artistas considerados:")

for z in fortunas:
    for j in fortunas[z]:
        print(f"{j}: R$ {fortunas[z][j][1]:.2f}")

print()

if vendeu:
    print("Na semana 2 tivemos vendas de novos artistas no mercado:")
    for k in vendeu:
        print(f"{k} - Discos vendidos: {fortunas[2][k][0]}")
else:
    print("Na semana 2 não tivemos vendas de novos artistas no mercado!")
        
     

