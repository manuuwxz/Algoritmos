def encontrarIntervalo(vetor, alvo):
    def buscaPrimeiraOcorrencia(vetor, alvo):
        inicio, fim = 0, len(vetor) - 1
        primeiroIndice = -1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if vetor[meio] == alvo:
                primeiroIndice = meio
                fim = meio - 1  
            elif alvo < vetor[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
        return primeiroIndice

    def buscaUltimaOcorrencia(vetor, alvo):
        inicio, fim = 0, len(vetor) - 1
        ultimoIndice = -1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if vetor[meio] == alvo:
                ultimoIndice = meio
                inicio = meio + 1  
            elif alvo < vetor[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
        return ultimoIndice

    primeiro = buscaPrimeiraOcorrencia(vetor, alvo)
    if primeiro == -1:
        return -1, -1
        
    ultimo = buscaUltimaOcorrencia(vetor, alvo)
    return primeiro, ultimo

meuVetor = [1, 3, 5, 5, 5, 5, 8, 9, 9, 12, 12]
alvo1 = 5
alvo2 = 9
alvo3 = 1
alvo4 = 7 

print(f"Vetor de busca: {meuVetor}\n")

print(f"Buscando pelo intervalo do número {alvo1}...")
intervalo1 = encontrarIntervalo(meuVetor, alvo1)
if intervalo1[0] != -1:
    print(f"O número {alvo1} foi encontrado no intervalo de índices: {intervalo1[0]} a {intervalo1[1]}")
else:
    print(f"O número {alvo1} não foi encontrado.")


print(f"Buscando pelo intervalo do número {alvo2}...")
intervalo2 = encontrarIntervalo(meuVetor, alvo2)
if intervalo2[0] != -1:
    print(f"O número {alvo2} foi encontrado no intervalo de índices: {intervalo2[0]} a {intervalo2[1]}")
else:
    print(f"O número {alvo2} não foi encontrado.")


print(f"Buscando pelo intervalo do número {alvo4}...")
intervalo4 = encontrarIntervalo(meuVetor, alvo4)
if intervalo4[0] != -1:
    print(f"O número {alvo4} foi encontrado no intervalo de índices: {intervalo4[0]} a {intervalo4[1]}")
else:
    print(f"O número {alvo4} não foi encontrado.")