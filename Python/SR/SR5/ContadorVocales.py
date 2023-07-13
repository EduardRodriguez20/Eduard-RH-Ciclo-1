print("\n\tContador de vocales")
print("\tPara finalizar el programa escribe (q)")
counter = 0
total_counter = 0

while True:
    sentence = input("\nIngrese una frase:\n")
    sentence = sentence.lower()
    if sentence == "q":
        print("\nHaz terminado el programa")
        break

    while True:
        for x in sentence:
            if "a" == x or "e" == x or "i" == x or "o" == x or "u" == x:
                counter += 1
        print(f"Hay {counter} vocales en la frase ingresada\n")
        break
    total_counter += counter

print(f"El total de vocales encontradas fueron: {total_counter}")
