from decimal import Decimal, getcontext

getcontext().prec = 50  # Define a precisão

questoes = input()
opcao = input()
questoes = questoes.split()
grafo = Decimal(questoes[0])
dinamica = Decimal(questoes[1])
geo = Decimal(questoes[2])

if opcao == "A":
    dinamica *= Decimal('1.5')
    geo *= Decimal('2.5')
elif opcao == "B":
    grafo *= Decimal(2/5)
    geo *= Decimal(5/3)
else:
    grafo *= Decimal('0.4')
    dinamica *= Decimal('0.6')

total = int(dinamica + geo + grafo)
print(total)