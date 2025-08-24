numeros = int(input("Quantos números serão calculados: "))
number = []

for i in range(numeros):
    num = input(f"Digite o {i+1}º número: ")
#    num.to
    if "," in num:
        num = num.replace(",",".")
        
    num = float(num)
    number.append(num)

if len(number) > 0:
    somar = sum(number)

    media = somar / len(number)

    print(f"\n A lista de números é: {number}")
    print(f"A média dos números é: {media:.2f}")

