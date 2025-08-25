nomes = ["Lucas", "João", "Maria", "Pedro", "Ana", "Elena", "Lorena", "Yuri", "Eduarda"]

busca = input("Digite o nome que você quer encontrar: ")

posicao = -1

for indice, nomeLista in enumerate(nomes):
    if nomeLista.strip().lower() == busca.strip().lower():
        encontrado = indice
        break

if posicao != -1:
    print(f"O nome {busca} foi encontrado na posição {encontrado}")

else:
    print(f"O nome {busca} não foi encontardo na lista")    