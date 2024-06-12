class Cadastro:
    nome = None    
    def __init__(self):
        pass

    def InserirNome(self, nome):
        nomeCorreto = self.validarNome(nome)    
        if nomeCorreto == True:
            self.nome = nome
            print("Valor cadastrado com sucesso")

    def validarNome(self, nome):
        if nome (len(nome) > 0):
            return True
        else:
            print("O nome tem que possuir mais de 1 caracter")
            return False
            

    idade = None
    def __init__(self):
        pass

    def InserirIdade(self, idade):
        idadeCorreta = self. ValidaIdade(idade)
        if idadeCorreta == True:
            self.idade = idade
            print("Valor cadastrado com sucesso")

    def ValidaIdade(self, idade):
        if idade <= 0:
            print("Idade precisa ser maior que 18 anos")
            return False
        else:
            return True
        

    saldo = None
    def __init__(self):
        pass
    def InserirSaldo(self, saldo):
        saldoCorreto = self. ValidaSaldo(saldo)
        if saldoCorreto == True:
            self.saldo = saldo
            print("Dados cadastrados com sucesso")

    def ValidaSaldo(self, saldo):
        if saldo <= 0:
            print("O saldo não pode ser negativo")
            return False
        else:
            return True
        

    statusCadastro = None
    def __init__(self):
        pass
    def InserirStatus(self, statusCadastro):
        statusCorreto = self. ValidaStatus(statusCadastro)
        if statusCorreto == True:
            self.statusCadastro = statusCadastro
            print("Status cadastrado com sucesso")
        
    def ValidaStatus(self,statusCadastrado):
        if statusCadastro == "Verdadeiro":
            return True
        else:
            print("O cadastro deve ser verdadeiro")
            return False 
