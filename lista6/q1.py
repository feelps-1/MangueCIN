def cadastro(nome, artista, lancamento, genero, catalogo):
    album = (nome, artista, lancamento)

    if genero in catalogo:    
        print("Este foi o novo álbum adicionado:")
        print(f"- {nome} do/da artista/banda {artista} lançado em {lancamento}")
    else:
        print("Este foi o novo álbum adicionado:")
        print(f"- {nome} do/da artista/banda {artista} lançado em {lancamento}")
        print("Oba, você adicionou um novo estilo musical ao catálogo!")
        catalogo[genero] = []

    catalogo[genero].append(album)

    return catalogo

def consulta(genero, catalogo):
    if genero in catalogo:
        print(f"Nessa galeria há {len(catalogo[genero])} albuns de {genero}. Os albuns encontrados foram:")

        for i in catalogo[genero]:
            print(f"- {i[0]} do/da artista/banda {i[1]} lançado em {i[-1]}")
    else:
        print("Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!")


cat = {"Rock": [("Abbey Road", "The Beatles", "1969"), ("The Dark Side of the Moon", "Pink Floyd", "1973"), ("Riot!", "Paramore", "2007")], 
       "Pop": [("Fearless", "Taylor Swift", "2008")], 
       "Manguebeat": [("Da Lama ao Caos", "Chico Science e Nação Zumbi", "1994")], 
       "MPB": [("Gal Costa", "Gal Costa", "1969"), ("Sim", "Vanessa da Mata", "2007"), ("Alucinação", "Belchior", "1976")], 
       "Forró": [("As 20 Melhores", "Luiz Gonzaga", "2004"), ("O Melhor de Dominguinhos", "Dominguinhos", "2013")], 
       "Samba": [("Samba Esquema Novo", "Jorge Ben Jor", "1963")]}

funciona = True

while funciona:
    comando = input()

    if comando == "CONSULTAR":
        gen = input()
        consulta(gen, cat)
    elif comando == "FIM":
        funciona = False
    else:
        art, ano, gen = input(), input(), input()
        cat = cadastro(comando, art, ano, gen, cat)