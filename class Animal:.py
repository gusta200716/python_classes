class Animal:
    def __init__(self, nome, idade, cor, raca):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca

    def emitir_som(self):
        print("Animal faz um som")

class Cachorro(Animal):
    def __init__(self, nome, idade, cor, raca, tamanho_cauda):
        super().__init__(nome, idade, cor, raca)
        self.tamanho_cauda = tamanho_cauda

    def emitir_som(self):
        print("Cachorro late")

    def rolar(self):
        print(f"{self.nome} está rolando")

    def deitar(self):
        print(f"{self.nome} está deitando")
class Animal:
    def __init__(self, nome, idade, cor, raca):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca

    def emitir_som(self):
        print("Animal faz um som")

class Cachorro(Animal):
    def __init__(self, nome, idade, cor, raca, tamanho_cauda):
        super().__init__(nome, idade, cor, raca)
        self.tamanho_cauda = tamanho_cauda

    def emitir_som(self):
        print("Cachorro late")

    def rolar(self):
        print(f"{self.nome} está rolando")

    def deitar(self):
        print(f"{self.nome} está deitando")

class Gato(Animal):
    def __init__(self, nome, idade, cor, raca, tamanho_cauda):
        super().__init__(nome, idade, cor, raca)
        self.tamanho_cauda = tamanho_cauda

    def emitir_som(self):
        print("Gato mia")

    def derrubar_copo(self):
        print(f"{self.nome} derrubou um copo")

class Passaro(Animal):
    def __init__(self, nome, idade, cor, raca, tipo_bico):
        super().__init__(nome, idade, cor, raca)
        self.tipo_bico = tipo_bico

    def emitir_som(self):
        print("Pássaro canta")

    def nada(self):
        print(f"{self.nome} está nadando")

cachorro = Cachorro("Thor", 5, "Preto", "Pitbull", "Longa")
gato = Gato("Bolinha", 3, "Branco", "Siamês", "Curta")
passaro = Passaro("Mat", 2, "Amarelo", "Canário", "Curto")

cachorro.emitir_som()
cachorro.rolar()
cachorro.deitar()

gato.emitir_som()
gato.derrubar_copo()

passaro.emitir_som()
passaro.nada()
