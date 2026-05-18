
if __name__ == "__main__":

    """
    sistema de análisis de emergencias.

    Este bloque ejecuta todo el proceso completo:
    1. Generación de datos simulados
    2. Carga y limpieza de datos
    3. Análisis estadístico
    4. Visualización mediante gráficas
    5. Simulación y predicción de emergencias futuras
    6. Generación de recomendaciones de ambulancias
    7. Exportación de datos limpios y creación del reporte PDF
    """

    # 1. GENERAR
    generador = GeneradorDatos()
    generador.cargar_datos(1000000)
    generador.exportar_csv()

    # 2. CARGAR ARCHIVO
    df = pd.read_csv("llamadas_sucias.csv", sep=";")

    # 3. LIMPIAR
    limpiador = LimpiarDatos(df)

    limpiador.limpiar_zonas()
    limpiador.limpiar_tipos()
    limpiador.limpiar_gravedad()
    limpiador.limpiar_fechas()
    limpiador.crear_hora()
    limpiador.ordenar_por_fecha()

    eliminados = limpiador.eliminar_duplicados()

    # actualizar df
    df = limpiador.df

    # 4. ANALIZAR
    analizador = AnalizadorDatos(df)
    graficas = Graficas(df)
    simulador = SimuladorDatos(df)


    print("Duplicados eliminados:", eliminados)

    print(analizador.clasificar_incidentes())
    print(analizador.identificar_zonas_criticas())

    print(analizador.emergencias_por_dia())
    print(analizador.promedio_movil())

    # 5. GRÁFICAS
    graficas.grafica_gravedad()
    graficas.grafica_zonas()
    graficas.grafica_tipos()
    graficas.grafica_horas()
    graficas.grafica_promedio_movil(analizador.promedio_movil())

    # 6. SIMULACIÓN
    pred = simulador.predecir(7)
    print(pred)
    graficas.graficar_prediccion(pred)

    #ambulancias
    recs = recomendacion_ambulancias(df)
    print("\nRECOMENDACIONES:")
    for r in recs:
      print("-", r)

    # 7. EXPORTAR LIMPIO
    df.to_csv("llamadas_limpias.csv", sep=";", index=False)
    generar_reporte_pdf(df, analizador, eliminados)

    print("Proceso completo ")