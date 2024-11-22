import pandas as pd
from sqlalchemy import text
from database import engine_empleados, engine_supervisores, engine_logs

# Función para verificar el inicio de sesión
def verificar_login(email, password, tipo_usuario):
    # Construir la consulta dependiendo del tipo de usuario
    if tipo_usuario == "Empleado":
        query = text("""
        SELECT * FROM "Employees"
        WHERE "Email" = :email AND "Password" = crypt(:password, "Password")
        """)
        params = {"email": email, "password": password}
        engine = engine_empleados
    else:  # Supervisor
        query = text("""
        SELECT * FROM "Supervisors"
        WHERE "Email" = :email AND "Password" = crypt(:password, "Password")
        """)
        params = {"email": email, "password": password}
        engine = engine_supervisores

    # Leer los datos desde la base de datos
    with engine.connect() as connection:
        result = pd.read_sql(query, connection, params=params)
    
    # Insertar registro en la tabla de auditoría
    if not result.empty:
        resultado = "Exitoso"
    else:
        resultado = "Fallido"

    log_query = text("""
        INSERT INTO "LoginAudit" ("email", "tipo_usuario", "resultado")
        VALUES (:email, :tipo_usuario, :resultado)
    """)
    
    # Registrar en la tabla de auditoría de logs
    with engine_logs.begin() as connection:
        connection.execute(log_query, {"email": email, "tipo_usuario": tipo_usuario, "resultado": resultado})

    return result