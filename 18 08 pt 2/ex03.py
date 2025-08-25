notas = []

print("Digite as notas dos alunos. (Digite -1 para parar)")

while True:
    notDig = input("Nota: ")
    if notDig == "-1":
        break

    if "," in notDig:
        notDig = notDig.replace(",",".")
    nota = float(notDig)
    notas.append(nota)

if notas:
    soma = sum(notas)

    total = len(notas)    

    media = soma / total

    notaMax = max(notas)

    notaMin = min(notas)

    acMedia = 0
    
    for nota in notas:
        if nota > media:
            acMedia += 1

    
    acMediaPor = (acMedia / total) * 100

    print("\nResultados")
    print(f"A média da turma é: {media:.2f}")

    print(f"A maior nota é: {notaMax}")
    print(f"A menor nota é: {notaMin}")

    print(f"Alunos acima da média: {acMediaPor}")

else:
    print("Nenhuma nota foi digitada")    