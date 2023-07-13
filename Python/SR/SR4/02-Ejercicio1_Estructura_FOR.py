number = int(input("Ingrese un numero entero: "))
acumulator = 0
sign = "-"
for i in range (1,number+1):
    variable =  1/i
    print(f"1/{i} {sign}" , end=" ")
    if i % 2 != 0:
        acumulator = acumulator + variable
        sign = "+"
    elif i % 2 == 0: 
        acumulator = acumulator - variable
        sign = "-"


print(f"\nEl resultado la operacion anterior es: ", "{:.3f}" .format(acumulator))