dictionary_category = {1:25000, 2:30000, 3:40000, 4:45000, 5:60000,}
total_hon = 0
teachers = {}

quantity = int(input("Cuantos docentes va a ingresar? "))
for i in range(quantity):
    while True:
        id = int(input("\nDigite la cedula del docente: "))
        if id in teachers:
            print("La cedula ya existe, digite una nueva")
        else:
            name = input("Digite el nombre del docente: ")
            while True:
                category = int(input("Categoria del docente: "))
                if category < 1 or category > 5:
                    print("La categoria es de 1 a 5")
                else:
                    break
            hours = int(input("Digite las horas laboradas: "))
            teachers[id] = {}
            teachers[id]["Name"] = name
            teachers[id]["Category"] = category
            teachers[id]["Hours"] = hours
            break

# while True:
#     id = int(input("Digite la cedula del docente: "))
#     name = input("Digite el nombre del docente: ")
#     category = int(input("Categoria del docente: "))
#     hours = int(input("Digite las horas laboradas: "))
#     teachers[id] = {}
#     teachers[id]["Name"] = name
#     teachers[id]["Category"] = category
#     teachers[id]["Hours"] = hours

#     option = input("Desea ingresar otro docente (S/N)?")
#     if option.lower() == "n":
#         break

print("\n\n *** INFORME ***")
print("=" *30)
for i in teachers.keys():
    pay = teachers[i]["Hours"] * dictionary_category[teachers[i]["Category"]]
    print(teachers[i]["Name"], f"-- ${pay:,}")
    total_hon += pay
print("=" *30)
print(f"El total de los honorarios fue: ${total_hon:,}")

