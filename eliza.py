import diccionario0 as dic
import random

def analizarcadena(dic,listaPalabras):
    #print(listaPalabras)
    for palabra in listaPalabras:
        if palabra in dic:
            respuesta = random.choice(dic[palabra])
            #print("true")
            #print(dic[palabra])
            listaPalabras.remove(palabra)
            #To Do - Crear listas temporales con las palabras que vamos analizando para diferencias clas que son palabras clave, de los atributos, de los conectores
            break
        else:
            respuesta = random.choice(dic["sinrespuesta"])
    return respuesta

print("Bienvenido a Eliza, tu psicologa virtual")
print("Escribe 'adios' para salir")
print()
entrada = input("Hola! ¿Cual es tu problema?")
while entrada != "adios":
    listaPalabras = entrada.split()
    respuestaInicial = analizarcadena(dic.diccionario, listaPalabras)
    print(respuestaInicial)
    print()
    entrada = input("")

print("¡Nos vemos! ¡Gracias!")

