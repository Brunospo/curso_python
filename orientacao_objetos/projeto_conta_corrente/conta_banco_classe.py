from datetime import datetime
from zoneinfo import ZoneInfo
import random

class ContaBanco:

  @staticmethod
  def _data_hora():
    fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
    horario = datetime.now(fuso_horario_sao_paulo)
    return horario.strftime('%d/%m/%Y %H:%M:%S')

  def __init__(self, nome, cpf, agencia, num_conta):
    self._nome = nome
    self._cpf = cpf
    self._saldo = 0
    self._limite = None
    self._agencia = agencia
    self._conta = num_conta
    self._transacoes = []
    self.cartoes = []

  def consultar_saldo(self):
    print('{}, seu saldo atual é de R$ {:,.2f}'.format(self._nome,self._saldo))

  def consultar_limte(self):
    print('{}, seu limite é de R$ {:,.2f}'.format(self._nome, self._limite_conta()))

  def depositar(self, valor):
    self._saldo += valor
    self._transacoes.append((valor, self._saldo, ContaBanco._data_hora()))

  def _limite_conta(self): #Convenção para metodos privados
    self._limite = -1000
    return self._limite

  def sacar (self, valor):
    if((self._saldo - valor) < self._limite_conta()):
      print('Saldo insuficiente')
      return
    self._saldo -= valor
    self._transacoes.append((-valor, self._saldo, ContaBanco._data_hora()))

  def transferir(self, valor, conta):
    self._saldo -= valor
    self._transacoes.append((-valor, self._saldo, ContaBanco._data_hora()))
    conta._saldo += valor
    conta._transacoes.append((valor, conta._saldo, ContaBanco._data_hora()))

  def visualizar_historico_transacoes(self):
    print('-' * 24)
    print('\t{}'.format(self._nome))
    print('Histórico de transações:')
    print('-' * 24)
    print(' Valor Saldo  Data')
    for transacao  in self._transacoes:
      print(transacao)

class CartaoCredito:
  @staticmethod
  def _gerarNumeroCartao():
    return random.randint(1000000000000000, 9999999999999999)
  
  @staticmethod
  def _gerarCodSeguranca():
    return '{}{}{}'.format(random.randint(0, 9),random.randint(0, 9),random.randint(0, 9))
  
  @staticmethod
  def _validadeCartao():
    fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
    horario = datetime.now(fuso_horario_sao_paulo)
    return '{}/{}'.format(horario.month, horario.year + 4)
  
  def __init__(self, titular, conta_corrente):
    self._numero = CartaoCredito._gerarNumeroCartao()
    self._titular = titular
    self._validade = CartaoCredito._validadeCartao()
    self._cod_seguranca = CartaoCredito._gerarCodSeguranca()
    self._limite = 1000
    self._senha = '1234'
    self._conta_corrente = conta_corrente
    conta_corrente.cartoes.append(self._numero)

  @property #Get
  def senha(self):
    return self._senha
  
  @senha.setter
  def senha(self, valor):
    if len(valor) > 4 and valor.isnumeric():
      self._senha = valor
    else:
      print("Senha inválida")
