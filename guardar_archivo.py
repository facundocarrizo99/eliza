#esto va al principio del programa#
registro_conversacion = []

#esto va adentro del while de adios#
registro_conversacion.append(f"Usuario: {entrada}\nEliza: {respuestaInicial + oracion_final}\n")

# Guardamos el registro de la conversación en un archivo de texto
with open('conversacion.txt', 'w') as archivo:
        for linea in registro_conversacion:
            archivo.write(linea)