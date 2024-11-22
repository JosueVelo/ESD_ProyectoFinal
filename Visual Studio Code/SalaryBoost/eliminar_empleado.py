import streamlit as st
from sqlalchemy import text

def eliminar_empleado(engine_supervisores):
    if st.session_state.login_exitoso and st.session_state.supervisor_datos is not None:
        st.header("🗑️ Eliminar Empleado")

        # Ingreso del EmpID para el empleado a eliminar
        emp_id = st.number_input("EmpID del empleado a eliminar:", min_value=1, step=1)

        # Confirmación de eliminación
        if st.checkbox("✔️ Estoy seguro de que quiero eliminar este empleado"):
            if st.button("🗑️ Confirmar Eliminación"):
                try:
                    with engine_supervisores.connect() as conn:
                        # Eliminar el empleado basado en el EmpID
                        delete_query = text("""
                            DELETE FROM "Employees"
                            WHERE "EmpID" = :emp_id
                        """)
                        result = conn.execute(delete_query, {"emp_id": emp_id})
                        conn.commit()  # Guardar cambios en la base de datos

                        # Verificar si se eliminó algún registro
                        if result.rowcount > 0:
                            st.success(f"✅ El empleado con ID **{emp_id}** ha sido eliminado exitosamente.")
                        else:
                            st.warning("⚠️ No se encontró ningún empleado con ese EmpID.")
                except Exception as e:
                    st.error(f"🚨 Ocurrió un error al eliminar el empleado: {str(e)}")
        else:
            st.info("Por favor, marque la casilla para confirmar que desea eliminar este empleado.")

