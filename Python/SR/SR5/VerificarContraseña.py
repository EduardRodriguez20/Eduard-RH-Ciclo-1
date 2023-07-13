print("\nRecomendaciones para una clave segura:")
print("• Debe tener una longitud mínima de 8 caracteres")
print("• Debe contener una letra en minúscula")
print("• Debe contener una letra en mayúscula")
print("• Debe contener un número")
print("• No puede contener espacios")
print("• Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)")
password = input("\nIngrese una contraseña:\n")

lenght = False
lower = False
capital = False
numbers = False
symbols = False
number = 0

while True:
    space = True
    for i in password:
        if len(password) >= 8:
            lenght = True
            if not lower:
                if i.islower():
                    lower = True
            if not capital:
                if i.isupper():
                    capital = True
            if not numbers:
                if i.isdigit():
                    number = number + 1
                    if number == 1:
                        numbers = True
            if space:
                if i == " ":
                    space = False
                else:
                    space = True

            if not symbols:
                if "%" == i or "^" == i or "&" == i:
                    symbols = True
    
    if lenght and lower and capital and numbers and space and symbols:
        print("La clave es segura")
        break
    else:
        print("La clave no cumple")
        password = input("Digite una nueva contraseña: ")
