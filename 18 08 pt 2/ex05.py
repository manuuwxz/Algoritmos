CPF = input("Digite seu CPF: ")

CPF = ''.join(filter(str.isdigit, CPF))

if len(CPF) > 11 or len(CPF) < 11:
    print(f"CPF invalido: {CPF}")
else:
    print(f"CPF Valido: {CPF}")