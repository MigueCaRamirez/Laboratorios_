estudiantes = {}
n = int(input("Cuantos estudiantes vas a procesar: "))

x = 1
while x <= n:
    nombre = input("Nombre del estudiante: ")
    calificacion = float(input("Calificacion: "))
    estudiantes[nombre] = calificacion
    x = x+1

for clave, valor in estudiantes.items():
    print(f"{clave}: {valor}")