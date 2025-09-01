import math

distancias = []

for i in range(6):
    km = float(input(f"Digite a distância da viagem {i+1} (em km): "))
    distancias.append(km)

total = sum(distancias)
maior = max(distancias)
menor = min(distancias)
media = total / len(distancias)
media_ceil = math.ceil(media)

print("\n=== Relatório de Viagens ===")
print(f"Distâncias registradas: {distancias}")
print(f"Distância total percorrida: {total} km")
print(f"Maior distância: {maior} km")
print(f"Menor distância: {menor} km")
print(f"Média das distâncias (arredondada p/ cima): {media_ceil} km")
