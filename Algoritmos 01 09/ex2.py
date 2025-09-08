# Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

aluno = {
    "nome":"Lucas",
    "idade": "25",
    "curso": "Engenharia de Software"
}  

aluno.update({"nota":"9.5"})

aluno.pop("idade")
print(aluno)