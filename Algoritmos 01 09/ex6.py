# Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# a. Adicione ao dicionário do carro a chave 'cor'.
# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).
# c. Acesse a nota de um dos alunos e exiba.
# d. Remova um aluno do dicionário de notas.

carro = {
    "marca":"Toyota",
    "modelo":"Hilux",
    "ano": "1984"
}


carro.update({"Cor":"Prata"})
print(carro)

notas = {
    "Emanuelly": 9.6,
    "Lucas": 7.3,
    "Laura": 8.5
}

print(notas.get("Emanuelly"))

del notas["Lucas"]


print(notas)