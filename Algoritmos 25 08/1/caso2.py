#Faça um programa que:
#1. Permita ao usuário adicionar itens a uma lista de compras.
#2. Caso o usuário digite "sair", o programa encerra.
#3. Mostre a lista final de compras organizada em ordem alfabética

ListaCompras = []

print("Esta é sua lista de compras!")
print("Digite 'sair' em qualquer momento para finalizar")

while True:
    item = input("Adicione um item a lista: ").strip()
    
    if item.lower() == 'sair':
        break
    
    ListaCompras.append(item)
    
ListaCompras.sort()

if ListaCompras:
    print("\n   Sua lista de compras   ")
    for item in ListaCompras:
        print(f"- {item}")
else:
    print("\nSua lista de compra está vazia")
    