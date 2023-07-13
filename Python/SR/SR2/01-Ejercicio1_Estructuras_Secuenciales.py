name = str(input("Ingrese el nombre del estudiante: \n"))
note_1 = float(input("Ingrese la nota del reto 1 del estudiante: \n"))
note_2 = float(input("Ingrese la nota del reto 2 del estudiante: \n"))
note_3 = float(input("Ingrese la nota del reto 3 del estudiante: \n"))
note_english = float(input("Ingrese la nota de ingles del estudiante: \n"))

final_note = (note_1 * 0.2) + (note_2 * 0.25) + (note_3 * 0.35) + (note_english * 0.20)
print(f"La nota definitiva del estudiante: {name} \nes: " "{:.2f}"  .format(final_note))