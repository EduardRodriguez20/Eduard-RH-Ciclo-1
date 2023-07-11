def verifyString(message):
    while True:
        try:
            name = input(message)
            if name.strip() == "":
                print("Digite un nombre valido, sin numeros ni caracteres especiales")
                input("Presione cualquier cualquier tecla para continuar")            
                continue
            return name
        except Exception as e:
            print("Error al ingresar el nombre ", name, ", valida el nombre")    

def verifyInt(message):
    while True:
        try:
            print("-" *60)
            number = int(input(message))
            if number < 1 or number > 5:
                print("Ingrese un estrato valido de 1 a 5")
                input("Presione cualquier cualquier tecla para continuar")            
                continue
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

def calTarifaBasica(stratum):
    if stratum == 1:
        value = 10000
    elif stratum == 2:
        value = 15000
    elif stratum == 3:
        value = 30000
    elif stratum == 4:
        value = 50000
    elif stratum == 5:
        value = 55000
    
    return value

name = verifyString("\nIngrese el nombre: ")
stratum = verifyInt("\nIngrese el estrato del usuario: ")

basic_rate = calTarifaBasica(stratum)

print("\n", "-" * 60)
print("Nombre del usuario: ", name)
print(f"Valor de la tarifa es: ${basic_rate:,}")