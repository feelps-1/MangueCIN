numero = input()
print(numero)
resto = ""

acabou = False

while not acabou:
    if len(numero) == 1:
        print(numero)
        break

    unidade = int(numero[len(numero) - 1])
    for i in range(len(numero) - 1):
        resto += numero[i]

    resultado = (int(resto) * 3) + unidade

    print(resultado)

    strresult = str(resultado)
    numero = strresult
    resto = ""

    if len(strresult) == 1:
        acabou = True
    