from funciones import tipoAtomico, registro, describir
def main():

    print("Bienvenido al programa de manejaDatos.\n",
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
                registro(opciones[1],opciones[2:], False)
            elif opciones[0].upper() == "UNION":
                registro(opciones[1],opciones[2:], True)
            elif opciones[0].upper() == "DESCRIBIR":
                describir(opciones[1])
            else:
                print("OPCION NO VALIDA\n",
                "Opciones: ATOMICO, STRUCT, UNION, DEFINIR, SALIR.\n")
   

if __name__ == "__main__":
    main()
