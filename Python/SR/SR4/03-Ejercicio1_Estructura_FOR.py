print("Los valores que permiten que se cumpla la expresion: (P ** 3 + Q ** 4 - 2 * P ** 2 < 680) \nson:")

for number1 in range(0, 500):
    for number2 in range(0, 500):
        if number1 ** 3 + number2 ** 4 - 2 * number1 ** 2 < 680:
            print(f"P = {number1}, Q = {number2}")

            
