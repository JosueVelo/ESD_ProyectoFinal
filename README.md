![image](https://github.com/user-attachments/assets/3406bd13-0537-4774-9598-00ce8b2a2619)

# Proyecto Final - Ética y Seguridad de Datos 
---
## Parte 1: Privacidad 
---
### A. Clasificación de los Datos de Empleados

#### 1. Datos Personales
- *FirstName*: Nombre del empleado.
- *LastName*: Apellido del empleado.
- *DOB*: Fecha de nacimiento.
- *Email*: Dirección de correo electrónico.
- *GenderCode*: Código de género.
- *RaceDesc*: Descripción de la raza.
- *MaritalDesc*: Descripción del estado civil.
- *EmpID*: ID único del empleado.

#### 2. Datos Sensibles
- *Password*: Contraseña del empleado (datos de seguridad).
- *Performance Score*: Puntuación de desempeño.
- *Current Employee Rating*: Calificación del empleado.

#### 3. Datos Públicos
- *EmployeeType*: Tipo de empleado (puede ser público, como si es permanente o temporal).
- *PayZone*: Zona de pago (aunque se puede considerar público en algunos contextos, es mejor manejarlo con cierta confidencialidad dependiendo de la empresa).
- *DepartmentType*: Tipo de departamento (también puede ser considerado público, dependiendo del contexto organizacional).
- *JobFunctionDescription*: Descripción del puesto de trabajo (aunque es información general, podría ser accesible públicamente dentro de la empresa).

#### 4. Datos Confidenciales 
- *monthly_salary*: Salario mensual (considerado confidencial debido a su naturaleza económica).

---

### B. Técnicas de Privacidad - Datos

1. **Anonimización**: Se eliminan completamente las columnas que contienen información identificable como `EmpID`, `FirstName` , `LastName`, `JobFunctionDescription`, `Title`, `Password`, `PayZone`, y `RaceDesc`. Esto elimina los datos personales que podrían identificar a los individuos directamente.

2. **Pseudonimización**: La columna `Email` es transformada aplicando un hash truncado (solo los primeros 5 caracteres del hash) del correo electrónico original, lo que asegura que no se pueda asociar el correo original a la persona, pero mantiene la estructura de correo (dominio) intacta.

4. **Privacidad Diferencial**: Se utiliza el algoritmo `BoundedMean` de la librería `pydp` para calcular un promedio diferencialmente privado sobre la columna `monthly_salary`. Esto introduce ruido controlado por el valor de `epsilon` para proteger la privacidad de los individuos en los datos.

5. **K-Anonimato**:
- Se aplica la técnica de K-anonimato utilizando la librería `pycanon`. El código evalúa si el conjunto de datos cumple con el criterio de anonimato para las columnas de identificación cuasi (`QI`), como `Performance Score` y `Current Employee Rating`. Además, se define un atributo sensible (SA), en este caso, `monthly_salary`, que se protege en el análisis para asegurar que no se pueda identificar a individuos a partir de estos datos.

- Las edades se agrupan en rangos predefinidos usando `pd.cut`, lo que anonimiza la edad exacta de los empleados y reduce la posibilidad de identificación. Esta categorización contribuye al fortalecimiento de la privacidad al evitar que la edad exacta se pueda conocer dentro de un grupo.

Estas técnicas permiten procesar y analizar los datos de empleados manteniendo su privacidad y utilidad para análisis.

---

### C. Funcionalidades de Privacidad en SalaryBoost

1. **Empleado / "Modificar Contraseña"**:
   - La opción de **modificar contraseña** permite a los empleados gestionar su acceso de manera autónoma, garantizando que solo ellos puedan acceder a sus cuentas. Este control sobre sus credenciales es fundamental para proteger la privacidad de los datos personales y de acceso, alineándose con principios de autonomía y control del usuario que establece el Reglamento General de Protección de Datos (RGPD).
   
2. **Supervisor / "Modificar Datos de Empleados"**:
   - La funcionalidad de **modificar datos de empleados** permite actualizar la información personal de los empleados bajo su solicitud. Esto es importante porque **SalaryBoost** permite que los empleados mantengan sus datos actualizados, lo que es un derecho protegido bajo el RGPD. Los empleados pueden corregir o actualizar cualquier dato erróneo o desactualizado, lo que garantiza que los registros sean precisos y conforme a los principios de integridad y exactitud de los datos.

3. **Supervisor / "Eliminar Empleado"**:
   - Cuando un empleado deja la empresa, **SalaryBoost** ofrece la opción de **eliminar sus datos**. Este procedimiento es crucial para cumplir con el principio de **limitación del almacenamiento** del RGPD, que estipula que los datos personales deben ser eliminados cuando ya no sean necesarios para el propósito para el cual fueron recopilados. Así, se asegura que los datos de los empleados no se mantengan en la plataforma una vez que ya no sean pertinentes, reduciendo el riesgo de exposición de información sensible.

4. **Supervisor / "Modificar Contraseña"**:
   - Los supervisores también pueden modificar la contraseña de un empleado, lo cual puede ser útil para situaciones de seguridad o cuando un empleado olvida sus credenciales. Esto asegura que el acceso al sistema se mantenga controlado y seguro. Esta función está alineada con las medidas de seguridad requeridas bajo el RGPD, que establece que los datos deben ser protegidos mediante medidas técnicas y organizativas adecuadas para evitar el acceso no autorizado.

#### Cumplimiento con el RGPD:
Las funcionalidades mencionadas son esenciales para `SalaryBoost` al cumplir con varios principios clave del `RGPD`, como:
- **Control del usuario**: Brindar al empleado la capacidad de modificar su contraseña y actualizar sus datos personales, asegurando su autonomía sobre la información que se recopila y gestiona.
- **Precisión de los datos**: Permitir la modificación de datos garantiza que la información almacenada en el sistema esté siempre actualizada y sea precisa, cumpliendo con el principio de exactitud.
- **Limitación del almacenamiento**: La opción de eliminar los datos de un empleado cuando ya no es necesario para el propósito original (cuando deja la empresa) asegura que la empresa no retenga información más allá de lo permitido por la ley.
- **Seguridad de los datos**: La capacidad de modificar contraseñas, tanto por parte del empleado como del supervisor, asegura que el acceso a los datos personales esté protegido y que los datos no sean accesibles sin la debida autorización.
  
Estas medidas garantizan que **SalaryBoost** no solo protege la privacidad de los empleados, sino que también cumple con las normativas internacionales de protección de datos, como el RGPD.

---

### D. Conclusión 
- En resumen, SalaryBoost garantiza la privacidad de los empleados mediante técnicas como anonimización, pseudonimización, privacidad diferencial y K-Anonimato, alineándose con el RGPD. Las funcionalidades clave, como la capacidad de modificar contraseñas, actualizar datos y eliminar registros, permiten a los empleados controlar su información personal, asegurando su precisión, seguridad y limitación del almacenamiento. Estas medidas protegen la privacidad de los empleados y aseguran el cumplimiento de normativas internacionales de protección de datos.

---
## Parte 2: Ética
---
### A. Evaluación de Impacto en la Protección de Datos (DPIA) para SalaryBoost

#### 1. Descripción del Flujo de Datos
SalaryBoost gestiona una variedad de datos de los empleados y supervisores. Estos datos incluyen información personal (como nombre, fecha de nacimiento, y género), información laboral (como salario mensual y rendimiento), y credenciales de acceso. Los datos son introducidos en el sistema por los supervisores y empleados, procesados y almacenados en bases de datos, y protegidos por medidas de seguridad como cifrado SSL, autenticación multifactor, y políticas de control de acceso.

El flujo de los datos incluye:
- **Recopilación de Datos**: Los supervisores ingresan datos del empleado, que pueden incluir información personal y laboral.
- **Almacenamiento de Datos**: Los datos se almacenan en bases de datos protegidas, con acceso restringido.
- **Acceso a Datos**: Supervisores y empleados acceden a datos de acuerdo con sus roles, y pueden modificar o eliminar ciertos datos bajo permisos específicos.
- **Uso de Datos**: Los supervisores utilizan estos datos para tomar decisiones relacionadas con el desempeño y compensación de los empleados.
- **Transferencia de Datos**: Se utiliza cifrado para garantizar que los datos no sean interceptados durante el tránsito.
  
#### 2. Identificación de Riesgos

Riesgos Potenciales:
- **Acceso No Autorizado**: Los datos podrían ser accedidos por usuarios no autorizados debido a fallos en la gestión de accesos o credenciales comprometidas.
- **Pérdida de Datos**: Pérdida de datos sensibles debido a fallos del sistema o incidentes de seguridad, como ataques de malware o ransomware.
- **Uso indebido de Datos**: Supervisores o empleados podrían modificar, eliminar o divulgar datos de forma inapropiada.
- **Vulnerabilidades en la Transmisión de Datos**: A pesar del cifrado SSL, podría haber vulnerabilidades en la transmisión de datos o en puntos de acceso no protegidos.
- **Violación de la Privacidad**: La exposición de datos personales (como salario o calificaciones) podría violar los derechos de privacidad de los empleados.

#### 3. Evaluación de Impacto
**1. Evaluación de la Necesidad y Proporcionalidad de la Recopilación de Datos** 

La recopilación de datos en SalaryBoost se justifica en función de las necesidades empresariales: gestionar el rendimiento de los empleados, aplicar aumentos salariales y realizar seguimiento de la productividad. Sin embargo, se debe garantizar que la cantidad de datos recopilados sea proporcional al objetivo, evitando la recopilación excesiva de información personal.

**2. Medidas para Mitigar los Riesgos Identificados** 
- **Cifrado de Datos**: Utilización de certificados SSL para proteger la transmisión de datos. Se recomienda implementar protocolos de seguridad adicionales, como TLS, para fortalecer la protección de la transmisión de datos.
- **Autenticación Multifactor (MFA)**: La autenticación de usuarios mediante MFA proporciona una capa adicional de seguridad para prevenir el acceso no autorizado. Es recomendable revisar y actualizar el sistema MFA periódicamente para asegurar su efectividad.
- **Gestión de Accesos y Roles**: Implementación de una política estricta de control de accesos basada en roles, asegurando que solo los usuarios autorizados tengan acceso a datos sensibles.
- **Backups Regulares**: Realización de copias de seguridad periódicas de la base de datos, asegurando la disponibilidad de los datos en caso de pérdida o corrupción.
- **Auditorías de Seguridad**: Implementación de auditorías de seguridad regulares para identificar vulnerabilidades y mitigar posibles riesgos de acceso no autorizado o manipulación de datos.
- **Entrenamiento y Concientización en Seguridad**: Capacitación continua a empleados y supervisores sobre prácticas de seguridad, detección de amenazas y gestión segura de contraseñas.
- **Política de Retención de Datos**: Implementación de políticas claras sobre la retención y eliminación de datos. Los datos deben ser eliminados cuando ya no sean necesarios para los fines para los cuales fueron recopilados.

**3. Riesgos Residuales**

A pesar de las medidas implementadas, existen riesgos residuales asociados a la gestión de datos sensibles:
- **Fugas de Datos**: Aunque se han tomado medidas para proteger los datos, siempre existe el riesgo de filtración de datos a través de vulnerabilidades imprevistas.
- **Errores Humanos**: Los usuarios podrían accidentalmente modificar o divulgar información sensible debido a falta de capacitación o errores de manejo de contraseñas.

#### 4. Plan de Mitigación
- **Monitoreo Continuo de la Plataforma**: Implementar sistemas de monitoreo en tiempo real para detectar posibles vulnerabilidades o accesos no autorizados.
- **Revisión y Mejora de Controles de Seguridad**: Establecer un ciclo de revisión regular de los controles de seguridad, incluyendo la autenticación y los accesos, para garantizar que sean adecuados a las amenazas emergentes.
- **Revisión de Políticas de Privacidad**: Asegurarse de que las políticas de privacidad y protección de datos sean revisadas y actualizadas con regularidad para cumplir con las leyes y regulaciones aplicables (como el RGPD).

---
### B. Reflexiones Éticas en el Contexto de SalaryBoost
**1. Sesgo Algorítmico**: El sesgo algorítmico ocurre cuando un sistema automatizado toma decisiones que reflejan prejuicios o injusticias en función de los datos en los que fue entrenado. En el caso de Salaryboost, una plataforma que podría utilizar algoritmos para prever el salario potencial de un individuo en función de su formación, experiencia, habilidades y otros factores, es crucial identificar y mitigar cualquier sesgo en el algoritmo que pueda perpetuar desigualdades preexistentes.

Posibles fuentes de sesgo:
- *Datos históricos sesgados*: Si los datos utilizados para entrenar el algoritmo contienen sesgos de género, raza, orientación sexual u otros factores, el modelo podría reforzar estos sesgos al predecir el salario. Por ejemplo, si históricamente ciertos grupos han tenido menores salarios debido a discriminación, el algoritmo podría replicar esta disparidad.

- *Selección de variables*: Las decisiones sobre qué variables incluir en el algoritmo (como la educación, la experiencia laboral, etc.) pueden estar influenciadas por prejuicios sociales y culturales. Si las variables seleccionadas no reflejan un contexto justo o equilibrado, el algoritmo puede favorecer ciertos perfiles sobre otros.

**Reflexión ética**: Es esencial que `Salaryboost` implemente procesos de `auditoría algorítmica` y realice `pruebas de sesgo` periódicas para asegurarse de que las recomendaciones salariales no estén perpetuando desigualdades injustas. También, debe considerar la implementación de `modelos de aprendizaje justo`, que minimicen las disparidades en las predicciones salariales para grupos históricamente desfavorecidos.

**2. Transparencia**: La transparencia en los algoritmos implica que los usuarios comprendan cómo y por qué se toman las decisiones. En el contexto de Salaryboost, es fundamental que los usuarios comprendan cómo se calculan sus estimaciones salariales, qué datos están siendo utilizados y de qué manera estos influyen en las predicciones.

**Reflexión ética**: Para promover la transparencia, `Salaryboost` debe proporcionar explicaciones claras y accesibles de cómo funciona su algoritmo, cómo se utilizan los datos personales y cómo se genera la predicción salarial. Esto no solo fomenta la confianza en la plataforma, sino que también permite a los usuarios tomar decisiones informadas sobre compartir sus datos. La `explicabilidad` es un principio ético clave en la inteligencia artificial que debería estar en el centro de cualquier sistema algorítmico.

**3. Consentimiento**: El `consentimiento` implica que los usuarios deben tener el control sobre sus propios datos y entender cómo se utilizarán. Para `Salaryboost,` esto significa que antes de recopilar o utilizar los datos personales de los usuarios (por ejemplo, información sobre salario, historial laboral, etc.), debe obtenerse el consentimiento explícito de los mismos.

**Reflexión ética**: `Salaryboost` debe asegurarse de que los usuarios den un consentimiento informado sobre el uso de sus datos. Esto incluye informarles sobre cómo se utilizarán sus datos, qué implicaciones tiene la recopilación de estos, y ofrecerles la opción de retirar su consentimiento en cualquier momento. Además, debe garantizar la `protección de datos` mediante el uso de `políticas de privacidad claras` y prácticas de seguridad de datos robustas.

---

### C. Conclusión
- Al integrar estos principios éticos en el diseño y funcionamiento de Salaryboost, se promueve no solo un entorno más justo y equitativo para los usuarios, sino también una plataforma más confiable y respetuosa con los derechos de los individuos. Reflexionar sobre temas como el sesgo algorítmico, la transparencia y el consentimiento puede contribuir a crear una cultura ética en el desarrollo de tecnologías basadas en datos y algoritmos.
