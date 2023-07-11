def sumar(num1,num2):
    result = num1 + num2
    return result

def leer():
    while True:
        try:
            n = int(input("Ingrese un numero entero: "))
            return n
        except ValueError:
            print("Error, ingrese un numero valido")

number1 = leer()
number2 = leer()
print("El resultado es: ", sumar(number1, number2))
