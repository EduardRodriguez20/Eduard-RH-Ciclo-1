import random

name_win = "0"
attemps_win = 10

while True:
    try:
        quantity = int(input("¿Cuantos participantes tendra el juego? "))
        break
    except ValueError:
        print("Ingrese un numero entero valido\n")

for x in range (quantity):
    num_pc = random.randrange(1,101)
    attemps_max = random.randrange(3,6)
    print(num_pc)
    while True:
        name = input(f"Ingrese el nombre del jugador {x+1}: ")
        if name.isalpha():
            break
        else:
            print("Ingresa un nombre valido sin caracteres especiales.")

    while True:
        attemps = 0
        print("_" * 60)
        print(f"Tienes {attemps_max} intentos para adivinar")
        while True:
            if attemps == attemps_max:
                print(f"Se acabaron tus intentos {name}\n")
                break
            
            while True:
                try:
                    print(f"Estas en el intento: {attemps+1}")
                    number = int(input("Ingresa un numero para adivinar: "))
                    break
                except ValueError:
                    print("Ingrese un numero entero valido\n")
            attemps += 1
            if number < num_pc:
                print("¡Demasiado bajo! Ingresa un numero mas alto\n")
            if number > num_pc:
                print("¡Demasiado alto! Ingresa un numero mas bajo\n")
            if number == num_pc:
                print(f"¡Felicidades! Adivinaste el numero en {attemps} intentos\n")
                if attemps < attemps_win:
                    name_win = name
                    attemps_win = attemps
                break
        break

if name == "0":
    print("No ganó ningun jugador")
else:
    print(f"El jugador {name_win} ganó con {attemps_win} intentos")
