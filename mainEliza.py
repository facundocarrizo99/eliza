import diccionario as dic
import random

def componerOracion(texto, listaPalabras):
    try:
        for palabra in listaPalabras:
            if palabra in dic.listaDeBasuras:
                listaPalabras.remove(palabra)
        value = texto.replace("*", listaPalabras[0])
    except IndexError:
        value = texto
    return value

def analizarCadena(dic, listaPalabras):
    for palabra in listaPalabras:
        if palabra in dic:
            respuesta = random.choice(dic[palabra])
            listaPalabras.remove(palabra)
            break
        else:
            respuesta = random.choice(dic["sinrespuesta"])
    return respuesta

def procesarCadena(entrada):
    listaPalabras = entrada.split()
    respuestaInicial = analizarCadena(dic.diccionario, listaPalabras)
    if "*" in respuestaInicial:
        cadCompuesta = componerOracion(respuestaInicial, listaPalabras)
        print(cadCompuesta)
        registro_conversacion.append(f"Usuario: {entrada}\nEliza: {cadCompuesta}\n")
    else:
        print(respuestaInicial)
        registro_conversacion.append(f"Usuario: {entrada}\nEliza: {respuestaInicial}\n")

def limpiarTexto(cad):
    cad = cad.lower()
    cad = "".join(c for c in cad if c.isalnum())
    return cad

def sacarPuntuacion(cadena):
    for carPuntuacion in cadena:
        if carPuntuacion in dic.punc:
            cadena = cadena.replace(carPuntuacion, "")
    return cadena

registro_conversacion = []
print("Bienvenido a Eliza, tu psicologa virtual")
print("Escribe 'adios' para salir")
print()
entrada = input("Hola! ¿Cual es tu problema?")
entrada = entrada.lower()
mensajeAnterior = ""

#TO DO: El analizador del diccionario solo llega hasta esperanza, linea 27, la 28 ya no

while entrada != "adios":
    ultimoMensaje = limpiarTexto(entrada)
    if ultimoMensaje == mensajeAnterior:
        print("ya te conteste esta pregunta, tienes otra consulta...?")
        mensajeAnterior = ultimoMensaje
    else:
        mensajeAnterior = ultimoMensaje
        procesarCadena(sacarPuntuacion(entrada)) #Sacamos los caracteres de puntuacion antes de comparar los elementos
    print()
    entrada = input("").lower()

print("¡Nos vemos! ¡Gracias!")
with open('conversacion.txt', 'a') as archivo:
    archivo.write("INICIO DE LA CONVERSACION\n")
    for linea in registro_conversacion:
        archivo.write(linea)
    archivo.write("FIN DE LA CONVERSACION\n\n")

