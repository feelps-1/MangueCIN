from decimal import Decimal, getcontext

getcontext().prec = 15

veiculos = int(input())
atrasoveiculos = Decimal(veiculos) * Decimal('0.6')

acidente = input()
distancia = float(input())
codigo = input()
serializada = ""

#calcula opção A

djato = Decimal(distancia) * Decimal('0.8')
dcarro = Decimal(distancia) * Decimal('0.2')

vjato = Decimal(djato) / Decimal('1089')
vcarro = Decimal(dcarro) / Decimal('60')

tempojato = Decimal(vjato) * Decimal('60') + Decimal(vcarro) * Decimal('60') + Decimal(atrasoveiculos)

tempojato = Decimal(tempojato) * Decimal('10') / Decimal('10')

#calcula opção B

tempoonibus = Decimal(distancia) / Decimal('40') * Decimal('60') + Decimal(atrasoveiculos)

tempoonibus = Decimal(tempoonibus) * Decimal('10') / Decimal('10')

if acidente == "sim":
    tempojato += Decimal('20')
    tempoonibus += Decimal('20')

#calcula opção C

tempoheli = Decimal(distancia) / Decimal('6') * Decimal('5')

tempoheli = Decimal(tempoheli) * Decimal('10') / Decimal('10')

print("Análise das opções de transporte até o show!")
print(f"Opção A - Você chegará ao show em {tempojato:.1f} minutos")
print(f"Opção B - Você chegará ao show em {tempoonibus:.1f} minutos")
print(f"Opção C - Você chegará ao show em {tempoheli:.1f} minutos")

#senha

print("---")

for i in range(len(codigo)):
    if int(codigo[i]) % 2 == 0:
        parte = codigo[i] + "23"
        serializada += parte
        parte = ""
    else:
        parte = codigo[i] + "78"
        serializada += parte
        parte = ""

print(f"Senha de serialização transformada: {serializada}, guarde com segurança!")


