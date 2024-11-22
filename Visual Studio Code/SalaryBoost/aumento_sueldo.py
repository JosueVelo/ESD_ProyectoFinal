import streamlit as st
from sqlalchemy import text

def aumento_sueldo(engine_empleados):
    if st.session_state.login_exitoso and st.session_state.supervisor_datos is not None:
        st.header("Aumento de Sueldo para Empleados")

        # Selección de Performance Scores
        performance_scores = ['Fully Meets', 'Exceeds', 'Needs Improvement', 'PIP']
        selected_performance_score = st.radio("Selecciona el Performance Score", performance_scores)

        # Entrada para Current Employee Rating
        current_employee_rating = st.number_input("Ingrese el Current Employee Rating (1 a 5)", min_value=1, max_value=5)

        # Entrada para el porcentaje de aumento de sueldo
        aumento_sueldo = st.number_input("Ingrese el porcentaje de aumento de sueldo (0 a 100)", min_value=0, max_value=100)

        if st.button("✅ Aplicar Aumento de Sueldo"):
            try:
                with engine_empleados.connect() as conn:
                    # Verificar cuántos registros cumplen con el criterio
                    select_query = text(""" 
                        SELECT COUNT(*)
                        FROM "Employees"
                        WHERE "Performance Score" = :performance_score
                          AND "Current Employee Rating" = :rating
                    """)
                    result = conn.execute(select_query, {"performance_score": selected_performance_score, "rating": current_employee_rating})
                    count = result.scalar()

                    # Imprimir cuántos empleados cumplen con el criterio
                    print("Empleados que cumplen con el criterio:", count)

                    if count > 0:
                        # Actualizar el salario de los empleados que cumplen con los criterios
                        query = text("""
                            UPDATE "Employees"
                            SET "monthly_salary" = "monthly_salary" * (1 + :aumento)
                            WHERE "Performance Score" = :performance_score
                              AND "Current Employee Rating" = :rating
                        """)
                        # Ejecutar la consulta de actualización
                        conn.execute(query, {"aumento": aumento_sueldo / 100.0, "performance_score": selected_performance_score, "rating": current_employee_rating})
                        conn.commit()  # Asegúrate de guardar los cambios

                        # Mensaje de éxito
                        st.success(f"✅ El aumento de sueldo del **{aumento_sueldo}%** ha sido aplicado a **{count} empleado(s)** que cumplen con los criterios.")
                    else:
                        # Mensaje si no se encontraron empleados
                        st.warning("⚠️ No se encontraron empleados que cumplan con los criterios seleccionados.")
            except Exception as e:
                # Captura de errores y mensaje de error
                st.error(f"🚨 Ocurrió un error: {str(e)}")
