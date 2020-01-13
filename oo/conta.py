import datetime

class Cliente():

    #construtor da classe
    def __init__ (self, nome,sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta():

    _total_contas = 0

    #criando um slot ( ele impede que o usuário crie outros atributos além dos que ue defini
    __slots__ = ['_numero','_titular','_saldo','_limite', '_historico']

    # construtor da classe
    def __init__(self,numero,cliente ,saldo,limite=1000):
        self._numero = numero
        self._titular = cliente.nome
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        type(self)._total_contas += 1


    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Saque de {}".format(valor))


    @property
    def saldo(self):
        return self._saldo

    '''
    Essa função seria o set 
    ela não é necessária pois eu quero que as pessoas usem o método saca e deposita
    
    @saldo.setter
    def saldo(self, saldo):
        if (self._saldo < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo'''

    def saca(self,valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {}".format(valor))
            return True
        else:
            return False

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere_para(self,nome_conta_destino,valor):
        retirou = self.saca(valor)

        if not retirou:
            return False
        else:
            nome_conta_destino.deposita(valor)
            self.historico.transacoes.append("Trasnferencia de {} para a conta {}".format(valor,nome_conta_destino.numero))
            return True

        @classmethod
        def get_total_contas(cls):
            return cls._total_contas

class Historico():

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")

        for t in self.transacoes:
            print("-", t)




if __name__ == '__main__':
    joao = Cliente("João","Silva", 345-455)
    conta = Conta('123-4',joao, 1000)
    print(conta._numero)
    print(conta._titular)
    print(conta.saldo)
    print(conta._limite)
