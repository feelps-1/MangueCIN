n = int(input())
aprovados = 0
neutros = 0
negados = 0

while n != 0:
    resposta = input()
    if resposta == "Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!":
        aprovados += 1
    elif resposta == "Não gostei. Muito sem graça, onde já se viu nome com duas letras?":
        negados += 1
    elif resposta == "Ainda estou me acostumando. Não tenho uma opinião formada sobre isso.":
        neutros += 1

    n -= 1

totais = aprovados + neutros + negados
aprovacao = (aprovados / totais) * 100
rejeicao = (negados / totais) * 100
abstencao = (neutros / totais) * 100

print("A pesquisa terminou e os resultados foram os seguintes:")
print(f"Taxa de aprovação: {aprovacao:.2f}")
print(f"Taxa de rejeição: {rejeicao:.2f}")
print(f"Taxa de abstencão: {abstencao:.2f}")

if aprovacao < rejeicao:
    print("Ops... Por essa eu não esperava.")
elif rejeicao < aprovacao:
    print("YES!!! Sabia que as pessoas gostariam!")
elif rejeicao == aprovacao:
    print("Bom... Vou olhar para o copo meio cheio!")