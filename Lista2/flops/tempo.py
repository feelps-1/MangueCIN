veiculos = int(input())
atrasoveiculos = veiculos * 0.6

acidente = input()
distancia = float(input())
codigo = input()
serializada = ""

#calcula opção A

djato = distancia * 0.8
dcarro = distancia * 0.2

vjato = djato / 1089
vcarro = dcarro / 60

tempojato = vjato * 60 + vcarro * 60 + atrasoveiculos

tempojato = int(tempojato * 10) / 10

#calcula opção B

tempoonibus = distancia / 40 * 60 + atrasoveiculos

tempoonibus = int(tempoonibus * 10) / 10

if acidente == "sim":
    tempojato += 20
    tempoonibus += 20

#calcula opção C

tempoheli = distancia / 6 * 5

tempoheli = int(tempoheli * 10) / 10

print("Análise das opções de transporte até o show!")
print(f"Opção A - Você chegará ao show em {tempojato} minutos")
print(f"Opção B - Você chegará ao show em {tempoonibus} minutos")
print(f"Opção C - Você chegará ao show em {tempoheli} minutos")

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


