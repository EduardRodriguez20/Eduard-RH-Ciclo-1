#PROGRAMA GENERAL
def menu():
    print("\n\t-- MENU --")
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Factorial")
    print("7. Cerrar")
    while True:
        try:
            x = int(input(""))
            if x <= 0 or x > 7:
                print("Digite una opcion valida")
            else:
                return x
        except ValueError:
            print("Digite solo numeros")

def verification(message):
    while True:
        try:
            print("-" *60)
            number = int(input(message))
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

def addition():
    number_one = verification("Digite un numero para sumar: ")
    number_two = verification("Digite otro numero para sumar: ")
    result = number_one + number_two
    print("-" *60)
    print(f"La suma de {number_one} y {number_two} es = {result}\n")
    input("--- Presione cualquier tecla para continuar ---")

def subtract():
    number_one = verification("Digite un numero para restar: ")
    number_two = verification("Digite otro numero para restar: ")
    result = number_one - number_two
    print("-" *60)
    print(f"La resta de {number_one} y {number_two} es = {result}\n")
    input("--- Presione cualquier tecla para continuar ---")

def multiplication():
    number_one = verification("Digite un numero para multiplicar: ")
    number_two = verification("Digite otro numero para multiplicar: ")
    result = number_one * number_two
    print("-" *60)
    print(f"\nLa multiplicacion de {number_one} y {number_two} es = {result}\n")
    input("--- Presione cualquier tecla para continuar ---")

def divition():
    while True:
        number_one = verification("Digite un numero para dividir: ")
        number_two = verification("Digite otro numero para dividir: ")
        if number_one == 0 or number_two == 0:
            print("No se puede dividir cero, digita otro valor")
        else:
            result = number_one / number_two
            print("-" *60)
            print(f"\nLa division de {number_one} y {number_two} es = ", "{:.2f}" .format(result))
            input("\n--- Presione cualquier tecla para continuar ---")
            break

def potency():
    number = verification("Digite un numero para obtener la potencia: ")
    power = verification("¿A cuanto quieres elevar el numero ingresado? ")
    result = number ** power
    print("-" *60)
    print(f"\nEl numero {number} elevado a {power} es igual a = {result}\n")
    input("--- Presione cualquier tecla para continuar ---")

def factorial():
    number = verification("Digite un numero para obtener su factorial: ")
    result = 1
    for i in range(1,number+1):
        result *= i
    print("-" *60)
    print(f"\nEl factorial del numero {number} es = {result}")
    input("\n--- Presione cualquier tecla para continuar ---")

while True:
    option = menu()
    if option == 1:
        addition()
    if option == 2:
        subtract()
    if option == 3:
        multiplication()
    if option == 4:
        divition()
    if option == 5:
        potency()
    if option == 6:
        factorial()
    if option == 7:
        print("\nGracias por usar la Mini-Calculadora")
        break
    