
def limpiar_texto(entrada):
    entrada = entrada.lower()
    entrada = "".join(c for c in entrada if c.isalnum())
    aux = entrada
    return entrada

entrada = limpiar_texto(cadena)

def verificar (cadena1,cadena2):
    if cadena1 == cadena2:
        print("ya te conteste esta pregunta, tienes otra consulta...?")


