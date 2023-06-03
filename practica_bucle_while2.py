import math
print("Programa de calculo de raiz cuadrada")
numero=int(input("introduce un numero por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hayar la raiz de un numero negativo")
    print("Inteto: ", intentos)

    if intentos == 2:
        print("Has introducido demasiados intentos")
        break;

    numero=int(input("introduce un numero por favor: "))
    if numero < 0:
        intentos += 1
        
if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada es: " + str(numero) + " es " + str(solucion))