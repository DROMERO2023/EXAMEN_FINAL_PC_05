import os
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib

def func_sender_email(sender_email, app_password, receiver_email, subject, message, file_paths=[]):
    # Configurar el servidor de correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Adjuntar archivos al mensaje
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            msg.attach(attachment)

    # Enviar el correo
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    # Imprimir mensaje de éxito
    print(f"Correo enviado exitosamente de {sender_email} a {receiver_email}")

# Ruta del archivo de datos
ruta_archivo = "src/cripto_currency.xlsx"

# Verificar si los archivos existen y eliminarlos si es necesario
if os.path.exists('resumen_crypto.xlsx'):
    os.remove('resumen_crypto.xlsx')
if os.path.exists('resumen_grafico.png'):
    os.remove('resumen_grafico.png')

# Cargar datos desde el archivo Excel
crypto_data = pd.read_excel(ruta_archivo)

# Verificar y crear la columna 'Tipo de Moneda'
if 'Tipo de Moneda' not in crypto_data.columns:
    crypto_data['Tipo de Moneda'] = 'Criptomoneda'

# Visualizar las primeras filas del DataFrame
print(crypto_data.head())

# Graficar datos y mostrar el gráfico en pantalla
plt.plot(crypto_data['Date'], crypto_data['Close'])
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre')
plt.title('Precio de Cierre de Criptomonedas')
plt.savefig('resumen_grafico.png')
plt.show()

# Agrupar por tipo de moneda y obtener estadísticas descriptivas
resumen_datos = crypto_data.groupby('Tipo de Moneda').describe()

# Imprimir resumen de datos
print(resumen_datos)

# Guardar el resumen en un archivo Excel sin índice múltiple
resumen_datos.to_excel('resumen_crypto.xlsx', index=True, header=True)

# Configuración del correo electrónico
sender_email = 'examenfinalpython@gmail.com'
app_password = 'dtng zuly mrjw itmj'
receiver_email = 'dennis.romero@pucp.pe'
subject = 'Reporte de Criptomonedas'
message = 'Adjunto encontrarás el informe de criptomonedas y los gráficos.'

# Llamada a la función de envío de correo
func_sender_email(sender_email, app_password, receiver_email, subject, message, ['resumen_crypto.xlsx', 'resumen_grafico.png'])
