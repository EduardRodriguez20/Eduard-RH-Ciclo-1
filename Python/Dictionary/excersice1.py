def verifyInt(message, note):
    print("-" *60)
    while True:
        try:
            if note:
                number = float(input(message))
                if number < 0 or number > 5:
                    print("Notas validas: 0.0 a 5.0")
                else:
                    return number
            else:
                number = int(input(message))
                return number
        except ValueError:
            print("Error, ingrese un numero valido")

def verifyString(message):
    while True:
        print("\n","-" *60)
        word = input(message)
        if word.strip() == "":
            print("No ingreses datos vacios")
            continue
        if not(word.isalpha()):
            print("Solo ingresa letras")
            continue
        return word

students = {}
print("\n")
quantity = verifyInt("Cuantos estudiantes va a ingresar? ", False)
for i in range(quantity):
    while True:
        id = verifyInt(f"\nDigite el codigo del {i+1} estudiante: ", False)
        if id in students:
            print("El codigo ya existe, digite uno diferente")
        else:
            break
    if id == 999:
        break
    name = verifyString("Digite el nombre del estudiante: ")
    note_1 = verifyInt(f"Digite la primer nota (30%): ", True)
    note_2 = verifyInt(f"Digite la segunda nota (30%): ", True)
    note_3 = verifyInt(f"Digite la tercer nota (40%): ", True)
    students[id] = {}
    students[id]["Name"] = name
    students[id]["Note1"] = note_1 * 0.3
    students[id]["Note2"] = note_2 * 0.3
    students[id]["Note3"] = note_3 * 0.4
    students[id]["FinalNote"] = students[id]["Note1"] + students[id]["Note2"] + students[id]["Note3"]
    result = "Reprobó"
    if students[id]["FinalNote"] >= 3.0:
        result = "Aprobó"
    students[id]["Status"] = result

print("\n\n\t\t---Resultados---")
for i in students.keys():
    print("=" *60)
    name = students[i]["Name"]
    final_note = students[i]["FinalNote"]
    result = students[i]["Status"]
    print(f"\nEl estudiante {name}, {result} con una nota final: {final_note:.2f}")
print("\n")
