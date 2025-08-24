def tabuada():

    num = int(input("Digite um número para ver a sua tabuada: "))
    
    for i in range (1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

tabuada()

