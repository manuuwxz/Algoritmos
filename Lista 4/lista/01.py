def buscaLinearSimples(vetor, alvo):
    for indice, numero in enumerate(vetor):
        if numero == alvo:
            return indice
    
    return -1


meuVetor = [10, 4, 33, 21, 5, 98, 45, 16]
numeroAlvo1 = 98 
numeroAlvo2 = 50  

print(f"Buscando o número {numeroAlvo1} no vetor...")
resultado1 = buscaLinearSimples(meuVetor, numeroAlvo1)

if resultado1 != -1:
    print(f"Sucesso! O número {numeroAlvo1} foi encontrado no índice: {resultado1}\n")
else:
    print(f"O número {numeroAlvo1} não foi encontrado no vetor.\n")


print(f"Buscando o número {numeroAlvo2} no vetor...")
resultado2 = buscaLinearSimples(meuVetor, numeroAlvo2)

if resultado2 != -1:
    print(f"Sucesso! O número {numeroAlvo2} foi encontrado no índice: {resultado2}")
else:
    print(f"O número {numeroAlvo2} não foi encontrado no vetor.")