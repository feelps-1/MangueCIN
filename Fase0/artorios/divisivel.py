x = input()
y = int(x)
string = x
tamanhox = len(x) - 1
Valora = 0
acabou = False
while not acabou:

    if len(string) == 1:
        print(x)
        break

    ultimo = int(string[tamanhox:])
    primeiros = int(string[:tamanhox])
    Valor = (primeiros * 3) + ultimo

    print(x)
    x = Valor
    string = str(Valor)
    tamanhox = len(string) - 1
