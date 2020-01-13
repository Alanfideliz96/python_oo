'''
Esse arquivo tem com o objetivo estudar orientação a objetos seguindo a apostla da caelun

'''

#criação da função para criar conta

def cria_conta(numero,titular,saldo,limite):
    conta = {"numero": numero, "titular": titular, "saldo":saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta,valor):
    conta['saldo'] -= valor

def extrato(conta):
     print("Numero: {} \nSaldo: {}" .format(conta['numero'], conta['saldo']))

