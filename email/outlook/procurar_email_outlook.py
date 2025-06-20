import win32com.client as win32
import os

outlook = win32.Dispatch("outlook.application")

caixas_email = outlook.GetNamespace("MAPI")

# for pasta in caixas_email.Folders:
#     print(pasta)

pasta_python = caixas_email.Folders.Item(2)

# for subpasta in pasta_python.Folders:
#     print(subpasta)

caixa_entrada = pasta_python.Folders.Item(1)

lista_emails = caixa_entrada.Items

print(len(lista_emails))

for email in lista_emails:
    anexos = email.Attachments
    if email.To == "seuemaildestino@hotmail.com" and len(anexos) > 0:
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        for anexo in anexos:
            print(anexo.FileName)
            caminho_codigo = os.getcwd()
            caminho_anexo_salvar = os.path.join(caminho_codigo, f"Email {email.Subject} - {anexo.FileName}")
            anexo.SaveAsFile(caminho_anexo_salvar)

print("Fim do código")