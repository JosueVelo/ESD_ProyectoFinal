import streamlit as st

# Función para mostrar los datos personales y de la empresa (empleado)
def mostrar_datos_empleado(datos_empleado):
    st.subheader("Datos Personales")
    st.markdown(f"""
    <div style="border: 1px solid #007bff; padding: 10px; border-radius: 5px;">
        <p><strong>Nombre completo:</strong> {datos_empleado['FirstName'].values[0]} {datos_empleado['LastName'].values[0]}</p>
        <p><strong>Correo electrónico:</strong> {datos_empleado['Email'].values[0]}</p>
        <p><strong>Fecha de nacimiento:</strong> {datos_empleado['DOB'].values[0]}</p>
        <p><strong>Género:</strong> {datos_empleado['GenderCode'].values[0]}</p>
        <p><strong>Raza o etnicidad:</strong> {datos_empleado['RaceDesc'].values[0]}</p>
        <p><strong>Estado civil:</strong> {datos_empleado['MaritalDesc'].values[0]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Datos de la Empresa")
    st.markdown(f"""
    <div style="border: 1px solid #28a745; padding: 10px; border-radius: 5px;">
        <p><strong>Posición o título:</strong> {datos_empleado['Title'].values[0]}</p>
        <p><strong>Departamento:</strong> {datos_empleado['DepartmentType'].values[0]}</p>
        <p><strong>Descripción de la función del trabajo:</strong> {datos_empleado['JobFunctionDescription'].values[0]}</p>
        <p><strong>Tipo de empleado:</strong> {datos_empleado['EmployeeType'].values[0]}</p>
        <p><strong>Zona salarial:</strong> {datos_empleado['PayZone'].values[0]}</p>
        <p><strong>Puntuación de desempeño:</strong> {datos_empleado['Performance Score'].values[0]}</p>
        <p><strong>Calificación actual del empleado:</strong> {datos_empleado['Current Employee Rating'].values[0]}</p>
        <p><strong>Salario mensual:</strong> {datos_empleado['monthly_salary'].values[0]}</p>
    </div>
    """, unsafe_allow_html=True)

# Función para mostrar los datos personales del supervisor
def mostrar_datos_supervisor(datos_supervisor):
    st.subheader("Datos Personales")
    st.markdown(f"""
    <div style="border: 1px solid #007bff; padding: 10px; border-radius: 5px;">
        <p><strong>Nombre completo:</strong> {datos_supervisor['FirstName'].values[0]} {datos_supervisor['LastName'].values[0]}</p>
        <p><strong>Correo electrónico:</strong> {datos_supervisor['Email'].values[0]}</p>
        <p><strong>Fecha de nacimiento:</strong> {datos_supervisor['DOB'].values[0]}</p>
        <p><strong>Género:</strong> {datos_supervisor['GenderCode'].values[0]}</p>
        <p><strong>Raza o etnicidad:</strong> {datos_supervisor['RaceDesc'].values[0]}</p>
        <p><strong>Estado civil:</strong> {datos_supervisor['MaritalDesc'].values[0]}</p>
        <p><strong>DNI:</strong> {datos_supervisor['DNI'].values[0]}</p>
        <p><strong>Edad:</strong> {datos_supervisor['Age'].values[0]}</p>
        <p><strong>Número de teléfono:</strong> {datos_supervisor['NumPhone'].values[0]}</p>
    </div>
    """, unsafe_allow_html=True)
