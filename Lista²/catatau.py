itens = [x for x in input().split(", ")]

necessarios = [x for x in input().split(", ")]

tem = 0

faltantes = 0

for i in range(len(itens)):
    if itens[i] in necessarios:
        tem += 1

if tem != 0:
  tem = 0
  print("Estes são os itens que já tenho na fazenda:")
  for j in range(len(itens)):
    if itens[j] in necessarios:
      tem += 1
      print(f"{tem}º item: {itens[j]}")

  if len(necessarios) == tem:
    faltantes = 0
  else:
    faltantes = len(necessarios) - tem

  if faltantes != 0:
    print(f"Vou precisar adquirir {faltantes} itens antes do festival!")
  else:
    print(f"Perfeito, encontrei todos os {len(necessarios)} itens aqui na fazenda!")

  print("Estou pronto para o festival de Stardew Valley! Que comece a diversão!")
else:
    print(f"Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {len(necessarios)} itens aqui na fazenda.")