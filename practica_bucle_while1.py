import os
#la función lambda se utiliza para llamar al sistema operativo y borrar la consola.
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

edad = int(input("Introduce tu edad: "))

while edad < 0:
    print("Has introducido una edad negativa, vuelve a intentarlo")
    edad = int(input("Introduce tu edad: "))

print("Gracias por su colaboracion, puede pasar")
print("La edad introducida es: " + str(edad))