musicas = [
    {
        "Titulo": "Mirrors",
        "Artista": "Justin Timberlake",
        "Downloads": 1330,
        "Avaliação": [5, 2, 4, 5, 3, 5]
    },
    {
        "Titulo": "Perfect",
        "Artista": "Ed Sheeran",
        "Downloads": 3619,
        "Avaliação": [3, 4, 2, 5, 3, 2]
    },
    {
        "Titulo": "Thinking out Loud",
        "Artista": "Ed Sheeran",
        "Downloads": 2886,
        "Avaliação": [3, 3, 4, 5, 5, 2]
    },
    {
        "Titulo": "Cardigan",
        "Artista": "Taylor Swift",
        "Downloads": 1765,
        "Avaliação": [4, 5, 4, 5, 3, 4]
    },
    {
        "Titulo": "Cruel Summer",
        "Artista": "Taylor Swift",
        "Downloads": 3072,
        "Avaliação": [5, 5, 4, 5, 3, 4]
    },
    {
        "Titulo": "Blank Space",
        "Artista": "Taylor Swift",
        "Downloads": 2199,
        "Avaliação": [5, 5, 2, 5, 5, 3]
    },
]

def mediaMusica():
    for musica in musicas:
        avaliacoes = musica["Avaliação"]
        media = sum(avaliacoes) / len(avaliacoes)
        
        # print(f"A média da música '{musica['Titulo']}' é: {media:.2f}")

mediaMusica()

def Downloads():
    artistasDownloads = {}
    
    for musica in musicas:
        artista = musica["Artista"]
        numeroDownloads = musica["Downloads"]
        
        if artista in artistasDownloads:
            artistasDownloads[artista] += numeroDownloads
        else:
            artistasDownloads[artista] = numeroDownloads
    
    maisDownloads = max(artistasDownloads, key=artistasDownloads.get)
    
    totalDownloads = artistasDownloads[maisDownloads]
    
    print(f"O artista com mais downloads é {maisDownloads} com um total de {totalDownloads} downloads.")

Downloads()

def ranking():
    rank = []

    for musica in musicas:
        avaliacoes = musica["Avaliação"]
        media = sum(avaliacoes) / len(avaliacoes)

        rank.append({'Titulo': musica["Titulo"], 'Media': media})

   
    rankOrdenado = sorted(rank, key=lambda item: item['Media'], reverse=True)

    print("    Ranking das Músicas    ")
    for item in rankOrdenado:
        print(f"Música: {item['Titulo']} | Média: {item['Media']:.2f}")

ranking()