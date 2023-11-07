def obtener_despues_de_porque(cadena):
    # Busca la palabra "porque" en la cadena
    indice_porque = cadena.find("porque")
    print(indice_porque)
    # Si se encuentra "porque", guarda todo lo que sigue
    if indice_porque != -1:
        resultado = cadena[indice_porque + len("porque"):]
        return resultado
    else:
        return "La cadena no contiene la palabra 'porque'."

# Solicita la entrada al usuario
entrada = input("Introduce una cadena: ")

# Llama a la función y muestra el resultado
resultado = obtener_despues_de_porque(entrada)
print("Lo que sigue a 'porque' en la cadena es:", resultado)