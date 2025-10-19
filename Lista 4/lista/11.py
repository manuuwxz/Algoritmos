def buscarPessoa(listaPessoas, nomeAlvo):
    for pessoa in listaPessoas:
        if pessoa["nome"].lower() == nomeAlvo.lower():
            return pessoa
    
    return None


pessoas = [
    {"nome": "Lucas", "idade": 25},
    {"nome": "Leonardo", "idade": 32},
    {"nome": "Elena", "idade": 21},
    {"nome": "Emanuelly", "idade": 19},
    {"nome": "Cecilia", "idade": 35}
]
nomeProcurado = "Elena"

print(f"Buscando pela pessoa com o nome '{nomeProcurado}'...\n")

pessoaEncontrada = buscarPessoa(pessoas, nomeProcurado)

if pessoaEncontrada:
    print("Pessoa encontrada!")
    print(f"  - Nome: {pessoaEncontrada['nome']}")
    print(f"  - Idade: {pessoaEncontrada['idade']}")
else:
    print(f"Pessoa com o nome '{nomeProcurado}' não foi encontrada na lista.")