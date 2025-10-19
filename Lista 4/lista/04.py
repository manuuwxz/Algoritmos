def encontrarMenorNumero(vetor):
    if not vetor:
        return None

    menorNumero = vetor[0]
    
    for numero in vetor:
        if numero < menorNumero:
            menorNumero = numero
            
    return menorNumero

meuVetor = [77, 15, 9, 34, 56, 2, 81]

print(f"O vetor é: {meuVetor}")
menor = encontrarMenorNumero(meuVetor)
print(f"Usando busca linear, o menor número encontrado foi: {menor}")