def words_counter ():
    print("\n\t-- Contador de Palabras --")
    while True:
        spaces = 1
        sentence = input("Digite una frase, recuerda separar con espacios:\n")
        if sentence.strip():
            spaces = sentence.count(" ")
            if spaces >= 1:                
                break
            else:
                print("Ingrese por lo menos 2 palabras o separe con espacio")
        else:
            print("Ingrese solo letras")
    
    print(f"En la frase ingresada hay {spaces+1} palabras")
    input("--- Presione cualquier tecla para volver al menu ---")

def greatest_common_factor ():
    print("\n\t--Calcular Maximo Comun Divisor--")
    while True:
        try:
            number1 = int(input("Ingresa el primer numero: "))
            number2 = int(input("Ingresa el segundo numero: "))
            break
        except ValueError:
            print("\nNo ingresaste bien los numeros.")
            print("Ingresa solo numeros enteros\n")
    if number1 > number2:
        bigger = number1
        minor = number2
    else: 
        minor = number1
        bigger = number2

    result = bigger / minor
    if bigger % minor == 0:
        print(f"El maximo comun divisor de {number1} y {number2} es: {result}")

    else:
        while True:
            result = bigger // minor
            module = bigger % minor
            if module == 0:
                print(f"El maximo comun divisor de {number1} y {number2} es: {minor}")
                break
            elif module == 1:
                print(f"El maximo comun divisor de {number1} y {number2} es: {module}")
                print("Ambos numeros son primos!")
                break
            else:
                x = minor * result
                y = bigger - x
                bigger = minor
                minor = y

def calculation_iva ():
    print("\n\t-- Calcular IVA --")  
    while True:
        try:
            total = int(input("Ingresa el valor de la factura: "))
            break
        except ValueError:
            print("Ingresa solo numeros enteros\n")

    while True:   
        try:
            print("\n---Si no ingresas nada o ingresas 0, se aplicara automaticamente el 21%---")
            iva = input("\nIngresa el porcentaje de iva a aplicar (0,100): ")
            if iva == "" or iva == "0":
                iva = 21
                break
            else:
                iva = int(iva)
                break
        except ValueError:
            print("Ingresa solo numeros enteros, no ingreses el signo (%)\n")

    iva /= 100
    print(iva)
    total = total + (total * iva)
    print(f"Se aplica iva de {iva} a la factura y el total con iva es: {int(total)}")

def menu():
    while True:
        print("\n\t-- MENU --")
        print("1. Contador de palabras")
        print("2. Maximo comun divisor")
        print("3. Calculador de IVA")
        print("4. Salir")
        option = int(input("\nOpcion: "))
        if option == 1:
            words_counter()
        if option == 2:
            greatest_common_factor()
        if option == 3:
            calculation_iva()
        if option == 4:
            print("\n\t Gracias por usar el programa")
            break
        else:
            print("Digite una opcion valida")

menu()