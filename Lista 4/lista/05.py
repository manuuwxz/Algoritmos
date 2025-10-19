def buscaBinariaVerificacao(vetorOrdenado, alvo):
    posicaoInicial = 0
    posicaoFinal = len(vetorOrdenado) - 1

    while posicaoInicial <= posicaoFinal:
        posicaoMeio = (posicaoInicial + posicaoFinal) // 2
        valorMeio = vetorOrdenado[posicaoMeio]
        
        if valorMeio == alvo:
            return posicaoMeio 
        elif alvo < valorMeio:
            posicaoFinal = posicaoMeio - 1
        else: 
            posicaoInicial = posicaoMeio + 1

    return -1

meuVetor = [10, 21, 35, 48, 55, 69, 72, 88, 93, 104]
alvoExistente = 72
alvoInexistente = 50

print(f"Vetor para busca: {meuVetor}\n")

print(f"Buscando pelo número {alvoExistente}...")
resultado1 = buscaBinariaVerificacao(meuVetor, alvoExistente)

if resultado1 != -1:
    print(f"Elemento {alvoExistente} existe e foi encontrado no índice {resultado1}.")
else:
    print(f"Elemento {alvoExistente} não foi encontrado.")



print(f"Buscando pelo número {alvoInexistente}...")
resultado2 = buscaBinariaVerificacao(meuVetor, alvoInexistente)

if resultado2 != -1:
    print(f"Elemento {alvoInexistente} existe e foi encontrado no índice {resultado2}.")
else:
    print(f"Elemento {alvoInexistente} não foi encontrado.")