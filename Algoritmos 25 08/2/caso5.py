palestra = ["Ana", "Carlos", "Marina"]
workshop = ["Carlos", "João", "Ana"]
mesaRedonda = ["Marina", "João", "Paula"]

participaramTodos = set(palestra) & set(workshop) & set(mesaRedonda)

todos = palestra + workshop + mesaRedonda
participaramUma = [nome for nome in set(todos) if todos.count(nome) == 1]

todosUnicos = set(todos)
quantidadeDistintos = len(todosUnicos)

print("=== Controle de Participação no Evento ===")
print(f"Participaram de todas as atividades: {participaramTodos}")
print(f"Participaram de apenas uma atividade: {participaramUma}")
print(f"Lista de todos os participantes únicos: {todosUnicos}")
print(f"Total de participantes distintos: {quantidadeDistintos}")
