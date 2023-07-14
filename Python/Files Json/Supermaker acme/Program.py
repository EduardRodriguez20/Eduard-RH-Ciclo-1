import json

rute_products = "Python/Files Json/Supermaker acme/Products.json"
def verifyInt(message, cod):
    while True:
        try:
            print("\n","-" *60)
            if cod:
                print("Digite un codigo que no se encuentre registrado")
                number = int(input(message))
                if number < 1:
                    print("\nDigita un codigo valido, no ingreses ceros")
                    continue
                return number
            if not(cod):
                number = int(input(message))
                if number < 1 or number > 160:
                    print("\nDigita un valor valido, no puede ser cero")
                    continue
                return number
        except ValueError:
            print("Error, ingrese un valor valido")

def verifyString(message, ):
    print("\n","-" *60)
    while True:
        letter = input(message)
        if letter.strip() == "":
            print("Digita un nombre, no ingreses espacios")
            continue
        elif not(letter.isalpha()):
            print("Solo ingresa letras")
            continue
        else:
            return letter

def read_products():
    products = {}
    try:
        with open(rute_products, "r") as f:
            data_file = json.load(f)
            print(data_file)
            for x in data_file.keys():
                products[x] = {}
                if x == 1:
                    for cod in data_file[x].keys():
                        products[x][cod] = data_file[x][cod]
                if x == 2:
                    for cod in data_file[x].keys():
                        products[x][cod] = data_file[x][cod]
        return products
    except:
        with open(rute_products, "w") as f:
            return products

def update_products(dictionary):
    with open(rute_products, "w") as f:
        json.dump(dictionary, f)
    dictionary.clear()
    return dictionary

def add_products():
    products = read_products()
    print("\n","-" *60)
    print("\n\t\t--INGRESAR PRODUCTOS--")
    while True:
        while True:
            print("--Categorias--")
            print("1. Bienes\n2. General")
            option = verifyInt("De que categoria es el producto a ingresar? ")
            if option < 1 or option > 2:
                print("Digite una opcion valida")
            else:
                products[option] = {}
                break
        while True:
            cod = verifyInt("Digita el codigo del producto: ", True)
            if cod in products[option]:
                print("Ya existe un producto con ese codigo, verifica")
            else:
                products[option][cod] = {}
                break
        name = verifyString("Digita el nombre del producto: ")
        products[option][cod]["Name"] = name
        value = verifyInt("Digita el valor del producto: ", False)
        products[option][cod]["Value"] = value
        print("Quieres ingresar otro producto?")
        
    
    products = update_products(products)
    input("\nPresione cualquier tecla para volver al menu")

print("PV micro-Acme")