def numero():
    numUm = int(input("Digite o primeiro número: "))

    numDois = int(input("Digite o segundo número: "))

    if numUm > numDois:
        print(f"O número {numUm} é maior que o número {numDois}")

    elif numDois > numUm:
        print(f"O número {numDois} é maior que o número {numUm}")

numero()