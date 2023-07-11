print("Validar si es palindroma o no")
word = input("Ingrese una palabra: ")
comparation = ""
for i in range(len(word), 0, -1):
    indicator = word[i-1]
    comparation = comparation + indicator
if word == comparation:
    print("La palabra es palindroma")
else:
    print(f"La palabra no es palindroma, asi es al revez: {comparation}")
