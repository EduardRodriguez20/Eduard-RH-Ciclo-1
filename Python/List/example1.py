def position_element(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    
    return -1

def verify_element(list, element):
    for i in list:
        if i == element:
            return True
    
    return False

my_list = []

my_list.append("Alirio")
print(my_list, len(my_list))
my_list.extend(["Andres", "Carlos", "Cristian", "Diana"])
print(my_list, len(my_list))
my_list.pop()
print(my_list, len(my_list))
my_list.insert(2,"Eduard")
print(my_list, len(my_list))
my_list.remove("Carlos")
print(my_list, len(my_list))

print("\n")
pos = 0
for i in my_list:
    print(pos, "-->", i)
    pos += 1

print("\n")
for x in range(len(my_list)):
    print(x, "-->", my_list[x] )

# Buscar un elemento y devuelve la posicion o -1

position = position_element(my_list, "Andres")
print(position)

# Buscar un elemento, devuelve true o false

indicator = verify_element(my_list, "Diana")
print(indicator)
