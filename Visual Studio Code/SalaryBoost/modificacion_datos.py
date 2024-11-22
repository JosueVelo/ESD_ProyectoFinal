import streamlit as st
from sqlalchemy import text

def modificar_datos_empleados(engine_empleados):
    if st.session_state.login_exitoso and st.session_state.supervisor_datos is not None:
        st.header("🛠️ Modificar Datos de Empleados")

        # Entrada para el EmpID del empleado
        emp_id = st.number_input("Ingrese el EmpID del empleado a modificar", min_value=1, step=1)

        if emp_id:
            with engine_empleados.connect() as conn:
                # Consulta para obtener los datos actuales del empleado
                query = text(""" 
                    SELECT "Title", "Email", "EmployeeType", "DepartmentType", 
                           "JobFunctionDescription", "MaritalDesc", 
                           "Performance Score", "Current Employee Rating", "monthly_salary"
                    FROM "Employees"
                    WHERE "EmpID" = :emp_id
                """)
                result = conn.execute(query, {"emp_id": emp_id})
                empleado = result.fetchone()

                if empleado:
                    st.subheader("📋 Datos Actuales del Empleado")
                    
                    # Mostrar los datos actuales del empleado en campos editables
                    title = st.text_input("Título", empleado[0])  # Acceso por índice
                    email = st.text_input("Correo Electrónico", empleado[1])  # Acceso por índice
                    employee_type = st.text_input("Tipo de Empleado", empleado[2])  # Acceso por índice
                    department_type = st.text_input("Tipo de Departamento", empleado[3])  # Acceso por índice
                    job_function_description = st.text_input("Descripción de la Función", empleado[4])  # Acceso por índice
                    marital_desc = st.text_input("Estado Civil", empleado[5])  # Acceso por índice

                    st.subheader("🌟 Evaluación")
                    performance_scores = ['Fully Meets', 'Exceeds', 'Needs Improvement', 'PIP']
                    performance_score = st.radio("Puntuación de Rendimiento", performance_scores, index=performance_scores.index(empleado[6]))  # Acceso por índice
                    
                    current_employee_rating = st.number_input("Calificación Actual del Empleado (1 a 5)", min_value=1, max_value=5, value=empleado[7], step=1)  # Aseguramos que sea un entero
                    
                    # Convertir el salario mensual a entero para evitar errores
                    monthly_salary = st.number_input("Salario Mensual", min_value=0, value=int(empleado[8]), format="%d", step=1)  # Aseguramos que sea un entero

                    # Botón para guardar cambios
                    if st.button("💾 Guardar Cambios", key="save_changes"):
                        try:
                            # Actualizar los datos del empleado en la base de datos
                            update_query = text(""" 
                                UPDATE "Employees"
                                SET "Title" = :title,
                                    "Email" = :email,
                                    "EmployeeType" = :employee_type,
                                    "DepartmentType" = :department_type,
                                    "JobFunctionDescription" = :job_function_description,
                                    "MaritalDesc" = :marital_desc,
                                    "Performance Score" = :performance_score,
                                    "Current Employee Rating" = :current_employee_rating,
                                    "monthly_salary" = :monthly_salary
                                WHERE "EmpID" = :emp_id
                            """)
                            conn.execute(update_query, {
                                "title": title,
                                "email": email,
                                "employee_type": employee_type,
                                "department_type": department_type,
                                "job_function_description": job_function_description,
                                "marital_desc": marital_desc,
                                "performance_score": performance_score,
                                "current_employee_rating": current_employee_rating,
                                "monthly_salary": monthly_salary,
                                "emp_id": emp_id
                            })
                            conn.commit()  # Guardar cambios en la base de datos
                            st.success("✅ Los datos del empleado han sido actualizados exitosamente.")
                        except Exception as e:
                            st.error(f"🚨 Ocurrió un error al guardar los cambios: {str(e)}")
                else:
                    st.warning("⚠️ No se encontró ningún empleado con el EmpID proporcionado.")
