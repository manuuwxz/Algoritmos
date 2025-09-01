#Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro
#diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu
#para criar um programa simples em Python para armazenar, analisar e gerar pequenos
#relatórios sobre as vendas do dia.
#O sistema precisa:
#1. Guardar os produtos vendidos (nome e preço).
#2. Mostrar o valor total arrecadado.
#3. Identificar o produto mais caro e o mais barato do dia.
#4. Permitir consultar se um produto específico foi vendido.

vendas = []

print("   Sistema de Registro de Vendas   ")
print("Digite 'fim' para encerrar o registro de vendas.")

while True:
    produto = input("Digite o nome do produto (ou 'fim' para sair): ")
    
    if produto.lower() == 'fim':
        break
    
    produto = float(input(f"Digite o preço de '{produto}': R$"))
            

    vendas.append({"produto": produto, "preco": produto})


if not vendas:
    print("\nNenhuma venda foi registrada.")
else:
    
    arrecadacao = sum(item['preco'] for item in vendas)
    print(f"\n   Relatório de Vendas do Dia   ")
    print(f"Total arrecadado: R${arrecadacao:.2f}")

    
    caro = vendas[0]
    barato = vendas[0]
    
   
    for venda in vendas:
        if venda['preco'] > caro['preco']:
            caro = venda
        if venda['preco'] < barato['preco']:
            barato = venda
    
    print(f"Produto mais caro: {caro['produto']} (R${caro['preco']:.2f})")
    print(f"Produto mais barato: {barato['produto']} (R${barato['preco']:.2f})")

   
    while True:
        consulta = input("\nConsultar produto (ou 'fim' para sair): ")
        if consulta.lower() == 'fim':
            break
        
        encontrado = False
        for venda in vendas:
            if venda['produto'].lower() == consulta.lower():
                print(f"O produto '{venda['produto']}' foi vendido pelo preço de R${venda['preco']:.2f}.")
                encontrado = True
                break
        
        if not encontrado:
            print(f"O produto '{consulta}' não foi encontrado na lista de vendas.")

print("\nPrograma encerrado.")