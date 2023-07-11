import io

fd = open("Python/Files/texto.txt", "r", encoding="utf-8")
leer = fd.read()
#leer2 = fd.readline()
#leer3 = fd.readlines()
fd.seek(51)
leer2 = fd.readline(6)
leer3 = fd.readlines()
fd.close()

#print(leer3[0].rstrip(), end="*")
print(leer2)
print(leer3)
counter = 1
for x in leer:
    if x == "\n":
        counter += 1
print(counter)