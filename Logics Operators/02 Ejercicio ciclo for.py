import math
print("Calcular el area de un triangulo")
side_one = int(input("Ingrese la longitud del primer lado: "))
side_two = int(input("Ingrese la longitud del segundo lado: "))
side_three = int(input("Ingrese la longitud del tercer lado: "))
p = (side_one + side_two + side_three)/2
if p > side_two and p > side_three and p > side_one:
    area = math.sqrt(p*((p-side_one)*(p-side_two)*(p-side_three)))
    print("El area del triangulo es: ", area)
else:
    print("Las medidas no cumplen con las de un triangulo")
