print("\tModulo de facturacion")
quantity = int(input("Cuantos articulos vas a ingresar? "))

for x in range (quantity):
    article = input("Ingrese el nombre del articulo: ")
    price = int(input(f"Ingrese el precio de {article}: "))
    amount = int(input(f"Cuantos {article} vas a llevar? "))
    total_price = price * amount
    iva = total_price * 0.15
    total_price += iva
    discount = 0
    if total_price > 10000:
        print("Obtuviste un descuento del 5%!")
        discount = total_price * 0.05
        total_price -= discount
    print("\nCantidad   Articulo  IVA   Descuento\t Total a pagar")
    print(f"   {quantity}\t   {article}     {iva}   {discount} \t\t    {total_price}\n")
    


