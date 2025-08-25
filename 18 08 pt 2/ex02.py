senhaCorreta = "senha123"
tentativas = 0
tentativasTotais = 3
login = False

while tentativas < tentativasTotais:
    senha = input("Digite a senha: ")

    tentativas = tentativas + 1

    if senha == senhaCorreta:
        print("Bem Vindo(a)!")
        login = True
        break
    else:
        tentRestantes = tentativasTotais - tentativas
        print(f"Senha incorreta. Você ainda tem {tentRestantes} tentativa(s)")

if not login:
    print("Acesso bloqueado")