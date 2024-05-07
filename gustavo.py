class Cliente: 
    def __init__ (self,nome,anoNascimento,sexo,saldo,endereco,ativo):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo
        
    def imprimir(self):
        print("---------")
        print("Nome:", self.nome)
        print("Ano:", self.anoNascimento)
        print("Sexo:", self.sexo)
        print("Saldo:", self.saldo)
        print("Endereco:", self.endereco)
        print("Ativo:", self.ativo)
        
    def ValidaCliente(self):
        if self.ativo:
            print("O cliente", self.nome, "está ativo.")
        else:
            print("O cliente", self.nome, "não está ativo.")
        
        
objeto = Cliente("Gustavo", 2007, "M", 500, "Rua São Paulo", True)
objeto2 = Cliente("Gustavo", 2007, "M", -500, "Rua São Paulo", True)
objeto3 = Cliente("Gustavo", 2007, "M", 500, "Rua São Paulo", False)
# objeto.imprimir()
# objeto2.imprimir()
# objeto3.imprimir()

objeto.ValidaCliente()
objeto2.ValidaCliente()
objeto3.ValidaCliente()

