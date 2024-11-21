#Guardaremos los tipos atomicos, registros y registros variantes en
#un diccionario

tipos = {}

#
def tipoAtomico(nombre, representacion, alineacion):
    if nombre in tipos:
        print("El tipo atomico", nombre, "ya fue definido.")
        return
    #Guardamos el tipo atomico
    tipos[nombre] = (int(representacion), int(alineacion))

def registro(nombre, campos):
    pass

def registroVariante(nombre, campos):
    pass

def describir(tipo):
    pass