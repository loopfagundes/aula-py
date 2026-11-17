class Casa: # Classe
    def __init__(self, cor, quartos, banheiros): # Construação
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self): # metodo
        print(f'Cor da casa: {self.cor}')

    def mostrar_quartos(self): # metodo
        print(f'Quartos tem: {self.quartos}')

    def mostrar_banheiros(self): #metodo
            print(f'Banheiro tem: {self.banheiros}')


casa1 = Casa('Azul', 2, 1) # instancia
casa2 = Casa('Verde', 4, 3) # instancia

print('\nCasa 1')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()

print('\nCasa 2')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()