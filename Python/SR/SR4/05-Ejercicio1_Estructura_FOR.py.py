first_num = 1
second_num = -2
next_num = 0

print("\nCual es el siguiente numero de la serie: 1, 1, 2, -1, 1, -2, ?")
print("\nSe imprimirá el siguiente numero a la serie anterior")
verification = int(input("\nQuieres ver mas numeros de la serie? \n(1 = Si , 2 = No) : "))

if verification == 1:
    quantity = int(input("Cuantos veces quiere que se calcule el proximo numero? "))
    print(f"La serie continua {quantity} veces asi:", end=" ")
    for i in range (1,quantity+1):
        next_num = first_num + second_num
        first_num = next_num
        second_num = second_num -1
        print(f" {first_num}, ", end=" ")
else:
    next_num = first_num + second_num
    print(f"El siguiente numero de la serie es: {next_num}")

print("\n")