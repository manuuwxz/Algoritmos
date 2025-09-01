vendas = [10, 15, 20, 5, 0, 8, 12, 30, 25, 18, 22, 5, 7, 19, 11, 13, 14, 21, 6, 9, 8, 27, 16, 4, 3, 10, 17, 29, 23, 20]

total = sum(vendas)
diaMax = vendas.index(max(vendas)) + 1
diaMin = vendas.index(min(vendas)) + 1
media = total / len(vendas)
diasAcimaMedia = [i+1 for i, v in enumerate(vendas) if v > media]

print("=== Análise de Vendas Mensais ===")
print(f"Total de vendas no mês: {total}")
print(f"Dia com mais vendas: Dia {diaMax} ({max(vendas)} vendas)")
print(f"Dia com menos vendas: Dia {diaMin} ({min(vendas)} vendas)")
print(f"Média de vendas por dia: {media:.2f}")
print(f"Dias com vendas acima da média: {diasAcimaMedia}")
