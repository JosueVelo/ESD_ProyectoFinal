from sqlalchemy import create_engine

# Configurar la conexión a la base de datos
engine_empleados = create_engine('postgresql://postgres:1234@localhost:5432/Employees')
engine_supervisores = create_engine('postgresql://postgres:1234@localhost:5432/Supervisors')
engine_logs = create_engine('postgresql://postgres:1234@localhost:5432/Logs') 
engine_employees_anonymized = create_engine('postgresql://postgres:1234@localhost:5432/Employees_anonymized')
