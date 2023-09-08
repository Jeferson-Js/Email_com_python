import os
import smtplib
import email.message
from dotenv import load_dotenv

load_dotenv()

def enviar_email():  
    corpo_email = """
    <p>Como enviar emails com python</p>
    <p>Parágrafo2</p>
    <p>Parágrafo3</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Programação python"
    msg['From'] = 'teste@teste.com'
    msg['To'] = 'teste@teste.com'
    password = str(os.getenv('LOG_USER')) 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()