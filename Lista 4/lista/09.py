def buscaBinaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1
    resultado = -1  

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valorMeio = vetor[meio]

        if valorMeio == alvo:
            resultado = meio  
            fim = meio - 1  
        elif alvo < valorMeio:
            fim = meio - 1
        else:
            inicio = meio + 1
            
    return resultado

meuVetor = [2, 5, 8, 8, 8, 10, 12, 12, 15, 15, 15, 20]
alvo1 = 8
alvo2 = 15
alvo3 = 9 

print(f"Vetor de busca: {meuVetor}\n")

print(f"Buscando pela primeira ocorrência do número {alvo1}...")
indice1 = buscaBinaria(meuVetor, alvo1)

if indice1 != -1:
    print(f"A primeira ocorrência do {alvo1} está no índice: {indice1}")
else:
    print(f"O número {alvo1} não foi encontrado.")


print(f"Buscando pela primeira ocorrência do número {alvo2}...")
indice2 = buscaBinaria(meuVetor, alvo2)
if indice2 != -1:
    print(f"A primeira ocorrência do {alvo2} está no índice: {indice2}")
else:
    print(f"O número {alvo2} não foi encontrado.")


print(f"Buscando pela primeira ocorrência do número {alvo3}...")
indice3 = buscaBinaria(meuVetor, alvo3)
if indice3 != -1:
    print(f"A primeira ocorrência do {alvo3} está no índice: {indice3}")
else:
    print(f"O número {alvo3} não foi encontrado.")