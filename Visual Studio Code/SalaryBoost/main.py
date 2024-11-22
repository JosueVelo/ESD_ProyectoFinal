import streamlit as st
import random
from streamlit_option_menu import option_menu
from login import verificar_login
from email_service import enviar_codigo_verificacion
from display import mostrar_datos_empleado, mostrar_datos_supervisor
from database import engine_empleados, engine_supervisores
import pandas as pd
from aumento_sueldo import aumento_sueldo
from modificacion_datos import modificar_datos_empleados 
from registro_empleado import registrar_nuevo_empleado
from modificacion_contrasena import modificar_contrasena
from eliminar_empleado import eliminar_empleado
from insight import visualizar_insights

# Función para mostrar el menú con estilo mejorado
def mostrar_menu_principal(tipo_usuario):
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: #007bff;'>🌟 Menú Principal</h1>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        
        if tipo_usuario == "Empleado":
            opciones = ["Datos del Empleado", "Modificar Contraseña", "Cerrar Sesión"]
            icons = ["info-circle", "key", "power"]
        elif tipo_usuario == "Supervisor":
            opciones = [
                "Datos del Supervisor", "Aumento de Sueldo", 
                "Modificar Datos de Empleados", "Registrar Nuevo Empleado",
                "Eliminar Empleado", "Modificar Contraseña","Insights", "Cerrar Sesión"
            ]
            icons = [
                "person-badge", "cash-coin", "pencil", 
                "plus-circle", "trash", "key", "bar-chart", "power"
            ]

        seleccion = option_menu(
            menu_title=None, 
            options=opciones, 
            icons=icons,
            menu_icon="cast", 
            default_index=0,
            styles={
                "container": {"padding": "2rem 0.5rem", "background-color": "#F7F9FB"},
                "icon": {"font-size": "1.3rem", "color": "#007bff"},  # Iconos con color azul
                "nav-link": {
                    "font-size": "1.2rem", 
                    "font-weight": "bold",
                    "text-align": "left", 
                    "margin": "0.5rem 0.5rem",
                    "padding": "0.7rem 1rem",
                    "color": "#333",
                    "border-radius": "10px",
                },
                "nav-link-selected": {"background-color": "#007bff", "color": "white"},
                "nav-link-hover": {"background-color": "#E1E8ED"},
            }
        )
    return seleccion

# Función para manejar las opciones del menú
def manejar_opciones_menu(seleccion, tipo_usuario):
    st.markdown(f"<h3 style='text-align: center;'>Bienvenido al panel de {tipo_usuario}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    if seleccion == "Datos del Empleado" and tipo_usuario == "Empleado":
        st.subheader("📋 Datos del Empleado")
        if st.session_state.empleado_datos is not None:
            mostrar_datos_empleado(st.session_state.empleado_datos)
        else:
            st.error("No se ha encontrado información del empleado.")
    
    if seleccion == "Datos del Supervisor" and tipo_usuario == "Supervisor":
        st.subheader("📋 Datos del Supervisor")
        if st.session_state.supervisor_datos is not None:
            mostrar_datos_supervisor(st.session_state.supervisor_datos)
        else:
            st.error("No se ha encontrado información del supervisor.")

    if seleccion == "Aumento de Sueldo" and tipo_usuario == "Supervisor":
        aumento_sueldo(engine_empleados)

    if seleccion == "Modificar Datos de Empleados" and tipo_usuario == "Supervisor":
        modificar_datos_empleados(engine_empleados)

    if seleccion == "Registrar Nuevo Empleado" and tipo_usuario == "Supervisor":
        registrar_nuevo_empleado(engine_empleados)

    if seleccion == "Eliminar Empleado" and tipo_usuario == "Supervisor":
        eliminar_empleado(engine_empleados)

    if seleccion == "Modificar Contraseña" and st.session_state.login_exitoso:
        modificar_contrasena(engine_empleados, engine_supervisores)
    
    if seleccion == "Insights" and tipo_usuario == "Supervisor":
            visualizar_insights()

    if seleccion == "Cerrar Sesión":
        st.session_state.login_exitoso = False
        st.session_state.codigo_enviado = False
        st.session_state.empleado_datos = None
        st.session_state.supervisor_datos = None
        st.success("Has cerrado sesión exitosamente.")

# Título de la aplicación
st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #007bff;'>💼 SalaryBoost</h2>
    </div>
""", unsafe_allow_html=True)


# Verificar si ya hay un inicio de sesión exitoso
if 'login_exitoso' not in st.session_state:
    st.session_state.login_exitoso = False

if 'codigo_enviado' not in st.session_state:
    st.session_state.codigo_enviado = False

if 'empleado_datos' not in st.session_state:
    st.session_state.empleado_datos = None

if 'supervisor_datos' not in st.session_state:
    st.session_state.supervisor_datos = None

# Pantalla de Inicio de Sesión
if not st.session_state.login_exitoso:
    with st.form(key='login_form'):
        email = st.text_input("📧 Correo Electrónico")
        password = st.text_input("🔑 Contraseña", type='password')
        tipo_usuario = st.selectbox("👤 Tipo de Usuario", ["Empleado", "Supervisor"])
        submit_button = st.form_submit_button(label='Iniciar Sesión')

    if submit_button:
        datos_usuario = verificar_login(email, password, tipo_usuario)
        if not datos_usuario.empty:
            codigo = random.randint(100000, 999999)
            enviar_codigo_verificacion(email, codigo)
            st.session_state.codigo_verificacion = codigo
            st.session_state.codigo_enviado = True
            if tipo_usuario == "Empleado":
                st.session_state.empleado_datos = datos_usuario
            else:
                st.session_state.supervisor_datos = datos_usuario
            st.success("Se ha enviado un código de verificación a tu correo.")
        else:
            st.error("Credenciales incorrectas. Intenta de nuevo.")

    if st.session_state.codigo_enviado:
        with st.form(key='verificacion_form'):
            codigo_ingresado = st.text_input("🔐 Ingresa el código de verificación enviado a tu correo")
            submit_verificacion = st.form_submit_button(label='Verificar Código')

            if submit_verificacion:
                if int(codigo_ingresado) == st.session_state.codigo_verificacion:
                    st.session_state.login_exitoso = True
                    st.session_state.tipo_usuario = tipo_usuario  # Guardar tipo de usuario
                    st.success("Inicio de sesión exitoso.")
                else:
                    st.error("Código incorrecto. Intenta de nuevo.")

# Pantalla de Menú Principal (Post Login)
if st.session_state.login_exitoso:
    seleccion = mostrar_menu_principal(st.session_state.tipo_usuario)
    manejar_opciones_menu(seleccion, st.session_state.tipo_usuario)
