#from mainEliza import sacarPuntuacion

prueba = "furioso"
tuplaRespuestas = ("Te parece normal estar furioso?", "Lo que me da mas bronca es que esto va a andar")

def convertirACSV(algo, otracosa):
    respuestas = str(otracosa)
    dato = algo + "," + respuestas
    return dato

dato = convertirACSV(prueba,tuplaRespuestas)

with open('../respuestasAgregadas.csv', 'a') as archivo:
    archivo.write(dato + "\n")
archivo.close()
############################################################################################

respuestas = []
try:
    with open('../respuestasAgregadas.csv', 'r') as archivo:
        for linea in archivo:
            listaDeLinea = linea.split(",")
            if listaDeLinea[0] == prueba:
                listaDeLinea.remove(prueba)
                for respuesta in listaDeLinea:
                    respuesta = sacarPuntuacion(respuesta)
                    respuesta = respuesta.replace("\n", "")
                    respuesta = respuesta.lstrip(" ")
                    respuestas.append(respuesta)
                print(respuestas)
                print(respuestas[0])
                print(respuestas[1])
                break
except OSError as message:
    print("No existe el archivo")
finally:
    try:
        archivo.close()
    except NameError:
        print("NameError")

