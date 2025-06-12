class TV:

  def __init__(self):
    self.cor = 'Preta'
    self.ligada = False
    self.polegadas = 55
    self.canal = 'Netfllix'
    self.volume = 10

  def mudar_canal(self):
    self.canal = 'Dysney+'

tv_sala = TV()
tv_sala.mudar_canal()

print(tv_sala.polegadas)
print(tv_sala.canal)