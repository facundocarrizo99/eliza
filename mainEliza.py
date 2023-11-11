import random

diccionario = {
    "necesito": ("Está seguro que necesita *", "Por que necesita *"),
    "puedo": ("Lo ha intentado?", "Como lo sabe?", "Quizas esta vez sea diferente"),
    "soy": ("Disfruta siendo * ?", "Por que me dice que es *", "Por que es usted *"),
    "Quiero": ("Por que usted quiere *", "Que significaría para usted si consiguiera *"),
    "sinrespuesta": ("ok", "no entiendo", "continue", "por que?", "hableme mas"),
    "hola": ("Hola", "Te escucho", "Contame", "Bienvenido"),
    "estoy": ("Porque estas *?", "A que se debe que estes asi", "porque pensas que estas *?", "crees que es normal estar *?"),
    "tengo": ("Porque tenes *?", "como crees que lo obtuviste?", "desde cuando tenes *?"),
    'si': ("Pareces muy seguro", "Ok, podes elaborar mas?"),
    'no': ("Por que no?", "Por que se muestra tan negativo sobre esto", "podes elaborar mas?"),
    "Que": ("Por que pregunta eso?", "que piensa usted que es?"),
    "como": ("Tal vez usted ya sabe la respuesta", "Esto es lo que realmente esta preguntando?", "No estoy capacitada para decirle exactamente como"),
    "Quien": ("Que respuesta lo dejaria tranquilo?", "quien cree usted que *"),
    "donde": ("usted realmente necesita saber donde?", "Que supondría para usted si yo le dijera donde *"),
    "cuando": ("Como podría saber cuando *", "En esta conversación el tiempo no es lo primordial", "Si hubiese sucedido en otro momento, sería diferente?"),
    "porque": ("No puedo dar una respuesta final, profundice", "usted realmente necesita saber por que *", "que otras razones recuerda?"),
    "Lo siento": ("No siempre tiene que disculparse", "En que otras ocasiones se disculpa", "Que sensacion experimenta cuando tiene que disculparse?"),
    "siempre": ("Deme un ejemplo concreto", "Utilizar siempre puede ser un tanto exagerado", "realmente considera que siempre le sucede eso"),
    'enojado': ("El enojo es normal. ¿Qué te pasó?", "Hablemos de eso. Expresar el enojo es importante.", "Contame más sobre por qué estás enojado."),
    'cansado': ("¿Tuviste un día agitado?", "¿Necesitás ayuda para relajarte?", "Hablemos sobre la importancia de descansar."),
    'terapia': ("La terapia es muy útil. ¿Alguna vez pensaste en hablar con un terapeuta profesional?", "La terapia puede brindarte apoyo. ¿Tenés dudas al respecto?", "Estoy acá para orientarte sobre la terapia."),
    'apoyo': ("El apoyo es fundamental. ¿En qué puedo ayudarte hoy?", "¿Necesitás consejos o simplemente charlar? Estoy acá para vos.", "Sentite libre de compartir tus pensamientos y preocupaciones."),
    'amor': ("Las relaciones son importantes. ¿Tenés alguna inquietud o consulta sobre el amor?", "El amor es un tema complicado. Estoy acá para hablar de tus inquietudes amorosas.", "Hablemos de tus experiencias en el amor."),
    'familia': ("¿Tenés problemas familiares que querés explorar?", "Hablemos de tus relaciones familiares y cómo te impactan.", "¿Hay tensiones familiares que quieras discutir?"),
    'ansiedad': ("La ansiedad es una preocupación constante que puede afectar tu bienestar emocional. ¿Quieres hablar sobre tus síntomas o desencadenantes?", "La ansiedad es común. ¿Cómo estás lidiando con ella?"),
    'depresión': ("La depresión puede causar sentimientos abrumadores de tristeza. ¿Cómo te sientes en tu día a día?", "Hablemos de la depresión y cómo afecta tu vida. ¿Has buscado ayuda?", "La depresión es una carga pesada. ¿En qué puedo ayudarte?"),
    'estrés': ("El estrés es una parte normal de la vida, pero demasiado estrés puede ser perjudicial. ¿Cómo estás manejando el estrés en tu vida?", "El estrés puede tener un impacto significativo en tu salud. ¿Necesitas estrategias para reducirlo?", "Hablemos de tus fuentes de estrés y cómo puedes aliviarlo."),
    'autoestima': ("La autoestima juega un papel crucial en tu bienestar emocional. ¿Cómo te sientes acerca de ti mismo?", "La autoestima puede influir en tus decisiones y relaciones. ¿Quierss hablar sobre cómo mejorarla?", "La autoestima es importante. ¿Cómo puedo apoyarte en construir una autoestima más positiva?"),
    'relaciones': ("Las relaciones personales pueden ser complicadas. ¿Tenés dificultades en tus relaciones con familiares, amigos o parejas?", "Las relaciones son fundamentales. ¿Necesitas consejos sobre cómo mejorar tus relaciones?", "Hablemos sobre tus desafíos en las relaciones y cómo superarlos."),
    'duelo': ("El duelo es un proceso natural cuando perdemos a alguien cercano. ¿Has experimentado una pérdida reciente?", "El duelo puede ser abrumador. ¿Necesitas apoyo para sobrellevarlo?", "Perder a un ser querido es una experiencia difícil. Estoy aquí para escucharte."),
    'autoayuda': ("La autoayuda es una herramienta valiosa para el crecimiento personal. ¿Necesitas consejos sobre cómo mejorar tu bienestar emocional?", "La autorreflexión y el crecimiento personal son importantes. ¿Cómo puedo ayudarte a crecer?", "La autoayuda es un camino hacia la mejora personal. Tenés metas en mente?", "La autoayuda es valiosa. ¿Querés consejos sobre cómo mejorar tu bienestar emocional?", "La autorreflexión y el crecimiento personal son importantes. Estoy acá para guiarte.", "La autoayuda es un camino hacia la mejora personal."),
    'fobias': ("Las fobias pueden ser debilitantes. ¿Tenés miedos irracionales que afectan tu vida diaria?", "Hablemos sobre tus fobias y cómo enfrentarlas. ¿Has considerado la terapia de exposición?", "Las fobias pueden superarse. Estoy aquí para apoyarte en el proceso."),
    'adicciones': ("Las adicciones pueden tener un gran impacto en la vida. ¿Tenés problemas con el abuso de sustancias o comportamientos adictivos?", "Las adicciones son desafiantes. ¿Necesitas recursos para la recuperación?", "La recuperación de las adicciones es un proceso. ¿En qué etapa te encuentras?"),
    'relajación': ("La relajación es clave para la salud mental. ¿Necesitás técnicas de relajación?", "Hablemos de cómo encontrar momentos de paz y calma en tu vida.", "La relajación puede ayudarte a reducir el estrés. Estoy acá para enseñarte."),
    'crecimiento': ("El crecimiento personal es un viaje continuo. ¿Tenés metas de crecimiento personal que quieras discutir?", "El desarrollo personal es importante. Estoy acá para apoyar tus objetivos.", "Hablemos de tus ambiciones y cómo alcanzarlas."),
    'escucha': ("Estoy aquí para escucharte. ¿Qué te preocupa hoy?", "La comunicación abierta es esencial. ¿Hay algo que quieras compartir?", "Puedes confiar en mí. Habla sobre tus pensamientos y sentimientos."),
    'esperanza': ("La esperanza es poderosa. ¿Qué te da esperanza en la vida?", "Hablemos de tus sueños y aspiraciones. La esperanza puede impulsarlos.", "La esperanza es una fuerza motivadora."),
    'pensamientos suicidas': ("Los pensamientos suicidas son extremadamente serios. Si estás teniendo estos pensamientos, busca ayuda profesional de inmediato.", "La vida puede ser abrumadora, pero hay ayuda disponible. No estás solo en esto. Hablar sobre tus pensamientos suicidas es un paso importante hacia la recuperación."),
    'trastornos alimentarios': ("Los trastornos alimentarios pueden afectar gravemente la salud. ¿Estás lidiando con problemas alimentarios? ¿Necesitas apoyo para superarlos?", "Hablemos de tus patrones alimentarios y cómo puedes trabajar en una relación más saludable con la comida.", "Los trastornos alimentarios son tratables. Estoy acá para ayudarte en tu proceso de recuperación."),
    'autolesiones': ("Las autolesiones son una preocupación seria. ¿Has experimentado autolesiones o conoces a alguien que lo ha hecho?", "Hablemos sobre tus sentimientos y el deseo de autolesionarte. Es importante buscar ayuda profesional.", "Las autolesiones son un síntoma de angustia emocional. ¿Cómo puedo ayudarte a encontrar alternativas saludables?"),
    'soledad': ("La soledad puede ser difícil. ¿Cómo estás lidiando con la soledad? ¿Necesitas consejos para superarla?", "Hablemos de estrategias para conectarte con otros y superar la soledad.", "La soledad es una experiencia común."),
    }

listaDeBasuras = ["me", "te", "se", "nos", "la", "lo", "las", "los", "muy", "mucho", "mega", "super", "re", "ultra"]
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def componerOracion(texto, listaPalabras):
    try:
        for palabra in listaPalabras:
            if palabra in listaDeBasuras:
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
    respuestaInicial = analizarCadena(diccionario, listaPalabras)
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
        if carPuntuacion in punc:
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
            procesarCadena(sacarPuntuacion(entrada))  # Sacamos los caracteres de puntuacion antes de comparar los elementos
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
    unaNuevasRespuestas = input("Ingrese una respuesta: ")
    while unaNuevasRespuestas != "1":
        listaRespuestas.append(unaNuevasRespuestas)
        unaNuevasRespuestas = input("Ingrese otra respuesta: ")
    return tuple(listaRespuestas)

def validarExistencia():
    clave = input("Ingrese UNA palabra clave: ")
    while clave in diccionario:
        clave = (input("Ingrese otra Palabra Clave, la anterior ya existe: "))
    return clave

def agregarRespuestas():
    print("Estas agregando una respuesta")
    print("Tene en cuenta que minimo debes agregar dos respuestas a una palabra clave")
    print("Con la cadena 1 no agregas mas respuetas")
    palabraClave = validarExistencia()
    tuplaRespuestas = agregarVariasRespuestas()
    diccionario[palabraClave] = tuplaRespuestas
    print(f"Agregamos satisfactoriamente la palabra clave {palabraClave} con las posibles respuestas {tuplaRespuestas}")

def recursividadMenu(num):
    if num == "1":
        hablarConEliza()
        recursividadMenu(input("Escriba 1, 2 o 3: "))
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
print("Para habalar con Eliza escriba 1")
print("Para agregar respuestas escriba 2")
print("Para salir escriba 3")
print()
selecMenu = input("Escriba 1, 2 o 3 segun corresponda: ")
recursividadMenu(selecMenu)