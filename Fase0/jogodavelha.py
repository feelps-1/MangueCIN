jogo = input()

if jogo.count("O") >= 2 or jogo.count("X") > 2:
    print("?")
elif jogo[1] == "O":
    print("*")
else:
    print("Alice")