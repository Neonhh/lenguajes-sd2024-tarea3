from funciones import tipoAtomico, registro, registroVariante, describir
def main():

    print("Bienvenido al programa de manejaDatos.\n"+
          "Opciones: ATOMICO, STRUCT, UNION, DESCRIBIR, SALIR.\n")
    while True:
        user_input = input("$> ")
        if user_input.split()[0].upper() == "SALIR":
            break
        else:
            opciones = user_input.split()
            
            if opciones[0].upper() == "ATOMICO":
                tipoAtomico(opciones[1], opciones[2], opciones[3])
            elif opciones[0].upper() == "STRUCT":
                registro(opciones[1],opciones[2:])
            elif opciones[0].upper() == "UNION":
                registroVariante(opciones[1],opciones[2:])
            elif opciones[0].upper() == "DESCRIBIR":
                describir(opciones[1])
            else:
                print("OPCION NO VALIDA"+
                "Opciones: ATOMICO, STRUCT, UNION, DEFINIR, SALIR.\n")
   

if __name__ == "__main__":
    main()
