def executar_pipeline():

    vagas = executar_main()   # coleta

    boas_vagas = [v for v in vagas if v["score"] >= 5]

    for v in boas_vagas:
        enviar_alerta(v)

    exportar_excel(vagas)

    print("🚀 Pipeline finalizado")