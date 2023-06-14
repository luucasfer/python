 
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero  # __dunder deixa o atributo privado, 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        return "Saldo {} do titular {}".format(self.__saldo, self.__titular)
    
    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #deixo o metodo privado, só pode ser usado dentro de def sacar()
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque de {} realizado".format(valor))
        else:
            print("O valor {} é maior que o seu limite disponivel".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("Você transferiu {}".format(valor))

    '''GETTERS'''
    @property         #retira a necessidade de digitar conta1.limite(), posso chamar conta1.limite
    def saldo(self):  #chamo a função com o mesmo nome do atributo
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property   
    def limite(self): 
        return self.__limite
    
    '''SETTERS'''
    @limite.setter               #posso chamar conta1.limite = 10.0, sem parenteses()
    def limite(self, novoLimite):
        self.__limite = novoLimite

    @staticmethod               #permite retornar um obj do construtor, sem o self
    def codigo_banco():         # sem ter que criar uma conta primeiro
        return print("Código do Banco: 0001")





'''Consultando codigo do banco'''
Conta.codigo_banco()

'''Criando contas'''    
conta1 = Conta(123, 'Lucas', 50.0, 1000.0)
conta2 = Conta(345, 'Marina', 70.0, 2000.0)
print(conta1.extrato())
print(conta2.extrato())
print()

'''transferindo dinheiro'''
conta1.transferir(10.0, conta2)
print(conta1.extrato())
print(conta2.extrato())
print()

'''Alterando limite'''
print("Limite da conta1: ",conta1.limite)
conta1.limite = 1200.0
print("Novo Limite da conta1: ",conta1.limite)
print()

'''Sacando dinheiro'''
conta1.sacar(2000)
conta1.sacar(200)

