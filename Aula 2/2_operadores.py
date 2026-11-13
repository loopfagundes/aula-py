num1 = 10
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2) # é um float
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

print("--------------------------------------")

preco = int(input("Qual o valor do produto? "))
desconto = int(input("Digite o desconto a ser aplicado: ")) # desconto em %

desconto_preco = preco - preco * desconto / 100

print(f'O valor com desconto é de {desconto_preco}')