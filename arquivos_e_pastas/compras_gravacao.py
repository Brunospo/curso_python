import os
import json
import time

caminho_save = os.getcwd() + '/arquivos_e_pastas'
arquivos = os.listdir(caminho_save)

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if compras.get(item):
      del compras[item]

def visualizar_compras(compras):
  if len(compras.keys()) == 0:
     print('A lista está vazia')
  for (produto, qtd) in compras.items():
    print(f'- {produto}: {qtd}')     
  print('Pressione Enter para continuar: ')      
  input()

def salvar_compras(compras, nome_lista):
    if nome_lista != None:
      with open(f"{caminho_save}/pasta_save/{nome_lista}.json", "w", encoding="utf-8") as arquivo:
        json.dump(compras, arquivo, indent=4)
      return
    
    while True:
      nome_arquivo = input('Digite o nome da lista: ')

      if f'{nome_arquivo}.json' in os.listdir(caminho_save + '/pasta_save'):
        print('Essa lista já existe')
        continue
      with open(f"{caminho_save}/pasta_save/{nome_arquivo}.json", "w", encoding="utf-8") as arquivo:
        json.dump(compras, arquivo, indent=4)
        break

def carregar_compras(nome_arquivo):
    with open(caminho_save + f'/pasta_save/{nome_arquivo}.json', "r", encoding="utf-8") as arquivo:
      compras_carregadas = json.load(arquivo)
      gerenciar_compras(compras_carregadas, nome_arquivo)

def menu_principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '3':
            break
        elif escolha == '2':

          os.system("cls" if os.name == "nt" else "clear")

          listas_carregadas = os.listdir(caminho_save + '/pasta_save')

          if len(listas_carregadas) == 0:
            print('Não há listas salvas')
            time.sleep(2)
            continue

          print(f"---------LISTA{'S' if len(listas_carregadas) > 1 else ''}---------")
          for indice, arquivo in enumerate(listas_carregadas):
            print(f'{indice + 1} = {arquivo}')
          print(f"-----------------------")

          nome_lista_selecionada = input('Digite o nome da lista (0 para sair): ')

          if nome_lista_selecionada == '0':
             continue
          if (nome_lista_selecionada + '.json') not in listas_carregadas:
             print('Essa lista não existe')
             time.sleep(3)
             continue
          carregar_compras(nome_lista_selecionada)
          pass
          
        elif escolha == '1':
            compras = {}
            gerenciar_compras(compras)

def gerenciar_compras(lista_compras, nome_lista = None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            item = input('Digite o nome do item: ')
            qtd = input('Digite a quantidade do item: ')
            adicionar_item(lista_compras, item, qtd)
        elif escolha == '2':
            item = input('Digite o nome do item a ser removido: ')
            remover_item(lista_compras, item)
        elif escolha == '3':
            os.system("cls" if os.name == "nt" else "clear")
            visualizar_compras(lista_compras)
        elif escolha == '4':
            salvar_compras(lista_compras, nome_lista)
            break
        elif escolha == '5':
            break

def main():
    if not 'pasta_save' in arquivos:
      os.makedirs(caminho_save + '/pasta_save')
    menu_principal()

main()