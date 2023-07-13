day = int(input("\nIngresa el dia (DD): \n"))
month = int(input("Ingresa el mes (MM): \n"))
year = int(input("Ingresa el año (AAAA): \n"))
print(f"\nLa fecha ingresada es: {day:02d}:{month:02d}:{year:02d}")

# VALIDACION DE LOS DIAS DEL MES
days_of_month = 30
if month == 2 :
    days_of_month = 28

# VALIDACION DEL AÑO BICIESTO
if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
    if month == 2 :
        days_of_month = 29

# VALIDACION DEL MES DE 31 DIAS
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
    days_of_month = 31

# INCREMENTAMOS EL DIA 
day = day + 1

# INCREMENTAMOS EL MES
if day > days_of_month:
    month = month + 1
    day = 1

# INCREMENTAMOS EL AÑO
if month > 12:
    year = year + 1
    month = 1

# IMPRIMIMOS EL RESULTADO
print(f"\nLa fecha del dia siguiente es: {day:02d}:{month:02d}:{year:02d}")