import random
def analizarcadena(d,e):
    divisiones = e.split()
    flag=0
    print(divisiones)
    for palabra in divisiones:
        if palabra in d:
            flag=random.choice(d[palabra])
            print("true")
            print(d[palabra])
    return flag

dicc={"porque":("huevo","Huevo2","HUEVO3","HUEVO4","HUEVO35"),
      "me":"hola",
      "estoy":"hola"}
entrada=str(input("ingrese su inquietud"))
respuesta=analizarcadena(dicc,entrada)
print(respuesta)
"""if respuesta==1:
    print("Se encontró la palabra")"""