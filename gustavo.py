
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
    
    def calcularIdade(self):
        anoAtual = 2024
        idade = anoAtual - self.anoNascimento
        print("A idade do cliente é:", idade, "anos")
        
    def VerificaSaldo(self):
        if self.saldo >=0:
            print("O saldo", self.saldo, "está positivo")
        else:
            print("O saldo", self.saldo, "está negativo")

        
        
objeto = Cliente("Gustavo", 2007, "M", 245, "Rua São Paulo", True)
objeto2 = Cliente("Jose", 2003, "M", -789, "Rua São Paulo", True)
objeto3 = Cliente("Rodolfo", 2001, "M", 457, "Rua São Paulo", False)
# objeto.imprimir()
# objeto2.imprimir()
# objeto3.imprimir()

# objeto.ValidaCliente()
# objeto2.ValidaCliente()
# objeto3.ValidaCliente()

print("---------")
#objeto.calcularIdade()
#objeto2.calcularIdade()
#objeto3.calcularIdade()

objeto.VerificaSaldo()
objeto2.VerificaSaldo()
objeto3.VerificaSaldo()





    

