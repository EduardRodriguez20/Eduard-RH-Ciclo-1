def verifyInt(message):
    while True:
        print("\n","-" *60)
        try:
            number = int(input(message))
            if number < 1 or number > 3:
                print("Digita una opcion valida")
                continue
            return number
        except ValueError:
            print("Error, ingrese un valor valido")

english = set([1,2,3,4,5,6,7,8,9])
french = set([10,1,2,3,11,21,55,6,8])
while True:
    print("\nEstudiantes que compraron:")
    print(f"El periodico Ingles: {len(english)}")
    print(f"El periodico Frances: {len(french)}")
    print("\nQuieres ver los estudiantes que compraron: ")
    print("1. Solo el periodico Ingles")
    print("2. Solo el periodico Frances")
    print("3. Salir")
    option = verifyInt("Digita la opcion: ")
    s_option = 0
    if option == 1:
        result = english - french
        print(f"\n{len(result)} compraron el periodico Ingles")
        print("\n¿Quieres ver los codigos de los estudiantes?")
        print("1. Si")
        print("2. No")
        s_option = verifyInt("Digita la opcion: ")
        if s_option == 1:
            print("".join(str(result)))
        print("\nVolveras al menu principal")
    elif option == 2:
        result = french - english
        print(f"\n{len(result)} compraron el periodico Frances")
        print("\n¿Quieres ver los codigos de los estudiantes?")
        print("1. Si")
        print("2. No")
        s_option = verifyInt("Digita la opcion: ")
        if s_option == 1:
            print("".join(str(result)))
        print("\nVolveras al menu principal")
    else:
        print("Gracias por usar el programa")
        break
