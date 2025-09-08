livros = [
    ["A Seleção", "Emanuelly", 5],
    ["Divinos Rivais", "Lucas", 12],
    ["Coraline", "Larissa", 3],
    ["Alice no pais das maravilhas", "Alice", 9],
    ["Crepusculo", "Isabella", 15]
]

livrosMaisDeSete = []
usuarios = []
diasEmprestados = []

for titulo, usuario, dias in livros:
    if dias > 7:
        livrosMaisDeSete.append([titulo, usuario, dias])
    usuarios.append(usuario)
    diasEmprestados.append(dias)

diaMaior = max(diasEmprestados)
indiceMaior = diasEmprestados.index(diaMaior)
maisTempo = livros[indiceMaior]
media = sum(diasEmprestados) / len(diasEmprestados)

print("Livros emprestados há mais de 7 dias:")
for livro in livrosMaisDeSete:
    print(f"- {livro[0]} ({livro[2]} dias)")

print(f"\nLivro emprestado há mais tempo: {maisTempo[0]} ({maisTempo[2]} dias)")
print(f"\nUsuários com livros emprestados: {usuarios}")
print(f"\nMédia de dias de empréstimo: {media:.1f} dias")