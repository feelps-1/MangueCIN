nome = input()
qntd = int(input())
streamsmaisouvida = 0
streamsmenosouvida = 1000

if qntd == 0:
    print(f"{nome} é team Taylor e não ouviu Kanye West")
elif qntd == 1:
    musica = input()
    streams = int(input())
    print(f"A única música que {nome} ouviu foi {musica} com {streams} streams")
else:
    while qntd != 0:
        musica = input()
        streams = int(input())

        if streams > streamsmaisouvida:
            maisouvida = musica
            streamsmaisouvida = streams

        if streams < streamsmenosouvida:
            menosouvida = musica
            streamsmenosouvida = streams
        qntd -= 1

    print(f"A música que {nome} mais ouviu foi {maisouvida} com {streamsmaisouvida} streams")
    if streamsmaisouvida != streamsmenosouvida:
        print(f"A música que {nome} menos ouviu foi {menosouvida} com {streamsmenosouvida} streams")

 

