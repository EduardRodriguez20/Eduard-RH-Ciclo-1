import json

def verifyInt(message, idd, note):
    print("\n","-" *60)
    while True:
        try:
            if note:
                print("Nota valida desde 0.0 a 10")
                number = float(input(message))
                if number < 0 or number > 10.0:
                    print("Digita una nota valida")
                    continue
                return number
            
            if idd:
                number = int(input(message))
                if number < 1 or number > 9999999999:
                    print("Digita una ID valida, maximo 10 digitos")
                    continue
                return number
            
            if not(idd):
                print("Los grados van de 1 a 11, digita solo el numero")
                number = int(input(message))
                if number < 1 or number > 11:
                    print("Digita una grado valido")
                    continue
                return number
        except ValueError:
            print("Error, no ingreses letras ni caracteres especiales")

def verifyString(message):
    print("\n","-" *60)
    while True:
        letter = input(message)
        if letter.strip() == "" or not(letter.isalpha()):
            print("No ingreses caracteres especiales ni espacios vacios")
            continue
        else:
            return letter

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

def read_students():
    students = {}
    try:
        with open(rute_students, "r") as f:
            data_file = json.load(f)
            for x in data_file.keys():
                students[int(x)] = {}
                for y in data_file[x].keys():
                    students[int(x)][int(y)] = data_file[x][y]
        return students
    except:
        with open(rute_students, "w") as f:
            json.dump(students, f)
            return students

def update_students(dictionary):
    with open(rute_students, "w") as f:
        json.dump(dictionary, f)

def add_student():
    students = read_students()
    print("\n","-" *60)
    print("INGRESAR ESTUDIANTES".center(50,"-"))
    while True:
        grade = verifyInt("Ingrese el grado del estudiante: ", False, False)
        if not(grade in students):
            students[grade] = {}
        else:
            print(f"Se han encontrado {len(students[grade])} estudiantes en el curso {grade}")
        while True:
            while True:
                idd = verifyInt("Ingrese el codigo del estudiante: ", True, False)
                if idd in students[grade]:
                    print("Ya existe un estudiante con el mismo codigo, verifica")
                    continue
                break
            students[grade][idd] = {}
            name = verifyString("Digite el nombre del estudiante: ")
            print("\nSexo del estudiante (M = Masculino) (F = Femenino)")
            while True:
                sex = verifyString("Ingresa: ")
                if sex == "M" or sex == "F":
                    break
                else:
                    print("Ingresa solamente M o F")
            students[grade][idd]["Name"] = name
            students[grade][idd]["Sex"] = sex
            quantity = verifyInt("Cuantas notas va a ingresar para el estudiante? ", False, False)
            notes = []
            for x in range(quantity):
                print("")
                note = verifyInt(f"Digita la {x+1} nota: ", False, True)
                notes.append(note)
            students[grade][idd]["Notes"] = notes
            prom = sum(notes) / quantity
            students[grade][idd]["Average"] = float(f"{prom:.2f}")
            print(f"La informacion del estudiante {name} se ha guardado")
            print("-" *60)
            print("\nQuieres ingresar otro estudiante? ")
            print("1. Si\n2. No")
            option = options(2)
            if option == 2:
                break
        print("-" *60)
        print("\nQuieres ingresar otro curso de estudiantes? ")
        print("1. Si\n2. No")
        option = options(2)
        if option == 2:
            break
    update_students(students)
    students = {}
    input("\nPresione cualquier tecla para volver al menu")

def modify_student():
    students = read_students()
    print("\n","-" *60)
    print("MODIFICAR DATOS DEL ESTUDIANTE".center(50,"-"))
    while True:
        grade = verifyInt("Ingrese el grado del estudiante: ", False, False)
        if not(grade in students):
            print(f"No existe un grado {grade}, verifica")
            continue
        break
    while True:
        idd = verifyInt("Ingrese el codigo del estudiante: ", True, False)
        if not(idd in students[grade]):
            print("No existe un estudiante con ese codigo, verifica")
            continue
        break
    name = (students[grade][idd]["Name"])
    print(f"\nQue datos quieres modificar del estudiante {name}?")
    print("1. Nombre")
    print("2. Notas")
    print("3. Sexo")
    option = options(3)
    if option == 1:
        new_name = verifyString("Digita el nuevo nombre del empleado: ")
        students[grade][idd]["Name"] = new_name
        print("Nombre modificado con exito")
    elif option == 2:
        quantity = verifyInt("Digita el valor de las nuevas horas: ", False, True, False)
        new_notes = []
        for x in range(quantity):
            print("")
            note = verifyInt(f"Digita la {x+1} nota: ", False, True)
            new_notes.append(note)
        students[grade][idd]["Notes"] = new_notes
        prom = sum(new_notes) / quantity
        students[grade][idd]["Average"] = float(f"{prom:.2f}")
        print("Notas modificadas con exito")
    else:
        print("\nSexo del estudiante (M = Masculino) (F = Femenino)")
        while True:
            new_sex = verifyString("Ingresa: ")
            if new_sex == "M" or new_sex == "F":
                break
            else:
                print("Ingresa solamente M o F")
        students[grade][idd]["Sex"] = new_sex
        print("El sexo del estudiante fue modificado con exito")

    input("\nPresione cualquier tecla para volver al menu")

def search():
    print("\n","-" *60)
    print("\n\t\t--BUSCAR DATOS DEL EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a buscar: ", True, False, False)
        if id in employees:
            break
        else:
            print("ID no encontrado, valida de nuevo.")
    name = employees[id]["Name"]
    hours = employees[id]["Hours"]
    value = employees[id]["Value"]
    print(f"\n\tDatos del empleado ID: {id}")
    print(f"Nombre: {name}")
    print(f"Horas laboradas: {hours}")
    print(f"Valor hora laboral: {value}")
    input("\nPresione cualquier tecla para volver al menu")

def delete ():
    print("\n","-" *60)
    print("\n\t\t--ELIMINAR EMPLEADO--")
    while True:
        id = verifyInt("Digita el ID del empleado a eliminar: ", True, False, False)
        if id in employees:
            break
        else:
            print("ID no encontrado, valida de nuevo.")

    name = employees[id]["Name"]
    del employees[id]
    print(f"Los datos del empleado {name} fueron eliminados correctamente")
    input("\nPresione cualquier tecla para volver al menu")

def show ():
    print("\n","-"*60)
    print("\n\t\t--EMPLEADOS INGRESADOS--")
    print(f"\nEmpleados encontrados: {len(employees)}\n")
    print("{:<10s} {:<15s} {:<20s} {:<10s}".format("ID", "NOMBRE", "HORAS LABORADAS", "VALOR HORA"))
    counter = 4
    for x in employees.keys():
        name = employees[x]["Name"]
        hours = employees[x]["Hours"]
        value = employees[x]["Value"]
        print("{:<10} {:<15} {:<20} {:<10}".format(x, name, hours, value))
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

def main_menu():
    while True:
        print("Instituto Academico ACME".center(50,"="))
        print("Menu Principal".center(50,"-"))
        print("\n1. Ingreso Estudiantes")
        print("2. Ingreso Notas")
        print("3. Reportes")
        print("4. Salir")
        option = verifyInt("\nDigita la opcion: ", False, False)
        if option < 1 or option > 4:
            print("Ingresa una opcion valida")
            continue
        else:
            return option



rute_students = "Python/WIC/Instituto ACME/students.json"