livros = [
    {"titulo": "A Seleção", "usuario": "Emanuelly", "diasEmprestado": 5},
    {"titulo": "Divinos Rivais", "usuario": "Lucas", "diasEmprestado": 12},
    {"titulo": "Coraline", "usuario": "Larissa", "diasEmprestado": 3},
    {"titulo": "Alice no pais das maravilhas", "usuario": "Alice", "diasEmprestado": 9},
    {"titulo": "Crepusculo", "usuario": "Isabella", "diasEmprestado": 15}
]

livrosMaisDeSete = []
usuarios = []
totalDias = 0
livroMaisTempo = livros[0]

for livro in livros:
    if livro["diasEmprestado"] > 7:
        livrosMaisDeSete.append(livro)
    usuarios.append(livro["usuario"])
    totalDias += livro["diasEmprestado"]
    if livro["diasEmprestado"] > livroMaisTempo["diasEmprestado"]:
        livroMaisTempo = livro

media = totalDias / len(livros)

print("Livros emprestados há mais de 7 dias:")
for livro in livrosMaisDeSete:
    print(f"- {livro['titulo']} ({livro['diasEmprestado']} dias)")

print(f"\nLivro emprestado há mais tempo: {livroMaisTempo['titulo']} ({livroMaisTempo['diasEmprestado']} dias)")
print(f"\nUsuários com livros emprestados: {usuarios}")
print(f"\nMédia de dias de empréstimo: {media:.1f} dias")
