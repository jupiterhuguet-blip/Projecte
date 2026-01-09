Nota = int(input("La teva nota es: "))
#Bucle principal del programa
if Nota <= 50:
    print("Nota insuficient")
elif Nota <= 70:
    print("Nota suficient")
elif Nota <= 90:
    print("Nota notable")
elif Nota > 90:
    print("Nota excel·lent")
else:
    print("Opcio no valida, torna-ho a intentar")
#Bucle principal del programa