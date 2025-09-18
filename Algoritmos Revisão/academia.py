atletas = [
    {
        "Nome": "Lucas",
        "Idade": 25,
        "Esportes": ["Luta", "Corrida", "Musculação"],
        "Treinos": {"Luta": 7, "Corrida": 15, "Musculação": 8}
    },
    {
        "Nome": "Emanuelly",
        "Idade": 19,
        "Esportes": ["Yoga", "Musculação"],
        "Treinos": {"Yoga": 9, "Musculação": 4}
    },
    {
        "Nome": "Elena",
        "Idade": 20,
        "Esportes": ["Pilates", "Musculação"],
        "Treinos": {"Pilates": 5, "Musculação": 2}
    },
    {
        "Nome": "Erick",
        "Idade": 23,
        "Esportes": ["Futebol", "Volei"],
        "Treinos": {"Futebol": 10, "Volei": 3}
    },
    {
        "Nome": "Luisa",
        "Idade": 28,
        "Esportes": ["Natação"],
        "Treinos": {"Natação": 3}
    },
]

def calculoMedia(atletas, esporte):
    idades = 0
    totalAtletas = 0
    
    for atleta in atletas:
        if esporte in atleta["Esportes"]:
            idades += atleta["Idade"]
            totalAtletas += 1
            
    media = idades / totalAtletas
    return media

esportesMedia = set()
for atleta in atletas:
    for esporte in atleta["Esportes"]:
        esportesMedia.add(esporte)
        
resultados = {}

for esporte in esportesMedia:
    media = calculoMedia(atletas, esporte)
    resultados[esporte] = media
    
for esporte, media in resultados.items():
    print(f"A média de idades dos atletas de {esporte} é: {media:.2f}")
    
def maisTreinado(atleta):
    treinos = atleta["Treinos"]
    
    esporte = max(treinos, key=treinos.get)
    return esporte

for atleta in atletas:
    esporteFav = maisTreinado(atleta)
    print(f"O esporte que {atleta['Nome']} mais treinou é: {esporteFav}.")

def esportesTreinados(atletas):
    nomes = []
    for atleta in atletas:
        if len(atleta["Esportes"]) > 1:
            nomes.append(atleta["Nome"])
            
            
    return nomes
    
listaNomes = esportesTreinados(atletas)
print(listaNomes)