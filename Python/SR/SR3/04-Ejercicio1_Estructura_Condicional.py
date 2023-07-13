KM = 2500
DISCOUNT = 0.3

print("\nCalcula el precio de tu ticket ingresando la distancia de ida y el tiempo de estancia")
distance = int(input("\nIngrese la distancia de tu viaje (Km): "))
days = int(input("¿Cuantos dias estarás de viaje? "))

price = (distance * KM) * 2
total_discount = price * DISCOUNT

if distance > 800 and days > 7:
    price = price - total_discount
    print("\nFelicidades! Has obtenido un descuento del 30%!")

print(f"\nEl precio de tu ticket (ida y vuelta) es: {price}\n")