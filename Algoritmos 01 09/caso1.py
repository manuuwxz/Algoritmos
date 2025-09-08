# Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve
# conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e
# manipular essas informações.
# Exemplo:#produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
# #print(f"O produto {produto["nome"]} custa R${produto["preco"]}")

produtos = [
    {"nome": "Arroz", "preco": 25.90, "estoque": 100},
    {"nome": "Feijão", "preco": 8.50, "estoque": 50},
    {"nome": "Macarrão", "preco": 4.20, "estoque": 80}
]

for produto in produtos:
    print(f"O produto {produto['nome']} custa R${produto['preco']}")