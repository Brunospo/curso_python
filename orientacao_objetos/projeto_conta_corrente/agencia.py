from random import randint

class Agencia:

  def __init__(self, telefone, cnpj,numero):
    self.telefone = telefone
    self.cnpj = cnpj
    self.numero = numero
    self.clientes = []
    self.caixa = 0
    self.emprestimos = []

  def verificar_caixa(self):
    if self.caixa < 1000000:
      print('Caixa abaixo do nivel recomendado. Caixa atual R${:,.2f}'.format(self.caixa))
    else:
      print('Caixa está OK. Caixa atual R$ {:,.2f}'.format(self.caixa))

  def emprestar_dinheiro(self, valor, cpf, juros):
    if self.caixa > valor:
      self.caixa -= valor
      self.emprestimos.append((valor, cpf, juros))
    else:
      print('Emprestimo não é possivel! Dinheiro não disponível em caixa.')

  def adicionar_cliente(self, nome, cpf, patrimonio):
    self.clientes.append((nome, cpf,patrimonio))

# Herança

class AgenciaVirtual(Agencia):
  
  def __init__(self, site, telefone, cnpj):
    self.site = site
    super().__init__(telefone, cnpj, 1000) #agencia padrao será 1000
    self.caixa = 1000000
    self.paypal = 0

  def depositar_paypal(self, valor):
    self.caixa -= valor
    self.paypal += valor

  def sacar_paypal(self, valor):
    self.caixa += valor
    self.paypal -= valor
    

class AgenciaComum(Agencia):
  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj, numero = randint(1001, 9999))
    self.caixa = 1000000
    

class AgenciaPremium(Agencia):
  def __init__(self, telefone, cnpj):
    super().__init__(telefone, cnpj, numero = randint(1001, 9999))
    self.caixa = 10000000

  def adicionar_cliente(self, nome, cpf, patrimonio):
    if patrimonio > 1000000:
      super().adicionar_cliente(nome, cpf, patrimonio)
    else:
      print(f'O Cliente {nome} não tem o patrimonio minimo necessário para entrar na Agencia Premium')


print('---- Agencia normal ----')
agencia = Agencia(11111111111,2222222222222, 65478)
agencia.caixa = 1000000
agencia.emprestar_dinheiro(1500, 56555556655, 0.02)
print(agencia.emprestimos)
agencia.verificar_caixa()
print('')

print('---- Agencia virtual ----')
agencia_virtual = AgenciaVirtual('https://www.agenciavirtual.com.br',78888888888, 45460000000)
agencia_virtual.caixa = 1000000
agencia_virtual.verificar_caixa()
agencia_virtual.depositar_paypal(1000)
print(agencia_virtual.paypal)
print(agencia_virtual.site)
print('')

print('---- Agencia premium ----')
agencia_premium = AgenciaPremium(7879465,4654654)
agencia_premium.verificar_caixa()
agencia_premium.adicionar_cliente('Lira', 11111145621, 100000)
agencia_premium.adicionar_cliente('Lara', 11111145621, 1000001)
print(agencia_premium.clientes)