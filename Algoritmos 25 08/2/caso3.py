estoque = [
    ["Arroz", 10, 25.0],
    ["Feijão", 3, 8.5],
    ["Macarrão", 15, 4.0],
    ["Óleo", 2, 7.0],
    ["Açúcar", 8, 5.5]
]

valorTotal = sum(qtd * preco for _, qtd, preco in estoque)
produtoMaiorValor = max(estoque, key=lambda item: item[1] * item[2])
estoqueBaixo = [nome for nome, qtd, _ in estoque if qtd < 5]

busca = input("Digite o nome do produto que deseja buscar: ")
produtoEncontrado = None
for nome, qtd, preco in estoque:
    if nome.lower() == busca.lower():
        produtoEncontrado = [nome, qtd, preco]
        break

print("\n=== Relatório de Estoque ===")
print(f"Valor total em estoque: R$ {valorTotal:.2f}")
print(f"Produto de maior valor total: {produtoMaiorValor[0]} "
      f"(R$ {produtoMaiorValor[1] * produtoMaiorValor[2]:.2f})")
print(f"Produtos com estoque abaixo de 5 unidades: {estoqueBaixo}")

if produtoEncontrado:
    print(f"Produto encontrado: Nome={produtoEncontrado[0]}, "
          f"Quantidade={produtoEncontrado[1]}, "
          f"Preço Unitário=R$ {produtoEncontrado[2]:.2f}")
else:
    print("Produto não encontrado.")
