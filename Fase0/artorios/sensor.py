from math import floor

quadrado = input().split()

quadrado = list(map(int, quadrado))

##oii não me julgue taa?
sensores = int(input())
cobertura = 0
for i in range(sensores):
    alcance = list(map(int, input().split()))
    acabou = False
    x = alcance[0]
    y = alcance[1]
    r = alcance[2]
    if r >= x:
        xto0 = x - 1
    else:
        xto0 = r
    if r + x <= quadrado[0]:
        xtomax = r
    else:
        xtomax = abs(quadrado[0] - x)

    rx = xtomax + xto0 + 1

    if r >= y:
        yto0 = y - 1
    else:
        yto0 = r

    if r + y <= quadrado[1]:
        ytomax = r
    else:
        ytomax = abs(quadrado[1] - y)

    ry = ytomax + yto0 + 1

    cobertura += ry * rx

print(floor(cobertura / (quadrado[0] * quadrado[1])))
