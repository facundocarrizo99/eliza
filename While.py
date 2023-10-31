print("Hola! ¿Cual es tu problema?")
entrada = input("ingrese su inquietud")
while entrada != "adios":
    respuesta = analizarcadena(dicc, entrada)
    print(respuesta)
    entrada = input("")

print("¡Nos vemos! ¡Gracias!")