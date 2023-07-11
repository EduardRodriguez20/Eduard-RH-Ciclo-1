print("\n\tValidar si un numero es primo")
print("Para finalizar digite (-1)")
x=0
while x != -1:
    primo = True
    x = int(input("\nDigite un numero: "))
    for i in range(2,x):
        if x % i == 0:
            primo = False
            divisor = i
    if x == -1:
        print("Fin del programa")
    else:
        if primo:
            print(f"El numero {x} es primo")
        else:
            print(f"El numero {x} no es primo, lo divide {divisor}")
    