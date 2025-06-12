from conta_banco_classe import CartaoCredito, ContaBanco

conta_lira = ContaBanco('Lira', '111.111.111-98', 1234, 345678)
cartao_lira = CartaoCredito('Lira', conta_lira)

print(cartao_lira._numero)
print(cartao_lira._cod_seguranca)
print(cartao_lira._validade)
print(cartao_lira.senha)

print(conta_lira.__dict__)