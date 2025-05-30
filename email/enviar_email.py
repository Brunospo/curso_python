# SMTP

import smtplib
import email.message
import ssl # Para segurança da conexão SSL/TLS


def enviar_email():
    
    msg = email.message.Message()
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
    corpo_email = corpo_email.encode("utf-8")

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)

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