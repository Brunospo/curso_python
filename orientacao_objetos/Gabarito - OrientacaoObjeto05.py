class TV:

    cor = 'preta' # Atributo de classe, é comop se fosse o valor obrigatório para todos os objetos

    def __init__(self, tamanho):
        self.ligada = False # Atributos de instancia
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV(55)
tv_quarto = TV(70)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print(tv_sala.cor)
print(tv_quarto.cor)

