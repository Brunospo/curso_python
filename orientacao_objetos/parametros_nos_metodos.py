class TV:

  def __init__(self):
    self.cor = 'Preta'
    self.ligada = False
    self.polegadas = 55
    self.canal = 'Netfllix'
    self.volume = 10

  def mudar_canal(self, novo_canal):
    self.canal = novo_canal

tv_sala = TV()
tv_quarto = TV()

tv_sala.mudar_canal("Youtube")
tv_quarto.mudar_canal("Globo")

print(tv_quarto.canal)
print(tv_sala.canal)