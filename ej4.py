# El dueño de un estacionamiento requiere un programa en Python que le permita determinar 
# cuánto debe cobrar por el uso del estacionamiento a sus clientes. Las tarifas que se tienen 
# son las siguientes: 
# - Las dos primeras horas a $5.00 c/u. 
# - Las siguientes tres a $4.00 c/u. 
# - Las cinco siguientes a $3.00 c/u. - Después de diez horas el costo por cada una es de dos pesos. 

print("Tarifa estacionamiento")
tiempo_hora=int(input("Ingresa la duracion de tu parking en horas: "))
tiempo_minutos=int(input("Ingresa la duracion de tu parking en minutos: "))
tiempo_segundos=int(input("Con cuantos segundos?: "))
print("Tiempo total de estacionamiento: ", tiempo_hora,"hrs, ", tiempo_minutos, "min, ", tiempo_segundos, "seg.")
precio_hora = 5
minutos = 60
segundos = minutos
costo_hora = tiempo_hora * precio_hora
costo_minutos = (tiempo_minutos / minutos) * precio_hora
costo_segundos = (tiempo_segundos / segundos) / costo_minutos
costo_total = costo_hora + costo_minutos + costo_segundos
print("Total a pagar: ",costo_total, " MXN")

#la solucion esperada solucion
print("Precio Estacionamiento")
tiempo_estacionamiento=int(input("Introduce el tiempo de estacionamiento: "))

if tiempo_estacionamiento <= 2:
    precio = tiempo_estacionamiento * 5
elif tiempo_estacionamiento <= 5:
    precio = 10 + (tiempo_estacionamiento - 2) * 4
elif tiempo_estacionamiento <= 10:
    precio = 22 + (tiempo_estacionamiento - 5) * 3
else:
    precio = 37 + (tiempo_estacionamiento - 10) * 2
    
print("El total a pagar es de", precio, "MXN")