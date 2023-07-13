name = input("Digite el nombre del empleado: \n")
hours_worked = int(input("Digite la cantidad de horas laboradas: \n"))

gross_salary = hours_worked * 20000
eps = gross_salary * 0.04
pension = gross_salary * 0.04
total_salary = gross_salary - eps - pension

print(f"\nConceptos de la nomina del empleado: {name}")
print(f"Sueldo bruto: {gross_salary}")
print(f"Valor a descontar de Eps: {eps}")
print(f"Valor a descontar de Pension: {pension}")
print(f"Sueldo neto: {total_salary}")