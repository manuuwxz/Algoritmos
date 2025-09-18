pedidos = [
    {
        "Cliente": "Lucas",
        "Itens": [
            {"Prato": "Macarrão a Bolonhesa", "Valor": 35},
            {"Prato": "Batata Frita", "Valor": 15},
            {"Prato": "Guaraná", "Valor": 10}
        ]
    },
    {
        "Cliente": "Emanuelly",
        "Itens": [
            {"Prato": "Combinado de Sushi", "Valor": 65},
            {"Prato": "Coca Cola", "Valor": 10}
        ]
    },
    {
        "Cliente": "Elena",
        "Itens": [
            {"Prato": "Pizza", "Valor": 45},
            {"Prato": "Suco de Laranja", "Valor": 8}
        ]
    },
    {
        "Cliente": "Leonardo",
        "Itens": [
            {"Prato": "Strogonoff", "Valor": 30},
            {"Prato": "Batata Frita", "Valor": 15},
            {"Prato": "Coca Cola", "Valor": 10}
        ]
    },
    {
        "Cliente": "Luisa",
        "Itens": [
            {"Prato": "Lasanha", "Valor": 25},
            {"Prato": "Batata Frita", "Valor": 15},
            {"Prato": "Suco de Laranja", "Valor": 10}
        ]
    },
]

def total(cliente):
    gasto = 0
    for pedido in pedidos:
        if pedido["Cliente"] == cliente:
            for item in pedido["Itens"]:
                gasto += item["Valor"]
    return gasto

def vendido():
    qntdPratos = {}
    for pedido in pedidos:
        for item in pedido["Itens"]:
            nomePrato = item["Prato"]
            if nomePrato in qntdPratos:
                qntdPratos[nomePrato] += 1
            else:
                qntdPratos[nomePrato] = 1
    pratoVendido = max(qntdPratos, key=qntdPratos.get)
    return pratoVendido

def ranking():
    gastoCliente = {}
    for pedido in pedidos:
        cliente = pedido["Cliente"]
        if cliente not in gastoCliente:
            gastoTotal = total(cliente)
            gastoCliente[cliente] = gastoTotal
    
    ranking_ordenado = sorted(gastoCliente.items(), key=lambda item: item[1], reverse=True)
    
    topTres = ranking_ordenado[:3]
    return topTres

print(f"O valor total gasto por Lucas foi: {total('Lucas')}")
print(f"O prato mais vendido no dia foi: {vendido()}")
print(f"O ranking de clientes que mais gastaram é: {ranking()}")