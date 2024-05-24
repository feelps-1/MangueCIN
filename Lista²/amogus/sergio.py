salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
recursosPrimavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursosVerao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursosOutono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursosInverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]
plantacoesPrimavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoesVerao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoesOutono = ["milho", "beringela", "abobora", "inhame"]
plantacoesInverno = ["mel", "geleia", "queijo", "tecido"]
faltaConjuntos = ['recursos da primavera', 'recursos do verao', 'recursos do outono', 'recursos do inverno', 'plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'plantacoes do inverno']
repetido = False

sala = input()
conjuntos = input().split(', ')

for x in conjuntos:
    if conjuntos.count(x) > 1:
        repetido = True

itensBau = input().split(', ')

for c in range(len(itensBau) - 1, -1, -1):
    if itensBau.count(itensBau[c]) > 1:
        itensBau.pop(c)
        repetido = True

if sala not in ['copa', 'artesanato'] and sala in salas:
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
elif sala not in salas:
    print("Essa sala não está no centro comunitário")
elif conjuntos == [" "] or itensBau == [" "]:
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
else:
    for x in itensBau:
        for y in conjuntos:
            if y not in faltaConjuntos:
                continue
            elif y == 'recursos da primavera' and sala == 'copa':
                if x in recursosPrimavera:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'recursos do verao' and sala == 'copa':
                if x in recursosVerao:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'recursos do outono' and sala == 'copa':
                if x in recursosOutono:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'recursos do inverno' and sala == 'copa':
                if x in recursosInverno:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'plantacoes da primavera' and sala == 'artesanato':
                if x in plantacoesPrimavera:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'plantacoes do verao' and sala == 'artesanato':
                if x in plantacoesVerao:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'plantacoes do outono' and sala == 'artesanato':
                if x in plantacoesOutono:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            elif y == 'plantacoes do inverno' and sala == 'artesanato':
                if x in plantacoesInverno:
                    print(f'{x} vai ser entregue ao centro logo!')
                    break
            else:
                print(f'{x} pode ser analisado depois')

    if repetido:
        print('Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
