import smtplib
import streamlit as st

# Función para enviar código de verificación
def enviar_codigo_verificacion(email, codigo):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('josue.velo@utec.edu.pe', 'gpcc ryug ssrd sgsz')  # Usa tu contraseña de aplicación
        mensaje = f'Subject: Código de Verificación\n\nTu código de verificación es: {codigo}'
        server.sendmail('josue.velo@utec.edu.pe', email, mensaje.encode('utf-8'))
        server.quit()
    except Exception as e:
        st.error(f"Ocurrió un error al enviar el correo: {e}")
