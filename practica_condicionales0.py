#operadores de concatenacion
salario_presidente=int(input("Introduce el salario del Presidente de la empresa: $"))
#la funcion str(salario_presidente) convierte en string el intup que acabamos de solicitar
print("Salario del Presidente: $" + str(salario_presidente))

salario_director=int(input("Introduce el salario del Director de la empresa: $"))
print("Salario del Director: $" + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del Jefe de área de la empresa: $"))
print("Salario del Jefe de área: $" + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del personal administrativo de la empresa: $"))
print("Salario de los administradores: $" + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo esta correcto en esta empresa")
else:
    print("Algo Falla en esta empresa")