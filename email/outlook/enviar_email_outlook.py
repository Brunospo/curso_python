import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application")

email = outlook.CreateItem(0)

email.To = "falseta_fake_0@hotmail.com"
email.Cc = "pythonimpressionador@gmail.com;falseta_fake+copia@hotmail.com"
email.Bcc = "pythonimpressionador+oculto@gmail.com"
email.Subject = "Email enviado pelo Outlook"
# email.Body = "Texto do email"
email.HTMLBody = """<p>Meu primeiro paragrafo</p>
<p>Outro paragrafo no email</p>
<img src='https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fa6d41686876ceccfc436dd310b9e49aa.cdn.bubble.io%2Ff1658516625802x148010885188176500%2Flogo%2520hash%2520oficial%2520-%2520letra%2520azul.png?w=&h=&auto=compress&dpr=1&fit=max'
width=200>"""

caminho_codigo = os.getcwd()
arquivo_anexar = "anexos/kivy.png"
lista_arquivos = os.listdir("anexos")

for nome_arquivo in lista_arquivos:
    caminho_anexo = os.path.join(caminho_codigo, "anexos", nome_arquivo)
    email.Attachments.Add(caminho_anexo)

email.Send() 