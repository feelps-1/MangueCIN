albums = {
    'sweetener': {
        'pontos': 0,
        'musicas':{
            'no tears left to cry': 0,
            'the light is coming': 0,
            'better off': 0,
            'everytime': 0
        }
    },
    'thank u, next':{
        'pontos': 0,
        'musicas': {
            'NASA': 0,
            'thank u, next': 0,
            "break up with your girlfriend, i'm bored": 0,
            'bad idea': 0
        }
    },
    'Positions':{
        'pontos': 0,
        'musicas':{
            'motive': 0,
            'safety net': 0,
            'nasty': 0,
            'pov': 0
        }
    },
    'eternal sunshine':{
        'pontos': 0,
        'musicas': {
            'yes, and?': 0,
            'eternal sunshine': 0,
            'the boy is mine': 0,
            "we can't be friends": 0
        }
    }
}

def compara(codificada):
    cifra = {chr(x+3) if x+3 < 123 else chr(x-23): chr(x) for x in range(97, 123)}
    palavra = ""
    
    for i in codificada:
        if i.lower().isalpha():
            if i.isupper():
                palavra += cifra[i.lower()].upper()
            else:
                palavra += cifra[i.lower()]
        else:
            palavra += i

    return palavra

coleta = True
limite = int(input())

while coleta:
    comando = input()

    if comando != "FIM":
        musicaCodificada, yeahs = comando.split(" - ")
        yeahs = int(yeahs)
        decodificada = compara(musicaCodificada)
        print(f'O nome da música decifrada é: {decodificada}')
        achou = False

        for a in albums:
            for m in albums[a]['musicas']:
                if decodificada == m:
                    achou = True
                    print("Ótimo! A música está na discografia da nossa base de dados!")
                    print(f"O album da música decifrada é {a}")
                    albums[a]['musicas'][decodificada] += yeahs
                    albums[a]['pontos'] += yeahs

                    if yeahs >= 10:
                        print("AVISA QUE ESSA JÁ É HIT NOS CHARTS!")
                    elif yeahs > 5:
                        print("Ariana fez o dever de casa e entregou uma música na média para os seus fãs.")
                    else:
                        print("A diva do pop não se empolgou nessa e decepcionou os arianators.")
            
            if albums[a]['pontos'] >= limite:
                coleta = False
                print(f"Atenção! O limite de pontuação foi atingido pelo álbum {a}!")

        if not achou:
            print('Poxa, essa música não está na discografia da base do nosso estúdio!')
    else:
        coleta = False
        
print("Fim da análise!\n")

maior, albumVencedor = 0, ''
for a in albums:
    if albums[a]['pontos'] > maior:
        maior = albums[a]['pontos']
        albumVencedor = a

pontosMusica = max(albums[albumVencedor]['musicas'].values())
musicaVencedora = ""

for a in albums:
    for m in albums[a]['musicas']:
        if albums[a]['musicas'][m] == pontosMusica:
            musicaVencedora = m

print(f"O álbum da estrela Ariana Grande com a maior pontuação foi {albumVencedor}, com um total de {maior} pontos!")
print(f"Entre todas as faixas desse álbum, a melhor pontuada foi {musicaVencedora}, que obteve {pontosMusica} pontos")
    
