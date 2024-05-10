nomeOuvinte = input()
quantidadeMusicas = int(input())
quantidadeMaisOuvida = 0
quantidadeMenosOuvida = 9999

if quantidadeMusicas == 0:
    print(f'{nomeOuvinte} é team Taylor e não ouviu Kanye West')
elif quantidadeMusicas == 1:
    musica = input()
    quantidadeStreams = int(input())
    print(f'A única música que {nomeOuvinte} ouviu foi {musica} com {quantidadeStreams} streams')
else:
    for c in range(quantidadeMusicas):
        musica = input()
        quantidadeStreams = int(input())

        if quantidadeStreams > quantidadeMaisOuvida:
            maisOuvida = musica
            quantidadeMaisOuvida = quantidadeStreams
        
        if quantidadeStreams < quantidadeMenosOuvida:
            menosOuvida = musica
            quantidadeMenosOuvida = quantidadeStreams

    print(f'A música que {nomeOuvinte} mais ouviu foi {maisOuvida} com {quantidadeMaisOuvida} streams')
    if quantidadeMenosOuvida != quantidadeMaisOuvida:
        print(f'A música que {nomeOuvinte} menos ouviu foi {menosOuvida} com {quantidadeMenosOuvida} streams')
