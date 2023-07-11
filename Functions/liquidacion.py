def verifyString(message):
    while True:
        try:
            print("\n","-" *60)
            name = input(message)
            if name.strip() == "":
                print("Digite un nombre valido")
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre ", name, ", valida el nombre")    

def verifyInt(message):
    while True:
        try:
            print("\n","-" *60)
            number = int(input(message))
            if number < 1 or number > 3:
                print("Ingrese un dato valido de 1 a 3")            
                continue
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

def programs():
    print("\n", "-" *60)
    print("\n1. Técnico en Sistemas")
    print("2. Técnico en Desarrollo de videojuegos")
    print("3. Técnico en Animación Digital\n")

def grants():
    print("\n", "-" *60)
    print("\n1. Beca por rendimiento académico: Descuento del 50%, en el valor de la matricula")
    print("2. Beca Cultural / Deportes: Descuento del 40%, en el valor matrícula")
    print("3. Sin beca.\n")

def calculation(program, grant):
    if program == 1:
        value = 800000
    elif program == 2:
        value = 1000000
    else:
        value = 1200000
    
    if grant == 1:
        discount = 0.5
    elif grant == 2:
        discount = 0.4
    else:
        discount = 0
    total = int(value - (value * discount))
    return total

def infomation():
    print("-" *60)
    code = input("\nDigite el codigo del estudiante: ")
    name = verifyString("Digite el nombre del estudiante: ")
    programs()
    program = verifyInt("Ingrese el opcion del programa academico del estudiante: ")
    grants()
    grant = verifyInt("Ingrese la opcion de la beca: ")
    total = calculation(program, grant)
    print(f"\nEl estudiante {name} con codigo {code}")
    print(f"Debe pagar su matricula por un valor de: ${total:,}")

print("\n\tCalculo de matricula por estudiante")
while True:
    while True:
        try:
            print("\n","-" *60)
            print("\nElige una opcion del siguiente menu")
            print("1. Calculo de la matricula del estudiante")
            print("2. Salir del programa")
            option = int(input())
            if option < 1 or option > 2:
                print("Digite una opcion valida")
                continue
            break
        except ValueError:
            print("Ingrese solo numeros")
    
    if option == 1:
        infomation()
    if option == 2:
        print("\nGracias por usar el programa\n")
        break