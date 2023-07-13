print("\n\tValidar si una palabra esta en la frase")
print("\tPara finalizar el programa escribe (salir)")
while True:
    sentence = input("\nIngrese una frase:\n")
    sentence = sentence.lower()
    if sentence == "salir":
        print("Haz terminado el programa")
        break

    while True:
        key_word = input("\nIngrese una palabra para encontrar en la frase: ")
        if key_word.isalpha():
            break
        else:
            print("Ingresa una palabra valida sin caracteres especiales.")
    
    key_word = key_word.lower()
    
    if key_word == "salir":
        print("Haz terminado el programa")
        break
    
    verification = sentence.find(key_word)
    if verification == -1:
        print("\nLa palabra ingresada no se encuentra en la frase")
        print("Intenta de nuevo con una nueva frase")
        print("_"*60 ,"\n")
    else:
        print(f"\n¡Excelente! la palabra ingresada ({key_word}) se encuentra en la frase ingresada\n")
        break
