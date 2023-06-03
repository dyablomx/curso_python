print("Programa de Evaluacion de notas")

nota_alumno=input("Ingresa la nota el alumno: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<=5:
        valoracion="suspenso"
    elif nota>10:
        valoracion="Inserte una calificacion correcta"
    return valoracion

print(evaluacion(int(nota_alumno)))
print("El programa ha finalizado satisfactoriamente.")