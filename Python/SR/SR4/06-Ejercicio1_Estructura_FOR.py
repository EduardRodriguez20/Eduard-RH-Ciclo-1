small_salary = 10**28
high_salary = 0
t_gross_salary = 0
t_eps = 0
t_pension = 0
t_net_salary = 0
name_h_salary = ""
name_s_salary = ""

print("\n\tCalculo de sueldo empresa ACME")
quantity = int(input("¿Cuantos empleados va a calcular el sueldo? "))
for i in range (quantity):
    name = input(f"\nDigite el nombre del {i+1} empleado: \n")
    hours_worked = int(input("Digite la cantidad de horas laboradas: \n"))
    gross_salary = hours_worked * 20000
    eps = gross_salary * 0.04
    pension = gross_salary * 0.04
    net_salary = gross_salary - eps - pension

    if net_salary < small_salary:
        name_s_salary = name
        small_salary = int(net_salary)
    if net_salary > high_salary:
        name_h_salary = name
        high_salary = int(net_salary)

    t_gross_salary = int(t_gross_salary + gross_salary)
    t_eps = int(t_eps + eps)
    t_pension = int(t_pension + pension)
    t_net_salary = int(t_net_salary + net_salary)

average_g_salary = int(t_gross_salary / quantity)
average_n_salary = int(t_net_salary / quantity)

print("\n","-"*60)
print("\t\t\tTotales")
print("{:<15s} {:<10s} {:<12s} {:<15s}".format("Salario Bruto", "EPS", "Pensión", "Salario Neto"))
print("{:<15d} {:<10d} {:<12d} {:<15d}".format(t_gross_salary, t_eps, t_pension, t_net_salary))
print(f"\nEl empleado {name_h_salary} tuvo el salario neto mas alto: {high_salary}")
print(f"El empleado {name_s_salary} tuvo el salario neto mas bajo: {small_salary}")
print(f"\nEl promedio de salarios brutos es: {average_g_salary}")
print(f"El promedio de salarios neto es: {average_n_salary}\n")