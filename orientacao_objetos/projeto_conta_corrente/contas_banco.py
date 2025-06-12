from datetime import datetime
from zoneinfo import ZoneInfo

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

conta_lira = ContaBanco('Lira', '111.111.111-98', 1234, 345678)

conta_lira.consultar_limte()
conta_lira.consultar_saldo()
conta_lira.sacar(100)
conta_lira.depositar(1000)
conta_lira.consultar_saldo()
conta_lira.sacar(1500)
conta_lira.consultar_saldo()

conta_lira.visualizar_historico_transacoes()

print('==' * 20)

conta_ana = ContaBanco('Ana', '222.222.222-22', 7894, 344578)
conta_joao = ContaBanco('Joao', '333.333.333-33', 4594, 963578)

conta_ana.depositar(1000)
conta_ana.consultar_saldo()
conta_ana.transferir(100, conta_joao)

conta_ana.visualizar_historico_transacoes()
conta_joao.visualizar_historico_transacoes()