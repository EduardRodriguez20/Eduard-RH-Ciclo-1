# name = input("Ingrese el nombre: ")
# salary = int(input("Ingrese su salario: "))

# if salary <= 1200000:
#     aux_trans = 120000
# else:
#     aux_trans = 0
# print("\n", "-" * 30)
# print("segun tu salario, tu auxilio de transporte es: ", aux_trans)

# name = input("Digite el nombre del estudiante: ")
# score = int(input(f"Digite la calificacion de 0-100 del estudiante {name} : "))
# if score <= 59:
#     qualification = "D"
# elif score <= 79:
#     qualification = "C"
# elif score <= 89:
#     qualification = "B"
# elif score <= 100:
#     qualification = "A"

# print("\n", "-" * 30)
# print(f"La calificacion cuantitativa del estudiante {name} \nes: {qualification} \n")



print("\nConversor de formato 12H a 24H \n")
hour = int(input("Digite las horas: "))
minutes = int(input("Digite los minutos: "))
seconds = int(input("Digite los segundos: "))
hour_format = str(input("Digite AM o PM: "))
print(f"\nHora en formato 12 horas: {hour:02d}:{minutes:02d}:{seconds:02d} {hour_format} \n")

if (hour_format == "AM" or hour_format == "am") and hour == 12:
    hour = hour - 12
if hour_format == "PM" or hour_format == "pm":
    hour = hour + 12

print(f"\nHora en formato 24 horas: {hour:02d}:{minutes:02d}:{seconds:02d}\n")



