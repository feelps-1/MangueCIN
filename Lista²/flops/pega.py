agricultura = [x for x in input().split(" - ")]
animais = [x for x in input().split(" - ")]
pesca = [x for x in input().split(" - ")]
mineracao = [x for x in input().split(" - ")]

tipos = ["agricultura", "criação", "pesca", "mineração"]

end = False
deNovo = False

opcao = []

while not end:
    for i in range(4):
        opcao.append(int(input()))

    if not deNovo:
        print("Itens selecionados! Hora de iniciar a mesclagem... Simbora!")

    print("Combinando Itens...")

    print(f"Item para agricultura: {agricultura[opcao[0]]}")
    print(f"Item para criação: {animais[opcao[1]]}")
    print(f"Item para pesca: {pesca[opcao[2]]}")
    print(f"Item para mineração: {mineracao[opcao[3]]}")

    opiniao = input()

    if opiniao == "Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...":
        end = True
        print("Meu dia tá garantido, obrigado pela ajuda Pega Móvel!")
    elif opiniao == "Esses itens são bem paia, acho que não gostei muito :(":
        opiniao = input()
        if opiniao == "Bom, vamos tentar mais uma vez...":
            end = False
            deNovo = True
        elif opiniao == "Essa máquina deve estar com defeito...":
            end = True
            print("É... acho que já chega de Stardew por hoje...")


