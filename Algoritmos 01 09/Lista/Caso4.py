vendas = [10, 15, 20, 5, 0, 8, 12, 18, 25, 7, 9, 14, 11, 13, 16, 22, 19, 6, 17, 21, 23, 24, 4, 3, 2, 1, 5, 8, 9, 10]

vendasTotais = sum(vendas)
diasMaisVendidos = vendas.index(max(vendas)) + 1
diasMenosVendidos = vendas.index(min(vendas)) + 1
mediasVendas = vendasTotais / len(vendas)
acimaMedia = [i + 1 for i, venda in enumerate(vendas) if venda > mediasVendas]

print(f"Total de vendas no mês: {vendasTotais}")
print(f"Dia com mais vendas: Dia {diasMaisVendidos} ({max(vendas)} vendas)")
print(f"Dia com menos vendas: Dia {diasMenosVendidos} ({min(vendas)} vendas)")
print(f"Média de vendas por dia: {mediasVendas:.2f}")
print(f"Dias com vendas acima da média: {acimaMedia}")