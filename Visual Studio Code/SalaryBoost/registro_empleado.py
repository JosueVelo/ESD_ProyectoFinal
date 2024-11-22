import streamlit as st
from sqlalchemy import text

def registrar_nuevo_empleado(engine_empleados):
    if st.session_state.login_exitoso and st.session_state.supervisor_datos is not None:
        st.header("📝 Registrar Nuevo Empleado")

        # Entrada para los datos del nuevo empleado
        emp_id = st.number_input("Ingrese el EmpID del nuevo empleado", min_value=1, step=1)
        first_name = st.text_input("Nombre")
        last_name = st.text_input("Apellido")
        title = st.text_input("Título")
        email = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")

        # Botones de opción para EmployeeType y PayZone
        employee_type = st.radio("Tipo de Empleado", ['Contract', 'Full-Time', 'Part-Time'])
        pay_zone = st.radio("Zona de Pago", ['Zone A', 'Zone B', 'Zone C'])

        department_type = st.text_input("Tipo de Departamento")
        dob = st.date_input("Fecha de Nacimiento")
        job_function_description = st.text_input("Descripción de la Función")
        gender_code = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
        race_desc = st.text_input("Raza")
        marital_desc = st.text_input("Estado Civil")

        performance_scores = ['Fully Meets', 'Exceeds', 'Needs Improvement', 'PIP']
        performance_score = st.radio("Puntuación de Rendimiento", performance_scores)

        current_employee_rating = st.number_input("Calificación Actual del Empleado (1 a 5)", min_value=1, max_value=5, step=1)
        monthly_salary = st.number_input("Salario Mensual", min_value=0, step=1)

        # Botón para registrar el nuevo empleado
        if st.button("💾 Registrar Empleado"):
            with engine_empleados.connect() as conn:
                try:
                    # Verificar si el EmpID ya existe
                    check_query = text("""
                        SELECT COUNT(*)
                        FROM "Employees"
                        WHERE "EmpID" = :emp_id
                    """)
                    result = conn.execute(check_query, {"emp_id": emp_id})
                    count = result.scalar()

                    if count > 0:
                        st.warning("⚠️ El EmpID ya existe. Por favor, ingrese un EmpID diferente.")
                    else:
                        # Insertar el nuevo empleado en la base de datos
                        insert_query = text("""
                            INSERT INTO "Employees" 
                            ("EmpID", "FirstName", "LastName", "Title", "Email", "Password", 
                             "EmployeeType", "PayZone", "DepartmentType", "DOB", 
                             "JobFunctionDescription", "GenderCode", "RaceDesc", 
                             "MaritalDesc", "Performance Score", "Current Employee Rating", 
                             "monthly_salary")
                            VALUES (:emp_id, :first_name, :last_name, :title, :email, :password, 
                                    :employee_type, :pay_zone, :department_type, :dob, 
                                    :job_function_description, :gender_code, :race_desc, 
                                    :marital_desc, :performance_score, :current_employee_rating, 
                                    :monthly_salary)
                        """)
                        conn.execute(insert_query, {
                            "emp_id": emp_id,
                            "first_name": first_name,
                            "last_name": last_name,
                            "title": title,
                            "email": email,
                            "password": password,  # Asegúrate de manejar la contraseña de manera segura
                            "employee_type": employee_type,
                            "pay_zone": pay_zone,
                            "department_type": department_type,
                            "dob": dob.isoformat(),  # Convertir a string en formato ISO
                            "job_function_description": job_function_description,
                            "gender_code": gender_code,
                            "race_desc": race_desc,
                            "marital_desc": marital_desc,
                            "performance_score": performance_score,
                            "current_employee_rating": current_employee_rating,
                            "monthly_salary": monthly_salary
                        })
                        conn.commit()  # Guardar cambios en la base de datos
                        st.success("✅ El nuevo empleado ha sido registrado exitosamente.")
                except Exception as e:
                    st.error(f"🚨 Ocurrió un error al registrar el empleado: {str(e)}")
