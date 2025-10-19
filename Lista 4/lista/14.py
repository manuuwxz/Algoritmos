def meuIndex(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    
    raise ValueError(f"'{valor}' não está na lista")

minhaLista = ['banana', 'maçã', 'uva', 'pera', 'maçã', 'laranja']

try:

    indiceUva = meuIndex(minhaLista, 'uva')
    print(f"O valor 'uva' foi encontrado no índice: {indiceUva}")

    indiceMaca = meuIndex(minhaLista, 'maçã')
    print(f"O valor 'maçã' foi encontrado pela primeira vez no índice: {indiceMaca}")

except ValueError as e:
    print(f"Erro: {e}")

try:
    print("Tentando encontrar o valor 'abacaxi'...")
    indiceAbacaxi = meuIndex(minhaLista, 'abacaxi')
    print(f"O valor 'abacaxi' foi encontrado no índice: {indiceAbacaxi}")

except ValueError as e:
    print(f"Erro ao buscar 'abacaxi': {e}")