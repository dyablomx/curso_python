valido=False
mail=input("introduce tu correo: ")

for i in range (len(mail)):
    if mail[i] == "@":
        valido=True

if valido == True:
    print("correo Valido")
else:
    print("Correo Invalido")