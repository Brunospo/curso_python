# SMTP

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import ssl # Para segurança da conexão SSL/TLS


def enviar_email():
    
    msg = MIMEMultipart()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = ""
    msg["To"] = ""
    # msg["Cc"] = "seuemailcopia@gmail.com;outroemailcopia@hotmail.com"
    # msg["Bcc"] = "seuemailcopiaoculta@gmail.com"
    
    link_imagem = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Number_sign.svg/1200px-Number_sign.svg.png"

    corpo_email = f"""<p>Boa tarde,</p>
    <p>Esse é meu primeiro email com Python usando smtplib</p>
    <p>Att., Lira</p>
    <img src='{link_imagem}'>"""

    msg.attach(MIMEText(corpo_email, "html"))

    # anexar arquivos
    lista_arquivos = os.listdir("email/anexos")
    for nome_arquivo in lista_arquivos:
        with open(f"email/anexos/{nome_arquivo}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    context = ssl.create_default_context()

    print(f"Conectando ao servidor SMTP...")
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:

        servidor.starttls(context=context)
        print("TLS iniciado. Autenticando...")

        servidor.login(msg["From"], "")
        print("Autenticação bem-sucedida. Enviando email...")
        servidor.send_message(msg)

    print("Email enviado")

enviar_email()