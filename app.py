import streamlit as st
import pandas as pd

from etapa3 import LimpiarDatos, AnalizadorDatos, Graficas, SimuladorDatos, generar_reporte_pdf, recomendacion_ambulancias

st.title("🚑 Sistema de Emergencias")

# SUBIR ARCHIVO
archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if archivo is not None:

    df = pd.read_csv(archivo, sep=";")

    st.subheader("Datos originales")
    st.write(df.head())

    # LIMPIEZA
    limpiador = LimpiarDatos(df)

    limpiador.limpiar_zonas()
    limpiador.limpiar_tipos()
    limpiador.limpiar_gravedad()
    limpiador.limpiar_fechas()
    limpiador.crear_hora()

    df = limpiador.df

    st.subheader("Datos limpios")
    st.write(df.head())

    # ANALISIS
    analizador = AnalizadorDatos(df)

    st.subheader("📊 Estadísticas")
    st.write(analizador.clasificar_incidentes())

    zona, cant = analizador.identificar_zonas_criticas()
    st.write(f"Zona crítica: {zona} ({cant})")



    # GRAFICAS
    graficas = Graficas(df)
    simulador = SimuladorDatos(df)

    if st.button("Generar gráficas"):
        graficas.grafica_gravedad()
        st.image("gravedad.png")

        graficas.grafica_zonas()
        st.image("zonas.png")

        graficas.grafica_tipos()
        st.image("tipos.png")

        graficas.grafica_horas()
        st.image("horas.png")
        

        prom = analizador.promedio_movil()
        graficas.grafica_promedio_movil(prom)
        st.image("promedio_movil.png")
        
        pred = simulador.predecir(7)
        graficas.graficar_prediccion(pred)
        st.image("proyeccion.png")

        st.success("Gráficas generadas")

    st.subheader("🚑 Recomendaciones de Ambulancias")
    recs = recomendacion_ambulancias(df)
    for r in recs:
        st.success(r)


    # PDF
    if st.button("Generar PDF"):
        generar_reporte_pdf(df, analizador, 0)
        st.success("PDF generado")