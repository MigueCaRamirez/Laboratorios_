
ContadorEmpleadoRango1 = 0
ContadorEmpleadoRango2 = 0
TotalSueldos = 0

Empleados = int(input("Ingrese el numero de empleados: "))

i = 1

while i <= Empleados:
    sueldo = int(input(f"Ingrese el salario del empleado {i}: " ))
    if sueldo >= 1000000 and sueldo <= 3000000:
        ContadorEmpleadoRango1 = ContadorEmpleadoRango1 + 1
    elif sueldo > 3000000:
        ContadorEmpleadoRango2 = ContadorEmpleadoRango2 + 1
    elif sueldo == -1:
        break
    else:
        print("El sueldo es invalido")
        continue

    TotalSueldos = TotalSueldos + sueldo
    i = i+1     
 
print(f"El Numero de empleados que gana entre 1000000 y 3000000 son: {ContadorEmpleadoRango1}")
print(f"El Numero de empleados que gana mas de 3000000 son: {ContadorEmpleadoRango2}")
print(f"El sueldo total de la empresa es de: {TotalSueldos}")

