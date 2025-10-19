def buscarProdutosPreço(listaProdutos, precoAlvo):
    produtosEncontrados = [] 
    for produto in listaProdutos:
        if 'preco' in produto and produto['preco'] == precoAlvo:
            produtosEncontrados.append(produto)
            
    return produtosEncontrados

catalogo = [
    {'nome': 'Notebook Gamer', 'preco': 5500.00, 'estoque': 15},
    {'nome': 'Mouse sem Fio', 'preco': 120.50, 'estoque': 40},
    {'nome': 'Teclado Mecânico', 'preco': 350.00, 'estoque': 25},
    {'nome': 'Monitor 24"', 'preco': 999.90, 'estoque': 20},
    {'nome': 'Webcam Full HD', 'preco': 350.00, 'estoque': 30},
    {'nome': 'Headset Gamer', 'preco': 350.00, 'estoque': 18}
]

precoDesejado = 350.00

print(f"Buscando por produtos que custam R$ {precoDesejado:.2f}...\n")

resultados = buscarProdutosPreço(catalogo, precoDesejado)

if resultados:  
    print("Produtos encontrados:")
    for produto in resultados:
        print(f"  - Nome: {produto['nome']}, Estoque: {produto['estoque']}")
else:
    print(f"Nenhum produto encontrado com o preço de R$ {precoDesejado:.2f}")