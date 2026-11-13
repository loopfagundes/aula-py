def  saudacao(nome):
    print(f'Ola {nome}, bora aprender Python')

def somar(a,b):
    return a + b

def verifica_idade():
    idade = int(input("Digite sua idade: "))
    carteira = False
    acima_idade = idade >= 18 or carteira
    print(f'Verificador: {acima_idade}')