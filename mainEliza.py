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

def limpiar_texto(entrada):
    entrada = entrada.lower()
    entrada = "".join(c for c in entrada if c.isalnum())
    return entrada

registro_conversacion = []
print("Bienvenido a Eliza, tu psicologa virtual")
print("Escribe 'adios' para salir")
print()
entrada = input("Hola! ¿Cual es tu problema?")
entrada = entrada.lower()
mensajeAnterior = ""

while entrada != "adios":
    ultimoMensaje = limpiar_texto(entrada)
    if ultimoMensaje == mensajeAnterior:
        print("ya te conteste esta pregunta, tienes otra consulta...?")
        mensajeAnterior = ultimoMensaje
    else:
        mensajeAnterior = ultimoMensaje
        procesarCadena(entrada)
    print()
    entrada = input("").lower()

print("¡Nos vemos! ¡Gracias!")
with open('conversacion.txt', 'a') as archivo:
    archivo.write("INICIO DE LA CONVERSACION\n")
    for linea in registro_conversacion:
        archivo.write(linea)
    archivo.write("FIN DE LA CONVERSACION\n\n")
