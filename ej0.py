#Mostrar informacion que ingrese el usuario segun la posicion del arreglo donde se encuentre
#arreglo vacio
arreglo = []

# Pedir al usuario que ingrese la información
for i in range(3):
    dato = input(f"Ingrese la información {i+1}: ")
    arreglo.append(dato)

# Mostrar los datos indexados
for i in range(len(arreglo)):
    print(f"{i}: {arreglo[i]}")