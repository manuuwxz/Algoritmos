def buscaNomes(listaNomes, nomeAlvo):
    for indice, nome in enumerate(listaNomes):
        if nome.strip().lower() == nomeAlvo.strip().lower():
            return indice
    return -1

print("    Cadastro de Nomes    ")
nomes = []
while True:
    nomeDigitado = input("Digite um nome (ou digite 'fim' para parar): ")
    if nomeDigitado.lower() == 'fim':
        break
    
    nomes.append(nomeDigitado)

print("\nLista de nomes cadastrados:", nomes)

if nomes: 
    print("\n    Busca de Nome    ")
    nomeBuscar = input("Qual nome você quer procurar? ")

    resultado = buscaNomes(nomes, nomeBuscar)

    if resultado != -1:
        print(f"\nO nome '{nomeBuscar}' foi encontrado na posição {resultado} da lista.")
    else:
        print(f"\nO nome '{nomeBuscar}' não está na lista.")
else:
    print("\nA lista está vazia, não há nomes para buscar.")