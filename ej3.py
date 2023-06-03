# Realice un programa que determine el promedio que obtendrá un alumno 
# considerando que realiza tres exámenes, de los cuales el primero y el segundo 
# tienen una ponderación de 25%, mientras que el tercero de 50%. 

print("Promedio del alumno")
calificacion1=int(input("Ingresa la calificacion del primer examen: "))
calificacion2=int(input("Ingresa la calificacion del segundo examen: "))
calificacion3=int(input("Ingresa la calificacion del tercer examen: "))
promedio=(calificacion1*0.25) + (calificacion2*0.25) + (calificacion3*0.5)
print("El promedio es: " + str(promedio))

if promedio < 6:
    print("El alumno fue reprobado")
else:
    print("El alumno fue aprobado")
