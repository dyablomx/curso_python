print("Programa de becas 2023")
distancia=int(input("Introduce la distancia de tu casa a la escuela en KM: "))
print("Distancia: " + str(distancia) + "km")

numero_hermanos=int(input("Introduce el numero de hermanos: "))
print("Numero de hermanos: " + str(numero_hermanos))

salario_familiar=int(input("Introduce el salario familiar mensual: "))
print("Salario Familiar: " + str(salario_familiar) + " MXN")

#if distancia>40 and numero_hermanos>2 and salario_familiar<=20000:
if distancia>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")