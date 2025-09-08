vendas = {
    1: 10, 2: 15, 3: 20, 4: 5, 5: 0, 6: 8, 7: 12, 8: 18, 9: 25, 10: 7,
    11: 9, 12: 14, 13: 11, 14: 13, 15: 16, 16: 22, 17: 19, 18: 6, 19: 17, 20: 21,
    21: 23, 22: 24, 23: 4, 24: 3, 25: 2, 26: 1, 27: 5, 28: 8, 29: 9, 30: 10
}

vendasTotais = sum(vendas.values())
diaMaisVendas = [dia for dia in vendas if vendas[dia] == max(vendas.values())][0]
diaMenosVendas = [dia for dia in vendas if vendas[dia] == min(vendas.values())][0]
mediaVendas = vendasTotais / len(vendas)
diasAcimaMedia = [dia for dia in vendas if vendas[dia] > mediaVendas]

print(f"Total de vendas no mês: {vendasTotais}")
print(f"Dia com mais vendas: Dia {diaMaisVendas} ({vendas[diaMaisVendas]} vendas)")
print(f"Dia com menos vendas: Dia {diaMenosVendas} ({vendas[diaMenosVendas]} vendas)")
print(f"Média de vendas por dia: {mediaVendas:.2f}")
print(f"Dias com vendas acima da média: {diasAcimaMedia}")
