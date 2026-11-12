#-INDEX     0        1         2
frutas = ["Maçã", "Banana", "Morango"]

# Ver a lista
print(frutas)

# baseado em index [0,1,2]
print(frutas[2])

# Add mais uma fruta na lista
frutas.append('Uva')
frutas.append("Laranja")

# Ver a lista que já adicionei
print(frutas)

# Remove uma fruta da lista
frutas.remove("Morango")
print(frutas)

# Quantidade dentro da Arrys
print(len(frutas))

print("#--------------------------------------------")

tarefas = []

#        add       texto
tarefas.append("Estudar Python") # 0
tarefas.append("Ler o artigo sobre IA") # 1
tarefas.append("Responder emails") # 2

print(tarefas)

print(tarefas[0])
print(tarefas[1])
print(tarefas[2])

print("#---------FOR----------------")

for tarefa in tarefas:
    print(f'Tarefa: {tarefa}')

print('#------------------------------')

usuario = {
    'nome': 'Luciano',
    'idade': '35',
    'departamento': 'TI'
}

print(usuario)

print(usuario['nome'])
print(usuario['idade'])

usuario['nome'] = 'Ken' # Trocar o nome
usuario['cidade'] = 'Porto Alegre' # add mais um 

print(usuario)