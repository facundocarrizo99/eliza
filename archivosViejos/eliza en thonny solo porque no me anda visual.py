import random

def analizarcadena(dic,listaPalabras):
    #print(listaPalabras)
    pclave=0
    for palabra in listaPalabras:
        if palabra in dic:
            pclave= palabra
            respuesta = random.choice(dic[palabra])
            #print("true")
            #print(dic[palabra])
            listaPalabras.remove(palabra)
            #To Do - Crear listas temporales con las palabras que vamos analizando para diferencias clas que son palabras clave, de los atributos, de los conectores
            break
        else:
            respuesta = random.choice(dic["sinrespuesta"])
            pclave=0
    return respuesta,pclave

dic = {
    "sinrespuesta":("ok","no entiendo","continue","por que?", "hableme mas"),
    "hola":("hola","te escucho","contame","bienvenido"),
    "estoy":("porque estas ","A que se debe que estes ","porque pensas que estas ","crees que es normal estar"),
    "tengo":("porque tenes?","como crees que lo obtuviste?","desde cuando?"),
    "adios":("nos vemos")
    }

print("Bienvenido a Eliza, tu psicologa virtual")
print("Escribe 'adios' para salir")
print()
entrada = input("Hola! ¿Cual es tu problema?")
while entrada != "adios":
    listaPalabras = entrada.split()
    respuestaInicial, arma_oraciones = analizarcadena(dic, listaPalabras)
    print(respuestaInicial)
    oracion_final = entrada[0 + len(str(arma_oraciones)):]
    print(respuestaInicial+oracion_final)
    print()
    entrada = input("")

print("¡Nos vemos! ¡Gracias!")