# quantity = [8.2, 3.4, 2.5, 4.2552, 6]
# x = sum(quantity) / len(quantity)
# print(x)
# y = float(f"{x:.2f}")
# print(y)

# def found(lista):
#     quantity = len(lista)
#     total = sum(lista)
#     return quantity,total

# (largo, total) = found(quantity)
# print(largo)
# print(total)

# print(total*2)
name = "    eduard andres rodriguez   "
name2 = "EDUARD ANDRES RODRIGUEZ"

students = {"eduard":123, "andres":321, "rodrigo":654, "alejandra":456, "diana": 987}
students2 = {123:{"eduard":123, "andres":321, "rodrigo":654, "alejandra":456, "diana": 987}}
quantity = [[2.6,"andres","1A"],[7.5,"rodrigo","2E"],[4.9,"aleja","3C"]]


print(name.strip())
print(name2.title())
print(students)
print(students2)
#print(quantity)
print("")

#print(sorted(students, key=lambda item:item[1]))
students3 = dict(sorted(students2[123].items(), key=lambda item:item[0]))
print(students3)

quantity = list(sorted(quantity, key=lambda item:item[0], reverse= True))
print(students)
print(quantity)


