"""
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = (base * altura) // 2 
print(f"El area del triangulo es: {area:.2f}")
"""

seconds = int(input("Digite una cantidad de segundos: "))
hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60

cant_seconds = (seconds - (minutes * 60)) - (hours * 3600)

print("Horas: ", hours)
print("Minutos: ", minutes)
print("Segundos: ", cant_seconds)

