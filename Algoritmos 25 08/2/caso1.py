
presencasSemana = {
    "Segunda": {"Ana", "Bruno", "Carlos", "Maria"},
    "Terça":   {"Ana", "Carlos", "Maria"},
    "Quarta":  {"Ana", "Bruno", "Maria"},
    "Quinta":  {"Ana", "Bruno", "Carlos", "Maria"},
    "Sexta":   {"Ana", "Carlos", "Maria"}
}

todosAlunos = set().union(*presencasSemana.values())

presentesTodosDias = set.intersection(*presencasSemana.values())

faltaramAlgumDia = todosAlunos - presentesTodosDias

presencasPorAluno = {aluno: 0 for aluno in todosAlunos}

for dia, presentes in presencasSemana.items():
    for aluno in presentes:
        presencasPorAluno[aluno] += 1

print("=== Controle de Presença da Semana ===\n")
print("Presentes todos os dias:", presentesTodosDias)
print("Faltaram pelo menos um dia:", faltaramAlgumDia)
print("\nNúmero total de presenças por aluno:")
for aluno, presencas in presencasPorAluno.items():
    print(f"- {aluno}: {presencas} presenças")
