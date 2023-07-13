name = input("Digite el nombre del conductor: \n")
plate = input("Digite la placa del vehiculo: \n")
total_tickets = int(input("Digite el valor total de pasajes: \n"))
total_parcels = int(input("Digite el valor total de encomiendas: \n"))
pay_total_tickets = total_tickets * 0.25
pay_total_parcels = total_parcels * 0.15
full_payment = pay_total_parcels + pay_total_tickets

print(f"\nNombre del conductor: {name} \t Placa del vehiculo: {plate}")
print(f"Valor total de pasajes: {total_tickets}")
print(f"Valor a pagar por concepto de pasajes: {pay_total_tickets}")
print(f"Valor total de encomiendas: {total_parcels}")
print(f"Valor a pagar por concepto de encomiendas: {pay_total_parcels}")
print(f"Total a pagar al conductor {name} : {full_payment}")