print("\tNumero mayor y menor de 10 numeros")
small_num = 10**28
high_num = 0
for i in range (1,11):
    number = int(input(f"Ingrese el {i} numero: "))
    
    if number < small_num:
        small_num = number
    elif number > high_num:
        high_num = number

print("\nDe los numeros que ingresaste: ")
print(f"El mayor: {high_num} y el menor: {small_num}\n")