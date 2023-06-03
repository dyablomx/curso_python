# Se requiere determinar el costo que tendrá realizar una llamada telefónica 
# con base en el tiempo que dura la llamada y en el costo por minuto. 

print("Calculo de costo de una llamada telefonica")
duracion_minutos=int(input("Ingresa la duracion de tu llamada telefonica en minutos: "))
duracion_segundos=int(input("Con cuantos segundos?: "))
costo_minuto = 5
segundos = 60
costo_total = (duracion_minutos * costo_minuto) + (costo_minuto / segundos) * duracion_segundos

print("El costo total de la llamada es: ",costo_total, "MXN")