import streamlit as st
import re
from sqlalchemy import text

def modificar_contrasena(engine_empleados, engine_supervisores):
    st.header("🔒 Modificar Contraseña")

    user_type = st.selectbox("Seleccione su tipo de usuario:", ["Empleado", "Supervisor"])
    email = st.text_input("Ingrese su correo electrónico (Gmail)", type="default")
    current_password = st.text_input("Ingrese su contraseña actual", type="password")
    new_password = st.text_input("Nueva Contraseña", type="password")
    confirm_password = st.text_input("Confirme su Nueva Contraseña", type="password")

    # Función para validar la contraseña
    def validar_contrasena(password):
        if len(password) < 9:
            return "La contraseña debe tener al menos 9 caracteres."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "La contraseña debe contener al menos un carácter especial."
        return None  # Contraseña válida

    if st.button("🛡️ Cambiar Contraseña"):
        # Verificar si las contraseñas coinciden
        if new_password != confirm_password:
            st.warning("⚠️ Las contraseñas no coinciden. Por favor, intente de nuevo.")
        else:
            # Validar la nueva contraseña
            error = validar_contrasena(new_password)
            if error:
                st.warning(f"⚠️ {error}")  # Mostrar el error si la validación falla
            else:
                try:
                    if user_type == "Empleado":
                        # Verificar si el correo y la contraseña actual son correctos para Empleado
                        with engine_empleados.connect() as conn:
                            verify_query = text("""
                                SELECT COUNT(*)
                                FROM "Employees"
                                WHERE "Email" = :email AND "Password" = crypt(:current_password, "Password")
                            """)
                            result = conn.execute(verify_query, {
                                "email": email,
                                "current_password": current_password
                            })
                            count = result.scalar()

                            if count > 0:
                                # Actualizar la contraseña en la base de datos
                                update_query = text("""
                                    UPDATE "Employees"
                                    SET "Password" = crypt(:new_password, gen_salt('bf'))
                                    WHERE "Email" = :email
                                """)
                                conn.execute(update_query, {
                                    "new_password": new_password,
                                    "email": email
                                })
                                conn.commit()  # Guardar cambios en la base de datos
                                st.success("✅ La contraseña ha sido actualizada exitosamente.")
                            else:
                                st.warning("⚠️ Correo electrónico o contraseña actual incorrectos.")

                    elif user_type == "Supervisor":
                        # Verificar si el correo y la contraseña actual son correctos para Supervisor
                        with engine_supervisores.connect() as conn:
                            verify_query = text("""
                                SELECT COUNT(*)
                                FROM "Supervisors"
                                WHERE "Email" = :email AND "Password" = crypt(:current_password, "Password")
                            """)
                            result = conn.execute(verify_query, {
                                "email": email,
                                "current_password": current_password
                            })
                            count = result.scalar()

                            if count > 0:
                                # Actualizar la contraseña en la base de datos
                                update_query = text("""
                                    UPDATE "Supervisors"
                                    SET "Password" = crypt(:new_password, gen_salt('bf'))
                                    WHERE "Email" = :email
                                """)
                                conn.execute(update_query, {
                                    "new_password": new_password,
                                    "email": email
                                })
                                conn.commit()  # Guardar cambios en la base de datos
                                st.success("✅ La contraseña ha sido actualizada exitosamente.")
                            else:
                                st.warning("⚠️ Correo electrónico o contraseña actual incorrectos.")

                except Exception as e:
                    st.error(f"🚨 Ocurrió un error al modificar la contraseña: {str(e)}")
