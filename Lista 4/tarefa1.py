import random
import time
import tracemalloc

def buscaSequencial(lista, chave): 
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
            return indice
    return -1

def buscaBinaria(lista, chave): 
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == chave:
            return pos_meio
        elif lista[pos_meio] > chave: 
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return -1

print("Gerando lista com 1.000.000 de elementos...")

listaGrande = [random.randint(1, 2000000) for i in range(1000000)]

listaOrdenada = sorted(listaGrande)

chaveBusca = listaOrdenada[-1]
print("Lista pronta. Iniciando testes...\n")


print("      Testando Busca Sequencial      ")
tracemalloc.start()
inicio = time.time()

buscaSequencial(listaOrdenada, chaveBusca)

final = time.time()
memoriaAtual, memoriaPico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.6f} segundos")
print(f"A memória atual é: {memoriaAtual/1024:.3f} KB")
print(f"O pico de memória é: {memoriaPico/1024:.3f} KB\n")


print("    Testando Busca Binária    ")
tracemalloc.start()
inicio = time.time()


buscaBinaria(listaOrdenada, chaveBusca)

final = time.time()
memoriaAtual, memoriaPico = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"O tempo de execução é: {final-inicio:.6f} segundos")
print(f"A memória atual é: {memoriaAtual/1024:.3f} KB")
print(f"O pico de memória é: {memoriaPico/1024:.3f} KB")