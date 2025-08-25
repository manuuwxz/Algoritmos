#Escreva um algoritmo que conte quantas operações básicas (somas) são executadas para calcular a soma dos números de 1 até n. 
# Exiba o resultado e compare com a fórmula matemática n*(n+1)/2.


n = int(input("Digite um número para N: "))

soma = 0
operacao = 0

for i in range(1, n + 1):
    soma = soma + i
    operacao = operacao + 1

formula = (n * (n + 1)) / 2
formulaOp = 3    

print("\nResultado do Algoritmo")
print(f"A soma dos números de 1 até {n} é: {soma}")
print(f"O número de operações de soma realizadas foi: {operacao}")

print("\nFórmula Matemática")
print(f"A soma pela fórmula é: {formula}")
print(f"O número de operações básicas da fórmula é: {formulaOp}")

print("\nComparar")
if soma == formula:
    print("Os resultados da soma estão iguais")
else:
    print("Os resultados da soma estão diferentes")