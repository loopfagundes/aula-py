#### Aula 01 Varivel ####

nome = input("Qual é o seu nome? ")

try:
    idade = int(input("Qual é a sua idade? "))
except ValueError:
    print("Erro: Você precisa digitar um número válido.")

fruta_favorita = input("Qual é a fruta favorita? ")
# -----------------------------------------------

print(nome, "é o seu nome.")
print(idade, "é sua idade.")

# sem f-string
print("Olá", nome, "e a sua idade é", idade)

# ------------------------------------------------

#### Aula 02 f-string ####

# com f-string
print(f"O {nome} tem {idade} anos e a sua fruta favorita é {fruta_favorita}")

# -------------------------------------------------
