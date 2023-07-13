# Leer una lista

# import json
# with open("Python/Files Json/lista.json", "r") as archivo:
#     lista = json.load(archivo)
# if not archivo.closed:
#     print("Cerrando archivo")
#     archivo.close()
# for x in lista:
#     print(x, end=", ")

# Encontrar un dato en una variable del dic

import json
with open("Python/Files Json/Dict.json", "r") as archivo:
    dict = json.load(archivo)
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Diccionario: ", dict)
print("\nDiccionario[Influencers][1][name]: ", dict["Influencers"][1]["name"])
