"""
Diseñar una funcion que calcule la media de tres
numeros leidos del teclado y poner un ejemplo
de su aplicacion.
"""
def verification(message):
    while True:
        try:
            print("-" *60)
            number = int(input(message))
            return number
        except ValueError:
            print("Error, ingrese un numero valido")

def media(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    return media

a = verification("Ingrese el primer numero ")
b = verification("Ingrese el segundo numero ")
c = verification("Ingrese el tercer numero ")
average = media(a,b,c)
print(f"\nLa media de {a}, {b}, {c} es = {average:.1f}")

