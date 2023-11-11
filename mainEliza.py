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

def hablarConEliza():
    print("Escribe 'adios' para salir")
    entrada = input("Hola! me llamo Eliza. Como te puedo ayudar hoy?: ")
    entrada = entrada.lower()
    mensajeAnterior = ""
    while entrada != "adios":
        ultimoMensaje = limpiarTexto(entrada)
        if ultimoMensaje == mensajeAnterior:
            print("ya te conteste esta pregunta, tienes otra consulta...?")
            mensajeAnterior = ultimoMensaje
        else:
            mensajeAnterior = ultimoMensaje
            procesarCadena(
                sacarPuntuacion(entrada))  # Sacamos los caracteres de puntuacion antes de comparar los elementos
        print()
        entrada = input("").lower()

    print("¡Nos vemos! ¡Gracias!")
    with open('conversacion.txt', 'a') as archivo:
        archivo.write("INICIO DE LA CONVERSACION\n")
        for linea in registro_conversacion:
            archivo.write(linea)
        archivo.write("FIN DE LA CONVERSACION\n\n")

def agregarVariasRespuestas():
    listaRespuestas = []
    unaNuevasRespuestas = input("Ingrese una respueta: ")
    while unaNuevasRespuestas != "xyz123":
        listaRespuestas.append(unaNuevasRespuestas)
        unaNuevasRespuestas = input("Ingrese otra respueta: ")
    return tuple(listaRespuestas)

def validarExistencia():
    clave = input("Ingrese UNA palabra clave: ")
    if clave in dic.diccionario:
        clave = input("Ingrese otra Palabra Clave, la anterior ya existe: ")
        validarExistencia()
    return clave

def agregarRespuestas():
    print("Estas agregando una respuesta")
    print("Tene en cuenta que minimo debes agregar dos respuestas a una palabra clave")
    palabraClave = validarExistencia()
    tuplaRespuestas = agregarVariasRespuestas()
    dic.diccionario[palabraClave] = tuplaRespuestas
    print(f"Agregamos satisfactoriamente la palabra clave {palabraClave} con las posibles respuestas {tuplaRespuestas}")
    print(dic.diccionario[palabraClave])


def recursividadMenu(num):
    if num == "1":
        hablarConEliza()
    elif num == "2":
        agregarRespuestas()
        recursividadMenu(input("Escriba 1, 2 o 3: "))
    elif num == "3":
        print("Fin del programa")
    else:
        recursividadMenu(input("Escriba 1, 2 o 3: "))


### MAIN ###

registro_conversacion = []
print("Bienvenido a Eliza, tu psicologa virtual")
print("Para habalar con Eliza seleccione 1")
print("Para agregar posibles respuestas seleccione 2")
print("Para salir escriba 3")
print()
selecMenu = input("Escriba 1, 2 o 3 segun corresponda: ")
recursividadMenu(selecMenu)