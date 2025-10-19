def buscaBinaria(vetor, alvo, inicio, fim):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2
    valorMeio = vetor[meio]

    if valorMeio == alvo:
        return meio 
    elif alvo < valorMeio:
        return buscaBinaria(vetor, alvo, inicio, meio - 1)
    else: 
     return buscaBinaria(vetor, alvo, meio + 1, fim)

meuVetor = [5, 12, 18, 24, 30, 41, 58, 64, 79, 95]
alvoExistente = 41
alvoInexistente = 50

print(f"Vetor para busca: {meuVetor}\n")

tamanhoLista = len(meuVetor)

print(f"Buscando (recursivamente) pelo número {alvoExistente}...")
resultado1 = buscaBinaria(meuVetor, alvoExistente, 0, tamanhoLista - 1)

if resultado1 != -1:
    print(f"Elemento {alvoExistente} foi encontrado no índice {resultado1}.")
else:
    print(f"Elemento {alvoExistente} não foi encontrado.")


print(f"Buscando (recursivamente) pelo número {alvoInexistente}...")
resultado2 = buscaBinaria(meuVetor, alvoInexistente, 0, tamanhoLista - 1)

if resultado2 != -1:
    print(f"Elemento {alvoInexistente} foi encontrado no índice {resultado2}.")
else:
    print(f"Elemento {alvoInexistente} não foi encontrado.")