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
            unique = True
            while True:
                idd = verifyInt("Ingrese el codigo del estudiante: ", True, False)
                for x in students:
                    if idd in students[x]:
                        print("Ya existe un estudiante con el mismo codigo, verifica")
                        unique = False
                        break
                if unique:
                    break
            students[grade][idd] = {}
            name = verifyString("Digite el nombre del estudiante: ")
            print("\nSexo del estudiante (M = Masculino) (F = Femenino)")
            while True:
                sex = verifyString("Ingresa: ")
                if sex.upper() == "M" or sex.upper() == "F":
                    break
                else:
                    print("Ingresa solamente M o F")
            students[grade][idd]["Name"] = name.title()
            students[grade][idd]["Sex"] = sex.upper()
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
        new_name = verifyString(f"Digita el nuevo nombre del estudiante {name}: ")
        students[grade][idd]["Name"] = new_name
        print("Nombre modificado con exito")
    elif option == 2:
        quantity = verifyInt("Cuantas notas vas a ingresar? ", False, True, False)
        new_notes = notes(quantity, False)
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

    update_students(students)
    students = {}
    input("\nPresione cualquier tecla para volver al menu")

def search_grade(students):
    found = False
    while True:
        id = verifyInt("Digita el codigo del estudiante: ", True, False, False)
        for x in students.keys():
            if id in students[x]:
                grade = x
                found = True
        if found:
            break
        else:
            print("Codigo no encontrado, valida de nuevo.")
    return grade, id

def show():
    students = read_students()
    print("\n","-" *60)
    print("BUSCAR ESTUDIANTE".center(50,"-"))
    (grade, id) = search_grade(students)    
    name = students[grade][id]["Name"]
    sex = students[grade][id]["Sex"]
    notes = students[grade][id]["Notes"]
    print("\n","-" *60)
    print(f"\nEstudiante {name}, Grado: {grade}")
    print(f"Sexo: {sex}")
    print(f"Notas: {notes}")
    students = {}
    input("\nPresione cualquier tecla para volver al menu")

def delete ():
    students = read_students()
    print("\n","-" *60)
    print("ELIMINAR ESTUDIANTE".center(50,"-"))
    (grade, id) = search_grade(students) 
    name = students[grade][id]["Name"]
    del students[grade][id]
    print(f"Los datos de {name} fueron eliminados correctamente")
    input("\nPresione cualquier tecla para volver al menu")

def notes(quantity, menu):
    if menu:
        students = read_students()
        while True:
            grade = verifyInt("Ingrese el grado a ingresar notas: ", False, False)
            if not(grade in students):
                print(f"No existe un grado {grade}, verifica")
                continue
            break
        
        quantity = verifyInt("Cuantas notas vas a ingresar? ", False, True, False)
        order_stu = {}

        for x in students[grade]:
            name = students[grade][x]["Name"]
            order_stu[name] = x
        order_stu = dict(sorted(order_stu.items(), key=lambda item:item[0]))

        for x in order_stu:
            notes = []
            cod = order_stu[x]
            print(f"\nNotas Estudiante: {x}")

            for y in range(quantity):
                note = verifyInt(f"Digita la {y+1} nota: ", False, True)
                notes.append(note)

            students[grade][cod]["Notes"] = notes
            prom = sum(notes) / quantity
            students[grade][cod]["Average"] = float(f"{prom:.2f}")

        update_students(students)
        input("\nPresione cualquier tecla para volver al menu")
    else:
        notes = []
        for x in range(quantity):
            note = verifyInt(f"Digita la {x+1} nota: ", False, True)
            notes.append(note)
        return notes

def students_menu():
    while True:
        print("Instituto Academico ACME".center(50,"="))
        print("Administracion Estudiantes".center(50,"-"))
        print("\n1. Ingreso Estudiantes")
        print("2. Modificar datos de un Estudiante")
        print("3. Mostrar informacion de un Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Volver al menu principal")
        option = options(5)
        if option == 1:
            add_student()
        elif option == 2:
            modify_student()
        elif option == 3:
            modify_student()
        elif option == 4:
            modify_student()
        else:
            break

def report_grade():
    print("Instituto Academico ACME".center(50,"="))
    print("Promedio de notas por grado".center(50,"-"))
    students = read_students()
    while True:
        grade = verifyInt("Ingrese el grado: ", False, False)
        if not(grade in students):
            print(f"No existe un grado {grade}, verifica")
            continue
        break
    print(f"\nGrado {grade}")
    print("\n{:<10} {:<14} {:<14} ".format("Codigo", "Estudiante", "Promedio"))
    for x in students[grade]:
        for y in students[grade][x]:
            name = students[grade][x]["Name"]
            average = students[grade][x]["Average"]
            print("\n{:<10} {:<20} {:<10} ".format(x, name, average))
    input("\nPresione cualquier tecla para volver al menu")

def excellence_grade():
    print("Instituto Academico ACME".center(50,"="))
    print("Terna de excelencia por grado".center(50,"-"))
    students = read_students()
    while True:
        grade = verifyInt("Ingrese el grado a ingresar notas: ", False, False)
        if not(grade in students):
            print(f"No existe un grado {grade}, verifica")
            continue
        break
    print(f"\nGrado {grade}")
    print("Los mejores 5 promedios son:")
    print("\n{:<10} {:<14} {:<14} ".format("Puesto", "Estudiante", "Promedio"))
    order_stu = {}
    for x in students[grade]:
        name = students[grade][x]["Name"]
        note = students[grade][x]["Average"]
        order_stu[name] = note
    order_stu = dict(sorted(order_stu.items(), key=lambda item:item[1]))
    counter = 1
    for x in order_stu:
        name = x
        average = order_stu[x]
        print("\n{:<10} {:<20} {:<10} ".format(counter, name, average))
        counter += 1
        if counter == 6:
            break
    input("\nPresione cualquier tecla para volver al menu")

def excellence_total():
    print("Instituto Academico ACME".center(50,"="))
    print("Terna de excelencia institucional".center(50,"-"))
    students = read_students()
    print("Los mejores 5 promedios del instituto son:")
    print("\n{:<10} {:<10} {:<14} {:<14} ".format("Puesto", "Grado", "Estudiante", "Promedio"))
    order_stu = []
    for x in students:
        new_list = []
        for y in students[x]:
            name = students[x][y]["Name"]
            note = students[x][y]["Average"]
            new_list = [note,name,x]
            order_stu.append(new_list)
    order_stu = list(sorted(order_stu, key=lambda item:item[0], reverse= True))
    counter = 1
    for x in order_stu:
        name = order_stu[x][1]
        average = order_stu[x][0]
        grade = order_stu[x][2]
        print("\n{:<10} {:<10} {:<20} {:<10} ".format(counter, grade, name, average))
        counter += 1
        if counter == 6:
            break
    input("\nPresione cualquier tecla para volver al menu")

def reports_menu():
    while True:
        print("Instituto Academico ACME".center(50,"="))
        print("Reportes Notas Estudiantes".center(50,"-"))
        print("\n1. Promedio por grado")
        print("2. Terna de excelencia por grado")
        print("3. Terna de excelencia del instituto")
        print("4. Volver al menu principal")
        option = options(4)
        if option == 1:
            report_grade()
        elif option == 2:
            excellence_grade()
        elif option == 3:
            excellence_total()
        else:
            break

def main_menu():
    while True:
        print("Instituto Academico ACME".center(50,"="))
        print("Menu Principal".center(50,"-"))
        print("\n1. Administracion Estudiantes")
        print("2. Ingreso Notas")
        print("3. Reportes")
        print("4. Salir")
        option = options(4)
        if option == 1:
            students_menu()
        elif option == 2:
            notes(0, True)
        elif option == 3:
            modify_student()
        else:
            print("\nSeguro que quieres salir del programa?")
            print("1. Si\n2. No")
            option = options(2)
            if option == 1:
                return print("Gracias por usar el programa")
            else:
                print("Haz vuelto al programa\n")

rute_students = "Python/WIC/Instituto ACME/students.json"
main_menu()