print("\n\tContador de vocales")
print("\tPara finalizar el programa escribe (q)")
counter = 0
total_counter = 0
close = False

while True:
    sentence = input("\nIngrese una frase:\n")
    sentence = sentence.lower()
    for x in sentence:
        if "a" == x or "e" == x or "i" == x or "o" == x or "u" == x:
            counter += 1
        if "q" == x:
            close = True
            break
    
    total_counter += counter
    if close:
        print("\nHaz terminado el programa")
        break
    print(f"Hay {counter} vocales en la frase ingresada\n")

print(f"El total de vocales encontradas fueron: {total_counter}")
