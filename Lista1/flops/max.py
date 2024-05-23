weather = input()
if weather == "chuvoso":
    wet = bool(input())

temp = input()
perf = input()
pos = int(input())

print("Estratégia de prova de Max Verstappen!")

if temp == "alta":
    if weather == "ensolarado":
        print("Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!")
    else:
        print("Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!")
else:
    if weather == "ensolarado":
        print("Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.")
    else:
        print("Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!")

if weather == "chuvoso" and wet:
    print("Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.")
elif weather == "chuvoso" and not wet:
    print("Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!")

if pos == 1 and perf == "bom":
    print("Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.")
elif pos == 1 and perf == "ruim":
    print("Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.")
elif pos > 1 and pos <= 12:
    print("Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
else:
    print("Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.")
