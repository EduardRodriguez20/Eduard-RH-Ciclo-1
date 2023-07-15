import json, datetime

def verifyInt(message, code, idd):
    while True:
        try:
            print("\n","-" *60)
            if idd:
                number = int(input(message))
                if number == -1:
                    number = "SALIR"
                    return number
                if number < 1 or number > 9999999999:
                    print("Digita una ID valida, maximo 10 digitos")
                    continue
                return number
            
            if code:
                number = int(input(message))
                if number == -1:
                    number = "SALIR"
                    return number
                if number < 1:
                    print("\nDigita un codigo valido, no ingreses ceros")
                    continue
                return number
            
            if not(code):
                number = int(input(message))
                if number < 1:
                    print("\nDigita un valor valido, no puede ser cero")
                    continue
                return number
        except ValueError:
            print("Error, ingrese un valor valido")

def verifyString(message):
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
            for x in data_file.keys():
                products[int(x)] = {}
                if x == "1":
                    for code in data_file[x].keys():
                        products[int(x)][int(code)] = data_file[x][code]
                        products[int(x)][int(code)]["IVA"] = 0.05
                if x == "2":
                    for code in data_file[x].keys():
                        products[int(x)][int(code)] = data_file[x][code]
                        products[int(x)][int(code)]["IVA"] = 0.19
        return products
    except:
        with open(rute_products, "w") as f:
            products[1] = {}
            products[2] = {}
            json.dump(products, f)
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
            print("Digite (-1) para volver al menu")
            option = verifyInt("De que categoria es el producto a ingresar? ", True, False)
            if option == "SALIR":
                return print("\nHaz salido al menu principal")
            if option == 1:
                print("\nHaz escogido categoria Bienes")
                break
            elif option == 2:
                print("\nHaz escogido categoria General")
                break
            else:
                print("Digite una opcion valida")
                
        while True:
            code = verifyInt("Digita el codigo del producto: ", True, False)
            if products:
                if code in products[option]:
                    print("Ya existe un producto con ese codigo, verifica")
                else:
                    products[option][code] = {}
                    break
            if not products:
                products[option][code] = {}
                break
        name = verifyString("Digita el nombre del producto: ")
        products[option][code]["Name"] = name
        value = verifyInt("Digita el valor del producto: ", False, False)
        products[option][code]["Value"] = value
        products[option][code]["Sold"] = 0
        if option == 1:
                products[option][code]["IVA"] = 0.05
        if option == 2:
                products[option][code]["IVA"] = 0.19
        
        while True:
            print("\nQuieres ingresar otro producto? ")
            print("1. Si\n2. No")
            more_products = verifyInt("\nOpcion ", False, False)
            
            if more_products < 1 or more_products > 2:
                print("Digite una opcion valida")
            else:
                break
        if more_products == 2:
            break
    
    products = update_products(products)
    input("\nPresione cualquier tecla para volver al menu")

def modify_products():
    products = read_products()
    print("\n","-" *60)
    print("\n\t\t--MODIFICAR PRODUCTO--")
    print("\nDigite (-1) para volver al menu")
    while True:
        code = verifyInt("Digita el codigo del producto a modificar: ", True, False)
        if code == "SALIR":
            return print("\nHaz salido al menu principal")
        if code in products[1]:
            kind = 1
            break
        elif code in products[2]:
            kind = 2
            break
        else:
            print("Codigo no encontrado, valida de nuevo.")

    name = products[kind][code]["Name"]
    value = products[kind][code]["Value"]
    print(f"\nPrecio anterior: {value}")
    new_value = verifyInt(f"\nDigita el nuevo precio para {name}: ", False, False)
    products[kind][code]["Value"] = new_value
    print("El nuevo valor fue asignado con exito")
    products = update_products(products)
    input("\nPresione cualquier tecla para volver al menu")

def menu_products():
    while True:
        print("\n\t --- Menu Productos ---")
        print("\n1. Agregar producto\n2. Modificar producto\n3. Salir")
        while True:
            option = verifyInt("\nDigita la opcion: ", False, False)
            if option < 1 or option > 3:
                print("Ingresa una opcion valida")
                continue
            break
        if option == 1:
            add_products()
        elif option == 2:
            modify_products()
        elif option == 3:
            break


def read_facturation():
    sales = {}
    try:
        with open(rute_sales, "r") as f:
            data_file = json.load(f)
            for x in data_file.keys():
                sales[int(x)] = {}
                sales[int(x)] = data_file[x]
        return sales
    except:
        with open(rute_sales, "w") as f:
            return sales

def uptade_fact(dictionary):
    with open(rute_sales, "w") as f:
        json.dump(dictionary, f)
    dictionary.clear()
    return dictionary

def format_fact(dictionary, idd):
    hour = datetime.datetime.now().time().hour
    minutes = datetime.datetime.now().time().minute
    seconds = datetime.datetime.now().time().second
    final_hour = str(f"{hour:02d}:{minutes:02d}:{seconds:02d}")
    print("\nTIRILLA DE PAGO".center(50, " "))
    print("\n\nMICROMERCADO ACCME".center(50, " "))
    print("\n{:<16} {:<14} {:<8} {:<14} ".format("Fecha:", str(date), "Hora:", final_hour))
    print("{:<16} {:<14} ".format("Cliente:", idd))
    print("{:<16} {:<14} ".format("Forma de pago:", "Efectivo"))
    print("{:<16} {:<14} ".format("Vendedor:", "CAJA 1"))
    print("\n{:<4s} {:<24s} {:<10s} {:<16s} ".format("Cant", "\tDetalles", "IVA", "Total"))
    t_iva = 0
    subtotal = 0
    t_neto = 0
    for x in dictionary[idd].keys():
        name = dictionary[idd][x]["Name"]
        quantity = dictionary[idd][x]["Quantity"]
        iva = dictionary[idd][x]["IVA"]
        value = dictionary[idd][x]["Value"]
        g_total = (value * quantity)
        increase = g_total * iva
        total = g_total + increase
        print("{:<4} {:<24} {:<10} {:<16} ".format(quantity, name, increase, total))
        t_iva += increase
        subtotal += g_total
        t_neto += total
    t_iva = str(f"${t_iva:.2f}")
    subtotal = str(f"${subtotal:.2f}")
    t_neto = str(f"${t_neto:.2f}")
    print("-" * 50)
    print("{:<24s} {:<10s} {:<16s} ".format(" ", "Subtotal:", subtotal))
    print("{:<24s} {:<10s} {:<16s} ".format(" ", "Iva:", t_iva))
    print("\n{:<24s} {:<10s} {:<16s} ".format(" ", "TOTAL:", t_neto))
    input("\nPresione cualquier tecla para continuar")

def facturation():
    t_quantity = 0
    while True:
        products = read_products()
        sales_day = read_facturation()
        print("\n\t\tMicromercado Acme")
        print("\t --- MODULO FACTURACION ---")
        print("Digite (-1) para volver al menu")
        idd = verifyInt("Digita la identificacion del cliente: ", None, True)
        if idd == "SALIR":
            print("\nHaz salido al menu principal")
            break
        sales_day[idd] = {}
        #sales_day[idd]["Complete"] = False
        counter = 1
        while True:
            while True:
                code = verifyInt(f"Digita el codigo del {counter} producto: ", True, False)
                if code == "SALIR":
                    print("Digite un valor valido")
                    continue
                if code in products[1]:
                    kind = 1
                    break
                if code in products[2]:
                    kind = 2
                    break
                else:
                    print("No existe producto con ese codigo, verifica")
        
            t_quantity += products[kind][code]["Sold"]
            name = products[kind][code]["Name"]
            print(f"Producto: {name}")
            while True:
                print("Esta exento de IVA?")
                print("1. Si\n2. No")
                exempt = verifyInt("Opcion? ", False, False)
                if exempt == 1:
                    exempt = 0
                    break
                elif exempt == 2:
                    exempt = products[kind][code]["IVA"]
                    break
                else:
                    print("Digite una opcion valida")
            quantity = verifyInt(f"Digita la cantidad: ", False, False)
            t_quantity += quantity
            products[kind][code]["Sold"] = t_quantity
            price = products[kind][code]["Value"]
            products = update_products(products)
            sales_day[idd][code] = {}
            sales_day[idd][code]["Name"] = name 
            sales_day[idd][code]["Quantity"] = quantity
            sales_day[idd][code]["IVA"] = exempt
            sales_day[idd][code]["Value"] = price
            while True:
                print("Desea ingresar otro producto?")
                print("1. Si\n2. No")
                more = verifyInt("\nOpcion? ", False, False)
                if more < 1 or more > 2:
                    print("Digite una opcion valida")
                else:
                    break
            counter += 1
            if more == 2:
                break
        format_fact(sales_day, idd)
        #sales_day[idd]["Complete"] = True
        uptade_fact(sales_day)
                
def main_menu():
    while True:
        print("\n\t   Micromercado Acme")
        print("\n\t --- Menu Principal ---")
        print("\n1. Administracion Productos")
        print("2. Facturacion")
        print("3. Administracion General")
        print("4. Salir")
        option = verifyInt("\nDigita la opcion: ", False, False)
        if option < 1 or option > 4:
            print("Ingresa una opcion valida")
            continue
        else:
            return option

def aditional_f():
    products = read_products()
    print("\n\t --- Cantidad de ventas por articulo ---")
    g_total = 0
    print("\n{:<14} {:<10} {:<14} {:<14} ".format("Producto", "Vendidos", "Total sin IVA", "Total con IVA"))
    for x in products.keys():
        for y in products[x].keys():
            name = products[x][y]["Name"]
            sold = products[x][y]["Sold"]
            value = products[x][y]["Value"]
            iva = products[x][y]["IVA"]
            total = value * sold
            increase = value * iva
            total_iva = (value + increase) * sold
            g_total += total_iva
            print("{:<14} {:<10} {:<14} {:<14} ".format(name, sold, total, total_iva))
    print(f"\nEl total de ventas con IVA es {g_total}")
    input("\nPresione cualquier tecla para volver al menu principal")

while True:
    rute_products = "Python/Files Json/Supermaker acme/Products.json"
    date = datetime.datetime.now().date()
    rute_sales = f"Python/Files Json/Supermaker acme/{str(date)}.json"

    option = main_menu()
    if option == 1:
        menu_products()
    elif option == 2:
        products = read_products()
        if not products:
            print("Primero ingresa al menos 1 producto")
            input("\nPresione cualquier tecla para volver al menu")
        else:
            products.clear()
            facturation()
    elif option == 3:
        products = read_products()
        if not products:
            print("Primero ingresa al menos 1 producto")
            input("\nPresione cualquier tecla para volver al menu")
        else:
            products.clear()
            aditional_f()
    elif option == 4:
        print("\nSeguro que quieres salir del programa?")
        print("1. Si\n2. No")
        while True:
            to_exit = verifyInt("Digita la opcion: ", False, False)
            if to_exit < 1 or to_exit > 2:
                print("Ingresa una opcion valida")
                continue
            break
        if to_exit == 1:
            print("Gracias por usar el programa.")
        if to_exit == 2:
            print("\nHaz vuelto al programa\n")
            continue
        break
