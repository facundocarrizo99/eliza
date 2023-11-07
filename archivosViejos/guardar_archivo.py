def guardar_conversacion(registro_conversacion):
    with open('../conversacion.txt', 'a') as archivo:
        archivo.write("INICIO DE LA CONVERSACION\n")
        for linea in registro_conversacion:
            archivo.write(linea)
        archivo.write("FIN DE LA CONVERSACION\n\n")