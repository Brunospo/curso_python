class TV:

  def __init__(self, polegadas_tv):
    self.cor = 'Preta'
    self.ligada = False
    self.polegadas = polegadas_tv
    self.canal = 'Netfllix'
    self.volume = 10

  def mudar_canal(self, novo_canal):
    self.canal = novo_canal

tv_sala = TV(42)
tv_quarto = TV(70)

print(tv_quarto.polegadas)
print(tv_sala.polegadas)