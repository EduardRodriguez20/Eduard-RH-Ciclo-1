number = int(input("Ingrese un numero: "))
count = 0

i = 1
while i != (number -1):
    if number % i == 0:
        count += i
    i += 1

if count == number:
    print(f"El numero {number} es un numero perfecto!")
else:
    print(f"El numero {number} no es un numero perfecto")