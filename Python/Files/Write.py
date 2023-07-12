# fd = open("Python/Files/prueba.txt", "w", encoding="utf-8")
# fd.write("Primera linea\n")
# fd.write("Segunda linea")
# fd.close()


fd = open("Python/Files/prueba2.txt", "w", encoding="utf-8")
lista = ["Primera linea\n", "Segunda linea"]
fd.writelines(lista)
fd.close()