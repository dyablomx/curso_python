contador=0
mails=input("Introduce tu direccion de Email: ")

for i in mails:
    if (i == "@" or i == "."):
        contador+=1

if contador>=2:
    print("Mail correcto")
else:
    print("Mail incorrecto")