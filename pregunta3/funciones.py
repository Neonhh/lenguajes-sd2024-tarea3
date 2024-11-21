#Guardaremos los tipos atomicos, registros y registros variantes en
#un diccionario

#Definimos constantes para representar los tipos
ATOMIC = 0
REGISTRO = 1
REGISTRO_VARIANTE = 2

tipos = {}

#
def tipoAtomico(nombre, representacion, alineacion):
    #Verificamos si el tipo atomico ya fue definido
    if nombre in tipos:
        print("El tipo atomico", nombre, "ya fue definido.")
        return
    #Guardamos el tipo atomico
    tipos[nombre] = [ATOMIC,int(representacion), int(alineacion)]

def registro(nombre, elementos, esVariante):
    #Verificamos si el tipo ya fue definido
    if nombre in tipos:
        print("El tipo", nombre, "ya fue definido.")
        return

    datosRegistro = [REGISTRO_VARIANTE if esVariante else REGISTRO,[],[]]
    
    #Verificamos que los elementos para el registro esten definidos
    for elemento in elementos:
        datos = tipos.get(elemento,0)
        if datos == 0:
            print("El tipo", elemento, "no ha sido definido.")
            return
        #Si esta definido, agregalo al registro variante
        datosRegistro[1].append(datos[1])
        datosRegistro[2].append(datos[2])
    
    #Guardamos el registro variante
    tipos[nombre] = datosRegistro

def describir(tipo):
    descripcion = tipos.get(tipo,0)
    if descripcion == 0:
        print("El tipo", tipo, "no ha sido definido.")
        return
    
    if descripcion[0] == ATOMIC:
        print("El tipo atomico", tipo, "tiene representacion", descripcion[1], "y alineacion", descripcion[2])
    elif descripcion[0] == REGISTRO:
        describirRegistro(tipo,descripcion)
    elif descripcion[0] == REGISTRO_VARIANTE:
        describirRegistroVariante(tipo,descripcion)
        
def describirRegistro(tipo, descripcion):
    print("Si se guardan los registros sin empaquetar,",)
    
    alineacionTipo = descripcion[2][0]
    bytesUsados = 0
    bytesRecorridos = 0
    for i in range(len(descripcion[1])):
        
        restoAlineacion = bytesRecorridos % descripcion[2][i]
            
        if restoAlineacion != 0:
            bytesRecorridos += descripcion[2][i] - restoAlineacion
        
        bytesUsados += descripcion[1][i]
        bytesRecorridos += descripcion[1][i]
        
            

    print("el registro", tipo, "ocupa", bytesRecorridos, "bytes",
              ", tiene alineacion", alineacionTipo, " y se desperdician", bytesRecorridos - bytesUsados, "bytes.")
        
    print("\nSi se guardan los registros empaquetados,\n",
        "el registro", tipo, "ocupa", bytesUsados , "bytes",
        ", tiene alineacion", alineacionTipo, " y no se desperdician bytes.")

def describirRegistroVariante(tipo, descripcion):
    pass