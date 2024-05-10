n = int(input())
aprovacao = 0
abstencao = 0
rejeicao = 0

for c in range(n):
    resposta = input()
    if resposta == 'Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!':
        aprovacao += 1
    elif resposta == 'Não gostei. Muito sem graça, onde já se viu nome com duas letras?':
        rejeicao += 1
    elif resposta == 'Ainda estou me acostumando. Não tenho uma opinião formada sobre isso.':
        abstencao += 1

totais = aprovacao + abstencao + rejeicao
taxaAprovacao = aprovacao / totais * 100
taxaRejeicao = rejeicao / totais * 100
taxaAbstencao = abstencao / totais * 100

print('A pesquisa terminou e os resultados foram os seguintes:')
print(f'Taxa de aprovação: {taxaAprovacao:.2f}')
print(f'Taxa de rejeição: {taxaRejeicao:.2f}')
print(f'Taxa de abstenção: {taxaAbstencao:.2f}')

if taxaAprovacao > taxaRejeicao:
    print('YES!!! Sabia que as pessoas gostariam!')
elif taxaAprovacao < taxaRejeicao:
    print('Ops... Por essa eu não esperava.')
elif taxaAprovacao == taxaRejeicao:
    print('Bom... Vou olhar para o copo meio cheio!')
