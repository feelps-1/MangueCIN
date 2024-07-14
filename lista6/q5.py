musicas = {
    "Samba": ['Preciso Me Encontrar', 'O Mundo É Um Moinho', 'Trem Das Onze', 
            'O Que É O Que É?', 'Disritmia', 'Timoneiro'],
    "Rock Nacional": ['Epitáfio', 'Meu Novo Mundo', 'À Sua Maneira', 'Que País É Este', 
                    'Um Minuto Para O Fim Do Mundo', 'Infinita Highway'],
    "Rock": ['Smells Like Teen Spirit', 'In The End', 'Californication', 'Welcome To The Jungle', 'Another Brick In The Wall', 
            'Bohemian Rapsody', 'Bring Me To Life', 'Paint It, Black', 'Stairway To Heaven'],
    "Pop": ['As It Was', 'Viva La Vida', 'Someone Like You', 'Blinding Lights', 'Maps', 'Talking To The Moon', 
            'Believer', 'Ghost', 'Wake Me Up', 'Rude', 'Perfect'],
    "MPB": ['O Descobridor Dos Sete Mares', 'Anunciação', 'Exagerado', 'João E Maria', 'Sujeito De Sorte', 
            'Naquela Mesa', 'Eduardo E Mônica', 'Lanterna Dos Afogados', 'Metamorfose Ambulante'],
    "Manguebeat": ['Da Lama Ao Caos', 'A Praieira', 'Maracatu Atômico', 'Manguetown', 'Um Sonho', 'A Cidade'],
    "Indie Folk": ['Ends Of The Earth', 'Welcome Home, Son', 'Riptide', 'Father And Son', 
                'Ho Hey', 'The Night We Met', 'Budapest', 'Atlantis'],
    "Forró": ['Xote Das Meninas', 'Xote Da Alegria', 'Deus Me Proteja', 'Numa Sala De Reboco', 
            'Meu Cenário', 'Colo De Menina', 'Riacho Do Navio']
}

padrao = ["Preciso Me Encontrar", 'Epitáfio', 'Smells Like Teen Spirit', 'As It Was', 
        'O Descobridor Dos Sete Mares', 'Da Lama Ao Caos', 'Ends Of The Earth', 'Xote Das Meninas']

ouvidas = {genero: 0 for genero in musicas}

def recomendar(repertorio, gosto):
    playlist, jaRecomendou = [], []
    vazio = []
    ranking = sorted(gosto, key=gosto.get, reverse=True)
    generosOuvidos = [k for k, v in gosto.items() if v != 0]

    primeiro = max(gosto.values())
    semPrimeiro = [x for x in gosto.values() if x != primeiro]
    segundo = max(semPrimeiro) if semPrimeiro else primeiro

    for p in repertorio:
        if not repertorio[p]:
            vazio.append(p)

    for p in ranking:
        if gosto[p] == 0:
            jaRecomendou.append(p)
        elif gosto[p] == primeiro and p not in jaRecomendou:
            if len(repertorio[p]) < 3:
                playlist.append(repertorio[p][:len(repertorio[p])])
            else:
                playlist.append(repertorio[p][:3])
        elif gosto[p] == segundo and p not in jaRecomendou:
                if len(repertorio[p]) < 2:
                    playlist.append(repertorio[p][:len(repertorio[p])])
                else:
                    playlist.append(repertorio[p][:2])

        elif p not in jaRecomendou:
                if len(repertorio[p]) < 1:
                    pass
                else:
                    playlist.append(repertorio[p][:1])

        jaRecomendou.append(p)

    if vazio == generosOuvidos:
        return [0, generosOuvidos]

    return playlist

nome = input()
nMusicas = int(input())

for i in range(nMusicas):
    musica = input()

    for j in musicas:
        if musica in musicas[j]:
            ouvidas[j] += 1
            musicas[j].remove(musica)


if nMusicas!= 0:
    recomendacao = recomendar(musicas, ouvidas)

    if recomendacao[0] == 0:
        recomendacao.pop(0)
        recomendacao = [x for sublista in recomendacao for x in sublista]
        if len(recomendacao) == 1:
            res = recomendacao[0]
        else:
            res = ", ".join(recomendacao[:-1]) + f" e {recomendacao[-1]}"
        print(f"{nome} já escutou todas as músicas disponíveis no(s) gênero(s): {res}. Infelizmente não sobrou nenhuma música disponível para recomendação.")
    else:
        recomendacao = [x for sublista in recomendacao for x in sublista]
        print(f"{nome} escutou {nMusicas} música(s) e estas são as próximas recomendações:\n")
        for l in range(len(recomendacao)):
            print(f"{l+1}. {recomendacao[l]}")   
    
else:
    print(f"Parece que {nome} não escutou nenhuma música. Vamos recomendar algumas músicas de gêneros diferentes:\n")
    for l in range(len(padrao)):
        print(f"{l+1}. {padrao[l]}")



        