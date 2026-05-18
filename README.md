
## Objetivo

Desarrollar un flujo de trabajo automatizado capaz de generar 1.000.000 de registros simulados, realizar la limpieza, análisis, visualización y simulación de datos relacionados con llamadas de emergencia; permitiendo transformar información desorganizada en conocimiento útil
---

##  Tecnologías utilizadas

**Python**  lenguaje principal
**pandas**  manejo y análisis de datos
**numpy**  cálculos numéricos y simulación
**matplotlib**  generación de gráficas
**FPDF** creación de reportes en PDF
**Streamlit**  interfaz web interactiva

---

## Estructura del sistema

El proyecto está dividido en varios módulos:

###  Generación de datos
Se simulan llamadas de emergencia con posibles errores (datos sucios) para representar escenarios reales.

### Limpieza de datos
Se corrigen inconsistencias como:
- zonas inválidas
- tipos incorrectos
- valores de gravedad fuera de rango
- fechas mal formateadas
- registros duplicados



###  Análisis de datos
Se obtienen métricas clave como:
- tipo de incidente más frecuente
- zona con más emergencias
- emergencias por día
- emergencias por hora

Estos análisis permiten identificar tendencias y apoyar procesos de predicción:

### Promedio móvil
Se utiliza para suavizar la tendencia de emergencias en el tiempo y detectar patrones reales sin ruido.

### Predicción
Se simulan emergencias futuras utilizando una distribución normal basada en el promedio histórico.



### Visualización
Se generan gráficas como:
- distribución de gravedad
- incidentes por tipo
- zonas con más emergencias
- horas pico
- promedio móvil
- predicción futura



###  Recomendación de ambulancias
El sistema identifica las zonas con mayor número de incidentes y genera recomendaciones para asignar más ambulancias en esas áreas.



###  Reporte en PDF
Se genera automáticamente un reporte que incluye:
- resumen general
- estadísticas
- tablas
- gráficas
- conclusiones
- recomendaciones


### Interfaz con Streamlit
Permite al usuario:
- subir archivos CSV
- visualizar datos
- generar análisis
- crear gráficas
- generar el PDF

## Cómo ejecutar el proyecto (todos los archivos deben estar en la misma carpeta)

```bash
#1. Instalar dependencias

pip install pandas numpy matplotlib fpdf streamlit

#2. ejecutar el programa principal con el main 
#esto genera los archivos csv para cargar en la interfaz

etapa3_compl.py

# 3. Ejecutar el programa principal sin el main (opcional)

etapa3.py

# 4. Ejecutar la interfaz de streamlit

#se ejecuta en el terminal, despues de ubicar la carpeta correcta
streamlit run app.py
