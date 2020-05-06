class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

if __name__ == '__main__':
    fulano = Pessoa(nome='Fulano')
    beltrano = Pessoa(fulano, nome="Beltrano")

    print(f'Filho: {fulano.nome}')
    print(f'Pai: {beltrano.nome}')
    for filho in beltrano.filhos:
        print(f'Filho de Beltrano é: {filho.nome}')