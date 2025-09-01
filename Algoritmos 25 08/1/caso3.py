#Escreva um programa que:
#1. Receba 10 números inteiros digitados pelo usuário.
#2. Separe-os em duas listas: pares e ímpares.
#3. Exiba quantos números pares e ímpares foram digitados.

par = []
impar = []

print("Digite 10 números: ")

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
        
print("\n   Resultado    ")
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")
print(f"\nTotal de números pares: {len(par)}")
print(f"Total de números ímpares: {len(impar)}")