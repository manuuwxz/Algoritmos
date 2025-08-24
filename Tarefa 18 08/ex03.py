def primo(num):

    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

number = input("Digite um número e verifique se ele é primo: ")
number = int(number)
if primo(number):
    print(f'O Número {number} é primo')
else:
    print(f'O Número {number} não é primo')