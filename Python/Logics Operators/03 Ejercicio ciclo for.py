number = int(input("Ingrese un numero: "))
count = 0

for i in range (1,number):
    if number % i == 0:
        count += i

if count == number:
    print(f"El numero {number} es un numero perfecto!")
else:
    print(f"El numero {number} no es un numero perfecto")