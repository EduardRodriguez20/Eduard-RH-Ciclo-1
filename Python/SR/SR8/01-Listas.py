ids = []
names = []
hours_worked = []
value_hour = []

def verifyInt(message, id, hours, value):
    while True:
        try:
            print("\n","-" *60)
            if id:
                number = int(input(message))
                if number < 1 or number > 9999999:
                    print("Digita una ID valida, maximo 10 digitos")
                    continue
                return number
            if hours:
                print("Ingresa las horas laboradas, minimo 1, maximo 160")
                number = int(input(message))
                if number < 1 or number > 160:
                    print("\nDigita las horas laboradas segun las recomendaciones")
                    continue
                return number
            if value:
                print("Ingresa el valor de la hora, minimo $8,000, maximo $150,000")
                number = int(input(message))
                if number < 8000 or number > 150000:
                    print("\nDigita las horas laboradas segun las recomendaciones")
                    continue
                return number
        except ValueError:
            print("Error, ingrese un valor valido")

def verifyString(message):
    print("\n","-" *60)
    while True:
        try:
            letter = input(message)
            if letter.strip() == "":
                print("Digita un nombre, no ingreses espacios")
                continue
            if not(letter.isalpha()):
                print("Solo ingresa letras")
                continue
            return letter
        except Exception as e:
            print("Valida lo que ingresaste") 

def add_employee():
    print("\n","-" *60)
    print("\n\t\t--INGRESAR EMPLEADO--")
    id = verifyInt("Digita la ID del empleado a ingresar: ", True, False, False)
    ids.append(id)
    name = verifyString("Digita el nombre del empleado: ")
    names.append(name)
    hour = verifyInt("Digita las horas laboradas: ", False, True, False)
    hours_worked.append(hour)
    value = verifyInt("Digita el valor de la hora laboral: ", False, False, True)
    value_hour.append(value)
    input("\nPresione cualquier tecla para volver al menu")

def modify_employee():
    print("\n","-" *60)
    print("\n\t\t--MODIFICAR DATOS DEL EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a modificar: ", True, False, False)
        if id in ids:
            location = ids.index(id)
            break
        else:
            print("ID no encontrado, valida de nuevo.")

    name = names[location]
    print(f"\nQue datos quieres modificar del empleado: {name}")
    print("1. Nombre")
    print("2. Horas trabajadas")
    print("3. Valor hora")
    while True:
        try:
            option = int(input("Opcion: "))
            if option < 1 or option > 3:
                print("Ingresa una opcion valida")
                continue
            break
        except ValueError:
            print("Ingresa un numero valido")
    
    if option == 1:
        new_name = verifyString("Digita el nuevo nombre del empleado: ")
        names[location] = new_name
        print("Nombre modificado con exito")
    elif option == 2:
        new_hours = verifyInt("Digita el valor de las nuevas horas: ", False, True, False)
        hours_worked[location] = new_hours
        print("Las horas fueron modificadas con exito")
    else:
        new_value = verifyInt("Digite las nuevas horas: ", False, False, True)
        value_hour[location] = new_value
        print("El valor de la hora fue modificado con exito")
    
    input("\nPresione cualquier tecla para volver al menu")

def search():
    print("\n","-" *60)
    print("\n\t\t--BUSCAR DATOS DEL EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a buscar: ", True, False, False)
        if id in ids:
            location = ids.index(id)
            break
        else:
            print("ID no encontrado, valida de nuevo.")

    print(f"\n\tDatos del empleado ID: {id}")
    print(f"Nombre: {names[location]}")
    print(f"Horas laboradas: {hours_worked[location]}")
    print(f"Valor hora laboral: {value_hour[location]}")
    input("\nPresione cualquier tecla para volver al menu")

def delete ():
    print("\n","-" *60)
    print("\n\t\t--ELIMINAR EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a eliminar: ", True, False, False)
        if id in ids:
            location = ids.index(id)
            name = names[location]
            break
        else:
            print("ID no encontrado, valida de nuevo.")

    ids.pop(location)
    names.pop(location)
    hours_worked.pop(location)
    value_hour.pop(location)
    print(f"Los datos del empleado {name} fueron eliminados correctamente")
    input("\nPresione cualquier tecla para volver al menu")

def show ():
    print("\n","-"*60)
    print("\n\t\t--EMPLEADOS INGRESADOS--")
    print(f"\nEmpleados encontrados: {len(ids)}\n")
    print("{:<10s} {:<15s} {:<20s} {:<10s}".format("ID", "NOMBRE", "HORAS LABORADAS", "VALOR HORA"))
    counter = 4
    for x in range(len(ids)):
        print("{:<10} {:<15} {:<20} {:<10}".format(ids[x], names[x], hours_worked[x], value_hour[x]))
        if x == counter:
            print("Se ha mostrado la informacion de 5 empleados, quieres ver mas?")
            print("1. Si")
            print("2. No")
            while True:
                try:
                    option = int(input())
                    if option < 1 or option > 2:
                        print("Ingresa una opcion valida")
                        continue
                    break
                except ValueError:
                    print("Ingresa un numero valido")
            if option == 1:
                counter += 5
            else:
                break
    
    input("\nPresione cualquier tecla para volver al menu")

def payroll():
    print("\n","-" *60)
    print("\n\t\t--BUSCAR NOMINA DEL EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a buscar: ", True, False, False)
        if id in ids:
            location = ids.index(id)
            break
        else:
            print("ID no encontrado, valida de nuevo.")
    
    g_salary = hours_worked[location] * value_hour[location]
    aux_transport = 0
    if g_salary < 1160000:
        aux_transport = 140606
    eps = g_salary * 0.04
    pension = g_salary * 0.04
    net_salary = int((g_salary - eps - pension) + aux_transport)

    print(f"\n\tLa nomina del empleado {names[location]} es: ")
    print(f"\n- Salario Bruto: {g_salary}")
    print(f"- Auxilio de transporte: {aux_transport}")
    print(f"- EPS: {eps}")
    print(f"- Pension: {pension}")
    print("-"*40)
    print(f"- Salario neto: {net_salary}")
    input("\nPresione cualquier tecla para volver al menu")

def payroll_employees():
    print("\n","-"*60)
    print("\n\t\t--NOMINA DE LOS EMPLEADOS INGRESADOS--")
    print(f"\nEmpleados encontrados: {len(ids)}\n")
    print("{:<10s} {:<15s} {:<15s} {:<10s} {:<10s} {:<10s}".format("NOMBRE", "SALARIO BRUTO", "AUX TRANSPORTE", "EPS", "PENSION", "SALARIO NETO"))
    counter = 4
    for x in range(len(ids)):
        g_salary = hours_worked[x] * value_hour[x]
        aux_transport = 0
        if g_salary < 1160000:
            aux_transport = 140.606
        eps = g_salary * 0.04
        pension = g_salary * 0.04
        net_salary = int((g_salary - eps - pension) + aux_transport)
        name = names[x]
        print("{:<10} {:<15} {:<15} {:<10} {:<10} {:<10}".format(name, g_salary, aux_transport, eps, pension, net_salary))
        if x == counter:
            print("Se ha mostrado la informacion de 5 empleados, quieres ver mas?")
            print("1. Si")
            print("2. No")
            while True:
                try:
                    option = int(input())
                    if option < 1 or option > 2:
                        print("Ingresa una opcion valida")
                        continue
                    break
                except ValueError:
                    print("Ingresa un numero valido")
            if option == 1:
                counter += 5
            else:
                break
    
    input("\nPresione cualquier tecla para volver al menu")

while True:
    print("\n\t *** NOMINA ACME ***")
    print("\t\tMENU")
    print("\n1. Agregar empleado")
    print("2- Modificar empleado")
    print("3- Buscar empleado")
    print("4- Eliminar empleado")
    print("5- Listar empleados")
    print("6- Listar nómina de un empleado")
    print("7- Listar nómina de todos los empleados")
    print("8- Salir")
    while True:
        try:
            option = int(input("\nDigita la opcion: "))
            if option < 1 or option > 8:
                print("Ingresa una opcion valida")
                continue
            break
        except ValueError:
            print("Ingresa un numero valido")
    if option == 1:
        add_employee()
    elif option == 2:
        modify_employee()
    elif option == 3:
        search()
    elif option == 4:
        delete()
    elif option == 5:
        show()
    elif option == 6:
        payroll()
    elif option == 7:
        payroll_employees()
    elif option == 8:
        print("\nSeguro que quieres salir del programa?")
        print("1- Si")
        print("2- No")
        while True:
            try:
                to_exit = int(input("Digita la opcion: "))
                if to_exit < 1 or to_exit > 2:
                    print("Ingresa una opcion valida")
                    continue
                break
            except ValueError:
                print("Ingresa un numero valido")
        if to_exit == 1:
            print("Gracias por usar el programa.")
        if to_exit == 2:
            print("\nHaz vuelto al programa\n")
            continue
        break