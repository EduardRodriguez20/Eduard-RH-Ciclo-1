import json, datetime, random

def verify_id(message):
    print("=" *60)
    while True:
        try:
            print("\nCedula de Ciudadania Valida: Minimo 8 digitos, Max 10 digitos")
            number = int(input(message))
            if number == -1:
                return number
            
            if number < 10000000 or number > 1999999999:
                print("\nDigita una cedula valida")
                continue
            return number
        except ValueError:
            print("Error, no ingreses letras ni caracteres especiales")

def verify_telephone(message):
    print("=" *60)
    while True:
        try:
            print("Numero de telefono valido de 10 digitos")
            number = int(input(message))
            if number < 3000000000 or number > 39999999999:
                print("Digita un telefono valido")
                continue
            return number
        except ValueError:
            print("Error, no ingreses letras ni caracteres especiales")

def verify_string(message):
    print("=" *60)
    while True:
        word = input(message)
        x = word.replace(" ","")
        if word.strip() == "" or not(x.isalpha()):
            print("No ingreses caracteres especiales ni espacios vacios")
            continue
        else:
            return word.strip()

def verify_sex(message):
    print("\nSexo del del cliente: (M = Masculino) (F = Femenino)")
    while True:
        sex = input(message)
        if sex.upper() == "M" or sex.upper() == "F":
            return sex
        else:
            print("Ingresa solamente las letras M o F")

def type_card(option):
    if option == 1:
        print("Haz elegido Master Card")
        return "Master Card"
    if option == 2:
        print("Haz elegido Visa")
        return "Visa"
    if option == 3:
        print("Haz elegido Américan Express")
        return "Américan Express"

def date_card():
    print("Informa al cliente la siguiente informacion:")
    date = datetime.datetime.now().date()
    x = str(date)
    year = int(x[0:4]) + 4
    month = x[5:7]
    final_date = month + "/" + str(year)
    print(f"Fecha expedicion: {month}/{year - 4}")
    print(f"Fecha de vencimiento: {final_date}")
    return final_date

def verify_card(message):
    print("-" *60)
    while True:
        try:
            print("Digita los 16 numeros de la tarjeta sin separacion")
            number = int(input(message))
            if number == -1:
                return number
            if number < 1000000000000000 or number > 9999999999999999:
                print("Digita un numero de tarjeta valido")
                continue
            return number
        except ValueError:
            print("No ingreses caracteres especiales, solo numeros")

def number_card(clients):
    while True:
        exist = False
        number = random.randrange(1000000000000000, 9999999999999999)
        for x in clients:
            if "Cards" in clients[x]:
                for y in clients[x]["Cards"]:
                    if number == y:
                        exist = True
        if not(exist):
            break
    y = str(number)
    x = y[:4] + "-" + y[4:8] + "-" + y[8:12] + "-" + y[12:]
    print(f"El numero de la tarjeta es: {x}")
    return number

def code_card(clients):
    while True:
        exist = False
        code = random.randrange(100,999)
        for x in clients:
            if "Cards" in clients[x]:
                for y in clients[x]["Cards"]:
                    z = clients[x]["Cards"][y]["Code"]
                    if code == z:
                        exist = True
        if not(exist):
            break
    print("El codigo de verificacion de la tarjeta es:", code)
    return code

def options(quantity):
    while True:
        try:
            option = int(input("Opcion: "))
            if option < 1 or option > quantity:
                print("Ingresa una opcion valida")
                continue
            break
        except ValueError:
            print("Ingresa un numero valido")
    return option

def options_change():
    print("Que desea modificar del cliente?")
    print("1. Nombre\n2. Numero telefonico\n3. Sexo\n4. Salir")
    option = options(4)
    return option

def op_change_card():
    print("Que desea modificar de la tarjeta?")
    print("1. Nuevo Numero\n2. Nuevo Codigo de Verificacion\n3. Salir")
    option = options(3)
    return option

def read_data():
    clients = {}
    try:
        with open(rute_bank, "r") as f:
            data_file = json.load(f)
            for x in data_file.keys():
                clients[int(x)] = data_file[x]
        return clients
    except:
        with open(rute_bank, "w") as f:
            json.dump(clients, f)
            return clients

def update_data(dictionary):
    with open(rute_bank, "w") as f:
        json.dump(dictionary, f)


def add_client():
    clients = read_data()
    print("=" *60)
    print(" Ingreso Clientes ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    while True:
        idd = verify_id("\nIngrese la Cedula del cliente: ")
        if idd == -1:
            to_exit = True
            break
        if idd in clients:
            print("Ya existe un cliente con la misma Cedula, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al Menu Gestion Clientes")

    names = verify_string("\nIngrese los nombres del cliente: ")
    last_name = verify_string("\nIngrese los apellidos del cliente: ")
    name = names + " " + last_name
    telephone = verify_telephone("\nDigite el numero de telefono del cliente: ")
    sex = verify_sex("\nIngresa el sexo del cliente: ")
    clients[idd] = {}
    clients[idd]["Name"] = name.title()
    clients[idd]["Telephone"] = telephone
    clients[idd]["Sex"] = sex.title()
    update_data(clients)
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def modify_client():
    clients = read_data()
    print("=" *60)
    print(" Modificar datos de Cliente ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    while True:
        idd = verify_id("Ingrese la Cedula del cliente: ")
        if idd == -1:
            to_exit = True
            break
        if not (idd in clients):
            print("No existe el cliente en el banco, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al Menu Gestion Clientes")
    name = clients[idd]["Name"]
    print(f"Cliente {name}, Cedula: {idd}")
    option = options_change()
    if option == 1:
        new_name = verify_string("Ingrese el nuevo nombre del cliente: ")
        clients[idd]["Name"] = new_name.title()
    if option == 2:
        new_telephone = verify_telephone("Ingrese el nuevo numero de telefono: ")
        clients[idd]["Telephone"] = new_telephone
    if option == 3:
        new_sex = verify_sex("Ingrese el nuevo sexo del cliente: ")
        clients[idd]["Sex"] = new_sex.title()
    if option == 4:
        print("Regresaras al Menu Gestion Clientes")
    update_data(clients)
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def show_client():
    clients = read_data()
    print("=" *60)
    print(" Mostrar datos de un Cliente ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    while True:
        idd = verify_id("Ingrese la Cedula del cliente: ")
        if idd == -1:
            to_exit = True
            break
        if not (idd in clients):
            print("No existe el cliente en el banco, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al Menu Gestion Clientes")
    name = clients[idd]["Name"]
    number = clients[idd]["Telephone"]
    sex = clients[idd]["Sex"]
    print(f"\nCliente {name}, Cedula: {idd}, Numero telefonico: {number}, Sexo: {sex}")
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def del_client():
    clients = read_data()
    print("=" *60)
    print(" Eliminar Cliente ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    while True:
        idd = verify_id("Ingrese la Cedula del cliente a eliminar: ")
        if idd == -1:
            to_exit = True
            break
        if not (idd in clients):
            print("No existe el cliente en el banco, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al Menu Gestion Clientes")
    name = clients[idd]["Name"]
    print(f"Seguro que quieres eliminar al cliente {name}?\n1. Si\n2.No")
    option = options(2)
    if option == 1:
        del clients[idd]
        update_data(clients)
        print(f"Se ha eliminado la informacion del cliente: {name}")
    else:
        print("\nHaz regresado al Menu Gestion Clientes")
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")


def add_card():
    clients = read_data()
    print("=" *60)
    print(" Tarjetas Credito ".center(60,"-"))
    print("\nIMPORTANTE: La persona debe ser cliente del banco")
    print("Para regresar al Menu digita -1")
    to_exit = False
    while True:
        idd = verify_id("Ingrese la Cedula del cliente: ")
        if idd == -1:
            to_exit = True
            break
        if not (idd in clients):
            print("No existe el cliente en el banco, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al menu principal")
    name = clients[idd]["Name"]
    print(f"\nCliente {name} , Cedula: {idd}")
    print("Tipos de tarjetas de credito")
    print("1. Master Card\n2. Visa\n3. Américan Express")
    option_card = options(3)
    card = type_card(option_card)
    date = date_card()
    number = number_card(clients)
    code = code_card(clients)
    clients[idd]["Cards"] = {}
    clients[idd]["Cards"][number] = {}
    clients[idd]["Cards"][number]["Type"] = card
    clients[idd]["Cards"][number]["Date"] = date
    clients[idd]["Cards"][number]["Code"] = code
    update_data(clients)
    clients = {}
    print("\nLa Tarjeta de credito ha sido creada con exito")
    input("\nPresiona cualquier tecla para volver al menu principal")

def modify_card():
    clients = read_data()
    print("=" *60)
    print(" Modificar Tarjeta de Credito ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    exist = False
    while True:
        number = verify_card("Numero de tarjeta: ")
        if number == -1:
            to_exit = True
            break
        for x in clients:
            for y in clients[x]["Cards"]:
                if number == int(y):
                    idd = x
                    exist = True
                    break
        if exist:
            break
        else:
            print("No existe el cliente en el banco, verifica")
    if to_exit:
        return print("\nHaz regresado al Menu Reportes")
    
    name = clients[idd]["Name"]
    print(f"Propietario: {name}, Cedula: {idd}")
    option = op_change_card()
    if option == 1:
        print("\nSe creara un nuevo numero de tarjeta")
        input("Presiona cualquier tecla para continuar")
        print(f"\nEl nuevo numero de la tarjeta es:\nAntes: {number}")
        new_number = number_card(clients)
        info = clients[idd]["Cards"][str(number)].copy()
        del clients[idd]["Cards"][str(number)]
        clients[idd]["Cards"][new_number] = info
        print("\nSe ha asignado el nuevo numero de Tarjeta")
        input("Presiona cualquier tecla para continuar")
    if option == 2:
        print("\nSe creara un nuevo codigo de verificacion")
        input("Presiona cualquier tecla para continuar")
        print(f"\nEl nuevo codigo de la tarjeta {number} es:")
        new_code = code_card(clients)
        clients[idd]["Cards"][str(number)]["Code"] = new_code
    if option == 4:
        print("Regresaras al Menu Gestion Clientes")
        input("Presiona cualquier tecla para continuar")
    update_data(clients)
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def del_card():
    clients = read_data()
    print("=" *60)
    print(" Eliminar Tarjeta de Credito ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    exist = False
    while True:
        number = verify_card("Numero de tarjeta: ")
        if number == -1:
            to_exit = True
            break
        for x in clients:
            for y in clients[x]["Cards"]:
                if number == int(y):
                    idd = x
                    exist = True
                    break
        if exist:
            break
        else:
            print("No existe el cliente en el banco, verifica")
    if to_exit:
        return print("\nHaz regresado al Menu Reportes")
    
    name = clients[idd]["Name"]
    y = str(number)
    x = y[:4] + "-" + y[4:8] + "-" + y[8:12] + "-" + y[12:]
    print(f"Propietario: {name}, Cedula: {idd}")
    print(f"Seguro que quieres eliminar la tarjeta {x}?\n1. Si\n2.No")
    option = options(2)
    if option == 1:
        del clients[idd]["Cards"][str(number)]
        update_data(clients)
        print(f"Se ha eliminado la tarjeta: {x}")
    else:
        print("\nHaz regresado al Menu Gestion Clientes")
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")


def cards_client():
    clients = read_data()
    print("=" *60)
    print(" Tarjetas de Credito por Cliente ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    while True:
        idd = verify_id("Ingrese la Cedula del cliente: ")
        if idd == -1:
            to_exit = True
            break
        if not (idd in clients):
            print("No existe el cliente en el banco, verifica")
            continue
        break
    if to_exit:
        return print("\nHaz regresado al Menu Reportes")
    
    name = clients[idd]["Name"]
    cards_exist = clients[idd]["Cards"]
    x = cards_exist.keys()
    print(f"\nEl Cliente {name} tiene {len(x)} Tarjetas con el Banco ACME\n")
    if clients[idd]["Cards"]:
        print("\n{:<18} {:<18} {:<16} ".format("Numero de Tarjeta", "Tipo", "Fecha Expiracion"))
        for x in clients[idd]["Cards"]:
            card = clients[idd]["Cards"][x]["Type"]
            date = clients[idd]["Cards"][x]["Date"]
            print("\n{:<18} {:<18} {:<16} ".format(x,card,date))
        clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def info_card():
    clients = read_data()
    print("=" *60)
    print(" Informacion de una Tarjeta de Credito ".center(60,"-"))
    print("Para regresar al Menu Reportes digita -1")
    to_exit = False
    exist = False
    while True:
        number = verify_card("Numero de tarjeta: ")
        if number == -1:
            to_exit = True
            break
        for x in clients:
            for y in clients[x]["Cards"]:
                if number == int(y):
                    idd = x
                    exist = True
                    break
        if exist:
            break
        else:
            print("No existe el cliente en el banco, verifica")
    
    if to_exit:
        return print("\nHaz regresado al Menu Reportes")
    name = clients[idd]["Name"]
    sex = clients[idd]["Sex"]
    print("Tarjeta encontrada")
    print(f"\nNombre del propietario: {name}")
    print("\n{:<14} {:<10} ".format("Cedula", "Sexo"))
    print("\n{:<14} {:<10} ".format(idd, sex))
    print("\n{:<18} {:<18} {:<16} ".format("Numero de Tarjeta", "Tipo", "Fecha Expiracion"))
    card = clients[idd]["Cards"][str(number)]["Type"]
    date = clients[idd]["Cards"][str(number)]["Date"]
    print("")
    print("{:<18} {:<18} {:<16} ".format(number,card,date))
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def clients_card():
    clients = read_data()
    print("=" *60)
    print(" Clientes con Tarjeta de Credito ".center(60,"-"))
    print("{:<35} {:<16} {:<26} {:<18} {:<14}".format("Nombre Cliente", "Cedula Cliente", "Numero de tarjeta", "Tipo de Tarjeta","Fecha Vencimiento"))
    for x in clients:
        if "Cards" in clients[x]:
            for y in clients[x]["Cards"]:
                name = clients[x]["Name"]
                card = clients[x]["Cards"][str(y)]["Type"]
                date = clients[x]["Cards"][str(y)]["Date"]
                print("{:<35} {:<16} {:<26} {:<18} {:<14}".format(name, x, y, card, date))
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")

def list_cards():
    clients = read_data()
    print("=" *60)
    print(" Listado de Tarjetas de Credito ".center(60,"-"))
    print("\nSe mostraran las tarjetas existentes por tipo")
    print("Tipos de tarjetas de credito")
    print("1. Master Card\n2. Visa\n3. Américan Express")
    option = options(3)
    card = type_card(option)
    print(f"Tarjetas de tipo {card} ingresadas:\n")
    print("{:<35} {:<16} {:<16} {:<18}".format("Titular", "Cedula Titular", "Numero de tarjeta", "Fecha Vencimiento"))
    for x in clients:
        for y in clients[x]["Cards"]:
            z = clients[x]["Cards"][y]["Type"]
            if card == z:
                name = clients[x]["Name"]
                date = clients[x]["Cards"][y]["Date"]
                print("{:<35} {:<16} {:<16} {:<18}".format(name, x, z, date))
    clients = {}
    input("\nPresiona cualquier tecla para volver al menu principal")


def menu_clients():
    while True:
        print("")
        print(" BANCO ACME ".center(60,"="))
        print(" Gestion Clientes ".center(60,"-"))
        print("\n1. Añadir Cliente")
        print("2. Modificar informacion de un cliente")
        print("3. Mostrar informacion de un cliente")
        print("4. Eliminar cliente")
        print("5. Volver al menu principal")
        option = options(5)
        print("\n")
        if option == 1:
            add_client()
        elif option == 2:
            modify_client()
        elif option == 3:
            show_client()
        elif option == 4:
            del_client()
        else:
            break

def menu_cards():
    while True:
        print("")
        print(" BANCO ACME ".center(60,"="))
        print(" Gestion Tarjetas de Credito ".center(60,"-"))
        print("\n1. Crear Tarjeta de Credito")
        print("2. Modificar Tarjeta de Credito")
        print("3. Eliminar Tarjeta de Credito")
        print("4. Volver al menu principal")
        option = options(4)
        print("\n")
        if option == 1:
            add_card()
        elif option == 2:
            modify_card()
        elif option == 3:
            del_card()
        else:
            break

def menu_reports():
    while True:
        print("")
        print(" BANCO ACME ".center(60,"="))
        print(" Reportes Tarjetas de Credito ".center(60,"-"))
        print("\n1. Tarjetas de Credito por Cliente")
        print("2. Informacion de una Tarjeta de Credito")
        print("3. Listado de Tarjetas de Credito")
        print("4. Cantidad de Tarjetas por Tipo")
        print("5. Volver al menu principal")
        option = options(5)
        print("\n")
        if option == 1:
            cards_client()
        elif option == 2:
            info_card()
        elif option == 3:
            clients_card()
        elif option == 4:
            list_cards()
        else:
            break

def main_menu():
    while True:
        print("\n\n")
        print(" BANCO ACME ".center(60,"="))
        print(" Menu Principal ".center(60,"-"))
        print("\n1. Gestion Clientes")
        print("2. Gestion Tarjeta de Credito")
        print("3. Reportes")
        print("4. Salir")
        option = options(4)
        print("\n")
        if option == 1:
            menu_clients()
        elif option == 2:
            menu_cards()
        elif option == 3:
            menu_reports()
        else:
            print("\nSeguro que quieres salir del programa?")
            print("1. Si\n2. No")
            option = options(2)
            if option == 1:
                return print("\nGracias por usar el programa")
            else:
                print("Haz vuelto al programa\n")

rute_bank = "Python/Prueba Filtro/bankacme.json"
main_menu()
