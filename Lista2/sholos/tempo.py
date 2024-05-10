from decimal import Decimal, getcontext
getcontext().prec = 15

quantidadeVeiculos = Decimal(input())
acidenteInfo = input()

if acidenteInfo == 'sim':
    acidenteInfo = Decimal('20')
else:
    acidenteInfo = Decimal('0')
distanciaTotal = Decimal(input())
codigoSerializacao = input()
serializacao = ''

print('Análise das opções de transporte até o show!')

tempoNecessario = Decimal(distanciaTotal * Decimal('0.8') / Decimal('1089') * Decimal('60') + distanciaTotal * Decimal('0.2') + quantidadeVeiculos * Decimal('36') / Decimal('60') + acidenteInfo)
print(f'Opção A - Você chegará ao show em {tempoNecessario:.1f} minutos')

tempoNecessario = Decimal(distanciaTotal / Decimal('40') * Decimal('60') + quantidadeVeiculos * Decimal('36') / Decimal('60') + acidenteInfo)
print(f'Opção B - Você chegará ao show em {tempoNecessario:.1f} minutos')

tempoNecessario = Decimal(distanciaTotal / Decimal('360') * Decimal('60') * Decimal('5'))
print(f'Opção C - Você chegará ao show em {tempoNecessario:.1f} minutos')

print('---')

for c in codigoSerializacao:
    if int(c) % Decimal('2') == Decimal('0'):
        serializacao += c + '23'
    else:
        serializacao += c + '78'

print(f'Senha de serialização transformada: {serializacao}, guarde com segurança!')
