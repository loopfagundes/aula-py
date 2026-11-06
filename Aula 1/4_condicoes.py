numero = int(input("Digite um numero:"))
numero2 = 20
boolean = True

if numero > numero2:
    print(f"{numero} > {numero2} = Passou")
elif numero == numero2:
    print(f"{numero} == {numero2} = Passou")
else:
    print(f"{numero} > {numero2} = Não passou")

if numero >= numero2:
    print(f"{numero} >= {numero2} = Passou")
else:
    print(f"{numero} >= {numero2} = Não passou")

# ---------------------------------------------

nota_aluno = float(input("Qual a nota do aluno:"))
nota_max = 10
nota_media = 6.5

if nota_aluno >= nota_max:
    print(f"{nota_aluno} >= {nota_max} = Excelente")
elif nota_aluno >= nota_media:
    print(f"{nota_aluno} >= {nota_media} = Que sorte! Passou")
elif nota_aluno <= nota_media:
    print(f"{nota_aluno} <= {nota_media} = Reprovado")

# -------------------------------------------------

usuario = input("Digite o usuario: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "abc123":
    print("Sucesso... Login permitido")
else:
    print("Usuario ou senha incorreto")
