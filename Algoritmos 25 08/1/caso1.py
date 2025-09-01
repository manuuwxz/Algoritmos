#Crie um programa que:
#1. Receba as temperaturas de 7 dias e armazene em uma lista.
#2. Mostre a média das temperaturas da semana.
#3. Informe o dia mais quente e o dia mais frio.
#4. Mostre quantos dias ficaram acima da média

temperatura = []

semana = ["Segunda Feira", "Terça Feira", "Quarta Feira", "Quinta Feira", "Sexta Feira", "Sábado", "Domingo"]

print("Digite as temperaturas da semana: ")

for i in range(7):
    temp = float(input(f"Temperatura de {semana[i]}: "))
    temperatura.append(temp)
    
    

soma = sum(temperatura)
media = soma / len(semana)
print(f"\n A media das temperaturas da semana foi: {media:.2f} ºC")

temperaturaMaxima = max(temperatura)
temperaturaMinima = min(temperatura)

quente = temperatura.index(temperaturaMaxima)
frio = temperatura.index(temperaturaMinima)

print(f"O dia mais quente foi {semana[quente]}, com {temperaturaMaxima} ºC")
print(f"O dia mais frio foi {semana[frio]}, com {temperaturaMinima} ºC")


acimaMedia = 0
for temp in temperatura:
    if temp > media:
        acimaMedia += 1
        
print(f"\n{acimaMedia} dias ficaram acima da média")