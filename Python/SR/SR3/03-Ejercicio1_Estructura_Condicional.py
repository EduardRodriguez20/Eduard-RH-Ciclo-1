print("\nEl codigo funciona ingresando un numero no mayor a 999.999")
number = int(input("\nIngrese un numero entero positivo: "))
digits = 1
counter = 9

if number > counter:
    digits = digits + 1
    counter = 99
    if number > counter:
        digits = digits + 1
        counter = 999
        if number > counter:
            digits = digits + 1
            counter = 9999
            if number > counter:
                digits = digits + 1
                counter = 99999
                if number > counter:
                    digits = digits + 1


print(f"\nEl numero ingresado tiene: {digits} digitos.\n")


