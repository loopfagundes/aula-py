class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou {self.especie}, a cor {self.cor} e chamado {self.nome}')


class Gato(Animal):
    def emitir_som(self):
        print('Meow!')

class Cachorro(Animal):
    def emitir_som(self):
        print('Woof, woof...')

gato1 = Gato('Tom', 'cinza', 'Azul Russo')
gato1.apresentar()
gato1.emitir_som()

cachorro1 = Cachorro('Bob', 'preto', 'Dachshund')
cachorro1.apresentar()
cachorro1.emitir_som()
