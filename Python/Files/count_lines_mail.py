#CONTAR LINEAS

import io
# wc -l ruta del archivo
# muestra en consola la cantidad de lineas, c muestra los caracteres

# fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
# counter = 0
# for x in fd:
#     counter += 1
# print(counter)
# fd.close()


#CONTAR PALABRAS FROM solo al inicio
# grep -e "^From" ruta | wc -l
# muestra en consola la cantidad de palabras from
# fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
# counter = 0
# for x in fd:
#     if x.startswith("From"):
#         counter += 1
# print("Cantidad de lineas que empiezan con From: ",counter)
# fd.close()


#CONTAR PALABRAS FROM
# fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
# counter = 0
# for x in fd:
#     if "from" in x.lower():
#         counter += 1
# print("Cantidad de lineas que empiezan con From: ",counter)
# fd.close()


#NO CONTENGA UNA PALABRA
# fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
# counter = 0
# for x in fd:
#     x = x.rstrip()
#     if not "@uct.ac.za" in x:
#         continue
#     print(x)
# fd.close()


# Cuente las cadenas que contienen Subject
# fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
# counter = 0
# for x in fd:
#     if "Subject" in x:
#         counter += 1
# print("Cantidad de lineas que tienen la palabra Subject son: ",counter)
# fd.close()


# Mostrar las lineas en mayusculas
fd = open("Python/Files/mbox-short.txt", "r", encoding="utf-8")
counter = 0
for x in fd:
    print(x.rstrip().upper())
#print("Cantidad de lineas que tienen la palabra Subject son: ",counter)
fd.close()