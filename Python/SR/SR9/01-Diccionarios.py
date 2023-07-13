def verifyInt(message):
    while True:
        print("\n","-" *60)
        try:
            number = int(input(message))
            if number < 1 or number > 5:
                print("Digita una opcion valida")
                continue
            return number
        except ValueError:
            print("Error, ingrese un valor valido")

articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

quantity = int(input("¿Cuantos articulos va a comprar? "))
for i in range (quantity):
    1