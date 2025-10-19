import random
import time

def buscaLinear(lista, alvo):
    for indice, elemento in enumerate(lista):
        if elemento == alvo:
            return indice
    return -1

def buscaBinaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

print("Gerando uma lista com 1.000.000 de elementos...")
listaGrande = [random.randint(1, 2000000) for _ in range(1000000)]

listaOrdenada = sorted(listaGrande)
print("Lista pronta e ordenada. Iniciando a comparação...\n")

alvo = listaOrdenada[-1]

print("    Testando Busca Linear    ")
inicioLinear = time.time()

resultadoLinear = buscaLinear(listaOrdenada, alvo)

fimLinear = time.time() 
tempoExecucaoLinear = fimLinear - inicioLinear

print(f"Elemento encontrado no índice: {resultadoLinear}")
print(f"Tempo de execução: {tempoExecucaoLinear:.6f} segundos")


print("    Testando Busca Binária    ")
inicioBinaria = time.time() 

resultadoBinaria = buscaBinaria(listaOrdenada, alvo)

fimBinaria = time.time() 
tempoExecucaoBinaria = fimBinaria - inicioBinaria

print(f"Elemento encontrado no índice: {resultadoBinaria}")
print(f"Tempo de execução: {tempoExecucaoBinaria:.6f} segundos")

print("\nComparação Final:")

if tempoExecucaoBinaria > 0:
    diferenca = tempoExecucaoLinear / tempoExecucaoBinaria
    print(f"A busca binária foi aproximadamente {diferenca:.0f} vezes mais rápida que a busca linear.")
else:
    print("A busca binária foi tão rápida que seu tempo de execução foi próximo de zero e muito mais eficiente que a busca linear.")