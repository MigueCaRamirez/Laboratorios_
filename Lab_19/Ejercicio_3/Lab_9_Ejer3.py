Cuadrante1 = 0
Cuadrante2 = 0
Cuadrante3 = 0
Cuadrante4 = 0

NumeroPuntos= int(input("ingrese el numero de puntos que quiere ingresar: "))


Contador = 1

for Contador in range(NumeroPuntos):
    
    coordenadaX = int(input(f"Ingrese la coordenada x del numero {Contador}: "))
    coordenadaY = int(input(f"Ingrese la coordenada y del numero {Contador}: "))

    if coordenadaY > 0 and coordenadaX > 0:
        Cuadrante1 = Cuadrante1 +1
    elif coordenadaX < 0 and coordenadaY >0:
        Cuadrante2 = Cuadrante2 +1
    elif coordenadaX < 0 and coordenadaY < 0:
        Cuadrante3 = Cuadrante3 + 1
    else:
        Cuadrante4 = Cuadrante4+1
    Contador = Contador +1

print(f"Los puntos en el cuadrante 1 son: {Cuadrante1}")
print(f"Los puntos en el cuadrante 2 son: {Cuadrante2}")
print(f"Los puntos en el cuadrante 3 son: {Cuadrante3}")
print(f"Los puntos en el cuadrante 4 son: {Cuadrante4}")