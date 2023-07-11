def verifyInt(message):
    while True:
        try:
            print("\n","-" *60)
            number = int(input(message))
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

def verifyString(message):
    while True:
        try:
            print("\n","-" *60)
            letter = input(message)
            if letter.strip() == "":
                print("Digita solo letras, no ingreses espacios")
                continue
            if len(letter) > 1:
                print("Digita una letra a la vez")
                continue
            if not(letter.isalpha()):
                print("Solo ingresa letras")
                continue
            return letter
        except Exception as e:
            print("Valida lo que ingresaste")    

def digits_letter(quantity):
    letters = []
    for x in range (quantity):
        letter = verifyString(f"Digite la {x+1} letra: ")
        letters.append(letter.lower())
    return letters

letters = []
vocals = ["a","e","i","o","u"]
counters = [0,0,0,0,0]
quantity = verifyInt("Cuantas letras vas a ingresar? ")
letters = digits_letter(quantity)

for x in letters:
    if x in vocals:
        counters[0] = letters.count("a")
        counters[1] = letters.count("e")
        counters[2] = letters.count("i")
        counters[3] = letters.count("o")
        counters[4] = letters.count("u")

print(f"\nLa cantidad vocales (a) son: {counters[0]}")
print(f"La cantidad vocales (e) son: {counters[1]}")
print(f"La cantidad vocales (i) son: {counters[2]}")
print(f"La cantidad vocales (o) son: {counters[3]}")
print(f"La cantidad vocales (u) son: {counters[4]}")