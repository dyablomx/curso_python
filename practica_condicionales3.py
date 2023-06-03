print("Asignaturas optativas 2023")
print("Informatica grafica - Pruebas de software - Usabilidad y Accesibilidad")
opcion=input("Escribe la asignatura optativa: ")

asignatura=opcion.lower()

#importante separar con comas la informacion dentro del in ( ) independientemente del tipo de dato
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Asignatura incorrecta")
