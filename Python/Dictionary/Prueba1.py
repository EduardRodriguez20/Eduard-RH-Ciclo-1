quantity_l = {}
values = []
def verifyString(message):
    while True:
        print("\n","-" *60)
        word = input(message)
        if word.strip() == "":
            print("No ingreses datos vacios")
            continue
        if not(word.isalpha()):
            print("Solo ingresa letras")
            continue
        if len(word) < 3 or len(word) > 10**4:
            print("Minimo 3 letras, maximo 10⁴ letras")
            continue
        return word

def verify_differents(sentence, letters):
    #word = set(sentence)
    for i in sentence:
        for x in letters:
            if i == x:
                quantity_l[i] = sentence.count(x)
                

    print(quantity_l)
    print(max(quantity_l))
    # values = quantity_l.values()
    # list_order = sorted(values, reverse=True)
    # print(list_order)
    for x in quantity_l.keys():
        key = x
        value = quantity_l[x]
        dic = {key:value}
        values.append(dic)
    
    print(values)
    for i in values:
        pass
    
    # high = max(x.values())
    # values.append(high)
    # del x[max(high)]
    # print(x)
    # counter += 1
    # if counter == 4:
    #     break
    # high = 0

print("\nRecomendaciones:")
print("- Ingresa por lo menos 3 letras")
print("- Deben haber minimo 3 letras distintas")
sentence = verifyString("Ingrese el nombre de la empresa: ")
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

verify_differents(sentence, letters)
