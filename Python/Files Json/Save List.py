# Crear json con lista
# import json
# lista = [10,20,30,40,60]
# with open("Python/Files Json/lista.json", "w") as archivo:
#     json.dump(lista,archivo)
#     print("Se ha escrito en disco")
# if not archivo.closed:
#     print("Cerrando archivo")
#     archivo.close()
# print("Se ha cerrado el archivo")


# Crear json con diccionario
import json
dictionary = {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapicero", "Valor":"Borrador"}
dictionary_2 = {
    "Influencers": [
        {
            "name": "Jaxon",
            "edad": 42,
            "work at": "Tech News"
        },
        {
            "name": "Miller",
            "edad": 35,
            "work at": "IT Day"
        }
    ]
    }
with open("Python/Files Json/Dict.json", "w") as archivo:
    #json.dump(dictionary,archivo)
    json.dump(dictionary_2,archivo)
    print("Se ha escrito en disco")
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
print("Se ha cerrado el archivo")