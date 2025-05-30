import requests
import json

link = ''

# dados = {"cliente": "Alon", "preco": 150, "produto": "teclado"}
# req = requests.post(f'{link}/vendas.json', data= json.dumps(dados)) # transforma o dicionario em json

# dados = {"cliente": "Lira"}
# req = requests.patch(f'{link}/vendas/-OQ3aVrfycuvErJKJec1.json', data= json.dumps(dados))

# print(req)
# print(req.text)

req = requests.get(f'{link}/vendas.json')
vendas_dict = req.json()

id = None

for id_venda in vendas_dict:
  cliente = vendas_dict[id_venda]['cliente']
  if cliente == "Alon":
    print(id_venda)
    id = id_venda

req = requests.delete(f'{link}/vendas/{id}.json')
