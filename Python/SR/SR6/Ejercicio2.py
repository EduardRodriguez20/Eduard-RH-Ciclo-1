print("Ingrese un numero de telefono con el siguiente formato: +34-#########-##")
counter = 0
indicator = 0
while True:
    number = input("Ingrese el numero de telefono: ")
    if len(number.strip()) == 16:
        if number[0] == "+":
            if number[3] == "-" and number[13] == "-":
                break
            else:
                print("Debe separar el prefijo y la extension con guion (-)")   
        else:
            print("Debe ingresar el signo + para el prefijo.")
    else:
        print("La longitud debe ser: (2) prefijo, (9) numero, (2) extension")

print("\nEl numero sin prefijo ni extension es:", end=" ")
for i in number:
    indicator = number[counter]
    if counter >= 4:
        print(indicator, end="")
    if counter == 12:
        break
    counter += 1

print("\n")