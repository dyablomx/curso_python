# Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. 
# ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? 

print("Sueldo profesor")
salario = 1500
incremento = salario * 0.1

for i in range(7):
    salario = salario + incremento
    print(i+1, "año", salario)