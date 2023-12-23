# EXAMEN FINAL - DENNIS A. ROMERO ROJAS
# Ejercicio 02 - ENVÍO DE CORREO CON DATOS ADJUNTOS
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def func_sender_email(sender_email: str, app_password: str, receiver_email: str, subject: str, message: str, archivo_adjunto: str) -> None:
    """Envío de correo electrónico con archivo adjunto"""

    # Configurar el servidor de correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Usar el token de aplicación en lugar de la contraseña
    server.login(sender_email, app_password)

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))

    # Adjuntar archivo
    attachment = open(archivo_adjunto, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % archivo_adjunto)
    msg.attach(part)

    # Enviar correo
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    # Imprimir mensaje de éxito
    print(f"Correo enviado exitosamente de {sender_email} a {receiver_email}")

# me posiciono sobre carpeta
os.chdir('reportes')

# Reemplaza los siguientes valores con los correctos
func_sender_email(sender_email='examenfinalpython@gmail.com',
                  app_password='dtng zuly mrjw itmj',
                  receiver_email='dennis.romero@pucp.pe',
                  subject='Reporte Brazil',
                  message='Reporte excel Brazil',
                  archivo_adjunto='Brazil.xlsx')
