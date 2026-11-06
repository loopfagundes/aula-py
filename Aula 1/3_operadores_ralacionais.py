
num1 = 10
num2 = 20

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 != num2)
print(num1 == num2)

#----------------------------------------------

idade = int(input("Digite sua idade: "))
carteira = False
acima_idade = idade >= 18 or carteira

print(f'Verificador: {acima_idade}')

#----------------------------------------------

usuario = input("Digite nome do usuario: ")
senha = input("Digite senha do usuario: ")

login_valido = usuario == "Admin" and senha == "abc123"

print(f"Validate: {login_valido}")
