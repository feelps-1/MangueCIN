salas = ["artesanato", "copa", "caldeira", "aquário", "mural"]
recursosPrimavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursosVerao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursosOutono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursosInverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]
plantacoesPrimavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoesVerao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoesOutono = ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]
faltaConjuntos = ['recursos da primavera', 'recursos do verao', 'recursos do outono', 'recursos do inverno', 'plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'artesao']
repetido = False
acabou = False

sala = input()
conjuntos = input().split(', ')

for c in range(len(conjuntos) - 1, -1, -1):
    if conjuntos.count(conjuntos[c]) > 1:
        conjuntos.pop(c)
        repetido = True

itensBau = input().split(', ')

for c in range(len(itensBau) - 1, -1, -1):
    if itensBau.count(itensBau[c]) > 1:
        itensBau.pop(c)
        repetido = True

if conjuntos == [" "] or itensBau == [" "]:
    print("Sérgio esqueceu algumas informações, será que ele pode enviar novamente?")
    acabou = True      

if sala in ['caldeira', 'aquário', 'mural']:
    print(f"Eu já conclui {sala}, não precisa doar mais itens para essa sala")
elif sala not in salas:
    print("Essa sala não está no centro comunitário")
elif not acabou:
    for x in itensBau:
        for y in conjuntos:
            if y not in faltaConjuntos:
                continue
            elif sala == 'copa':
                if y == 'recursos da primavera':
                    if x in recursosPrimavera:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'recursos do verao':
                    if x in recursosVerao:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'recursos do outono':
                    if x in recursosOutono:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'recursos do inverno':
                    if x in recursosInverno:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                else:
                    print(f'{x} pode ser analisado depois')
                    break
            elif sala == 'artesanato':
                if y == 'plantacoes da primavera':
                    if x in plantacoesPrimavera:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'plantacoes do verao':
                    if x in plantacoesVerao:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'plantacoes do outono':
                    if x in plantacoesOutono:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                elif y == 'artesao':
                    if x in artesao:
                        print(f'{x} vai ser entregue ao centro logo!')
                        break
                else:
                    print(f'{x} pode ser analisado depois')
                    break
            

    if repetido:
        print('Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
