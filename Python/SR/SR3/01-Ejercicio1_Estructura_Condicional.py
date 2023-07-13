num_one = int(input("Digite el primer numero: "))
num_two = int(input("Digite el segundo numero: "))
num_three = int(input("Digite el tercer numero: "))

#           VALIDACION PRIMER, SEGUNDO Y TERCERO
if num_one > num_two and num_two > num_three:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_one}, {num_two}, {num_three}")
elif num_one > num_three and num_three > num_two:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_one}, {num_three}, {num_two}")

#           VALIDACION SEGUNDO, PRIMERO Y TERCERO
if num_two > num_one and num_one > num_three:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_two}, {num_one}, {num_three}")
elif num_two > num_three and num_three > num_two:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_two}, {num_three}, {num_one}")

#           VALIDACION TERCERO, PRIMERO Y SEGUNDO
if num_three > num_one and num_one > num_two:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_three}, {num_one}, {num_two}")
elif num_three > num_two and num_two > num_one:
    print("\nEl orden de mayor a menor de los numeros ingresados es: ")
    print(f"{num_three}, {num_two}, {num_one}")