class Carro:
    def __init__(self, marca, modelo, tracao, cor, ano, nacionalidade):
        self.marca = marca
        self.modelo = modelo
        self.tracao = tracao
        self.cor = cor
        self.ano = ano
        self.nacionalidade = nacionalidade
        self.ligado = False

    def informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Tracao: {self.tracao}')
        print(f'Cor: {self.cor}')
        print(f'Ano: {self.ano}')
        print(f'Nacionalidade: {self.nacionalidade}')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Carro ligado')
        else:
            print('Carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('Carro desligado')
        else:
            print('Carro já estava desligado')

    def alarme(self):
        if not self.ligado:
            print('Carro ativa a alarme')
        else:
            print('Carro não ativa a alarme')

carro1 = Carro('RAM', '2500','4x4', 'vermelho', 2019, 'EUA')
carro1.informacoes()
carro1.ligar()
#carro1.desligar()
carro1.alarme()
