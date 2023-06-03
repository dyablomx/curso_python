# Crear un arreglo vacío
arreglo = []

# Pedir al usuario que ingrese los 7 calificaciones
for i in range(7):
    calificaciones = float(input(f"Ingrese calificacion {i+1}: "))
    arreglo.append(calificaciones)

# Calcular el promedio de los 7 datos
#sum => sumara los valores dentro del arreglo / len => dividira entre el numero de posiciones en el arreglo
promedio = sum(arreglo) / len(arreglo)

print("El promedio de las 7 calificaciones es: " + str(promedio))

if promedio <= 5.99:
    print("Reprobado")
elif promedio >= 6:
    print("Aprobado")

print("El programa ha terminado satisfactoriamente")