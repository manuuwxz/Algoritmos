def contarOcorrencias(vetor, alvo):
    contador = 0
    for numero in vetor:
        if numero == alvo:
            contador += 1
            
    return contador

meuVetor = [5, 8, 2, 5, 9, 5, 1, 8, 5]

numeroAlvo1 = 5   
numeroAlvo2 = 9   
numeroAlvo3 = 7  

resultado1 = contarOcorrencias(meuVetor, numeroAlvo1)
print(f"O número {numeroAlvo1} aparece {resultado1} vez(es) no vetor.")

resultado2 = contarOcorrencias(meuVetor, numeroAlvo2)
print(f"O número {numeroAlvo2} aparece {resultado2} vez(es) no vetor.")

resultado3 = contarOcorrencias(meuVetor, numeroAlvo3)
print(f"O número {numeroAlvo3} aparece {resultado3} vez(es) no vetor.")