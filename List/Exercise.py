def verifyInt(message):
    while True:
        try:
            print("\n","-" *60)
            number = float(input(message))
            if number < 0 or number > 5:
                print("Ingrese un dato valido de 0.0 a 5.0")            
                continue
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

notes = []
print("\tIngreso de notas")
for x in range (1,11):
    note = verifyInt(f"Ingrese la nota del estudiante #{x}: ")
    notes.append(note)

note_max = max(notes)
print("La nota mayor es: ", note_max)
note_min = min(notes)
print("La nota menor es: ", note_min)

average = sum(notes) / 10
print(f"El promedio es: {average:.2f}" )

notes.sort(reverse=True)
three_notes = notes[0:3]
print("Las tres mejores notas son: ", three_notes)

