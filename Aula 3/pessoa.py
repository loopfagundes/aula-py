class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
        print(f'{self.nome} foi promo para a nova: {novo_cargo}')
        self.cargo = novo_cargo

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'{self.nome}: Atualizado a idade: {self.idade} para {nova_idade}')
        elif nova_idade == self.idade:
            print(f'{self.nome}: A mesma idade {self.idade}')
        else:
            print(f'{self.nome}: Idade tem que atualizar.')

colaborador1 = Pessoa('Fernando', 30, 'Dev')
colaborador1.informacoes()
colaborador1.promover('Dev Pleno')
colaborador1.atualizar_idade(31)