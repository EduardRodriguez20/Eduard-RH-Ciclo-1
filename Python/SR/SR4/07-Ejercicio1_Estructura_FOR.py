acumulator1 = 0
acumulator2 = 0

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

for i in range (1,number1):
    if number1 % i == 0: 
        acumulator1 = acumulator1 + i
        print(i , end=" ")
print("\n")
for x in range (1,number2):
    if number2 % x == 0: 
        acumulator2 = acumulator2 + x
        print(x, end=" ")

if acumulator1 == number2 and acumulator2 == number1:
    print("Los numeros son amigos.")

