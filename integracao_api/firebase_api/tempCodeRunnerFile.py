dados = {"cliente": "Alon", "preco": 150, "produto": "teclado"}
req = requests.post(f'{link}/vendas.json', data= json.dumps(dados)) # transforma o dicionario em json