livros = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["Senhor dos Anéis", "João", 15]
]

mais = [livro for livro in livros if livro[2] > 7]
livroMaisTempo = max(livros, key=lambda x: x[2])
usuarios = [livro[1] for livro in livros]
mediaDias = sum(livro[2] for livro in livros) / len(livros)

print("=== Sistema de Biblioteca ===")
print(f"Livros emprestados há mais de 7 dias: {mais}")
print(f"Livro emprestado há mais tempo: {livroMaisTempo}")
print(f"Usuários com livros emprestados: {usuarios}")
print(f"Média de dias de empréstimo: {mediaDias:.2f}")
