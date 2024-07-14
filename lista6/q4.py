discos = {
}

artista1 = input()
artista2 = input()

discos[artista1] = {
    1: 0
}
discos[artista2] = {
    1: 0
}

for i in range(2):
    coleta = True
    while coleta:
        nomeDisco = input()

        if nomeDisco == "acabou":
            coleta = False
        else:
            precoDisco = float(input())
            if i == 0:
                discos[artista1][nomeDisco] = precoDisco
            else:
                discos[artista2][nomeDisco] = precoDisco

venda = True
receita, receitaArt1, receitaArt2, diff = 0, 0, 0, 0
maisVendeu, menosVendeu = "",""
print("Bem-vindo(a) à 'Sergio Bieber's Disco Shop'!")
print(f"E os artistas de hoje são {artista1} e {artista2}!")
print("-----COMEÇO DO EXPEDIENTE!-----")

while venda:
    comando = input()

    if comando == "FIM":
        venda = False
        print("-----FIM DO EXPEDIENTE!-----")
    else:
        if comando in discos[artista1]:
            discos[artista1][1] += 1
            print(f"{comando} vendido")
            receitaArt1 += discos[artista1][comando]
            receita += discos[artista1][comando]
        elif comando in discos[artista2]:
            discos[artista2][1] += 1
            print(f"{comando} vendido")
            receitaArt2 += discos[artista2][comando]
            receita += discos[artista2][comando]
        else:
            print("Parece que não temos esse disco...")

        maisVendeu = artista1 if discos[artista1][1] > discos[artista2][1] else artista2
        menosVendeu = artista1 if maisVendeu == artista2 else artista2

        diff = discos[maisVendeu][1] - discos[menosVendeu][1]

        if diff % 3 == 0 and diff != 0:
            print(f"A diferença está ficando muito grande! AUMENTA R$4 DE {maisVendeu.upper()} E ABAIXA R$4 DE {menosVendeu.upper()}!")
            for j in discos[maisVendeu]:
                if j == 1:
                    pass
                else:
                    discos[maisVendeu][j] += 4.00

            for z in discos[menosVendeu]:
                if z == 1:
                    pass
                else:
                    discos[menosVendeu][z] -= 4.00
                    if discos[menosVendeu][z] < 1.00:
                        discos[menosVendeu][z] = 1.00
     
vendas = discos[artista2][1] + discos[artista1][1]

if vendas == 0:
    print(f"O total de receita gerado foi de {receita:.0f} e foram vendidos {vendas} discos.")
    print("Que tristeza! Só artista péssimo...")
elif discos[artista2][1] == discos[artista1][1]:
    print(f"O total de receita gerado foi de {receita:.1f} e foram vendidos {vendas} discos.")
    print("Difícil de escolher o melhor!")
elif discos[artista2][1] > discos[artista1][1]:
    print(f"O total de receita gerado foi de {receita:.1f} e foram vendidos {vendas} discos.")
    print(f"O artista que mais gerou dinheiro para a loja foi {artista2}, acumulando uma receita de {receitaArt2:.1f} e vendendo {discos[artista2][1]} discos.")
else:
    print(f"O total de receita gerado foi de {receita:.1f} e foram vendidos {vendas} discos.")
    print(f"O artista que mais gerou dinheiro para a loja foi {artista1}, acumulando uma receita de {receitaArt1:.1f} e vendendo {discos[artista1][1]} discos.")


            
     
