class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("Veículo ligado")

    def desligar(self):
        print("Veículo desligado")

    def imprimir_propriedades(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numeroDePortas):
        super().__init__(marca, modelo, ano)
        self.numeroDePortas = numeroDePortas

    def mostrar_numero_de_portas(self):
        print("O Carro possui:", self.numeroDePortas)

    def imprimir_propriedades(self):
        super().imprimir_propriedades()
        print(f"Número de Portas: {self.numeroDePortas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def mostrar_cilindradas(self):
        print("A Moto possui:", self.cilindradas)

    def imprimir_propriedades(self):
        super().imprimir_propriedades()
        print(f"Cilindradas: {self.cilindradas}")


veiculo = Veiculo("Porsche", "Porsche 911 Turbo", 2023)
carro = Carro("Hyundai", "Creta", 2020, 4)
moto = Moto("Honda", "CBR", 2021, 650)

veiculo.ligar()
veiculo.desligar()
veiculo.imprimir_propriedades()

carro.ligar()
carro.desligar()
carro.mostrar_numero_de_portas()
carro.imprimir_propriedades()

moto.ligar()
moto.desligar()
moto.mostrar_cilindradas()
moto.imprimir_propriedades()