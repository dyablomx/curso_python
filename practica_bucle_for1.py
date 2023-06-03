email=False
mails=input("Introduce tu direccion de Email: ")

for i in mails:
    if (i=="@"):
        email=True

if email == True:
    print("Mail correcto")
else:
    print("Mail incorrecto")