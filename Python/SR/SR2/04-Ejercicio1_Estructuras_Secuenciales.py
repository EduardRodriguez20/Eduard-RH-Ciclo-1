hour = int(input("Digite la hora: "))
minutes = int(input("Digite los minutos: "))
#current_hour = 
print(f"Hora: {hour}:{minutes}")
add_minutes = int(input("Ingrese los minutos adicionales: "))
total_minutes = (hour * 60) + minutes + add_minutes
hour = total_minutes // 60
minutes = total_minutes - (hour * 60)
print(f"Nueva hora: {hour}:{minutes}")
