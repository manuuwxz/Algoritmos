filmes = [
    {
        "Titulo": "Avatar", 
        "Diretor": "James Cameron",
        "Bilheteria": 2923,
        "Avaliações": [10, 10, 10, 9, 10]
    },
    {
        "Titulo": "Avatar: O Caminho da Água", 
        "Diretor": "James Cameron",
        "Bilheteria": 2244,
        "Avaliações": [10, 8, 10, 9, 9]
    },
    {
        "Titulo": "Barbie", 
        "Diretor": "Greta Gerwig",
        "Bilheteria": 1440,
        "Avaliações": [10, 8, 7, 6, 9]
    },
    {
        "Titulo": "Vingadores: Ultimato", 
        "Diretor": "Anthony Russo",
        "Bilheteria": 2797,
        "Avaliações": [10, 8, 7, 6, 9]
    },
    {
        "Titulo": "Crepúsculo", 
        "Diretor": "Catherine Hardwicke",
        "Bilheteria": 393,
        "Avaliações": [5, 9, 8, 7, 9]
    },
]

def topBilheteria(filmes):
    ranking = sorted(filmes, key=lambda filme: filme["Bilheteria"], reverse=True)
    
    topTres = ranking[0:3]
    return topTres

rankBilheteria = topBilheteria(filmes)

print("    Top 3 Filmes com maior bilheteria:    ")
for filme in rankBilheteria:
    print(f"- {filme['Titulo']} (Bilheteria: ${filme['Bilheteria']}M)")
    
def topAvaliacoes(filmes):
    mediaFilmes = []
    
    for filme in filmes:
        avaliacoes = filme["Avaliações"]
        
        media = sum(avaliacoes) / len(avaliacoes)
            
        mediaFilmes.append({
            "Titulo": filme["Titulo"],
            "Media": media
        })

    topTres = sorted(mediaFilmes, key=lambda item: item["Media"], reverse=True)
    
    return topTres[0:3]

rankingAvaliacao = topAvaliacoes(filmes)

print("    Top 3 Filmes com a melhor avaliação:     ")
for filme in rankingAvaliacao:
    print(f"- {filme['Titulo']} (Média de Avaliação: {filme['Media']:.2f})")
    
def bilheteriaPorDiretor(filmes):
    totalBilheteria = {}
    
    for filme in filmes:
        diretor = filme["Diretor"]
        bilheteria = filme["Bilheteria"]
        
        if diretor in totalBilheteria:
            totalBilheteria[diretor] += bilheteria
        else:
            totalBilheteria[diretor] = bilheteria
            
        return totalBilheteria
    
bilheteriaDiretores = bilheteriaPorDiretor(filmes)

print(bilheteriaDiretores)

def campeao(filmes):
    mediaAvaliacoes = {}
    
    pontuacoes = {}
    
    maiorBilheteria = 0
    maiorMedia = 0
    
    for filme in filmes:
        titulo = filme["Titulo"]
        bilheteria = filme["Bilheteria"]
        avaliacoes = filme["Avaliações"]
        
        if bilheteria > maiorBilheteria:
            maiorBilheteria = bilheteria
        
        avaliacao = sum(avaliacoes) / len(avaliacoes)
        mediaAvaliacoes[titulo] = avaliacao
        
        if avaliacao > maiorMedia:
            maiorMedia = avaliacao
            
    for filme in filmes:
        titulo = filme["Titulo"]
        bilheteria = filme["Bilheteria"]
        
        avaliacao = mediaAvaliacoes[titulo]
        
        bilheteriaOriginal = bilheteria / maiorBilheteria
        avaliacaoOriginal = avaliacao / maiorMedia
        
        pontuacao = bilheteriaOriginal + avaliacaoOriginal
        pontuacoes[titulo] = pontuacao
        
    melhorFilme = max(pontuacoes, key=pontuacoes.get)
    
    return melhorFilme

filmeCampeao = campeao(filmes)
print(f"O filme campeão, combinando bilheteria e avaliação, é: {filmeCampeao}")
